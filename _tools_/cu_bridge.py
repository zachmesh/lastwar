#!/usr/bin/env python3
"""Bridge the Last War operator to the computer-use MCP server.

The computer-use project at ~/computer-use exposes four tools over MCP
stdio: computer_use_start, computer_use_status, computer_use_respond and
computer_use_control. A desktop run must stay inside one server process
for its whole life, so this bridge keeps one server alive behind a Unix
socket and lets short CLI calls start, poll and stop runs.

Commands:

  serve                         Run the daemon in the foreground.
  ensure                        Start the daemon if none is running (never a second one).
  restart                       End every daemon and its MCP child, start a fresh one.
  self-test                     Initialize MCP and list the four tools.
  start --task TEXT [--app ID]  Start a desktop run on the named apps. Before it asks the server it reads the desktop-run lock
                                (read-only): a live run or hold, another seat's or this one's, a waiter, or an ORPHAN entry
                                of a dead run refuses it with a report - retry later; the bridge never waits, retries or
                                breaks a lock. --skip-lock-check leaves the check to the server; --accept-orphan, only on
                                the coordinator's word, lets the server reclaim an orphan the way its own protocol does.
  lock                          Report the desktop-run lock: free, held (run), hold, waiting or orphan. Read-only; exit 0 free,
                                1 busy or orphan, 2 unreadable.
  status [--run-id ID] [--wait N] [--image PATH]
                                Poll the latest or named run on the daemon
                                that owns it; save the final screenshot when
                                one is returned. Always lists every daemon
                                (reachable, orphan) and every recorded run.
  respond --run-id ID --question-id QID --answer TEXT
                                Answer a question the agent asked (status shows it as `question` and as a bridge_note).
                                Questions only: consent and take-over stay human-only. A question left unanswered for 15
                                minutes ends the run as `needs_input`, which status now reports as a question, not a timeout.
  control --run-id ID --command pause|resume|stop|guide [--text TEXT]
                                Send a caller command to the owning daemon;
                                `stop` ends an unreachable owner and its MCP
                                child instead. Consent and take-over are
                                human-only and are not accepted here.
  runs                          List runs recorded by this bridge.
  stop-daemon                   Stop every bridge daemon and its MCP child.

The bridge never approves an app, a consent request, a purchase or a
send. App approval and consent come only from the owner through the
control link printed by `start`, in a real terminal:

  node ~/computer-use/_tools_/agent-core/cli.mjs control-link <run-id>

The desktop-run lock belongs to the computer-use project (`_environments_/macos-desktop/run-lock.mjs`, state under
/tmp/cu-desktop-run): the server takes it for the life of each run under the `--seat` this bridge passes (CU_SEAT, default
`cu-lastwar`, as agreed with the cu team 2026-11-23: it fits their seat pattern and resets nothing persistent) and frees it on
finish, abort and exit; a run killed by a signal leaves an entry the next acquire reclaims once its
pid is dead. The seat must be a [cu] key, `^cu-[a-z0-9]+(-[a-z0-9]+){0,3}$` (`lastwar` alone would read as no run to their guards):
a bad CU_SEAT stops `start` with exit 2. CUT-OVER from cu-owner: only between runs, when no run or hold of this seat is live, and
`cu_bridge.py restart` so the daemon reads the new default; a hold taken as cu-owner is released as cu-owner. An explicit hold
outside a bridge run (a bridge run needs none) is `node <computer-use checkout>/_environments_/macos-desktop/run-lock.mjs hold
--seat cu-lastwar --minutes N --reason "<run id>" [--wait-free SECONDS]` and `... release --seat cu-lastwar` in an EXIT trap (exit 0
done, 1 refused, 2 usage, 3 held but busy: release if you give up); `status` reads it, and `lock` here wraps that.

Exit codes: 0 ok, 1 refused or failed, 2 usage or environment error.
"""

from __future__ import annotations

import argparse
import base64
import fcntl
import json
import os
import re
import shutil
import signal
import socket
import subprocess
import sys
import threading
import time
from pathlib import Path

# _tools_/queue.py is a repository tool, not the standard library module.
# Drop this script's directory from sys.path before importing queue, or the
# local file shadows it and `queue.Queue` disappears.
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path[:] = [p for p in sys.path if os.path.abspath(p or ".") != _SCRIPT_DIR]

import queue  # noqa: E402  (must come after the sys.path cleanup)

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "_tools_/state"
SOCKET_PATH = STATE / "cu_bridge.sock"
PID_PATH = STATE / "cu_bridge.pid"
RUNS_PATH = STATE / "cu_runs.json"
MCP_LOG = STATE / "cu_mcp.log"
BRIDGE_LOG = STATE / "cu_bridge.log"
LAST_IMAGE = STATE / "cu_last.png"
DAEMON_LOCK = STATE / "cu_bridge.lock"
SCRIPT = str(Path(__file__).resolve())

