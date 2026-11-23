#!/usr/bin/env python3
"""Bridge the Last War operator to the computer-use MCP server.

The computer-use project at ~/computer-use exposes four tools over MCP
stdio: computer_use_start, computer_use_status, computer_use_respond and
computer_use_control. A desktop run must stay inside one server process
for its whole life, so this bridge keeps one server alive behind a Unix
socket and lets short CLI calls start, poll and stop runs.

Commands:

  serve                         Run the daemon in the foreground.
  ensure                        Start the daemon if it is not running.
  self-test                     Initialize MCP and list the four tools.
  start --task TEXT [--app ID]  Start a desktop run on the named apps.
  status [--run-id ID] [--wait N] [--image PATH]
                                Poll the latest or named run; save the
                                final screenshot when one is returned.
  control --run-id ID --command pause|resume|stop|guide [--text TEXT]
                                Send a caller command. Consent and
                                take-over are human-only and are not
                                accepted here.
  runs                          List runs recorded by this bridge.
  stop-daemon                   Stop the bridge daemon.

The bridge never approves an app, a consent request, a purchase or a
send. App approval and consent come only from the owner through the
control link printed by `start`, in a real terminal:

  node ~/computer-use/_tools_/agent-core/cli.mjs control-link <run-id>

Exit codes: 0 ok, 1 refused or failed, 2 usage or environment error.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
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

PROJECT = Path(os.environ.get("CU_PROJECT", str(Path.home() / "computer-use"))).expanduser()
SERVER = PROJECT / "_tools_/computer-use-mcp" / "server.mjs"
KEY_FILE = Path(
    os.environ.get("CU_KEY_FILE", str(Path.home() / ".heddle/keys/conclave.api.key"))
).expanduser()
SEAT = os.environ.get("CU_SEAT", "cu-owner")
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


def _send(request: dict, timeout: float = 90) -> dict:
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        sock.connect(str(SOCKET_PATH))
        sock.sendall((json.dumps(request) + "\n").encode())
        sock.shutdown(socket.SHUT_WR)
        chunks = []
        while True:
            chunk = sock.recv(65536)
            if not chunk:
                break
            chunks.append(chunk)
    raw = b"".join(chunks).decode().strip()
    if not raw:
        raise RuntimeError("empty bridge reply")
    return json.loads(raw)


def _ensure_daemon() -> None:
    if _daemon_alive():
        return
    _ensure_state()
    with open(BRIDGE_LOG, "a", encoding="utf-8") as log:
        subprocess.Popen(
            [sys.executable, str(Path(__file__).resolve()), "serve"],
            stdin=subprocess.DEVNULL,
            stdout=log,
            stderr=log,
            start_new_session=True,
        )
    deadline = time.monotonic() + 20
    while time.monotonic() < deadline:
        if _daemon_alive():
            return
        time.sleep(0.25)
    raise RuntimeError(f"bridge daemon did not start; see {BRIDGE_LOG}")


def serve() -> int:
    _ensure_state()
    for stale in (SOCKET_PATH, PID_PATH):
        try:
            stale.unlink()
        except FileNotFoundError:
            pass
    try:
        mcp = McpClient()
    except Exception as error:
        print(f"cu_bridge: cannot start MCP: {error}", file=sys.stderr)
        return 1
    server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server.bind(str(SOCKET_PATH))
    server.listen(4)
    PID_PATH.write_text(f"{os.getpid()}\n")
    try:
        while True:
            conn, _ = server.accept()
            with conn:
                try:
                    raw = b""
                    while not raw.endswith(b"\n"):
                        chunk = conn.recv(65536)
                        if not chunk:
                            break
                        raw += chunk
                    request = json.loads(raw.decode() or "{}")
                    reply = handle(mcp, request)
                except Exception as error:
                    reply = {"ok": False, "error": str(error)}
                conn.sendall((json.dumps(reply) + "\n").encode())
    finally:
        server.close()
        mcp.close()
        for path in (SOCKET_PATH, PID_PATH):
            try:
                path.unlink()
            except FileNotFoundError:
                pass
    return 0


def handle(mcp: McpClient, request: dict) -> dict:
    cmd = request.get("cmd")
    if cmd == "ping":
        return {"ok": True, "pid": os.getpid()}
    if cmd == "tools":
        return {"ok": True, "result": mcp.request("tools/list", {})}
    if cmd == "call":
        name = request.get("name")
        arguments = request.get("arguments") or {}
        timeout = float(request.get("timeout", 60))
        return {"ok": True, "result": mcp.call(name, arguments, timeout=timeout)}
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


def cmd_start(args: argparse.Namespace) -> int:
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
    try:
        started = json.loads(text)
    except json.JSONDecodeError:
        _die(f"unexpected start result: {text[:400]}", 1)
    run_id = started.get("run_id", "")
    _remember(
        {
            "run_id": run_id,
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


def cmd_status(args: argparse.Namespace) -> int:
    _ensure_daemon()
    run_id = args.run_id or _latest_run_id()
    if not run_id:
        _die("no run recorded; start one first", 1)
    wait = max(0, min(int(args.wait), MAX_WAIT))
    reply = _send(
        {
            "cmd": "call",
            "name": "computer_use_status",
            "arguments": {"run_id": run_id, "wait_seconds": wait},
            "timeout": wait + 15,
        },
        timeout=wait + 25,
    )
    if not reply.get("ok"):
        _die(f"status refused: {reply.get('error')}", 1)
    text, image = _content_text(reply["result"])
    print(text)
    if image:
        target = Path(args.image) if args.image else LAST_IMAGE
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(image)
        print(f"\nfinal image: {target}")
    state = ""
    try:
        state = json.loads(text).get("state", "")
    except json.JSONDecodeError:
        pass
    if state:
        _update_run(run_id, state=state, last_text=text[:500])
    return 0


def cmd_control(args: argparse.Namespace) -> int:
    _ensure_daemon()
    arguments = {"run_id": args.run_id, "command": args.command}
    if args.text:
        arguments["text"] = args.text
    reply = _send(
        {"cmd": "call", "name": "computer_use_control", "arguments": arguments, "timeout": 30},
        timeout=40,
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
    print(json.dumps(_read_runs(), indent=2))
    return 0


def cmd_ensure(_args: argparse.Namespace) -> int:
    _ensure_daemon()
    print(json.dumps({"ok": True, "socket": str(SOCKET_PATH)}))
    return 0


def cmd_stop(_args: argparse.Namespace) -> int:
    try:
        _send({"cmd": "shutdown"}, timeout=5)
    except Exception:
        pass
    print(json.dumps({"ok": True, "stopped": not _daemon_alive()}))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("serve", help="run the bridge daemon in the foreground").set_defaults(func=lambda _a: serve())

    ensure = sub.add_parser("ensure", help="start the daemon if it is not running")
    ensure.set_defaults(func=cmd_ensure)

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
    start.set_defaults(func=cmd_start)

    status = sub.add_parser("status", help="poll a run")
    status.add_argument("--run-id", default="")
    status.add_argument("--wait", type=int, default=0)
    status.add_argument("--image", default="")
    status.set_defaults(func=cmd_status)

    control = sub.add_parser("control", help="pause, resume, stop or guide a run")
    control.add_argument("--run-id", required=True)
    control.add_argument("--command", required=True, choices=["pause", "resume", "stop", "guide"])
    control.add_argument("--text", default="")
    control.set_defaults(func=cmd_control)

    runs = sub.add_parser("runs", help="list recorded runs")
    runs.set_defaults(func=cmd_runs)

    stop = sub.add_parser("stop-daemon", help="stop the bridge daemon")
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
