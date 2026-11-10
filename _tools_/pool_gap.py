#!/usr/bin/env python3
"""Branch-vs-live queue pool gap - the measurement slice of issue #251.

Issue #251 (2026-11-03 retro): at the retro snapshot the
records/2026-11-03 branch done pool held 670 units in the 7-day
window while the live working-tree pool held 756 - a gap of 86
done units, almost all of Nov 3 - because records PR 207 jammed
behind a conflict and deliveries queued behind it. The branch
inbox at the same snapshot carried 32 past-expiry units and 12
inbox copies of units already closed in done, while the live
pool showed 0 on both counts. The retro's canonical appendix
therefore understated Nov 3 as a near-empty day (16 units)
when the live day executed 95 units.

This tool does NOT fix the delivery jam: it makes the gap
measurable the same way at every snapshot, so the next retro
does not hand-count two pools out of bundles. It reads two
pool roots - a branch checkout and the live working tree -
and reports, for the same rolling window:

  done_in_window   done units dated inside the window
  done_by_date     per local date, for the dates that differ
  inbox_total      files still in inbox
  inbox_past_expiry inbox files whose parsed expires_at is
                   already past (unparsable expiry is counted
                   separately and never counted as past, the
                   same "parsed expires_at" reading #251 uses)
  inbox_done_overlap inbox unit ids already closed in done

A unit is dated by result.finished_at, else result.started_at,
else planned_for, else the date in its file name - the
retro_report.py rule, applied identically to both pools, and
without retro_report's records-INDEX fallback, so a pool is
measured purely by the files it holds. Local dates are
America/Los_Angeles, the queue timezone.

Usage:
  pool_gap.py --branch-pool DIR --live-pool DIR
              [--days 7] [--end YYYY-MM-DD] [--now ISO]
              [--format text|json]

Each pool argument is a repository root (the pool is read at
<root>/_queue_) or a _queue_ directory itself. A pool root
that holds no pool state directory is an error (exit 2),
never a silent zero: a missing branch checkout must fail
loudly instead of reporting a clean gap.

Verdict, the #251 closure rule: PASS when the absolute
done-in-window gap is under 10 units AND the branch inbox
past-expiry count is 0. Exit 0 on PASS, 1 on FAIL, 2 on a
usage or pool error.
"""

import argparse
import importlib.util
import json
import os
import re
import sys
from datetime import date, datetime, timedelta, timezone

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
TOOL_VERSION = "1.0.0"
GAP_LIMIT = 10


def _load_queue():
    spec = importlib.util.spec_from_file_location(
        "lastwar_queue", os.path.join(TOOLS_DIR, "queue.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


Q = _load_queue()
parse_iso = Q.parse_iso
LOCAL_TZ = Q.LOCAL_TZ
DATE_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})")


def resolve_pool(arg):
    """Return the _queue_ directory for a repo root or a pool dir."""
    if os.path.isdir(os.path.join(arg, "_queue_")):
        return os.path.join(arg, "_queue_")
    if os.path.isdir(os.path.join(arg, "inbox")) or \
            os.path.isdir(os.path.join(arg, "done")):
        return arg
    return None


def _local_date(fields, unit_name):
    """Local date of a done unit, following retro_report.py."""
    result = fields.get("result") or {}
    if isinstance(result, dict):
        for key in ("finished_at", "started_at"):
            stamp = parse_iso(result.get(key, ""))
            if stamp:
                return stamp.astimezone(LOCAL_TZ).date()
    stamp = parse_iso(fields.get("planned_for", ""))
    if stamp:
        return stamp.astimezone(LOCAL_TZ).date()
    m = DATE_RE.search(unit_name)
    if m:
        try:
            return date(int(m.group(1)), int(m.group(2)),
                        int(m.group(3)))
        except ValueError:
            pass
    return None


