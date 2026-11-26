#!/usr/bin/env python3
"""tcc_who: who asked macOS for a protected folder, and which Python is running now (read-only; Coordinator and Steer A, 2026-11-26).

A UserNotificationCenter window that names Python and the Desktop, Documents, Music, All Files or Media Library is a hung process walking the home
folder: dismissing the window lets it ask for the next folder (16:58Z then 17:01Z). Read this BEFORE any kill; it only reads and prints.

  tcc_who.py pythons [--min-age SECONDS]        every Python of this user: pid, the script's FILE NAME (never a path or an argument), elapsed, the
                                                 names of its parents up to the DSH host, and whether Steer A's 17:11Z kill rule would let it be
                                                 stopped (named session-inbox.py, alive over 60 s, not the DSH host, the bridge daemon or release-watch)
  tcc_who.py window START END [--all]           the tccd requests between two UTC times (HH:MM:SSZ today, or YYYY-MM-DDTHH:MM:SSZ), by requester:
                                                 first request time, responsible process, services (preflight=no means an actual access); Apple's
                                                 own services are left out unless --all; names and counts only, never a path or a reason

Only names are ever printed: a command line carries the owner's user name in its paths. Exit 0 always for a read; 2 when `ps` or `log` cannot run. TCC_WHO_PS_FILE and TCC_WHO_LOG_FILE read recorded output instead (the tests).
"""
from __future__ import annotations

import argparse
import collections
import os
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone

MAX_WINDOW_SECONDS = 600
RISKY = {"session-inbox.py": "session-inbox: globs ~/*/*/TEAM.yaml when its sender is not named in the roster (reflection mirror, KNOWN_ROSTERS)"}
SECRET = re.compile(r"(gh[pousr]_[A-Za-z0-9]{8,}|github_pat_\w+|sk-[A-Za-z0-9_\-]{10,}|(?i:bearer)\s+\S+|[A-Fa-f0-9]{32,})")
KEYED = re.compile(r"(?i)((?:token|password|passwd|secret|api[-_]?key)=)\S+")


def mask(text: str) -> str:
    return SECRET.sub("***", KEYED.sub(r"\1***", text))


def etime_seconds(text: str) -> int:
    """ps etime: [[dd-]hh:]mm:ss."""
    days = 0
    if "-" in text:
        d, text = text.split("-", 1)
        days = int(d)
    parts = [int(p) for p in text.split(":")]
    while len(parts) < 3:
        parts.insert(0, 0)
    return days * 86400 + parts[0] * 3600 + parts[1] * 60 + parts[2]


def human(seconds: int) -> str:
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    return f"{h}h{m:02d}m{s:02d}s" if h else f"{m}m{s:02d}s"


def read_ps() -> str:
    path = os.environ.get("TCC_WHO_PS_FILE")
    if path:
        return open(path, encoding="utf-8", errors="replace").read()
    out = subprocess.run(["ps", "-axww", "-o", "pid=,ppid=,etime=,command="], capture_output=True, text=True)
    if out.returncode != 0:
        raise OSError("ps failed")
    return out.stdout


def parse_ps(text: str) -> dict[int, dict]:
    procs = {}
    for line in text.splitlines():
        m = re.match(r"^\s*(\d+)\s+(\d+)\s+(\S+)\s+(.*)$", line)
        if m:
            procs[int(m.group(1))] = {"pid": int(m.group(1)), "ppid": int(m.group(2)), "etime": m.group(3), "command": m.group(4)}
    return procs


def executable(command: str) -> str:
    first = command.split(" ", 1)[0] if not command.startswith("/") else re.split(r"\s(?=-|\w+\.)", command, 1)[0]
    return os.path.basename(first.split(" ", 1)[0]) or first


def is_python(command: str) -> bool:
    exe_path = command.split(" ", 1)[0]
    base = os.path.basename(exe_path).lower()
    return bool(re.fullmatch(r"python[\d.]*", base)) or "python.app/contents/macos/python" in command.lower().split(" ", 1)[0]


def chain(procs: dict[int, dict], pid: int, limit: int = 6) -> list[str]:
    out, seen = [], {pid}
    cur = procs.get(pid, {}).get("ppid")
    while cur and cur not in seen and cur in procs and len(out) < limit and cur != 1:
        seen.add(cur)
        command = procs[cur]["command"]
        host = "volta-shim" in command or "/.volta/bin/dsh" in command or bool(re.search(r"(^|/)dsh(\s|$)", command))
        out.append(f"{executable(command)}({cur})" + (" [DSH host]" if host else ""))
        if host:
            break
        cur = procs[cur]["ppid"]
    return out


PROTECTED_SCRIPTS = {"release-watch.py": "release-watch", "cu_bridge.py": "the bridge daemon"}
KILL_NAMED = "session-inbox.py"
KILL_MIN_AGE = 60


