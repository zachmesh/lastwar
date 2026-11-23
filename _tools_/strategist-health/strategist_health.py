#!/usr/bin/env python3
"""strategist_health: is the Strategist, and its strategy, observed and learning? Read-only, counts only.

From Steer A's prototype. It reads the strategy folders `_records_/<date>/strategy/`, git's view of them and, for the session,
`session-relay.py inspect`; it writes nothing (git status runs with --no-optional-locks). Output is counts, percentages and
hours: no claim text, no ids, no file names. Six checks, each threshold a flag:

  durability   strategy files untracked, or modified and not committed, for more than --untracked-hours (2): not landed
  freshness    the newest key file (plan of record, lever ranking, hypothesis register, forecast ledger) older than
               --fresh-hours (12); a plan of record missing once strategy files exist
  register     hypothesis-register.csv: every claim has a test, an owner_seat and a read_by_utc, and no open claim is overdue
  forecasts    forecast-ledger.csv calibration, rows of kind binary and continuous only (deterministic and retired are
               excluded; a continuous row whose point is not strictly inside its interval is excluded):
               binary      Brier score (alarm over --brier-limit 0.25, the score of always saying 50 percent) and a
                           reliability table by probability band
               continuous  interval hit rate against --hit-target (80; alarm beyond --hit-tolerance 20 points) and bias
                           (mean signed error in percent of the point; alarm beyond --bias-limit 20)
               both are split by source tag (M, D, S, G). Fewer than --min-sample (5) scored rows is no alarm, only a note.
  decisions    dec-*.md records (a count)
  session      the strategist seat's context (session-relay.py inspect --json) at or over --context-percent (75)

Exit 0 healthy, 1 at least one alarm, 2 the repository cannot be read. A check with no data is n/a, never an alarm, except a
missing plan of record and a missing forecast ledger beside an existing plan, which alarm. Standard library only.

  strategist_health.py [--root PATH] [--now ISO] [--format text|json] [--no-session] [--session ID]
"""
from __future__ import annotations

import argparse
import csv
import glob
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
KEY_FILES = re.compile(r"(plan-of-record|lever-ranking|hypothesis-register|forecast-ledger)")
BANDS = ((0.0, 0.2), (0.2, 0.4), (0.4, 0.6), (0.6, 0.8), (0.8, 1.0000001))
YES, NO = {"1", "yes", "y", "true", "realized", "realised", "success"}, {"0", "no", "n", "false", "unrealized", "not realized", "failed"}
TAGS = ("M", "D", "S", "G")


def stamp(value):
    m = re.match(r"^(\d{4}-\d{2}-\d{2})[T ](\d{2}):(\d{2})(?::(\d{2}))?", (value or "").strip())
    if not m:
        return None
    y, mo, d = (int(x) for x in m.group(1).split("-"))
    return datetime(y, mo, d, int(m.group(2)), int(m.group(3)), int(m.group(4) or 0), tzinfo=timezone.utc)


def num(value):
    try:
        return float(str(value).replace(",", "").strip())
    except ValueError:
        return None


def rows_of(path: Path):
    with open(path, newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle))


def hours_old(path: Path, now) -> float:
    return (now - datetime.fromtimestamp(path.stat().st_mtime, timezone.utc)).total_seconds() / 3600


def git_status(root: Path, dirs):
    out = subprocess.run(["git", "-C", str(root), "--no-optional-locks", "status", "--porcelain=v1", "--untracked-files=all", "--", *dirs],
                         capture_output=True, text=True)
    if out.returncode:
        raise OSError(f"git status failed: {out.stderr.strip()[:120]}")
    return [(line[:2], line[3:].strip().strip('"')) for line in out.stdout.splitlines() if line.strip()]