PROJECT = Path(os.environ.get("CU_PROJECT", str(Path.home() / "computer-use"))).expanduser()
SERVER = PROJECT / "_tools_/computer-use-mcp" / "server.mjs"
KEY_FILE = Path(
    os.environ.get("CU_KEY_FILE", str(Path.home() / ".heddle/keys/conclave.api.key"))
).expanduser()
SEAT = os.environ.get("CU_SEAT", "cu-lastwar")      # was cu-owner until 2026-11-23: the cu team asked for a name that tells these runs from the owner's
SEAT_PATTERN = re.compile(r"^cu-[a-z0-9]+(-[a-z0-9]+){0,3}$")      # the computer-use lock's own pattern (run-lock.mjs SEAT_PATTERN)
RUN_LOCK_DIR = Path(os.environ.get("CU_RUN_LOCK_DIR", "/tmp/cu-desktop-run"))
DEFAULT_APP = os.environ.get("CU_APP", "com.lastwar.ios")
NODE = os.environ.get("CU_NODE_BIN") or shutil.which("node") or ""

MAX_WAIT = 50


def _now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%S%z")


def _die(message: str, code: int = 2) -> None:
    print(f"cu_bridge: {message}", file=sys.stderr)
    raise SystemExit(code)


def _ensure_state() -> None:
    STATE.mkdir(parents=True, exist_ok=True)


