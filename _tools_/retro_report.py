#!/usr/bin/env python3
"""Retro report - the aggregation half of the retro review.

Implements the aggregation specification of the retro review
mechanism (_conventions_/local-conventions/task-unit-queue-design.md,
section 14). The daily retro pass reads people-written judgement;
this tool produces the numbers it cites. It aggregates the unit
results in the done pool by task type (regular), per local day and
over a rolling window, and writes a machine-readable metrics
appendix into _records_/retro/ for the day retro file to cite -

  _records_/retro/<end-date>-data.json   canonical metrics
  _records_/retro/<end-date>-data.md     the same metrics as tables

Both outputs are overwritten, never appended, and are a pure
function of the pool state: a re-run over the same window and the
same pool produces identical files (the appendix states the pool
state it was derived from as a hash over the scanned units, so a
reader can tell whether the pool moved between runs).

What is counted, per section 14 -

  - execution count and the full status distribution;
  - target attainment, achieved over target, summed over the
    units that carry both figures and as a per-unit mean ratio;
  - resources gained itemised by type, and points, with output
    per minute against total execution minutes;
  - total duration and median duration;
  - the top repeated blockers, by blocker_category (the miss
    audit classes a to i) and by the named blocker when a unit
    records one in stats.blocker;
  - the unverified closing count - a unit is unverified when its
    verified does not read yes, when it closes without a result,
    or when it is missing a required stats key. The required keys
    are target, achieved, resources_gained, costs and verified,
    plus blocker_category whenever the unit fell short of its
    target or closed partial, failed or skipped-needs-owner.
    points is aggregated whenever present but is not a required
    key - it applies to scoring types only, and the pool carries
    no authoritative list of which types those are.

Data sources are only inside the repository - the done pool at
_queue_/done and, as a fallback, the day INDEX files in
_records_. A unit whose file carries no result is looked up by
unit id in its day INDEX: found there, it is counted as an
execution with status unknown and data source records-index, and
no figure is invented for it; not found, its data source is
missing. A file that cannot be parsed at all is listed under
parse_errors, never silently skipped. A regular from the
_tools_/regulars.json roster with no executions in the window is
listed under no_data_regulars, stated, not omitted.

A unit belongs to the local date of its result.finished_at in
the queue timezone (America/Los_Angeles), falling back to
started_at, planned_for, and finally the date in its file name.

Usage:
  retro_report.py [--days 7] [--end YYYY-MM-DD] [--root DIR]
                  [--out-dir DIR] [--format text|json]

--root is the repository root (default - the repository this
tool lives in); the pool is read at <root>/_queue_ and outputs
land in <root>/_records_/retro unless --out-dir says otherwise.
"""

import argparse
import hashlib
import importlib.util
import json
import os
import re
import statistics
import sys
from datetime import date, datetime, timedelta, timezone

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
TOOL_VERSION = "1.0.0"