def check_durability(root, files, dirs, now, a):
    status = git_status(root, dirs) if dirs else []
    untracked = [p for code, p in status if code == "??"]
    modified = [p for code, p in status if code != "??"]
    def old(paths):
        return [p for p in paths if (root / p).is_file() and hours_old(root / p, now) > a.untracked_hours]
    old_untracked, old_modified = old(untracked), old(modified)
    counts = {"strategy_files": len(files), "strategy_folders": len(dirs), "untracked": len(untracked), "modified_uncommitted": len(modified),
              "untracked_over_limit": len(old_untracked), "modified_over_limit": len(old_modified)}
    alarms = []
    if old_untracked or old_modified:
        oldest = max(hours_old(root / p, now) for p in old_untracked + old_modified)
        alarms.append({"alarm": "durability", "untracked_over_limit": len(old_untracked), "modified_over_limit": len(old_modified),
                       "oldest_hours": round(oldest, 1), "limit_hours": a.untracked_hours})
    return counts, alarms


def check_freshness(root, files, now, a):
    key = [f for f in files if KEY_FILES.search(f.name)]
    counts = {"key_files": len(key), "plan_of_record": any("plan-of-record" in f.name for f in files)}
    alarms = []
    if not files:
        return counts, alarms, ["freshness (no strategy files)"]
    newest = min((hours_old(f, now) for f in key), default=None)
    counts["newest_key_file_hours"] = None if newest is None else round(newest, 1)
    if newest is None or newest > a.fresh_hours:
        alarms.append({"alarm": "freshness", "newest_hours": None if newest is None else round(newest, 1), "limit_hours": a.fresh_hours})
    if not counts["plan_of_record"]:
        alarms.append({"alarm": "no-plan-of-record"})
    return counts, alarms, []


def latest(files, name):
    found = sorted((f for f in files if f.name == name), key=lambda f: f.parent.parent.name)
    return found[-1] if found else None


def check_register(files, now):
    path = latest(files, "hypothesis-register.csv")
    if path is None:
        return {}, [], ["register (no hypothesis-register.csv)"]
    rows = rows_of(path)
    is_open = lambda r: (r.get("status") or "").strip().lower().startswith("open")
    no_test = sum(1 for r in rows if not (r.get("test") or "").strip())
    no_owner = sum(1 for r in rows if not (r.get("owner_seat") or "").strip())
    no_read = sum(1 for r in rows if stamp(r.get("read_by_utc")) is None)
    overdue = sum(1 for r in rows if is_open(r) and stamp(r.get("read_by_utc")) is not None and stamp(r["read_by_utc"]) < now)
    counts = {"claims": len(rows), "open": sum(1 for r in rows if is_open(r)), "closed": sum(1 for r in rows if not is_open(r)),
              "without_test": no_test, "without_owner_seat": no_owner, "without_read_by": no_read, "overdue_open_reads": overdue}
    alarms = []
    if no_test or no_owner or no_read:
        alarms.append({"alarm": "register-incomplete", "without_test": no_test, "without_owner_seat": no_owner, "without_read_by": no_read})
    if overdue:
        alarms.append({"alarm": "register-overdue", "overdue_open_reads": overdue})
    return counts, alarms, []


def outcome(value):
    v = (value or "").strip().lower()
    return 1 if v in YES else 0 if v in NO else None