def script_name(command: str) -> str:
    """The script's file name, `-m module` or `-c (inline code)`: never a path, never an argument."""
    try:
        import shlex
        tokens = shlex.split(command)
    except ValueError:
        tokens = command.split()
    i = 1
    while i < len(tokens):
        t = tokens[i]
        if t == "-m" and i + 1 < len(tokens):
            return f"-m {mask(tokens[i + 1])}"
        if t == "-c":
            return "-c (inline code)"
        if t.startswith("-"):
            i += 1 + (1 if t in ("-W", "-X") else 0)
            continue
        return mask(os.path.basename(t))
    return "(interactive)"


def kill_verdict(row: dict) -> str:
    """Steer A's 17:11Z rule (b): all three must hold. Returns 'eligible' or 'not eligible: <what fails>'."""
    why = []
    if row["script"] != KILL_NAMED:
        why.append(f"not {KILL_NAMED}")
    if row["age"] <= KILL_MIN_AGE:
        why.append(f"alive {row['age']} s, not over {KILL_MIN_AGE}")
    if row["script"] in PROTECTED_SCRIPTS:
        why.append(f"it is {PROTECTED_SCRIPTS[row['script']]}")
    if row["pid"] == 1335 and "it is the bridge daemon" not in why:
        why.append("it is the bridge daemon")
    return "eligible" if not why else "not eligible: " + "; ".join(why)


def hint(script: str) -> str:
    return RISKY.get(script, "")


def pythons(procs: dict[int, dict], min_age: int = 0) -> list[dict]:
    rows = []
    for p in procs.values():
        if is_python(p["command"]) and etime_seconds(p["etime"]) >= min_age and p["pid"] != os.getpid():
            rows.append({**p, "age": etime_seconds(p["etime"]), "chain": chain(procs, p["pid"]), "script": script_name(p["command"]), "hint": ""})
            rows[-1]["hint"] = hint(rows[-1]["script"])
            rows[-1]["verdict"] = kill_verdict(rows[-1])
    rows.sort(key=lambda r: -r["age"])
    return rows


def show_pythons(rows: list[dict]) -> str:
    eligible = [r for r in rows if r["verdict"] == "eligible"]
    lines = [f"{len(rows)} Python process(es) of this user, longest-running first; {len(eligible)} could be stopped under the 17:11Z rule"
             + ("" if eligible else " (none: if a window stands, only the one `killall -9 UserNotificationCenter`)")]
    for r in rows:
        lines.append(f"pid {r['pid']}  script {r['script']}  elapsed {human(r['age'])}  parent {r['chain'][0] if r['chain'] else '-'}  "
                     f"chain {' < '.join(r['chain']) or '-'}")
        lines.append(f"    kill rule: {r['verdict']}" + (f"   (stop it once with `kill {r['pid']}`, no -9, BEFORE the window is dismissed; tell the cu coordinator and the owning seat)"
                                                       if r["verdict"] == "eligible" else ""))
        if r["hint"]:
            lines.append(f"    hint: {r['hint']}")
    return "\n".join(lines)


# --- tccd ---------------------------------------------------------------------------------------------------

