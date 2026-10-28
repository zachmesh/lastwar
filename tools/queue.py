#!/usr/bin/env python3
"""Task unit queue for the Last War routine.

Implements the pool mechanics of the task unit queue design
(_conventions_/local-conventions/task-unit-queue-design.md): units are
Markdown files that move inbox -> claimed -> done by atomic rename,
claims carry a lease, an executor batch is bounded to 15 minutes, and
exactly one executor holds the device token at a time.

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
             [--follow-up TEXT]
  queue.py [--root DIR] release --unit UNIT      # partial: back to inbox
  queue.py [--root DIR] token-acquire --executor NAME
  queue.py [--root DIR] token-release --executor NAME
  queue.py [--root DIR] reap                      # expired leases to inbox

--root defaults to the repository _queue_ folder; tests point it at a
scratch directory.
"""

import argparse
import os
import re
import sys
from datetime import datetime, timedelta, timezone

BATCH_CAP_MINUTES = 15          # owner rule 2026-10-28
DEFAULT_LEASE_MINUTES = 20
DEFAULT_EST_MINUTES = 5
STATES = ("inbox", "claimed", "done")
TOKEN_NAME = "device-token.md"


def now_utc():
    return datetime.now(timezone.utc).replace(microsecond=0)


def iso(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_iso(text):
    if not text:
        return None
    try:
        return datetime.strptime(text, "%Y-%m-%dT%H:%M:%SZ").replace(
            tzinfo=timezone.utc)
    except ValueError:
        return None


def read_unit(path):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    fields = {}
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if m:
        for line in m.group(1).splitlines():
            if ": " in line:
                key, value = line.split(": ", 1)
                fields[key.strip()] = value.strip()
            elif line.endswith(":"):
                fields[line[:-1].strip()] = ""
    return fields, text


def write_frontmatter(path, fields, order, body):
    lines = ["---"]
    for key in order:
        value = fields.get(key, "")
        lines.append(f"{key}: {value}" if value else f"{key}:")
    lines.append("---")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n" + body)


FM_ORDER = ["unit", "regular", "activity", "segment", "priority",
            "created_at", "expires_at", "window", "est_minutes",
            "claimed_by", "claimed_at", "lease_until"]


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
            fields["_file"] = name
            out.append(fields)
    return out


def pick_key(fields):
    """Earliest expiry first, then priority, then age."""
    expires = parse_iso(fields.get("expires_at", "")) or datetime.max.replace(
        tzinfo=timezone.utc)
    try:
        priority = int(fields.get("priority", "3"))
    except ValueError:
        priority = 3
    created = parse_iso(fields.get("created_at", "")) or datetime.min.replace(
        tzinfo=timezone.utc)
    return (expires, priority, created)


def cmd_enqueue(args):
    regular = args.regular
    cycle = now_utc().strftime("%Y-%m-%d-%H%M")
    unit = f"{regular}-{cycle}"
    path = unit_path(args.root, "inbox", unit)
    if os.path.exists(path):
        print(f"already queued: {unit}")
        return 1
    fields = {
        "unit": unit,
        "regular": regular,
        "activity": args.activity or "",
        "segment": str(args.segment or ""),
        "priority": str(args.priority),
        "created_at": iso(now_utc()),
        "expires_at": args.expires_at or "",
        "window": args.window or "",
        "est_minutes": str(args.est_minutes),
        "claimed_by": "",
        "claimed_at": "",
        "lease_until": "",
    }
    body = (f"\n# {regular}\n\nProduced by tools/queue.py. The executor "
            "reads the activity metadata and the standing rules before "
            "acting.\n")
    os.makedirs(state_dir(args.root, "inbox"), exist_ok=True)
    write_frontmatter(path, fields, FM_ORDER, body)
    print(f"queued {unit}")
    return 0


def cmd_list(args):
    states = [args.state] if args.state else list(STATES)
    for state in states:
        units = list_units(args.root, state)
        print(f"{state}: {len(units)}")
        for fields in units:
            print(f"  {fields.get('unit', fields['_file'])}"
                  f"  p{fields.get('priority', '?')}"
                  f"  expires {fields.get('expires_at') or '-'}"
                  f"  by {fields.get('claimed_by') or '-'}")
    return 0


def cmd_next(args):
    candidates = [f for f in list_units(args.root, "inbox")]
    candidates.sort(key=pick_key)
    for fields in candidates:
        try:
            est = int(fields.get("est_minutes", DEFAULT_EST_MINUTES))
        except ValueError:
            est = DEFAULT_EST_MINUTES
        if est <= args.budget_minutes:
            print(fields.get("unit", ""))
            return 0
    print("")
    return 0


def cmd_claim(args):
    state, path = find_unit(args.root, args.unit)
    if state != "inbox":
        print(f"cannot claim {args.unit}: state is {state}")
        return 1
    fields, text = read_unit(path)
    body = text.split("---\n", 2)[-1] if text.startswith("---") else text
    stamp = now_utc()
    fields["claimed_by"] = args.executor
    fields["claimed_at"] = iso(stamp)
    fields["lease_until"] = iso(stamp + timedelta(minutes=args.lease_minutes))
    target = unit_path(args.root, "claimed", args.unit)
    os.rename(path, target)                      # atomic claim
    write_frontmatter(target, fields, FM_ORDER, "\n" + body.lstrip("\n"))
    print(f"claimed {args.unit} by {args.executor} "
          f"until {fields['lease_until']}")
    return 0


def cmd_complete(args):
    state, path = find_unit(args.root, args.unit)
    if state != "claimed":
        print(f"cannot complete {args.unit}: state is {state}")
        return 1
    fields, text = read_unit(path)
    claimed_items = ("[" + ", ".join(
        i.strip() for i in args.claimed_items.split(",") if i.strip()) + "]"
        if args.claimed_items else "[]")
    block = (
        "\n```yaml\nresult:\n"
        f"  status: {args.status}\n"
        f"  started_at: {fields.get('claimed_at', '')}\n"
        f"  finished_at: {iso(now_utc())}\n"
        f"  executor: {fields.get('claimed_by', '')}\n"
        f"  summary: {args.summary or ''}\n"
        f"  claimed: {claimed_items}\n"
        f"  evidence: {args.evidence or ''}\n"
        f"  follow_up: {args.follow_up or 'none'}\n"
        "```\n")
    target = unit_path(args.root, "done", args.unit)
    os.makedirs(state_dir(args.root, "done"), exist_ok=True)
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(block)
    os.rename(path, target)
    print(f"completed {args.unit} with status {args.status}")
    return 0


def cmd_release(args):
    state, path = find_unit(args.root, args.unit)
    if state != "claimed":
        print(f"cannot release {args.unit}: state is {state}")
        return 1
    fields, text = read_unit(path)
    body = text.split("---\n", 2)[-1] if text.startswith("---") else text
    for key in ("claimed_by", "claimed_at", "lease_until"):
        fields[key] = ""
    target = unit_path(args.root, "inbox", args.unit)
    os.rename(path, target)
    write_frontmatter(target, fields, FM_ORDER, "\n" + body.lstrip("\n"))
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
                  minutes=BATCH_CAP_MINUTES))}
    tmp = path + ".tmp"
    write_frontmatter(tmp, fields,
                      ["claimed_by", "claimed_at", "lease_until"],
                      "\n# Device token\n")
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
    for fields in list_units(args.root, "claimed"):
        lease = parse_iso(fields.get("lease_until", ""))
        if lease and lease <= now_utc():
            unit = fields.get("unit")
            if unit:
                class A:  # minimal arg shim for cmd_release
                    pass
                shim = A()
                shim.unit = unit
                shim.root = args.root
                if cmd_release(shim) == 0:
                    moved += 1
    print(f"reaped {moved} expired claim(s)")
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
    p.set_defaults(fn=cmd_enqueue)

    p = sub.add_parser("list")
    p.add_argument("--state", choices=STATES, default="")
    p.set_defaults(fn=cmd_list)

    p = sub.add_parser("next")
    p.add_argument("--budget-minutes", type=int, default=BATCH_CAP_MINUTES)
    p.set_defaults(fn=cmd_next)

    p = sub.add_parser("claim")
    p.add_argument("--unit", required=True)
    p.add_argument("--executor", required=True)
    p.add_argument("--lease-minutes", type=int, default=DEFAULT_LEASE_MINUTES)
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

    args = parser.parse_args(argv)
    args.root = os.path.abspath(args.root)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