def _read_unit(path):
    """Parse one unit file; returns (fields, error or None)."""
    try:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
    except OSError as exc:
        return None, f"unreadable - {exc}"
    if not text.startswith("---"):
        return None, "no frontmatter block"
    try:
        fields, _ = Q.parse_frontmatter(text)
    except Exception as exc:  # malformed frontmatter, not a crash
        return None, f"frontmatter parse failed - {exc}"
    if not isinstance(fields, dict):
        return None, "frontmatter is not a mapping"
    return fields, None


def scan_pool(pool_dir, start, end, now):
    """Measure one pool. Returns a dict of counts and unit lists."""
    done_total = 0
    done_in_window = 0
    done_by_date = {}
    done_ids = set()
    parse_errors = []
    done_folder = os.path.join(pool_dir, "done")
    if os.path.isdir(done_folder):
        for name in sorted(os.listdir(done_folder)):
            if not name.endswith(".md"):
                continue
            fields, error = _read_unit(os.path.join(done_folder, name))
            if error is not None:
                parse_errors.append({"file": name, "error": error})
                continue
            done_total += 1
            unit = str(fields.get("unit") or name[:-3])
            done_ids.add(unit)
            day = _local_date(fields, unit)
            if day is not None and start <= day <= end:
                done_in_window += 1
                key = day.isoformat()
                done_by_date[key] = done_by_date.get(key, 0) + 1
    inbox_total = 0
    inbox_past_expiry = []
    inbox_unparsable_expiry = []
    inbox_ids = set()
    inbox_folder = os.path.join(pool_dir, "inbox")
    if os.path.isdir(inbox_folder):
        for name in sorted(os.listdir(inbox_folder)):
            if not name.endswith(".md"):
                continue
            fields, error = _read_unit(os.path.join(inbox_folder, name))
            if error is not None:
                parse_errors.append({"file": name, "error": error})
                continue
            inbox_total += 1
            unit = str(fields.get("unit") or name[:-3])
            inbox_ids.add(unit)
            raw = fields.get("expires_at", "")
            stamp = parse_iso(raw) if isinstance(raw, str) else None
            if stamp is None:
                inbox_unparsable_expiry.append(unit)
            else:
                if stamp.tzinfo is None:
                    stamp = stamp.replace(tzinfo=timezone.utc)
                if stamp < now:
                    inbox_past_expiry.append(unit)
    claimed_total = 0
    claimed_folder = os.path.join(pool_dir, "claimed")
    if os.path.isdir(claimed_folder):
        claimed_total = sum(
            1 for name in os.listdir(claimed_folder)
            if name.endswith(".md"))
    overlap = sorted(inbox_ids & done_ids)
    return {
        "done_total": done_total,
        "done_in_window": done_in_window,
        "done_by_date": done_by_date,
        "inbox_total": inbox_total,
        "inbox_past_expiry": sorted(inbox_past_expiry),
        "inbox_past_expiry_count": len(inbox_past_expiry),
        "inbox_unparsable_expiry": sorted(inbox_unparsable_expiry),
        "inbox_done_overlap": overlap,
        "inbox_done_overlap_count": len(overlap),
        "claimed_total": claimed_total,
        "parse_errors": parse_errors,
    }


def compare(branch, live, start, end):
    """Gap between the branch pool and the live pool."""
    gap = live["done_in_window"] - branch["done_in_window"]
    per_date = {}
    day = start
    while day <= end:
        key = day.isoformat()
        b = branch["done_by_date"].get(key, 0)
        lv = live["done_by_date"].get(key, 0)
        if b != lv:
            per_date[key] = {"branch": b, "live": lv, "gap": lv - b}
        day += timedelta(days=1)
    verdict_pass = abs(gap) < GAP_LIMIT and \
        branch["inbox_past_expiry_count"] == 0
    return {
        "done_in_window_gap": gap,
        "done_in_window_gap_abs": abs(gap),
        "done_by_date_gap": per_date,
        "inbox_past_expiry_gap":
            live["inbox_past_expiry_count"] -
            branch["inbox_past_expiry_count"],
        "verdict": "PASS" if verdict_pass else "FAIL",
        "verdict_rule": f"abs(done gap) < {GAP_LIMIT} and "
                        "branch inbox past-expiry == 0",
    }