def parse_when(text: str, today: datetime) -> datetime:
    text = text.strip()
    for fmt in ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%MZ"):
        try:
            return datetime.strptime(text, fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            pass
    for fmt in ("%H:%M:%SZ", "%H:%MZ"):
        try:
            t = datetime.strptime(text, fmt)
            return today.astimezone(timezone.utc).replace(hour=t.hour, minute=t.minute, second=t.second, microsecond=0)
        except ValueError:
            pass
    raise ValueError(f"not a UTC time: {text!r} (use HH:MM:SSZ or YYYY-MM-DDTHH:MM:SSZ)")


def read_log(start: datetime, end: datetime) -> str:
    path = os.environ.get("TCC_WHO_LOG_FILE")
    if path:
        return open(path, encoding="utf-8", errors="replace").read()
    local = lambda d: d.astimezone().strftime("%Y-%m-%d %H:%M:%S")
    out = subprocess.run(["/usr/bin/log", "show", "--style", "compact", "--predicate",
                          'process == "tccd" AND (eventMessage CONTAINS "AUTHREQ_ATTRIBUTION" OR eventMessage CONTAINS "AUTHREQ_CTX")',
                          "--start", local(start), "--end", local(end)], capture_output=True, text=True)
    if out.returncode != 0:
        raise OSError("log show failed")
    return out.stdout


ROLE = re.compile(r"(responsible|accessing|requesting)=\{TCCDProcess: identifier=([^,]+), pid=(\d+)")


def parse_tccd(text: str, tz_offset_from_log=None) -> list[dict]:
    """One row per request: time (as printed), service, preflight, the accessing (else requesting) process and the responsible process."""
    ctx, attr = {}, {}
    for line in text.splitlines():
        stamp = line[:23]
        m = re.search(r"AUTHREQ_CTX: msgID=([\d.\-]+),.*?service=(kTCCService\w+), preflight=(\w+)", line)
        if m:
            ctx.setdefault(m.group(1), []).append((stamp, m.group(2).replace("kTCCService", ""), m.group(3)))
            continue
        m = re.search(r"AUTHREQ_ATTRIBUTION: msgID=([\d.\-]+), attribution=\{(.*)\}", line)
        if m:
            attr[m.group(1)] = {role: (ident, int(pid)) for role, ident, pid in ROLE.findall(m.group(2))}
    rows = []
    for mid, items in ctx.items():
        roles = attr.get(mid, {})
        who = roles.get("accessing") or roles.get("requesting") or ("unknown", 0)
        resp = roles.get("responsible")
        for stamp, service, pre in items:
            rows.append({"time": stamp, "service": service, "preflight": pre, "who": who, "responsible": resp})
    return sorted(rows, key=lambda r: r["time"])


def group(rows: list[dict], include_apple: bool) -> list[dict]:
    groups: dict[tuple, dict] = {}
    for r in rows:
        resp_apple = r["responsible"] is None or r["responsible"][0].startswith("com.apple.")
        if not include_apple and r["who"][0].startswith("com.apple.") and resp_apple:
            continue
        key = (r["who"], r["responsible"])
        g = groups.setdefault(key, {"who": r["who"], "responsible": r["responsible"], "first": r["time"], "last": r["time"], "services": collections.Counter()})
        g["last"] = r["time"]
        g["services"][r["service"] + ("(access)" if r["preflight"] == "no" else "")] += 1
    return sorted(groups.values(), key=lambda g: g["first"])


def show_window(rows: list[dict], groups: list[dict], start: str, end: str, include_apple: bool) -> str:
    unc = [r for r in rows if r["who"][0] == "com.apple.UserNotificationCenter"]
    lines = [f"tccd requests {start} to {end} UTC: {len(rows)} in all, {sum(sum(g['services'].values()) for g in groups)} shown"
             + ("" if include_apple else " (Apple's own services left out; --all shows them)")]
    offset = datetime.now().astimezone().strftime("%z")
    lines.append(f"times below are this Mac's local time as `log` prints them (UTC{offset[:3]}:{offset[3:]})")
    if unc:
        lines.append(f"UserNotificationCenter pid {unc[0]['who'][1]} first asked at {unc[0]['time'][11:]}: the window comes about 0.5 s later")
    for g in groups:
        resp = f"{g['responsible'][0]} pid {g['responsible'][1]}" if g["responsible"] else "-"
        services = ", ".join(f"{k} {v}" if v > 1 else k for k, v in sorted(g["services"].items()))
        span = g["first"][11:] if g["first"] == g["last"] else f"{g['first'][11:]} to {g['last'][11:]}"
        lines.append(f"{span}  {g['who'][0]} pid {g['who'][1]}  responsible {resp}  ->  {services}")
    if not groups:
        lines.append("no non-Apple requester in this window")
    protected = [g for g in groups if any(s.split("(")[0] in ("SystemPolicyDesktopFolder", "SystemPolicyDocumentsFolder", "SystemPolicyDownloadsFolder", "MediaLibrary",
                                                              "SystemPolicyAllFiles") for s in g["services"])]
    for g in protected:
        lines.append(f"-> {g['who'][0]} pid {g['who'][1]} asked for protected folders: find it with `tcc_who.py pythons` BEFORE dismissing the window")
    return "\n".join(lines)


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="tcc_who.py", description=__doc__.split("\n\n")[0])
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("pythons")
    a.add_argument("--min-age", type=int, default=0, help="only Pythons alive at least this many seconds")
    w = sub.add_parser("window")
    w.add_argument("start")
    w.add_argument("end")
    w.add_argument("--all", action="store_true", help="include Apple's own requesters")
    args = p.parse_args(argv)
    try:
        if args.cmd == "pythons":
            print(show_pythons(pythons(parse_ps(read_ps()), args.min_age)))
            return 0
        now = datetime.now(timezone.utc)
        start, end = parse_when(args.start, now), parse_when(args.end, now)
        if end <= start or (end - start).total_seconds() > MAX_WINDOW_SECONDS:
            print(f"tcc_who: the window must be positive and at most {MAX_WINDOW_SECONDS} s (log show is slow on long windows)", file=sys.stderr)
            return 2
        rows = parse_tccd(read_log(start, end))
        print(show_window(rows, group(rows, args.all), start.strftime("%H:%M:%SZ"), end.strftime("%H:%M:%SZ"), args.all))
        return 0
    except ValueError as exc:
        print(f"tcc_who: {exc}", file=sys.stderr)
        return 2
    except OSError as exc:
        print(f"tcc_who: cannot read: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
