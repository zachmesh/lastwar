#!/usr/bin/env python3
"""Task unit queue for the Last War routine.

Implements the pool mechanics of the task unit queue design
(_conventions_/local-conventions/task-unit-queue-design.md). A task
unit is a Markdown file whose frontmatter is one structured YAML
document describing the task, its queue state and, once executed, its
result and result stats - so tools can gather status and statistics
reliably without scraping prose. Units move inbox -> claimed -> done
by atomic rename, claims carry a lease, an executor batch is bounded
to 15 minutes, and exactly one executor holds the device token.

This tool manages files only. It never touches the game or the device;
executors do the playing and call this tool around their work.

Usage:
  queue.py [--root DIR] enqueue --regular vip [--priority 1]
             [--expires-at ISO] [--est-minutes 3] [--window TEXT]
  queue.py [--root DIR] list [--state inbox|claimed|done]
  queue.py [--root DIR] next [--budget-minutes 15]
  queue.py [--root DIR] claim --unit UNIT --executor NAME
             [--lease-minutes 20]
  queue.py [--root DIR] complete --unit UNIT --status done
             [--summary TEXT] [--claimed-items a,b] [--evidence PATH]
             [--follow-up TEXT] [--stat key=value ...]
  queue.py [--root DIR] release --unit UNIT      # partial: back to inbox
  queue.py [--root DIR] token-acquire --executor NAME
  queue.py [--root DIR] token-release --executor NAME
  queue.py [--root DIR] reap                      # expired leases to inbox
  queue.py [--root DIR] stats [--format text|yaml|json]

--root defaults to the repository _queue_ folder; tests point it at a
scratch directory.

Frontmatter dialect: the small YAML subset this tool writes - plain
scalars, [a, b] flow lists, and mappings nested by 2 space indents
(the result block and its stats). No external YAML library is needed.
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone

UNIT_CAP_MINUTES = 15           # owner rule 2026-10-28: per unit
DEFAULT_LEASE_MINUTES = 20
DEFAULT_EST_MINUTES = 5
DEFAULT_MAX_ATTEMPTS = 3
STATES = ("inbox", "claimed", "done")
TOKEN_NAME = "device-token.md"
FM_ORDER = ["unit", "regular", "activity", "segment", "priority",
            "created_at", "expires_at", "window", "est_minutes",
            "chain_id", "chain_seq", "attempts", "max_attempts",
            "claimed_by", "claimed_at", "lease_until", "result"]
RESULT_ORDER = ["status", "started_at", "finished_at",
                "duration_seconds", "executor", "summary", "claimed",
                "claimed_count", "evidence", "follow_up", "stats"]


def now_utc():
    return datetime.now(timezone.utc).replace(microsecond=0)


def iso(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_iso(text):
    if not text or not isinstance(text, str):
        return None
    try:
        return datetime.strptime(text, "%Y-%m-%dT%H:%M:%SZ").replace(
            tzinfo=timezone.utc)
    except ValueError:
        return None


# ---------------------------------------------------------------------
# Frontmatter subset: parse and serialize
# ---------------------------------------------------------------------

def _scalar(text):
    text = text.strip()
    if text.startswith("[") and text.endswith("]"):
        inner = text[1:-1].strip()
        return [i.strip() for i in inner.split(",")] if inner else []
    if re.fullmatch(r"-?\d+", text):
        return int(text)
    return text


def parse_frontmatter(text):
    """Return (fields, body). fields is a nested dict."""
    m = re.match(r"---\n(.*?)\n---\n?(.*)", text, re.S)
    if not m:
        return {}, text
    fields = {}
    stack = [(-1, fields)]          # (indent, container)
    for line in m.group(1).splitlines():
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        key, _, value = line.strip().partition(":")
        key = key.strip()
        value = value.strip()
        while stack and indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]
        if value == "":
            child = {}
            parent[key] = child
            stack.append((indent, child))
        else:
            parent[key] = _scalar(value)
    return fields, m.group(2)


def _fmt(value):
    if isinstance(value, list):
        return "[" + ", ".join(str(v) for v in value) + "]"
    return str(value)


def dump_frontmatter(fields):
    lines = ["---"]
    for key in FM_ORDER:
        if key not in fields:
            continue
        value = fields[key]
        if isinstance(value, dict):
            lines.append(f"{key}:")
            order = RESULT_ORDER if key == "result" else list(value)
            for sub in order:
                if sub not in value:
                    continue
                subval = value[sub]
                if isinstance(subval, dict):
                    lines.append(f"  {sub}:")
                    for k2, v2 in subval.items():
                        lines.append(f"    {k2}: {_fmt(v2)}")
                else:
                    lines.append(f"  {sub}: {_fmt(subval)}")
        elif value in ("", None):
            lines.append(f"{key}:")
        else:
            lines.append(f"{key}: {_fmt(value)}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def read_unit(path):
    with open(path, encoding="utf-8") as fh:
        return parse_frontmatter(fh.read())


def write_unit(path, fields, body):
    if body and not body.startswith("\n"):
        body = "\n" + body
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(dump_frontmatter(fields) + body)


# ---------------------------------------------------------------------
# Pool helpers
# ---------------------------------------------------------------------

def state_dir(root, state):
    return os.path.join(root, state)


def unit_path(root, state, unit):
    return os.path.join(state_dir(root, state), unit + ".md")


def find_unit(root, unit):
    for state in STATES:
        path = unit_path(root, state, unit)
        if os.path.exists(path):
            return state, path
    return None, None


def list_units(root, state):
    folder = state_dir(root, state)
    if not os.path.isdir(folder):
        return []
    out = []
    for name in sorted(os.listdir(folder)):
        if name.endswith(".md") and name != TOKEN_NAME:
            fields, _ = read_unit(os.path.join(folder, name))
            fields["_state"] = state
            fields["_file"] = name
            out.append(fields)
    return out


def pick_key(fields):
    """Earliest expiry first, then priority, then age."""
    expires = parse_iso(fields.get("expires_at", "")) or \
        datetime.max.replace(tzinfo=timezone.utc)
    try:
        priority = int(fields.get("priority", 3))
    except (TypeError, ValueError):
        priority = 3
    created = parse_iso(fields.get("created_at", "")) or \
        datetime.min.replace(tzinfo=timezone.utc)
    return (expires, priority, created)


# ---------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------

def chain_seq_next(root, chain_id):
    seq = 0
    for state in STATES:
        for f in list_units(root, state):
            if f.get("chain_id") == chain_id:
                try:
                    seq = max(seq, int(f.get("chain_seq", 0)))
                except (TypeError, ValueError):
                    pass
    return seq + 1


def cmd_enqueue(args):
    if args.est_minutes > UNIT_CAP_MINUTES:
        print(f"refused: est_minutes {args.est_minutes} exceeds the "
              f"{UNIT_CAP_MINUTES} minute unit cap - split the task")
        return 1
    chain_seq = ""
    if args.chain_id:
        chain_seq = chain_seq_next(args.root, args.chain_id)
        unit = f"{args.regular}-{args.chain_id}-{chain_seq:03d}"
    else:
        unit = f"{args.regular}-{now_utc().strftime('%Y-%m-%d-%H%M')}"
    path = unit_path(args.root, "inbox", unit)
    if os.path.exists(path):
        print(f"already queued: {unit}")
        return 1
    fields = {
        "unit": unit, "regular": args.regular,
        "activity": args.activity or "", "segment": args.segment or "",
        "priority": args.priority,
        "created_at": iso(now_utc()),
        "expires_at": args.expires_at or "", "window": args.window or "",
        "est_minutes": args.est_minutes,
        "chain_id": args.chain_id or "", "chain_seq": chain_seq,
        "attempts": 0, "max_attempts": args.max_attempts,
        "claimed_by": "", "claimed_at": "", "lease_until": "",
    }
    body = (f"# {args.regular}\n\nProduced by tools/queue.py. The "
            "executor reads the activity metadata and the standing "
            "rules before acting.\n")
    os.makedirs(state_dir(args.root, "inbox"), exist_ok=True)
    write_unit(path, fields, body)
    print(f"queued {unit}")
    return 0


def cmd_list(args):
    for state in ([args.state] if args.state else list(STATES)):
        units = list_units(args.root, state)
        print(f"{state}: {len(units)}")
        for f in units:
            result = f.get("result", {})
            status = result.get("status", "") if isinstance(
                result, dict) else ""
            print(f"  {f.get('unit', f['_file'])}"
                  f"  p{f.get('priority', '?')}"
                  f"  expires {f.get('expires_at') or '-'}"
                  f"  by {f.get('claimed_by') or '-'}"
                  f"  {status}")
    return 0


def cmd_next(args):
    candidates = sorted(list_units(args.root, "inbox"), key=pick_key)
    for f in candidates:
        try:
            est = int(f.get("est_minutes", DEFAULT_EST_MINUTES))
        except (TypeError, ValueError):
            est = DEFAULT_EST_MINUTES
        if est <= args.budget_minutes:
            print(f.get("unit", ""))
            return 0
    print("")
    return 0


def cmd_claim(args):
    state, path = find_unit(args.root, args.unit)
    if state != "inbox":
        print(f"cannot claim {args.unit}: state is {state}")
        return 1
    fields, body = read_unit(path)
    stamp = now_utc()
    try:
        fields["attempts"] = int(fields.get("attempts", 0)) + 1
    except (TypeError, ValueError):
        fields["attempts"] = 1
    fields["claimed_by"] = args.executor
    fields["claimed_at"] = iso(stamp)
    fields["lease_until"] = iso(stamp + timedelta(
        minutes=args.lease_minutes))
    os.makedirs(state_dir(args.root, "claimed"), exist_ok=True)
    target = unit_path(args.root, "claimed", args.unit)
    os.rename(path, target)                      # atomic claim
    write_unit(target, fields, body)
    print(f"claimed {args.unit} by {args.executor} "
          f"until {fields['lease_until']}")
    return 0


def cmd_complete(args):
    state, path = find_unit(args.root, args.unit)
    if state != "claimed":
        print(f"cannot complete {args.unit}: state is {state}")
        return 1
    fields, body = read_unit(path)
    finished = now_utc()
    started = parse_iso(fields.get("claimed_at", ""))
    duration = int((finished - started).total_seconds()) if started \
        else ""
    claimed_items = [i.strip() for i in args.claimed_items.split(",")
                     if i.strip()] if args.claimed_items else []
    stats = {}
    for pair in args.stat or []:
        if "=" in pair:
            key, value = pair.split("=", 1)
            stats[key.strip()] = _scalar(value)
    fields["result"] = {
        "status": args.status,
        "started_at": fields.get("claimed_at", ""),
        "finished_at": iso(finished),
        "duration_seconds": duration,
        "executor": fields.get("claimed_by", ""),
        "summary": args.summary or "",
        "claimed": claimed_items,
        "claimed_count": len(claimed_items),
        "evidence": args.evidence or "",
        "follow_up": args.follow_up or "none",
        "stats": stats,
    }
    target = unit_path(args.root, "done", args.unit)
    os.makedirs(state_dir(args.root, "done"), exist_ok=True)
    write_unit(path, fields, body)
    os.rename(path, target)
    print(f"completed {args.unit} with status {args.status}")
    return 0


def _dead_letter(root, path, fields, body):
    fields["result"] = {
        "status": "failed",
        "started_at": fields.get("claimed_at", ""),
        "finished_at": iso(now_utc()),
        "duration_seconds": "",
        "executor": fields.get("claimed_by", ""),
        "summary": "attempts exhausted - dead lettered",
        "claimed": [], "claimed_count": 0,
        "evidence": "", "follow_up": "inspect and re-enqueue manually",
        "stats": {},
    }
    for key in ("claimed_by", "claimed_at", "lease_until"):
        fields[key] = ""
    os.makedirs(state_dir(root, "done"), exist_ok=True)
    target = unit_path(root, "done", fields.get("unit", ""))
    write_unit(path, fields, body)
    os.rename(path, target)


def _release(args, unit):
    state, path = find_unit(args.root, unit)
    if state != "claimed":
        return 1
    fields, body = read_unit(path)
    try:
        attempts = int(fields.get("attempts", 0))
        max_attempts = int(fields.get("max_attempts",
                                      DEFAULT_MAX_ATTEMPTS))
    except (TypeError, ValueError):
        attempts, max_attempts = 0, DEFAULT_MAX_ATTEMPTS
    if attempts >= max_attempts:
        _dead_letter(args.root, path, fields, body)
        return 0
    for key in ("claimed_by", "claimed_at", "lease_until"):
        fields[key] = ""
    fields.pop("result", None)
    os.makedirs(state_dir(args.root, "inbox"), exist_ok=True)
    target = unit_path(args.root, "inbox", unit)
    os.rename(path, target)
    write_unit(target, fields, body)
    return 0


def cmd_release(args):
    if _release(args, args.unit) != 0:
        print(f"cannot release {args.unit}: not claimed")
        return 1
    print(f"released {args.unit} back to inbox")
    return 0


def token_path(root):
    return os.path.join(state_dir(root, "claimed"), TOKEN_NAME)


def cmd_token_acquire(args):
    path = token_path(args.root)
    os.makedirs(state_dir(args.root, "claimed"), exist_ok=True)
    if os.path.exists(path):
        fields, _ = read_unit(path)
        lease = parse_iso(fields.get("lease_until", ""))
        if lease and lease > now_utc():
            print(f"token held by {fields.get('claimed_by', '?')} "
                  f"until {fields.get('lease_until')}")
            return 1
    fields = {"claimed_by": args.executor,
              "claimed_at": iso(now_utc()),
              "lease_until": iso(now_utc() + timedelta(
                  minutes=UNIT_CAP_MINUTES))}
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write("---\n"
                 f"claimed_by: {fields['claimed_by']}\n"
                 f"claimed_at: {fields['claimed_at']}\n"
                 f"lease_until: {fields['lease_until']}\n"
                 "---\n\n# Device token\n")
    os.rename(tmp, path)
    print(f"token acquired by {args.executor} "
          f"until {fields['lease_until']}")
    return 0


def cmd_token_release(args):
    path = token_path(args.root)
    if not os.path.exists(path):
        print("no token held")
        return 0
    fields, _ = read_unit(path)
    if fields.get("claimed_by") not in ("", args.executor):
        print(f"token held by {fields.get('claimed_by')}, not "
              f"{args.executor}")
        return 1
    os.remove(path)
    print(f"token released by {args.executor}")
    return 0


def cmd_reap(args):
    moved = 0
    stamp = now_utc()
    for f in list_units(args.root, "claimed"):
        lease = parse_iso(f.get("lease_until", ""))
        if lease and lease <= stamp and f.get("unit"):
            if _release(args, f["unit"]) == 0:
                moved += 1
    print(f"reaped {moved} expired claim(s)")
    return 0


def gather_stats(root):
    stamp = now_utc()
    report = {"generated_at": iso(stamp),
              "by_state": {}, "by_regular": {}, "durations_seconds": {},
              "late": [], "expired_waiting": [], "overdue_claims": [],
              "result_status": {}, "chains": {}}
    durations = []
    for state in STATES:
        units = list_units(root, state)
        report["by_state"][state] = len(units)
        for f in units:
            regular = f.get("regular", "?")
            entry = report["by_regular"].setdefault(
                regular, {"inbox": 0, "claimed": 0, "done": 0})
            entry[state] += 1
            chain = f.get("chain_id")
            if chain:
                centry = report["chains"].setdefault(
                    chain, {"done": 0, "pending": 0})
                if state == "done":
                    centry["done"] += 1
                else:
                    centry["pending"] += 1
            expires = parse_iso(f.get("expires_at", ""))
            result = f.get("result", {})
            if not isinstance(result, dict):
                result = {}
            if state == "inbox" and expires and expires <= stamp:
                report["expired_waiting"].append(f.get("unit"))
            if state == "claimed":
                lease = parse_iso(f.get("lease_until", ""))
                if lease and lease <= stamp:
                    report["overdue_claims"].append(f.get("unit"))
            if state == "done":
                status = result.get("status", "?")
                report["result_status"][status] = \
                    report["result_status"].get(status, 0) + 1
                dur = result.get("duration_seconds")
                if isinstance(dur, int):
                    durations.append(dur)
                finished = parse_iso(result.get("finished_at", ""))
                if expires and finished and finished > expires:
                    report["late"].append(f.get("unit"))
    if durations:
        report["durations_seconds"] = {
            "count": len(durations),
            "avg": round(sum(durations) / len(durations), 1),
            "max": max(durations)}
    return report


def cmd_stats(args):
    report = gather_stats(args.root)
    if args.format == "json":
        print(json.dumps(report, indent=2, ensure_ascii=False))
    elif args.format == "yaml":
        print("queue_stats:")
        print(f"  generated_at: {report['generated_at']}")
        print("  by_state:")
        for k, v in report["by_state"].items():
            print(f"    {k}: {v}")
        print("  result_status:")
        for k, v in report["result_status"].items():
            print(f"    {k}: {v}")
        d = report["durations_seconds"]
        if d:
            print(f"  durations_seconds: count {d['count']}, "
                  f"avg {d['avg']}, max {d['max']}")
        for key in ("late", "expired_waiting", "overdue_claims"):
            print(f"  {key}: [{', '.join(report[key])}]")
        print("  by_regular:")
        for reg, counts in sorted(report["by_regular"].items()):
            print(f"    {reg}: inbox {counts['inbox']}, "
                  f"claimed {counts['claimed']}, done {counts['done']}")
        if report["chains"]:
            print("  chains:")
            for chain, counts in sorted(report["chains"].items()):
                print(f"    {chain}: done {counts['done']}, "
                      f"pending {counts['pending']}")
    else:
        print(f"queue stats at {report['generated_at']}")
        print(f"  states: " + ", ".join(
            f"{k} {v}" for k, v in report["by_state"].items()))
        print(f"  results: " + (", ".join(
            f"{k} {v}" for k, v in report["result_status"].items())
            or "none"))
        d = report["durations_seconds"]
        if d:
            print(f"  durations: n={d['count']} avg={d['avg']}s "
                  f"max={d['max']}s")
        for key, label in (("late", "finished after expiry"),
                           ("expired_waiting", "expired in inbox"),
                           ("overdue_claims", "claims past lease")):
            if report[key]:
                print(f"  {label}: {', '.join(report[key])}")
        for reg, counts in sorted(report["by_regular"].items()):
            print(f"  {reg}: inbox {counts['inbox']}, "
                  f"claimed {counts['claimed']}, done {counts['done']}")
        for chain, counts in sorted(report["chains"].items()):
            print(f"  chain {chain}: done {counts['done']}, "
                  f"pending {counts['pending']}")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "_queue_"))
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("enqueue")
    p.add_argument("--regular", required=True)
    p.add_argument("--activity", default="")
    p.add_argument("--segment", type=int, default=0)
    p.add_argument("--priority", type=int, default=3)
    p.add_argument("--expires-at", default="")
    p.add_argument("--est-minutes", type=int, default=DEFAULT_EST_MINUTES)
    p.add_argument("--window", default="")
    p.add_argument("--chain-id", default="")
    p.add_argument("--max-attempts", type=int,
                   default=DEFAULT_MAX_ATTEMPTS)
    p.set_defaults(fn=cmd_enqueue)

    p = sub.add_parser("list")
    p.add_argument("--state", choices=STATES, default="")
    p.set_defaults(fn=cmd_list)

    p = sub.add_parser("next")
    p.add_argument("--budget-minutes", type=int, default=UNIT_CAP_MINUTES)
    p.set_defaults(fn=cmd_next)

    p = sub.add_parser("claim")
    p.add_argument("--unit", required=True)
    p.add_argument("--executor", required=True)
    p.add_argument("--lease-minutes", type=int,
                   default=DEFAULT_LEASE_MINUTES)
    p.set_defaults(fn=cmd_claim)

    p = sub.add_parser("complete")
    p.add_argument("--unit", required=True)
    p.add_argument("--status", default="done",
                   choices=["done", "partial", "failed",
                            "skipped-needs-owner"])
    p.add_argument("--summary", default="")
    p.add_argument("--claimed-items", default="")
    p.add_argument("--evidence", default="")
    p.add_argument("--follow-up", default="")
    p.add_argument("--stat", action="append", default=[])
    p.set_defaults(fn=cmd_complete)

    p = sub.add_parser("release")
    p.add_argument("--unit", required=True)
    p.set_defaults(fn=cmd_release)

    p = sub.add_parser("token-acquire")
    p.add_argument("--executor", required=True)
    p.set_defaults(fn=cmd_token_acquire)

    p = sub.add_parser("token-release")
    p.add_argument("--executor", required=True)
    p.set_defaults(fn=cmd_token_release)

    p = sub.add_parser("reap")
    p.set_defaults(fn=cmd_reap)

    p = sub.add_parser("stats")
    p.add_argument("--format", choices=["text", "yaml", "json"],
                   default="text")
    p.set_defaults(fn=cmd_stats)

    args = parser.parse_args(argv)
    args.root = os.path.abspath(args.root)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