def _read_runs() -> dict:
    try:
        return json.loads(RUNS_PATH.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        return {"runs": []}


def _write_runs(data: dict) -> None:
    _ensure_state()
    tmp = RUNS_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    tmp.replace(RUNS_PATH)


def _remember(run: dict) -> None:
    data = _read_runs()
    runs = [r for r in data.get("runs", []) if r.get("run_id") != run.get("run_id")]
    runs.insert(0, run)
    data["runs"] = runs[:50]
    _write_runs(data)


def _update_run(run_id: str, **fields) -> None:
    data = _read_runs()
    for run in data.get("runs", []):
        if run.get("run_id") == run_id:
            run.update(fields)
            run["updated_at"] = _now()
            break
    _write_runs(data)


def _latest_run_id() -> str | None:
    runs = _read_runs().get("runs", [])
    return runs[0].get("run_id") if runs else None


# --- daemons: registry, discovery and ending --------------------------------------------------------------------
# Each daemon binds its own socket (cu_bridge-<pid>.sock) and records itself in cu_bridge-<pid>.json; cu_bridge.sock is a
# symlink to the current one. A daemon never removes another live daemon's files, and every daemon, registered or only
# visible in the process table, can be listed and ended together with its MCP child.

def _sock_for(pid: int) -> Path:
    return STATE / f"cu_bridge-{pid}.sock"


def _info_for(pid: int) -> Path:
    return STATE / f"cu_bridge-{pid}.json"


def _pid_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def _process_table() -> list[tuple[int, int, str]]:
    out = subprocess.run(["ps", "-axo", "pid=,ppid=,command="], capture_output=True, text=True).stdout
    rows = []
    for line in out.splitlines():
        parts = line.strip().split(None, 2)
        if len(parts) >= 2 and parts[0].isdigit() and parts[1].isdigit():
            rows.append((int(parts[0]), int(parts[1]), parts[2] if len(parts) > 2 else ""))
    return rows


def _descendants(pid: int, table=None) -> list[int]:
    table = table if table is not None else _process_table()
    found, frontier = [], [pid]
    while frontier:
        parent = frontier.pop()
        for child, ppid, _ in table:
            if ppid == parent and child not in found:
                found.append(child)
                frontier.append(child)
    return found


def _is_serve(cmd: str) -> bool:
    tokens = cmd.split()
    return SCRIPT in tokens and tokens.index(SCRIPT) + 1 < len(tokens) and tokens[tokens.index(SCRIPT) + 1] == "serve"


def _daemon_pids() -> list[int]:
    """Every daemon of this checkout: the registered ones that are alive and any bridge `serve` process in the process table
    (an orphan whose files were removed by an older bridge is still found)."""
    pids = {pid for pid, _, cmd in _process_table() if pid != os.getpid() and _is_serve(cmd)}
    for info in STATE.glob("cu_bridge-*.json"):
        try:
            pid = int(json.loads(info.read_text())["pid"])
        except (OSError, ValueError, KeyError):
            continue
        if _pid_alive(pid):
            pids.add(pid)
    return sorted(pids)


def _daemon_info(pid: int) -> dict:
    registry = {}
    try:
        registry = json.loads(_info_for(pid).read_text())
    except (OSError, ValueError):
        pass
    sock = _sock_for(pid)
    reachable = False
    for timeout in (3, 6, 10):                 # a loaded machine can starve a healthy daemon for seconds: ask again,
        if not sock.exists() or not _pid_alive(pid):       # slower, before calling it unreachable (`control stop` ends orphans)
            break
        try:
            reachable = _send({"cmd": "ping"}, timeout=timeout, sock=sock).get("ok") is True
        except Exception:
            reachable = False
        if reachable:
            break
    return {"pid": pid, "alive": _pid_alive(pid), "reachable": reachable, "orphan": _pid_alive(pid) and not reachable,
            "registered": bool(registry), "mcp_pid": registry.get("mcp_pid"), "started_at": registry.get("started_at"),
            "socket": str(sock)}


def _daemons() -> list[dict]:
    return [_daemon_info(pid) for pid in _daemon_pids()]


def _end_daemon(pid: int) -> dict:
    """End a daemon and the processes below it (its MCP server): ask politely, then SIGTERM, then SIGKILL."""
    table = _process_table()
    below = _descendants(pid, table)
    sock = _sock_for(pid)
    if sock.exists():
        try:
            _send({"cmd": "shutdown"}, timeout=3, sock=sock)
        except Exception:
            pass
    deadline = time.monotonic() + 4
    while _pid_alive(pid) and time.monotonic() < deadline:
        time.sleep(0.1)
    for sig in (signal.SIGTERM, signal.SIGKILL):
        for target in [pid] + below:
            if _pid_alive(target):
                try:
                    os.kill(target, sig)
                except ProcessLookupError:
                    pass
        deadline = time.monotonic() + 3
        while any(_pid_alive(t) for t in [pid] + below) and time.monotonic() < deadline:
            time.sleep(0.1)
    for path in (sock, _info_for(pid)):
        try:
            path.unlink()
        except FileNotFoundError:
            pass
    _fix_pointer()
    return {"pid": pid, "ended": not _pid_alive(pid), "children_ended": [t for t in below if not _pid_alive(t)]}


def _fix_pointer() -> None:
    """Point cu_bridge.sock and cu_bridge.pid at a live daemon, or remove them."""
    live = [i for i in STATE.glob("cu_bridge-*.json") if _pid_alive(int(json.loads(i.read_text()).get("pid", 0)))] \
        if STATE.exists() else []
    for path in (SOCKET_PATH, PID_PATH):
        if path.is_symlink() or path.exists():
            if not live or (path == SOCKET_PATH and not SOCKET_PATH.resolve().exists()):
                path.unlink()


def _mark_runs_of(pid: int, state: str, note: str) -> None:
    data = _read_runs()
    for run in data.get("runs", []):
        if run.get("daemon_pid") == pid and run.get("state") not in ("stopped", "completed", "failed", "lost"):
            run.update(state=state, note=note, updated_at=_now())
    _write_runs(data)


def _owner_of(run_id: str) -> int | None:
    for run in _read_runs().get("runs", []):
        if run.get("run_id") == run_id:
            return run.get("daemon_pid")
    return None


def _listing() -> dict:
    daemons = _daemons()
    by_pid = {d["pid"]: d for d in daemons}
    runs = []
    for run in _read_runs().get("runs", []):
        owner = by_pid.get(run.get("daemon_pid"))
        place = "no owner recorded" if run.get("daemon_pid") is None else (
            "reachable" if owner and owner["reachable"] else "orphan" if owner and owner["orphan"] else "daemon gone")
        runs.append({"run_id": run.get("run_id"), "state": run.get("state"), "daemon_pid": run.get("daemon_pid"), "daemon": place})
    return {"daemons": daemons, "runs": runs}


class McpClient:
    """One long-lived MCP server process over stdio."""

    def __init__(self) -> None:
        if not NODE:
            raise RuntimeError("node was not found on PATH")
        if not SERVER.is_file():
            raise RuntimeError(f"computer-use MCP server not found at {SERVER}")
        if not KEY_FILE.is_file():
            raise RuntimeError(f"computer-use gateway key not found at {KEY_FILE}")
        env = os.environ.copy()
        # A clean exec matters to the desktop helper's peer check; a loader
        # variable would make the server re-exec itself and break our pipes.
        env.pop("NODE_PATH", None)
        env.pop("NODE_OPTIONS", None)
        env.pop("DYLD_INSERT_LIBRARIES", None)
        # The owner has opted this Mac out of the 300 s local-input wait for
        # runs the Last War bridge starts (CU-191/D-066). The computer-use
        # default stays 300; a caller that wants it can set the variable.
        env.setdefault("CU_OWNER_IDLE_SECONDS", "0")
        self.log = open(MCP_LOG, "a", encoding="utf-8")
        self.proc = subprocess.Popen(
            [NODE, str(SERVER), "--seat", SEAT, "--key-file", str(KEY_FILE)],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=self.log,
            text=True,
            bufsize=1,
            env=env,
        )
        self._next_id = 1
        self._inbox: queue.Queue = queue.Queue()
        self._reader = threading.Thread(target=self._read_stdout, daemon=True)
        self._reader.start()
        self.request(
            "initialize",
            {
                "protocolVersion": "2025-06-18",
                "capabilities": {},
                "clientInfo": {"name": "lastwar-cu-bridge", "version": "0.1.0"},
            },
            timeout=30,
        )

    def _read_stdout(self) -> None:
        assert self.proc.stdout is not None
        for line in self.proc.stdout:
            line = line.strip()
            if not line:
                continue
            try:
                self._inbox.put(json.loads(line))
            except json.JSONDecodeError:
                self._inbox.put({"method": "log", "params": {"line": line}})

    def request(self, method: str, params: dict, timeout: float = 60) -> dict:
        if self.proc.poll() is not None:
            raise RuntimeError(f"MCP server exited with {self.proc.returncode}")
        request_id = self._next_id
        self._next_id += 1
        message = {"jsonrpc": "2.0", "id": request_id, "method": method, "params": params}
        assert self.proc.stdin is not None
        self.proc.stdin.write(json.dumps(message) + "\n")
        self.proc.stdin.flush()
        deadline = time.monotonic() + timeout
        while True:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise TimeoutError(f"MCP {method} timed out after {timeout}s")
            try:
                reply = self._inbox.get(timeout=min(remaining, 1.0))
            except queue.Empty:
                continue
            if reply.get("id") != request_id:
                continue
            if "error" in reply:
                error = reply["error"]
                raise RuntimeError(f"MCP {method} error {error.get('code')}: {error.get('message')}")
            return reply.get("result", {})

    def call(self, name: str, arguments: dict, timeout: float = 60) -> dict:
        return self.request("tools/call", {"name": name, "arguments": arguments}, timeout=timeout)

    def close(self) -> None:
        try:
            if self.proc.stdin:
                self.proc.stdin.close()
        except Exception:
            pass
        try:
            self.proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            self.proc.terminate()
            try:
                self.proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.proc.kill()
        self.log.close()


def _content_text(result: dict) -> tuple[str, bytes | None]:
    texts = []
    image = None
    for item in result.get("content", []):
        if item.get("type") == "text":
            texts.append(item.get("text", ""))
        elif item.get("type") == "image":
            try:
                image = base64.b64decode(item.get("data", ""))
            except Exception:
                image = None
    return "\n".join(texts), image


def _call_tool(name: str, arguments: dict, timeout: float = 60) -> dict:
    _ensure_state()
    client = McpClient()
    try:
        return client.call(name, arguments, timeout=timeout)
    finally:
        client.close()


def _daemon_alive() -> bool:
    if not SOCKET_PATH.exists():
        return False
    try:
        reply = _send({"cmd": "ping"}, timeout=2)
        return reply.get("ok") is True
    except Exception:
        return False


def _send(request: dict, timeout: float = 90, sock: Path | None = None) -> dict:
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as conn:
        conn.settimeout(timeout)
        conn.connect(str(sock or SOCKET_PATH))
        conn.sendall((json.dumps(request) + "\n").encode())
        conn.shutdown(socket.SHUT_WR)
        chunks = []
        while True:
            chunk = conn.recv(65536)
            if not chunk:
                break
            chunks.append(chunk)
    raw = b"".join(chunks).decode().strip()
    if not raw:
        raise RuntimeError("empty bridge reply")
    return json.loads(raw)


def _ensure_daemon() -> dict:
    """Make sure one daemon answers; never start a second while one is alive, busy or still starting."""
    _ensure_state()
    deadline = time.monotonic() + 45
    while True:
        live = [d for d in _daemons() if d["alive"]]
        reachable = [d for d in live if d["reachable"]]
        if reachable:
            return {"pid": reachable[0]["pid"], "started": False}
        if not live or time.monotonic() > deadline:
            break
        time.sleep(0.5)
    if live:
        pids = ", ".join(str(d["pid"]) for d in live)
        raise RuntimeError(f"bridge daemon(s) {pids} alive but not answering; run `cu_bridge.py restart` to end them")
    with open(BRIDGE_LOG, "a", encoding="utf-8") as log:
        subprocess.Popen(
            [sys.executable, SCRIPT, "serve"],
            stdin=subprocess.DEVNULL,
            stdout=log,
            stderr=log,
            start_new_session=True,
        )
    deadline = time.monotonic() + 20
    while time.monotonic() < deadline:
        for d in _daemons():
            if d["reachable"]:
                return {"pid": d["pid"], "started": True}
        time.sleep(0.25)
    raise RuntimeError(f"bridge daemon did not start; see {BRIDGE_LOG}")


def _raise_exit(_signum, _frame):
    raise SystemExit(0)


def serve(replace: bool = False) -> int:
    _ensure_state()
    with open(DAEMON_LOCK, "w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)           # two simultaneous starts cannot both pass the check below
        others = [pid for pid in _daemon_pids() if pid != os.getpid()]
        if others:
            if not replace:
                print(f"cu_bridge: another daemon is alive (pid {', '.join(map(str, others))}); not starting a second. "
                      f"Use `restart` to replace it.", file=sys.stderr)
                return 1
            for pid in others:
                _end_daemon(pid)
        try:
            mcp = McpClient()
        except Exception as error:
            print(f"cu_bridge: cannot start MCP: {error}", file=sys.stderr)
            return 1
        me = os.getpid()
        sock_path = _sock_for(me)
        for stale in (sock_path,):
            try:
                stale.unlink()
            except FileNotFoundError:
                pass
        server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        server.bind(str(sock_path))
        server.listen(8)
        _info_for(me).write_text(json.dumps({"pid": me, "socket": str(sock_path), "mcp_pid": mcp.proc.pid,
                                             "started_at": _now()}) + "\n")
        tmp_link = SOCKET_PATH.with_name(".cu_bridge.sock.new")
        try:
            tmp_link.unlink()
        except FileNotFoundError:
            pass
        os.symlink(sock_path.name, tmp_link)
        os.replace(tmp_link, SOCKET_PATH)
        PID_PATH.write_text(f"{me}\n")
    signal.signal(signal.SIGTERM, _raise_exit)       # the finally below must run so the MCP child ends with us
    signal.signal(signal.SIGINT, _raise_exit)
    mcp_lock = threading.Lock()
    try:
        while True:
            conn, _ = server.accept()
            threading.Thread(target=_serve_connection, args=(conn, mcp, mcp_lock), daemon=True).start()
    finally:
        server.close()
        mcp.close()
        for path in (sock_path, _info_for(me)):
            try:
                path.unlink()
            except FileNotFoundError:
                pass
        _fix_pointer()
    return 0


def _serve_connection(conn: socket.socket, mcp: McpClient, mcp_lock: threading.Lock) -> None:
    """One request per connection, each in its own thread, so a ping or a stop is answered while a long poll waits; the
    calls into the one MCP server are taken in turn."""
    with conn:
        try:
            raw = b""
            while not raw.endswith(b"\n"):
                chunk = conn.recv(65536)
                if not chunk:
                    break
                raw += chunk
            request = json.loads(raw.decode() or "{}")
            reply = handle(mcp, request, mcp_lock)
        except Exception as error:
            reply = {"ok": False, "error": str(error)}
        try:
            conn.sendall((json.dumps(reply) + "\n").encode())
        except OSError:
            pass


def handle(mcp: McpClient, request: dict, mcp_lock: threading.Lock | None = None) -> dict:
    cmd = request.get("cmd")
    mcp_lock = mcp_lock or threading.Lock()
    if cmd == "ping":
        return {"ok": True, "pid": os.getpid()}
    if cmd == "tools":
        with mcp_lock:
            return {"ok": True, "result": mcp.request("tools/list", {})}
    if cmd == "call":
        name = request.get("name")
        arguments = request.get("arguments") or {}
        timeout = float(request.get("timeout", 60))
        with mcp_lock:
            return {"ok": True, "result": mcp.call(name, arguments, timeout=timeout), "daemon_pid": os.getpid()}
    if cmd == "shutdown":
        threading.Thread(target=_shutdown_after_reply, daemon=True).start()
        return {"ok": True, "stopping": True}
    return {"ok": False, "error": f"unknown command {cmd!r}"}


def _shutdown_after_reply() -> None:
    time.sleep(0.3)
    os.kill(os.getpid(), signal.SIGTERM)


def _app_list(value: str | None) -> list[str]:
    if not value:
        return [DEFAULT_APP]
    apps = [part.strip() for part in value.split(",") if part.strip()]
    return apps or [DEFAULT_APP]


def _pid_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def lock_state() -> dict:
    """The desktop-run lock as the computer-use project reports it (`run-lock.mjs status`, one JSON line: hold, run, sentinel,
    waiter, ownerIdle), read-only, plus one check the status hides: whether the pid in run.json is alive. state is free, held (a
    live run), hold (a seat's reservation), waiting, orphan (an entry whose process is dead: reported, never broken here) or
    unknown (the status could not be read). No pid is ever returned."""
    cli = Path(os.environ.get("CU_RUN_LOCK_CLI") or PROJECT / "_environments_/macos-desktop/run-lock.mjs")
    if not NODE or not cli.is_file():
        return {"state": "unknown", "reason": f"run-lock.mjs not found at {cli}"}
    command = [NODE, str(cli), "status"] + (["--dir", str(RUN_LOCK_DIR)] if "CU_RUN_LOCK_DIR" in os.environ else [])
    try:
        out = subprocess.run(command, capture_output=True, text=True, timeout=15)
        data = json.loads([ln for ln in out.stdout.splitlines() if ln.strip()][-1])
    except (OSError, subprocess.SubprocessError, ValueError, IndexError):
        return {"state": "unknown", "reason": "the lock status could not be read"}
    run, hold, waiter, sentinel = data.get("run"), data.get("hold"), data.get("waiter"), bool(data.get("sentinel"))
    entry = None
    try:
        entry = json.loads((RUN_LOCK_DIR / "run.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        pass
    report = {"run": None if not run else {k: run.get(k) for k in ("seat", "runId", "startedAt")},
              "hold": None if not hold else {k: hold.get(k) for k in ("seat", "until", "reason")},
              "waiter": waiter, "owner_idle_seconds": (data.get("ownerIdle") or {}).get("seconds")}
    if isinstance(entry, dict) and not entry.get("sentinel") and isinstance(entry.get("pid"), int) and not _pid_alive(entry["pid"]):
        report.update(state="orphan", run={k: entry.get(k) for k in ("seat", "runId", "startedAt")})
    elif run and not sentinel:
        report["state"] = "held"
    elif hold or sentinel:
        report["state"] = "hold"
    elif waiter:
        report["state"] = "waiting"
    else:
        report["state"] = "free"
    return report


def _lock_sentence(state: dict) -> str:
    run, hold = state.get("run") or {}, state.get("hold") or {}
    if state["state"] == "free":
        return "the desktop lock is free"
    if state["state"] == "unknown":
        return f"the desktop lock could not be read ({state.get('reason')})"
    who = run.get("seat") or hold.get("seat") or state.get("waiter") or "another seat"
    mine = " (this bridge's own seat)" if who == SEAT else ""
    if state["state"] == "held":
        return f"the desktop is held by {who}{mine}: run {run.get('runId')} since {run.get('startedAt')}"
    if state["state"] == "hold":
        return f"the desktop is on hold for {who}{mine} until {hold.get('until')}" + (f" ({hold.get('reason')})" if hold.get("reason") else "")
    if state["state"] == "waiting":
        return f"a waiter ({who}) is queued for the desktop"
    return (f"ORPHAN desktop lock: run {run.get('runId')} of {who} since {run.get('startedAt')} names a process that is gone; "
            f"reported, not broken")


def cmd_lock(args: argparse.Namespace) -> int:
    state = lock_state()
    print(_lock_sentence(state))
    print(json.dumps(state, sort_keys=True))
    return {"free": 0, "unknown": 2}.get(state["state"], 1)


def cmd_start(args: argparse.Namespace) -> int:
    if not SEAT_PATTERN.match(SEAT):
        _die(f"CU_SEAT {SEAT!r} is not a [cu] seat key (^cu-[a-z0-9]+(-[a-z0-9]+){{0,3}}$): the computer-use desktop lock refuses "
             f"it; use a name such as cu-lastwar", 2)
    if not args.skip_lock_check and not args.browser:          # the browser has its own gate, capped at two
        state = lock_state()
        if state["state"] in ("held", "hold", "waiting"):
            _die(f"start refused: {_lock_sentence(state)}. Retry later; this bridge never waits, retries or breaks a lock.", 1)
        if state["state"] == "orphan" and not args.accept_orphan:
            _die(f"start refused: {_lock_sentence(state)}. Tell the coordinator; --accept-orphan, on the coordinator's word, lets the "
                 f"computer-use server reclaim it by its own rule.", 1)
        if state["state"] == "unknown":
            print(f"cu_bridge: note: {_lock_sentence(state)}; the server still refuses a start while the desktop is held", file=sys.stderr)
    _ensure_daemon()
    if args.browser:
        if not args.start_url:
            _die("--browser needs --start-url", 2)
        payload = {
            "task": args.task,
            "environment": "chrome-browser",
            "start_url": args.start_url,
            "max_steps": args.max_steps,
            "max_minutes": args.max_minutes,
            "max_cost_usd": args.max_cost,
            "live_view": True,
        }
    else:
        payload = {
            "task": args.task,
            "environment": "macos-desktop",
            "apps": _app_list(args.app),
            "max_steps": args.max_steps,
            "max_minutes": args.max_minutes,
            "max_cost_usd": args.max_cost,
            "live_view": True,
        }
    if args.model:
        payload["model"] = args.model
    reply = _send(
        {"cmd": "call", "name": "computer_use_start", "arguments": payload, "timeout": 180},
        timeout=200,
    )
    if not reply.get("ok"):
        _die(f"start refused: {reply.get('error')}", 1)
    text, _ = _content_text(reply["result"])
    if reply["result"].get("isError"):                     # the server's own refusal (a held desktop, bad input): report it, once
        busy = re.search(r"desktop|lock|hold|active|refused", text, re.I)
        _die(f"start refused: {text[:400]}" + (" Retry later; this bridge never waits, retries or breaks a lock." if busy else ""), 1)
    try:
        started = json.loads(text)
    except json.JSONDecodeError:
        _die(f"unexpected start result: {text[:400]}", 1)
    run_id = started.get("run_id", "")
    _remember(
        {
            "run_id": run_id,
            "daemon_pid": reply.get("daemon_pid"),
            "task": args.task,
            "apps": payload.get("apps", []),
            "started_at": _now(),
            "updated_at": _now(),
            "state": started.get("state", "started"),
            "view_url": started.get("view_url", ""),
        }
    )
    print(json.dumps(started, indent=2))
    print()
    print("Approve the app (first use only) and control the run from a real terminal:")
    print(f"  node {PROJECT}/_tools_/agent-core/cli.mjs control-link {run_id}")
    return 0


def _route(run_id: str, for_stop: bool = False) -> tuple[Path | None, str]:
    """(socket of the daemon that owns the run, note). A run with no recorded owner goes to the current daemon. When the
    owner is unreachable the note says what to do; for a stop the owner is ended instead (socket None)."""
    owner = _owner_of(run_id)
    if owner is None:
        _ensure_daemon()
        return SOCKET_PATH, ""
    info = _daemon_info(owner)
    if info["reachable"]:
        return Path(info["socket"]), ""
    if info["alive"]:
        if for_stop:
            ended = _end_daemon(owner)
            _mark_runs_of(owner, "stopped", f"unreachable daemon {owner} ended with its MCP child")
            return None, f"daemon {owner} was alive but unreachable (an orphan); it and its MCP child were ended: {json.dumps(ended)}"
        raise RuntimeError(f"run {run_id} belongs to daemon {owner}, alive but unreachable (an orphan); "
                           f"`control --run-id {run_id} --command stop` ends it")
    _mark_runs_of(owner, "lost", f"its daemon {owner} is gone")
    if for_stop:
        return None, f"the daemon {owner} that owned run {run_id} is gone; nothing of it is running"
    raise RuntimeError(f"run {run_id}: its daemon {owner} is gone, so the run is lost")


def cmd_status(args: argparse.Namespace) -> int:
    run_id = args.run_id or _latest_run_id()
    if not run_id:
        print(json.dumps({"bridge": _listing()}, indent=2))
        _die("no run recorded; start one first", 1)
    wait = max(0, min(int(args.wait), MAX_WAIT))
    try:
        sock, _ = _route(run_id)
    except RuntimeError as error:
        print(json.dumps({"bridge": _listing()}, indent=2))
        raise
    reply = _send(
        {
            "cmd": "call",
            "name": "computer_use_status",
            "arguments": {"run_id": run_id, "wait_seconds": wait},
            "timeout": wait + 15,
        },
        timeout=wait + 25,
        sock=sock,
    )
    if not reply.get("ok"):
        _die(f"status refused: {reply.get('error')}", 1)
    text, image = _content_text(reply["result"])
    body = None
    try:
        body = json.loads(text)
    except json.JSONDecodeError:
        pass
    note = _question_note(body, run_id)
    if note and isinstance(body, dict):
        body["bridge_note"] = note
        text = json.dumps(body, indent=2)
        print(f"cu_bridge: {note}", file=sys.stderr)
    print(text)
    if image:
        target = Path(args.image) if args.image else LAST_IMAGE
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(image)
        print(f"\nfinal image: {target}")
    state = body.get("state", "") if isinstance(body, dict) else ""
    if state:
        fields = {"state": state, "last_text": text[:500]}
        question = (body.get("question") or {}) if isinstance(body, dict) else {}
        result = (body.get("result") or {}) if isinstance(body, dict) else {}
        if question:
            fields.update(question_id=question.get("question_id", ""), question=str(question.get("text", ""))[:300], ended_on_question=False)
        elif result.get("status") == "needs_input":
            fields.update(question_id="", question=str(result.get("finalMessage") or "")[:300], ended_on_question=True)
        else:
            fields.update(question_id="", question="", ended_on_question=False)
        _update_run(run_id, **fields)
    print(json.dumps({"bridge": _listing()}, indent=2))
    return 0


def _question_note(body, run_id: str) -> str:
    """A line for a run that waits on a question, or that ended on one (status needs_input), else empty. The question text is the
    model's own words about the task, never a secret; the answer command is spelled out."""
    if not isinstance(body, dict):
        return ""
    question = body.get("question") or {}
    if question.get("question_id"):
        return (f"QUESTION PENDING in run {run_id}: {str(question.get('text', ''))[:300]!r}. Answer it within 15 minutes or the run ends "
                f"on it: cu_bridge.py respond --run-id {run_id} --question-id {question['question_id']} --answer '<answer>'")
    result = body.get("result") or {}
    if body.get("state") == "finished" and result.get("status") == "needs_input":
        return (f"RUN {run_id} ENDED ON A QUESTION (needs_input), not a timeout: {str(result.get('finalMessage') or '')[:300]!r}. "
                f"Nothing answered it. Start a new run with the answer in the task text, or say 'never ask' in the task.")
    return ""


def cmd_respond(args: argparse.Namespace) -> int:
    if not args.answer.strip():
        _die("respond needs a non-empty --answer", 2)
    sock, _note = _route(args.run_id)
    reply = _send(
        {"cmd": "call", "name": "computer_use_respond",
         "arguments": {"run_id": args.run_id, "question_id": args.question_id, "answer": args.answer}, "timeout": 30},
        timeout=40,
        sock=sock,
    )
    if not reply.get("ok"):
        _die(f"respond refused: {reply.get('error')}", 1)
    text, _ = _content_text(reply["result"])
    if reply["result"].get("isError"):
        _die(f"respond refused: {text[:400]}", 1)
    _update_run(args.run_id, question_id="", question="", answered_at=_now())
    print(text)
    return 0


def cmd_control(args: argparse.Namespace) -> int:
    stop = args.command == "stop"
    sock, note = _route(args.run_id, for_stop=stop)
    if sock is None:                                  # the owner was ended or is gone: a stop has done its work
        print(json.dumps({"ok": True, "run_id": args.run_id, "note": note}))
        return 0
    arguments = {"run_id": args.run_id, "command": args.command}
    if args.text:
        arguments["text"] = args.text
    reply = _send(
        {"cmd": "call", "name": "computer_use_control", "arguments": arguments, "timeout": 30},
        timeout=40,
        sock=sock,
    )
    if not reply.get("ok"):
        _die(f"control refused: {reply.get('error')}", 1)
    text, _ = _content_text(reply["result"])
    print(text)
    return 0


def cmd_self_test(_args: argparse.Namespace) -> int:
    _ensure_daemon()
    reply = _send({"cmd": "tools"}, timeout=30)
    if not reply.get("ok"):
        _die(f"tools/list failed: {reply.get('error')}", 1)
    names = [tool.get("name") for tool in reply["result"].get("tools", [])]
    print(json.dumps({"ok": True, "server": str(SERVER), "tools": names}, indent=2))
    return 0


def cmd_runs(_args: argparse.Namespace) -> int:
    print(json.dumps({**_read_runs(), "bridge": _listing()}, indent=2))
    return 0


def cmd_ensure(_args: argparse.Namespace) -> int:
    got = _ensure_daemon()
    print(json.dumps({"ok": True, "socket": str(SOCKET_PATH), "pid": got["pid"], "started": got["started"]}))
    return 0


def cmd_restart(_args: argparse.Namespace) -> int:
    """End every daemon and the MCP server below it, then start one fresh daemon."""
    ended = []
    for pid in _daemon_pids():
        ended.append(_end_daemon(pid))
        _mark_runs_of(pid, "lost", f"daemon {pid} was restarted")
    got = _ensure_daemon()
    print(json.dumps({"ok": True, "ended": ended, "started": got["pid"]}))
    return 0


def cmd_stop(_args: argparse.Namespace) -> int:
    ended = []
    for pid in _daemon_pids():
        ended.append(_end_daemon(pid))
        _mark_runs_of(pid, "stopped", f"daemon {pid} was stopped")
    print(json.dumps({"ok": True, "stopped": not _daemon_pids(), "ended": ended}))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    serve_p = sub.add_parser("serve", help="run the bridge daemon in the foreground (refuses while another is alive)")
    serve_p.add_argument("--replace", action="store_true", help="end any other daemon and its MCP child first")
    serve_p.set_defaults(func=lambda a: serve(replace=a.replace))

    ensure = sub.add_parser("ensure", help="start the daemon if none is running; never a second")
    ensure.set_defaults(func=cmd_ensure)

    restart = sub.add_parser("restart", help="end every daemon and its MCP child, then start a fresh one")
    restart.set_defaults(func=cmd_restart)

    test = sub.add_parser("self-test", help="initialize MCP and list its tools")
    test.set_defaults(func=cmd_self_test)

    start = sub.add_parser("start", help="start a desktop or browser run")
    start.add_argument("--task", required=True)
    start.add_argument("--browser", action="store_true", help="run in a fresh headless Chrome instead of the desktop")
    start.add_argument("--start-url", default="", help="browser mode: the http(s) page to open")
    start.add_argument("--app", default=DEFAULT_APP, help="desktop mode: comma-separated bundle ids")
    start.add_argument("--model", default="", help="claude-gateway/<model> or a local alias")
    start.add_argument("--max-steps", type=int, default=20)
    start.add_argument("--max-minutes", type=float, default=10)
    start.add_argument("--max-cost", type=float, default=1.0, help="USD cap")
    start.add_argument("--skip-lock-check", action="store_true", help="leave the desktop-lock check to the server (it still refuses a held desktop)")
    start.add_argument("--accept-orphan", action="store_true", help="coordinator's word only: start although an orphan desktop lock is reported")
    start.set_defaults(func=cmd_start)

    status = sub.add_parser("status", help="poll a run")
    status.add_argument("--run-id", default="")
    status.add_argument("--wait", type=int, default=0)
    status.add_argument("--image", default="")
    status.set_defaults(func=cmd_status)

    respond = sub.add_parser("respond", help="answer a question the agent asked (questions only; never consent)")
    respond.add_argument("--run-id", required=True)
    respond.add_argument("--question-id", required=True)
    respond.add_argument("--answer", required=True)
    respond.set_defaults(func=cmd_respond)
    control = sub.add_parser("control", help="pause, resume, stop or guide a run")
    control.add_argument("--run-id", required=True)
    control.add_argument("--command", required=True, choices=["pause", "resume", "stop", "guide"])
    control.add_argument("--text", default="")
    control.set_defaults(func=cmd_control)

    lock = sub.add_parser("lock", help="report the desktop-run lock (read-only; exit 0 free, 1 busy or orphan, 2 unreadable)")
    lock.set_defaults(func=cmd_lock)
    runs = sub.add_parser("runs", help="list recorded runs")
    runs.set_defaults(func=cmd_runs)

    stop = sub.add_parser("stop-daemon", help="stop every bridge daemon and its MCP child")
    stop.set_defaults(func=cmd_stop)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return int(args.func(args) or 0)
    except (RuntimeError, TimeoutError) as error:
        print(f"cu_bridge: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