def check_forecasts(files, has_plan, now, a):
    path = latest(files, "forecast-ledger.csv")
    if path is None:
        return {}, ([{"alarm": "no-forecast-ledger"}] if has_plan else []), ([] if has_plan else ["forecasts (no ledger, no plan)"])
    rows = rows_of(path)
    kinds = {}
    for r in rows:
        kinds[(r.get("kind") or "other").strip().lower() or "other"] = kinds.get((r.get("kind") or "other").strip().lower() or "other", 0) + 1
    counts = {"rows": len(rows), "by_kind": kinds, "excluded_deterministic_or_retired": kinds.get("deterministic", 0) + kinds.get("retired", 0)}
    binary, cont, bad_interval, late = [], [], 0, 0
    for r in rows:
        kind = (r.get("kind") or "").strip().lower()
        created, started = stamp(r.get("created_at_utc")), stamp(r.get("actual_start"))
        if created and started and created > started:
            late += 1
        if kind == "binary":
            p, o = num(r.get("p_success")), outcome(r.get("actual_realized"))
            if p is not None and o is not None and 0 <= p <= 1:
                binary.append((p, o, (r.get("p_source") or "").strip().upper()))
        elif kind == "continuous":
            low, point, high, actual = (num(r.get(k)) for k in ("predicted_low", "predicted_point", "predicted_high", "actual_value"))
            if None in (low, point, high):
                continue
            if not low < point < high:
                bad_interval += 1
                continue
            if actual is not None:
                cont.append((low, point, high, actual, (r.get("value_source") or "").strip().upper()))
    counts.update({"binary_scored": len(binary), "continuous_scored": len(cont), "continuous_point_not_inside_interval": bad_interval,
                   "rows_written_after_their_action_started": late})
    alarms, notes = [], []
    if binary:
        brier = sum((p - o) ** 2 for p, o, _t in binary) / len(binary)
        counts["brier"] = round(brier, 3)
        counts["reliability"] = [{"band": f"{lo:.1f}-{min(hi, 1.0):.1f}", "n": len(sel), "mean_p": round(sum(p for p, _o, _t in sel) / len(sel), 2),
                                   "observed": round(sum(o for _p, o, _t in sel) / len(sel), 2)}
                                  for lo, hi in BANDS for sel in [[x for x in binary if lo <= x[0] < hi]] if sel]
        if len(binary) >= a.min_sample and brier > a.brier_limit:
            alarms.append({"alarm": "brier", "score": round(brier, 3), "limit": a.brier_limit, "n": len(binary)})
    if cont:
        hits = sum(1 for low, _pt, high, act, _t in cont if low <= act <= high)
        hit = 100.0 * hits / len(cont)
        bias_rows = [(act - pt) / abs(pt) * 100 for _l, pt, _h, act, _t in cont if pt != 0]
        counts["interval_hit_percent"] = round(hit)
        counts["interval_hit_target_percent"] = a.hit_target
        counts["bias_percent"] = None if not bias_rows else round(sum(bias_rows) / len(bias_rows), 1)
        if len(cont) >= a.min_sample:
            if abs(hit - a.hit_target) > a.hit_tolerance:
                alarms.append({"alarm": "interval-hit-rate", "percent": round(hit), "target": a.hit_target, "n": len(cont)})
            if bias_rows and abs(sum(bias_rows) / len(bias_rows)) > a.bias_limit:
                alarms.append({"alarm": "bias", "percent": round(sum(bias_rows) / len(bias_rows), 1), "limit": a.bias_limit, "n": len(cont)})
    split = {}
    for tag in TAGS:
        b = [(p, o) for p, o, t in binary if t == tag]
        c = [(low, pt, high, act) for low, pt, high, act, t in cont if t == tag]
        if b or c:
            split[tag] = {"binary_n": len(b), "brier": round(sum((p - o) ** 2 for p, o in b) / len(b), 3) if b else None,
                          "continuous_n": len(c), "hit_percent": round(100.0 * sum(1 for lo, _p, hi, ac in c if lo <= ac <= hi) / len(c)) if c else None}
    counts["by_tag"] = split
    if len(binary) < a.min_sample or len(cont) < a.min_sample:
        notes.append(f"calibration needs at least {a.min_sample} scored rows of a kind (binary {len(binary)}, continuous {len(cont)})")
    return counts, alarms, notes


def team_session_id(root: Path, seat="strategist"):
    team = root / "TEAM.yaml"
    if not team.is_file():
        return None
    key = None
    for line in team.read_text(encoding="utf-8", errors="replace").splitlines():
        m = re.match(r"^  - key: (\S+)\s*$", line)
        if m:
            key = m.group(1)
        m = re.match(r"^    session_id: (\S+)\s*$", line)
        if m and key == seat:
            return m.group(1)
    return None


def relay_command():
    override = os.environ.get("STRATEGIST_HEALTH_RELAY")
    if override:
        return override.split()
    script = Path("~/dtadpole/reflection/_tools_/session-relay/session-relay.py").expanduser()
    return [sys.executable, "-B", str(script)] if script.is_file() else None