def render_text(data):
    """Human-readable snapshot comparison."""
    lines = [
        f"pool gap window {data['window']['start']} to "
        f"{data['window']['end']} ({data['window']['days']} days)",
        f"branch done in window {data['branch']['done_in_window']} "
        f"(total {data['branch']['done_total']}); "
        f"live done in window {data['live']['done_in_window']} "
        f"(total {data['live']['done_total']}); "
        f"gap {data['gap']['done_in_window_gap']:+d}",
    ]
    for day in sorted(data["gap"]["done_by_date_gap"]):
        row = data["gap"]["done_by_date_gap"][day]
        lines.append(f"  {day}: branch {row['branch']} live "
                     f"{row['live']} gap {row['gap']:+d}")
    lines.append(
        f"branch inbox {data['branch']['inbox_total']} "
        f"past-expiry {data['branch']['inbox_past_expiry_count']} "
        f"done-overlap {data['branch']['inbox_done_overlap_count']}; "
        f"live inbox {data['live']['inbox_total']} "
        f"past-expiry {data['live']['inbox_past_expiry_count']} "
        f"done-overlap {data['live']['inbox_done_overlap_count']}")
    if data["branch"]["parse_errors"] or data["live"]["parse_errors"]:
        lines.append(
            f"parse errors branch "
            f"{len(data['branch']['parse_errors'])} live "
            f"{len(data['live']['parse_errors'])}")
    lines.append(f"verdict {data['gap']['verdict']} "
                 f"({data['gap']['verdict_rule']})")
    return "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Compare a branch queue pool against the live pool.")
    parser.add_argument("--branch-pool", required=True,
                        help="branch checkout root or its _queue_ dir")
    parser.add_argument("--live-pool", required=True,
                        help="live working-tree root or its _queue_ dir")
    parser.add_argument("--days", type=int, default=7)
    parser.add_argument("--end", default=None,
                        help="window end date YYYY-MM-DD, default today "
                             "in America/Los_Angeles")
    parser.add_argument("--now", default=None,
                        help="expiry comparison instant ISO, default now")
    parser.add_argument("--format", choices=("text", "json"),
                        default="text")
    args = parser.parse_args(argv)
    if args.days < 1:
        parser.error("--days must be at least 1")
    if args.end:
        try:
            end = datetime.strptime(args.end, "%Y-%m-%d").date()
        except ValueError:
            print("error: --end must be YYYY-MM-DD", file=sys.stderr)
            return 2
    else:
        end = datetime.now(LOCAL_TZ).date()
    start = end - timedelta(days=args.days - 1)
    if args.now:
        now = parse_iso(args.now)
        if now is None:
            print("error: --now is not a parseable ISO timestamp",
                  file=sys.stderr)
            return 2
        if now.tzinfo is None:
            now = now.replace(tzinfo=timezone.utc)
    else:
        now = datetime.now(timezone.utc)
    branch_dir = resolve_pool(args.branch_pool)
    live_dir = resolve_pool(args.live_pool)
    if branch_dir is None:
        print(f"error: no pool state directory under "
              f"{args.branch_pool}", file=sys.stderr)
        return 2
    if live_dir is None:
        print(f"error: no pool state directory under "
              f"{args.live_pool}", file=sys.stderr)
        return 2
    branch = scan_pool(branch_dir, start, end, now)
    live = scan_pool(live_dir, start, end, now)
    data = {
        "tool": "pool_gap",
        "version": TOOL_VERSION,
        "window": {"start": start.isoformat(), "end": end.isoformat(),
                   "days": args.days},
        "branch": branch,
        "live": live,
        "gap": compare(branch, live, start, end),
    }
    if args.format == "json":
        print(json.dumps(data, indent=2, sort_keys=True,
                         ensure_ascii=False))
    else:
        print(render_text(data), end="")
    return 0 if data["gap"]["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