def _load_queue():
    spec = importlib.util.spec_from_file_location(
        "lastwar_queue", os.path.join(TOOLS_DIR, "queue.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


Q = _load_queue()
parse_iso = Q.parse_iso
LOCAL_TZ = Q.LOCAL_TZ

REQUIRED_KEYS = ("target", "achieved", "resources_gained", "costs",
                 "verified")
SHORT_STATUSES = ("partial", "failed", "skipped-needs-owner")
TRUTHY = ("yes", "true", "y", "verified")
BLOCKER_CLASSES = "abcdefghi"


# ---------------------------------------------------------------------
# Value helpers
# ---------------------------------------------------------------------

def _num(value):
    """Coerce a frontmatter scalar to a number, or None."""
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        text = value.replace(",", "").strip()
        if not text:
            return None
        try:
            return float(text)
        except ValueError:
            return None
    return None


def _clean(number):
    """Render a float as an int when integral, else rounded."""
    if number is None:
        return None
    if float(number).is_integer():
        return int(number)
    return round(float(number), 4)


def _is_verified(value):
    if value is True:
        return True
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return value == 1
    if isinstance(value, str):
        return value.strip().lower() in TRUTHY
    return False


_AMOUNT_TAIL = re.compile(r"^(.+?)[\s:]+(-?[\d,]+(?:\.\d+)?)$")
_AMOUNT_HEAD = re.compile(r"^(-?[\d,]+(?:\.\d+)?)[\s:]+(.+)$")


def _parse_amount_entry(text):
    """Parse one 'name amount' or 'amount name' entry."""
    text = text.strip()
    m = _AMOUNT_TAIL.match(text)
    if m:
        return m.group(1).strip(), _num(m.group(2))
    m = _AMOUNT_HEAD.match(text)
    if m:
        return m.group(2).strip(), _num(m.group(1))
    return None, None


def _itemise(value):
    """Itemise a resources_gained or costs value.

    Returns (items, unparsed) - items maps a name to its numeric
    total, unparsed lists the raw entries no number could be
    read from, so nothing is dropped silently.
    """
    items = {}
    unparsed = []
    if isinstance(value, dict):
        for name, raw in value.items():
            number = _num(raw)
            if number is None:
                unparsed.append(f"{name}: {raw}")
            else:
                items[str(name)] = items.get(str(name), 0.0) + number
    elif isinstance(value, list):
        for entry in value:
            if isinstance(entry, str):
                name, number = _parse_amount_entry(entry)
                if number is None:
                    unparsed.append(entry)
                else:
                    items[name] = items.get(name, 0.0) + number
            else:
                unparsed.append(str(entry))
    elif isinstance(value, str) and value.strip():
        name, number = _parse_amount_entry(value)
        if number is None:
            unparsed.append(value)
        else:
            items[name] = items.get(name, 0.0) + number
    return items, unparsed


def _blocker_class(raw):
    """Normalise a blocker_category value to its audit class."""
    if raw is None:
        return None
    text = str(raw).strip().lower()
    if not text:
        return None
    if text[0] in BLOCKER_CLASSES and \
            (len(text) == 1 or text[1] in " -:"):
        return text[0]
    return text


# ---------------------------------------------------------------------
# Unit loading
# ---------------------------------------------------------------------

def _local_date(fields, unit_name):
    """The local date a unit belongs to, and how it was derived."""
    result = fields.get("result") or {}
    for key in ("finished_at", "started_at"):
        stamp = parse_iso(result.get(key, "")) if \
            isinstance(result, dict) else None
        if stamp:
            return stamp.astimezone(LOCAL_TZ).date(), f"result.{key}"
    stamp = parse_iso(fields.get("planned_for", ""))
    if stamp:
        return stamp.astimezone(LOCAL_TZ).date(), "planned_for"
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", unit_name)
    if m:
        try:
            return date(int(m.group(1)), int(m.group(2)),
                        int(m.group(3))), "file name"
        except ValueError:
            pass
    return None, "none"


def load_units(root):
    """Read the done pool. Returns (units, parse_errors, scanned).

    Each unit is a plain dict of the fields the aggregation
    needs; units without a result keep result as None and are
    resolved against the records INDEX by the caller.
    """
    folder = os.path.join(root, "_queue_", "done")
    units = []
    parse_errors = []
    scanned = 0
    if not os.path.isdir(folder):
        return units, parse_errors, scanned
    for name in sorted(os.listdir(folder)):
        if not name.endswith(".md"):
            continue
        scanned += 1
        path = os.path.join(folder, name)
        try:
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
        except OSError as exc:
            parse_errors.append({"file": name,
                                 "error": f"unreadable - {exc}"})
            continue
        if not text.startswith("---"):
            parse_errors.append({"file": name,
                                 "error": "no frontmatter block"})
            continue
        fields, _ = Q.parse_frontmatter(text)
        unit_name = str(fields.get("unit") or name[:-3])
        result = fields.get("result")
        if not isinstance(result, dict) or not result.get("status"):
            result = None
        day, date_source = _local_date(fields, unit_name)
        units.append({
            "unit": unit_name,
            "file": name,
            "regular": str(fields.get("regular") or
                           unit_name.split("-")[0]),
            "date": day,
            "date_source": date_source,
            "result": result,
            "data_source": "unit-result" if result else "missing",
        })
    return units, parse_errors, scanned


def apply_records_fallback(root, units):
    """Resolve result-less units against the day INDEX files."""
    index_cache = {}
    for unit in units:
        if unit["result"] is not None or unit["date"] is None:
            continue
        day = unit["date"].isoformat()
        if day not in index_cache:
            path = os.path.join(root, "_records_", day, "INDEX.md")
            try:
                with open(path, encoding="utf-8") as fh:
                    index_cache[day] = fh.read()
            except OSError:
                index_cache[day] = ""
        if unit["unit"] in index_cache[day]:
            unit["data_source"] = "records-index"


def roster(root):
    """The regular ids from _tools_/regulars.json, or []."""
    path = os.path.join(root, "_tools_", "regulars.json")
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, ValueError):
        return []
    items = data.get("regulars", []) if isinstance(data, dict) else data
    out = []
    for item in items:
        if isinstance(item, dict) and item.get("id"):
            out.append(str(item["id"]))
    return out


# ---------------------------------------------------------------------
# Aggregation
# ---------------------------------------------------------------------

def _empty_bucket():
    return {
        "executions": 0,
        "statuses": {},
        "durations": [],
        "duration_total": 0.0,
        "target_sum": 0.0,
        "achieved_sum": 0.0,
        "attainment_units": 0,
        "ratios": [],
        "resources_gained": {},
        "resources_unparsed": [],
        "points_total": 0.0,
        "points_units": 0,
        "costs": {},
        "blockers": {},
        "named_blockers": {},
        "unverified": 0,
        "unverified_reasons": {"verified_not_yes": 0,
                               "missing_required_stats": 0,
                               "missing_result": 0},
        "missing_key_counts": {},
    }


def _feed(bucket, unit):
    bucket["executions"] += 1
    result = unit["result"]
    if result is None:
        bucket["statuses"]["unknown"] = \
            bucket["statuses"].get("unknown", 0) + 1
        bucket["unverified"] += 1
        bucket["unverified_reasons"]["missing_result"] += 1
        return
    status = str(result.get("status"))
    bucket["statuses"][status] = bucket["statuses"].get(status, 0) + 1
    duration = _num(result.get("duration_seconds"))
    if duration is not None:
        bucket["durations"].append(duration)
        bucket["duration_total"] += duration
    stats = result.get("stats")
    if not isinstance(stats, dict):
        stats = {}
    target = _num(stats.get("target"))
    achieved = _num(stats.get("achieved"))
    if target is not None and achieved is not None:
        bucket["target_sum"] += target
        bucket["achieved_sum"] += achieved
        bucket["attainment_units"] += 1
        if target > 0:
            bucket["ratios"].append(achieved / target)
    gained, unparsed = _itemise(stats.get("resources_gained"))
    for name, number in gained.items():
        bucket["resources_gained"][name] = \
            bucket["resources_gained"].get(name, 0.0) + number
    bucket["resources_unparsed"].extend(unparsed)
    points = _num(stats.get("points"))
    if points is not None:
        bucket["points_total"] += points
        bucket["points_units"] += 1
    costs, _ = _itemise(stats.get("costs"))
    for name, number in costs.items():
        bucket["costs"][name] = bucket["costs"].get(name, 0.0) + number
    # Unverified accounting, per the section 14 definition.
    missing = [key for key in REQUIRED_KEYS if key not in stats]
    fell_short = (target is not None and achieved is not None
                  and achieved < target)
    if (fell_short or status in SHORT_STATUSES) and \
            "blocker_category" not in stats:
        missing.append("blocker_category")
    unverified = False
    if not _is_verified(stats.get("verified")):
        bucket["unverified_reasons"]["verified_not_yes"] += 1
        unverified = True
    if missing:
        bucket["unverified_reasons"]["missing_required_stats"] += 1
        unverified = True
        for key in missing:
            bucket["missing_key_counts"][key] = \
                bucket["missing_key_counts"].get(key, 0) + 1
    if unverified:
        bucket["unverified"] += 1
    category = _blocker_class(stats.get("blocker_category"))
    if category:
        bucket["blockers"][category] = \
            bucket["blockers"].get(category, 0) + 1
    named = stats.get("blocker")
    if isinstance(named, str) and named.strip():
        key = named.strip()
        bucket["named_blockers"][key] = \
            bucket["named_blockers"].get(key, 0) + 1


def _summarise(bucket):
    minutes = bucket["duration_total"] / 60.0
    out = {
        "executions": bucket["executions"],
        "statuses": dict(sorted(bucket["statuses"].items())),
        "duration_total_seconds": _clean(bucket["duration_total"]),
        "duration_median_seconds": _clean(
            statistics.median(bucket["durations"]))
            if bucket["durations"] else None,
        "target_sum": _clean(bucket["target_sum"]),
        "achieved_sum": _clean(bucket["achieved_sum"]),
        "attainment_summed": _clean(
            bucket["achieved_sum"] / bucket["target_sum"])
            if bucket["target_sum"] > 0 else None,
        "attainment_mean_ratio": _clean(
            sum(bucket["ratios"]) / len(bucket["ratios"]))
            if bucket["ratios"] else None,
        "attainment_units": bucket["attainment_units"],
        "resources_gained": {k: _clean(v) for k, v in
                             sorted(bucket["resources_gained"].items())},
        "points_total": _clean(bucket["points_total"]),
        "points_units": bucket["points_units"],
        "costs": {k: _clean(v) for k, v in
                  sorted(bucket["costs"].items())},
        "resources_per_minute": {k: _clean(v / minutes) for k, v in
                                 sorted(bucket["resources_gained"].items())}
            if minutes > 0 else {},
        "points_per_minute": _clean(bucket["points_total"] / minutes)
            if minutes > 0 else None,
        "blockers": dict(sorted(bucket["blockers"].items(),
                                key=lambda kv: (-kv[1], kv[0]))),
        "named_blockers": dict(sorted(bucket["named_blockers"].items(),
                                      key=lambda kv: (-kv[1], kv[0]))),
        "unverified": bucket["unverified"],
        "unverified_reasons": dict(bucket["unverified_reasons"]),
        "missing_key_counts": dict(sorted(
            bucket["missing_key_counts"].items())),
        "resources_unparsed_count": len(bucket["resources_unparsed"]),
    }
    return out


def aggregate(units, start, end):
    """Aggregate window units per regular, rolling and per day."""
    per_regular = {}
    totals_bucket = _empty_bucket()
    for unit in units:
        if unit["date"] is None or not (start <= unit["date"] <= end):
            continue
        entry = per_regular.setdefault(
            unit["regular"], {"rolling": _empty_bucket(), "by_day": {}})
        _feed(entry["rolling"], unit)
        day_key = unit["date"].isoformat()
        day_bucket = entry["by_day"].setdefault(day_key, _empty_bucket())
        _feed(day_bucket, unit)
        _feed(totals_bucket, unit)
    regulars = {}
    for regular in sorted(per_regular):
        entry = per_regular[regular]
        regulars[regular] = {
            "rolling": _summarise(entry["rolling"]),
            "by_day": {day: _summarise(entry["by_day"][day])
                       for day in sorted(entry["by_day"])},
        }
    return regulars, _summarise(totals_bucket)


def pool_state_hash(units):
    lines = []
    for unit in units:
        result = unit["result"] or {}
        lines.append("|".join([
            unit["unit"],
            str(result.get("finished_at", "")),
            str(result.get("status", "")),
        ]))
    digest = hashlib.sha256("\n".join(sorted(lines)).encode("utf-8"))
    return digest.hexdigest()


# ---------------------------------------------------------------------
# Outputs
# ---------------------------------------------------------------------

def render_markdown(data):
    end = data["window"]["end"]
    lines = [
        "---",
        f"title: Retro Data {end}",
        "description: Machine generated metrics appendix for the "
        "daily retro, produced by _tools_/retro_report.py",
        "generated_by: _tools_/retro_report.py",
        f"window_end: {end}",
        "---",
        "",
        f"# Retro data - window {data['window']['start']} to {end}",
        "",
        f"Window of {data['window']['days']} days ending {end}. "
        f"Derived from {data['derived_from']['done_units_scanned']} "
        f"done units ({data['derived_from']['in_window']} in window); "
        f"pool state sha256 "
        f"{data['derived_from']['pool_state_sha256']}.",
        "",
        "## Totals",
        "",
    ]
    totals = data["totals"]
    lines += [
        f"- Executions {totals['executions']}; statuses "
        + ", ".join(f"{k} {v}" for k, v in totals["statuses"].items()),
        f"- Attainment summed {totals['attainment_summed']} over "
        f"{totals['attainment_units']} units with both figures",
        f"- Duration total {totals['duration_total_seconds']}s, "
        f"median {totals['duration_median_seconds']}s",
        f"- Points {totals['points_total']}; unverified closings "
        f"{totals['unverified']}",
        "",
        "## Per regular (rolling window)",
        "",
        "| Regular | Exec | Done | Partial | Skipped | Attainment | "
        "Points | Median s | Unverified | Top blockers |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for regular, entry in data["regulars"].items():
        roll = entry["rolling"]
        blockers = ", ".join(f"{k} {v}" for k, v in
                             list(roll["blockers"].items())[:3]) or "-"
        lines.append(
            f"| {regular} | {roll['executions']} | "
            f"{roll['statuses'].get('done', 0)} | "
            f"{roll['statuses'].get('partial', 0)} | "
            f"{roll['statuses'].get('skipped-needs-owner', 0)} | "
            f"{roll['attainment_summed']} | {roll['points_total']} | "
            f"{roll['duration_median_seconds']} | "
            f"{roll['unverified']} | {blockers} |")
    lines += ["", "## No data in window", ""]
    if data["no_data_regulars"]:
        lines += [f"- {name}" for name in data["no_data_regulars"]]
    else:
        lines.append("- none")
    lines += ["", "## Records fallback units", ""]
    if data["derived_from"]["records_fallback_units"]:
        for item in data["derived_from"]["records_fallback_units"]:
            lines.append(f"- {item['unit']} - data source "
                         f"{item['data_source']}")
    else:
        lines.append("- none")
    lines += ["", "## Parse errors", ""]
    if data["parse_errors"]:
        for item in data["parse_errors"]:
            lines.append(f"- {item['file']} - {item['error']}")
    else:
        lines.append("- none")
    lines.append("")
    return "\n".join(lines)


def run(args):
    root = os.path.abspath(args.root)
    if args.end:
        end = datetime.strptime(args.end, "%Y-%m-%d").date()
    else:
        end = datetime.now(LOCAL_TZ).date()
    start = end - timedelta(days=args.days - 1)
    units, parse_errors, scanned = load_units(root)
    apply_records_fallback(root, units)
    regulars, totals = aggregate(units, start, end)
    known = roster(root)
    no_data = [name for name in known if name not in regulars]
    in_window = sum(1 for u in units if u["date"] is not None
                    and start <= u["date"] <= end)
    fallback_units = [
        {"unit": u["unit"], "data_source": u["data_source"]}
        for u in units
        if u["result"] is None and u["date"] is not None
        and start <= u["date"] <= end
    ]
    data = {
        "tool": "retro_report",
        "version": TOOL_VERSION,
        "window": {"start": start.isoformat(), "end": end.isoformat(),
                   "days": args.days},
        "derived_from": {
            "done_units_scanned": scanned,
            "in_window": in_window,
            "pool_state_sha256": pool_state_hash(units),
            "records_fallback_units": fallback_units,
        },
        "parse_errors": parse_errors,
        "totals": totals,
        "regulars": regulars,
        "no_data_regulars": no_data,
    }
    out_dir = args.out_dir or os.path.join(root, "_records_", "retro")
    os.makedirs(out_dir, exist_ok=True)
    json_path = os.path.join(out_dir, f"{end.isoformat()}-data.json")
    md_path = os.path.join(out_dir, f"{end.isoformat()}-data.md")
    with open(json_path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, sort_keys=True,
                  ensure_ascii=False)
        fh.write("\n")
    with open(md_path, "w", encoding="utf-8") as fh:
        fh.write(render_markdown(data))
    summary = {
        "window": data["window"],
        "outputs": [json_path, md_path],
        "in_window": in_window,
        "parse_errors": len(parse_errors),
        "totals": totals,
        "no_data_regulars": no_data,
    }
    if args.format == "json":
        print(json.dumps(summary, indent=2, sort_keys=True,
                         ensure_ascii=False))
    else:
        print(f"retro window {start.isoformat()} to {end.isoformat()} "
              f"({args.days} days)")
        print(f"units in window {in_window}; parse errors "
              f"{len(parse_errors)}; unverified {totals['unverified']}")
        print(f"wrote {json_path}")
        print(f"wrote {md_path}")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--days", type=int, default=7)
    parser.add_argument("--end", default="")
    parser.add_argument("--root", default=os.path.join(
        TOOLS_DIR, ".."))
    parser.add_argument("--out-dir", default="")
    parser.add_argument("--format", choices=["text", "json"],
                        default="text")
    args = parser.parse_args(argv)
    if args.days < 1:
        parser.error("--days must be at least 1")
    if args.end:
        try:
            datetime.strptime(args.end, "%Y-%m-%d")
        except ValueError:
            parser.error("--end must be YYYY-MM-DD")
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