def check_session(root, now, a):
    if a.no_session:
        return {}, [], ["session (skipped by --no-session)"]
    session = a.session or team_session_id(root)
    command = relay_command()
    if not session or not command:
        return {}, [], ["session (no strategist session id or no relay tool)"]
    try:
        out = subprocess.run([*command, "inspect", "--runtime", "dsh", "--session", session, "--json"], capture_output=True, text=True, timeout=45)
        view = json.loads(out.stdout)
    except (OSError, ValueError, subprocess.SubprocessError):
        return {}, [], ["session (the relay could not be read)"]
    ctx = view.get("context") or {}
    counts = {"running": bool(view.get("running")), "turns": view.get("turns")}
    last = view.get("last_event_ms")
    if last:
        counts["minutes_since_last_event"] = round((now.timestamp() * 1000 - last) / 60000)
    alarms = []
    if ctx.get("contextWindow") and ctx.get("projectedTokens") is not None:
        pct = 100.0 * ctx["projectedTokens"] / ctx["contextWindow"]
        counts["context_percent"] = round(pct)
        if pct >= a.context_percent:
            alarms.append({"alarm": "session-context", "percent": round(pct), "limit": a.context_percent})
        return counts, alarms, []
    return counts, alarms, ["session (the relay gave no context figure)"]


def evaluate(root: Path, now, a) -> dict:
    dirs = sorted(str(Path(d).relative_to(root)) for d in glob.glob(str(root / "_records_" / "*" / "strategy")) if os.path.isdir(d))
    files = sorted(Path(f) for d in dirs for f in glob.glob(str(root / d / "*")) if os.path.isfile(f))
    result = {"at": now.strftime("%Y-%m-%dT%H:%MZ"), "checks": {}, "alarms": [], "not_applicable": []}
    def add(name, triple):
        counts, alarms, notes = triple
        result["checks"][name] = counts
        result["alarms"] += alarms
        result["not_applicable"] += notes
    add("durability", check_durability(root, files, dirs, now, a) + ([],))
    fresh = check_freshness(root, files, now, a)
    add("freshness", fresh)
    add("register", check_register(files, now))
    add("forecasts", check_forecasts(files, fresh[0]["plan_of_record"], now, a))
    add("decisions", ({"decision_records": sum(1 for f in files if re.match(r"dec-.*\.md$", f.name))}, [], []))
    add("session", check_session(root, now, a))
    return result


def render(result) -> str:
    lines = [f"== STRATEGIST HEALTH ({result['at']}) =="]
    for name, counts in result["checks"].items():
        if counts:
            lines.append(f"{name}: " + ", ".join(f"{k} {json.dumps(v) if isinstance(v, (dict, list)) else v}" for k, v in counts.items()))
    for alarm in result["alarms"]:
        lines.append(f"ALARM {alarm['alarm']}: " + ", ".join(f"{k} {v}" for k, v in alarm.items() if k != "alarm"))
    if result["not_applicable"]:
        lines.append("n/a: " + "; ".join(result["not_applicable"]))
    lines.append("healthy" if not result["alarms"] else f"{len(result['alarms'])} alarm(s)")
    return "\n".join(lines)


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", default=str(HERE.parent.parent), help="the repository (default: the one holding this tool)")
    p.add_argument("--now", default="", help="the instant to judge at, ISO 8601 UTC (default: now)")
    p.add_argument("--format", choices=("text", "json"), default="text")
    p.add_argument("--no-session", action="store_true", help="skip the session check (no relay call)")
    p.add_argument("--session", default="", help="the strategist's session id (default: its TEAM.yaml entry)")
    p.add_argument("--untracked-hours", type=float, default=2)
    p.add_argument("--fresh-hours", type=float, default=12)
    p.add_argument("--min-sample", type=int, default=5)
    p.add_argument("--hit-target", type=float, default=80)
    p.add_argument("--hit-tolerance", type=float, default=20)
    p.add_argument("--brier-limit", type=float, default=0.25)
    p.add_argument("--bias-limit", type=float, default=20)
    p.add_argument("--context-percent", type=float, default=75)
    a = p.parse_args(argv)
    now = stamp(a.now) if a.now else datetime.now(timezone.utc)
    root = Path(a.root)
    if now is None or not root.is_dir():
        print("strategist_health: bad --now or --root", file=sys.stderr)
        return 2
    try:
        result = evaluate(root, now, a)
    except OSError as error:
        print(f"strategist_health: cannot read the repository: {error}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=1, sort_keys=True) if a.format == "json" else render(result))
    return 1 if result["alarms"] else 0


if __name__ == "__main__":
    sys.exit(main())
