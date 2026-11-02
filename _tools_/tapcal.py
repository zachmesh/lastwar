#!/usr/bin/env python3
"""Tap calibration and scoring - the measurement half of issue #123.

Issue #123 (IMP-20261101-08, owner direction of 2026-11-01) asked
for screenshot-grounded tap calibration and verification tooling:
measured coordinates instead of eye estimates, a tap-verify loop,
per-activity visual reference anchors, and a per-session systematic
offset measured against a fixed anchor and stored as compensation.
The 2026-11-01 urgent harvest that prompted it needed five owner
corrections inside one unit, and no first-try tap rate was measured
anywhere yet.

This tool is deliberately only the measurement half, in the same
way earlier tool-developer PRs shipped a measurement half first
(stall_expired triage, PR 146; stall-evidence stats, PR 163).
It does NOT tap, drive a device, or capture screenshots: that is
game operation, which this job does not do. It consumes the
executor's tap log and anchor observations - both plain JSON the
executor can write from the grounding coordinates it already
records - and returns measured numbers the retro can read:

  score      - first-try success rate, owner-correction count,
               miss vectors and the median miss, overall and
               per activity, from a tap log.
  calibrate  - the systematic offset of a session from anchor
               observations (observed minus expected, median),
               plus its spread, so a scattered set of misses is
               not mistaken for a systematic offset.
  compensate - the aim point for a target under a stored
               compensation: aim = target - offset, clamped to
               the coordinate range. The sign is the whole point:
               if taps land offset dx to the right of where they
               were aimed, aiming dx to the left lands on target.
  anchor-add / anchor-list - the per-activity visual reference
               anchor store: activity, anchor name, normalized
               coordinates, landmark and screenshot reference,
               which executors ground against before tapping.

Coordinates are the normalized 0..1000 convention already used
in execution records (norm x,y, x right, y down). Every value
is validated: a coordinate outside 0..1000, a missing required
field, or a malformed entry is an input error (exit 2) naming
the entry, never silently skipped - a bad log must not
masquerade as a clean day, following records_batch.py.

A tap log is a JSON list, or an object with a "taps" list.
Each tap attempt carries:

  activity          string, e.g. "resource-collection"
  target            {"x": int, "y": int}, the grounded target
  tapped            {"x": int, "y": int} or null, where the tap
                    actually landed (null when no tap was placed)
  changed           bool, whether the game state changed
  attempt           int >= 1, 1 for the first try at that target
  owner_correction  bool, default false, whether the owner had
                    to correct this tap
  session           optional string, for grouping only

First-try success is attempt == 1 and changed == true. The
first-try rate is null, not zero, when a log carries no
first-try taps: zero taps is no evidence, not a 0% rate.
An empty log is a valid empty result (exit 0); a malformed log
is an error (exit 2).

Anchor observations for `calibrate` are a JSON list, or an
object with an "observations" list, of:

  anchor    string, the fixed reference, e.g. "top-resource-bar"
  expected  {"x": int, "y": int}, where the anchor should be
  observed  {"x": int, "y": int}, where grounding found it
  activity  optional string

Calibrating from zero observations is an error: no observations
means no offset, not a zero offset.

Usage:
  tapcal.py score --log FILE [--format text|json]
  tapcal.py calibrate --observations FILE [--format text|json]
                      [--out FILE]
  tapcal.py compensate --comp FILE --x N --y N [--format text|json]
  tapcal.py anchor-add --store FILE --activity A --name N
                       --x X --y Y [--landmark L] [--screenshot S]
  tapcal.py anchor-list --store FILE [--format text|json]

The compensation file for `compensate` is the JSON object
`calibrate` writes with --out (or an equivalent {"dx":..,
"dy":..} object). Exit codes: 0 success (even when the rate
is low - a low rate is a finding, not a tool failure), 2 on
any usage or input error.
"""

import argparse
import json
import statistics
import sys

TOOL_VERSION = "1.0.0"
COORD_MIN = 0
COORD_MAX = 1000


class InputError(Exception):
    """A malformed input file or argument; reported, never skipped."""


def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as handle:
            return json.load(handle)
    except OSError as exc:
        raise InputError(f"cannot read {path}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise InputError(f"{path} is not valid JSON: {exc}") from exc


def extract_list(data, key, path):
    if isinstance(data, list):
        return data
    if isinstance(data, dict) and isinstance(data.get(key), list):
        return data[key]
    raise InputError(
        f"{path}: expected a JSON list or an object with a {key!r} list"
    )


def check_point(point, where):
    if not isinstance(point, dict):
        raise InputError(f"{where}: expected an object with x and y")
    for axis in ("x", "y"):
        value = point.get(axis)
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise InputError(f"{where}: {axis} must be a number, got {value!r}")
        if not COORD_MIN <= value <= COORD_MAX:
            raise InputError(
                f"{where}: {axis}={value} outside {COORD_MIN}..{COORD_MAX}"
            )
    return {"x": point["x"], "y": point["y"]}


def check_bool(value, where, default=False):
    if value is None:
        return default
    if not isinstance(value, bool):
        raise InputError(f"{where}: expected true or false, got {value!r}")
    return value


def parse_tap(entry, index):
    where = f"tap entry {index}"
    if not isinstance(entry, dict):
        raise InputError(f"{where}: expected an object")
    activity = entry.get("activity")
    if not isinstance(activity, str) or not activity:
        raise InputError(f"{where}: activity must be a non-empty string")
    if "target" not in entry:
        raise InputError(f"{where}: missing required field 'target'")
    target = check_point(entry["target"], f"{where} target")
    tapped = entry.get("tapped")
    if tapped is not None:
        tapped = check_point(tapped, f"{where} tapped")
    changed = check_bool(entry.get("changed"), f"{where} changed")
    if entry.get("changed") is None:
        raise InputError(f"{where}: missing required field 'changed'")
    attempt = entry.get("attempt")
    if isinstance(attempt, bool) or not isinstance(attempt, int) or attempt < 1:
        raise InputError(f"{where}: attempt must be an integer >= 1")
    owner_correction = check_bool(
        entry.get("owner_correction"), f"{where} owner_correction"
    )
    return {
        "activity": activity,
        "target": target,
        "tapped": tapped,
        "changed": changed,
        "attempt": attempt,
        "owner_correction": owner_correction,
    }


def rate(successes, total):
    if total == 0:
        return None
    return successes / total


def score_taps(taps):
    per_activity = {}
    first_try = 0
    first_try_success = 0
    retries = 0
    owner_corrections = 0
    miss_dx = []
    miss_dy = []
    for tap in taps:
        bucket = per_activity.setdefault(
            tap["activity"],
            {
                "taps": 0,
                "first_try_taps": 0,
                "first_try_successes": 0,
                "owner_corrections": 0,
            },
        )
        bucket["taps"] += 1
        if tap["owner_correction"]:
            owner_corrections += 1
            bucket["owner_corrections"] += 1
        if tap["attempt"] == 1:
            first_try += 1
            bucket["first_try_taps"] += 1
            if tap["changed"]:
                first_try_success += 1
                bucket["first_try_successes"] += 1
            elif tap["tapped"] is not None:
                miss_dx.append(tap["tapped"]["x"] - tap["target"]["x"])
                miss_dy.append(tap["tapped"]["y"] - tap["target"]["y"])
        else:
            retries += 1
    for bucket in per_activity.values():
        bucket["first_try_rate"] = rate(
            bucket["first_try_successes"], bucket["first_try_taps"]
        )
    return {
        "tool": "tapcal",
        "version": TOOL_VERSION,
        "taps_total": len(taps),
        "first_try_taps": first_try,
        "first_try_successes": first_try_success,
        "first_try_rate": rate(first_try_success, first_try),
        "retries": retries,
        "owner_corrections": owner_corrections,
        "first_try_misses_with_vector": len(miss_dx),
        "median_miss_dx": statistics.median(miss_dx) if miss_dx else None,
        "median_miss_dy": statistics.median(miss_dy) if miss_dy else None,
        "per_activity": dict(sorted(per_activity.items())),
    }


def parse_observation(entry, index):
    where = f"observation {index}"
    if not isinstance(entry, dict):
        raise InputError(f"{where}: expected an object")
    anchor = entry.get("anchor")
    if not isinstance(anchor, str) or not anchor:
        raise InputError(f"{where}: anchor must be a non-empty string")
    if "expected" not in entry or "observed" not in entry:
        raise InputError(f"{where}: missing 'expected' or 'observed'")
    expected = check_point(entry["expected"], f"{where} expected")
    observed = check_point(entry["observed"], f"{where} observed")
    return {
        "anchor": anchor,
        "dx": observed["x"] - expected["x"],
        "dy": observed["y"] - expected["y"],
    }


def calibrate_observations(observations):
    if not observations:
        raise InputError("calibrate: no observations, cannot compute an offset")
    dxs = [item["dx"] for item in observations]
    dys = [item["dy"] for item in observations]
    median_dx = statistics.median(dxs)
    median_dy = statistics.median(dys)
    return {
        "tool": "tapcal",
        "version": TOOL_VERSION,
        "dx": median_dx,
        "dy": median_dy,
        "n": len(observations),
        "anchors": sorted({item["anchor"] for item in observations}),
        "spread_dx": max(abs(value - median_dx) for value in dxs),
        "spread_dy": max(abs(value - median_dy) for value in dys),
    }


def compensate_point(comp, x, y):
    dx = comp["dx"]
    dy = comp["dy"]
    aimed_x = int(round(x - dx))
    aimed_y = int(round(y - dy))
    clamped_axes = []
    if aimed_x < COORD_MIN:
        aimed_x = COORD_MIN
        clamped_axes.append("x")
    if aimed_x > COORD_MAX:
        aimed_x = COORD_MAX
        clamped_axes.append("x")
    if aimed_y < COORD_MIN:
        aimed_y = COORD_MIN
        clamped_axes.append("y")
    if aimed_y > COORD_MAX:
        aimed_y = COORD_MAX
        clamped_axes.append("y")
    return {
        "tool": "tapcal",
        "version": TOOL_VERSION,
        "target": {"x": x, "y": y},
        "offset": {"dx": dx, "dy": dy},
        "compensated": {"x": aimed_x, "y": aimed_y},
        "clamped": bool(clamped_axes),
        "clamped_axes": clamped_axes,
    }


def parse_comp(data, path):
    if not isinstance(data, dict):
        raise InputError(f"{path}: expected a compensation object")
    for axis in ("dx", "dy"):
        value = data.get(axis)
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise InputError(f"{path}: {axis} must be a number, got {value!r}")
    return {"dx": data["dx"], "dy": data["dy"]}


def parse_anchor(entry, index):
    where = f"anchor entry {index}"
    if not isinstance(entry, dict):
        raise InputError(f"{where}: expected an object")
    for field in ("activity", "name"):
        value = entry.get(field)
        if not isinstance(value, str) or not value:
            raise InputError(f"{where}: {field} must be a non-empty string")
    point = check_point(
        {"x": entry.get("x"), "y": entry.get("y")}, f"{where} coordinates"
    )
    landmark = entry.get("landmark", "")
    screenshot = entry.get("screenshot", "")
    for field, value in (("landmark", landmark), ("screenshot", screenshot)):
        if not isinstance(value, str):
            raise InputError(f"{where}: {field} must be a string")
    return {
        "activity": entry["activity"],
        "name": entry["name"],
        "x": point["x"],
        "y": point["y"],
        "landmark": landmark,
        "screenshot": screenshot,
    }


def load_anchor_store(path):
    data = load_json(path)
    entries = extract_list(data, "anchors", path)
    return [parse_anchor(entry, index) for index, entry in enumerate(entries)]


def fmt_score(result):
    lines = [
        f"first-try taps: {result['first_try_taps']}",
        f"first-try successes: {result['first_try_successes']}",
        (
            "first-try rate: "
            + (
                f"{result['first_try_rate']:.3f}"
                if result["first_try_rate"] is not None
                else "none (no first-try taps)"
            )
        ),
        f"retries: {result['retries']}",
        f"owner corrections: {result['owner_corrections']}",
        f"first-try misses with vector: {result['first_try_misses_with_vector']}",
        f"median miss dx: {result['median_miss_dx']}",
        f"median miss dy: {result['median_miss_dy']}",
    ]
    for activity, bucket in result["per_activity"].items():
        rate_text = (
            f"{bucket['first_try_rate']:.3f}"
            if bucket["first_try_rate"] is not None
            else "none"
        )
        lines.append(
            f"{activity}: first-try {bucket['first_try_successes']}/"
            f"{bucket['first_try_taps']} ({rate_text}), "
            f"owner corrections {bucket['owner_corrections']}"
        )
    return "\n".join(lines) + "\n"


def fmt_calibrate(result):
    return (
        f"offset dx: {result['dx']}\n"
        f"offset dy: {result['dy']}\n"
        f"observations: {result['n']}\n"
        f"anchors: {', '.join(result['anchors'])}\n"
        f"spread dx: {result['spread_dx']}\n"
        f"spread dy: {result['spread_dy']}\n"
    )


def fmt_compensate(result):
    target = result["target"]
    comp = result["compensated"]
    return (
        f"target: {target['x']},{target['y']}\n"
        f"offset: {result['offset']['dx']},{result['offset']['dy']}\n"
        f"compensated: {comp['x']},{comp['y']}\n"
        f"clamped: {result['clamped']}\n"
    )


def fmt_anchors(anchors):
    if not anchors:
        return "no anchors\n"
    lines = []
    for item in anchors:
        extra = ""
        if item["landmark"]:
            extra += f" landmark={item['landmark']}"
        if item["screenshot"]:
            extra += f" screenshot={item['screenshot']}"
        lines.append(
            f"{item['activity']}/{item['name']}: "
            f"{item['x']},{item['y']}{extra}"
        )
    return "\n".join(lines) + "\n"


def build_parser():
    parser = argparse.ArgumentParser(prog="tapcal.py")
    sub = parser.add_subparsers(dest="command", required=True)

    score = sub.add_parser("score", help="score a tap log")
    score.add_argument("--log", required=True)
    score.add_argument("--format", choices=("text", "json"), default="text")

    calib = sub.add_parser("calibrate", help="offset from anchor observations")
    calib.add_argument("--observations", required=True)
    calib.add_argument("--format", choices=("text", "json"), default="text")
    calib.add_argument("--out", default=None)

    comp = sub.add_parser("compensate", help="aim point under a compensation")
    comp.add_argument("--comp", required=True)
    comp.add_argument("--x", required=True, type=float)
    comp.add_argument("--y", required=True, type=float)
    comp.add_argument("--format", choices=("text", "json"), default="text")

    add = sub.add_parser("anchor-add", help="upsert one anchor in a store")
    add.add_argument("--store", required=True)
    add.add_argument("--activity", required=True)
    add.add_argument("--name", required=True)
    add.add_argument("--x", required=True, type=float)
    add.add_argument("--y", required=True, type=float)
    add.add_argument("--landmark", default="")
    add.add_argument("--screenshot", default="")

    lst = sub.add_parser("anchor-list", help="list anchors in a store")
    lst.add_argument("--store", required=True)
    lst.add_argument("--format", choices=("text", "json"), default="text")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        if args.command == "score":
            data = load_json(args.log)
            entries = extract_list(data, "taps", args.log)
            taps = [parse_tap(entry, i) for i, entry in enumerate(entries)]
            result = score_taps(taps)
            if args.format == "json":
                print(json.dumps(result, indent=2, sort_keys=True))
            else:
                print(fmt_score(result), end="")
            return 0

        if args.command == "calibrate":
            data = load_json(args.observations)
            entries = extract_list(data, "observations", args.observations)
            observations = [
                parse_observation(entry, i) for i, entry in enumerate(entries)
            ]
            result = calibrate_observations(observations)
            if args.out:
                try:
                    with open(args.out, "w", encoding="utf-8") as handle:
                        json.dump(result, handle, indent=2, sort_keys=True)
                        handle.write("\n")
                except OSError as exc:
                    raise InputError(
                        f"cannot write {args.out}: {exc}"
                    ) from exc
            if args.format == "json":
                print(json.dumps(result, indent=2, sort_keys=True))
            else:
                print(fmt_calibrate(result), end="")
            return 0

        if args.command == "compensate":
            comp = parse_comp(load_json(args.comp), args.comp)
            point = check_point({"x": args.x, "y": args.y}, "target")
            result = compensate_point(comp, point["x"], point["y"])
            if args.format == "json":
                print(json.dumps(result, indent=2, sort_keys=True))
            else:
                print(fmt_compensate(result), end="")
            return 0

        if args.command == "anchor-add":
            try:
                anchors = load_anchor_store(args.store)
            except InputError as exc:
                if "cannot read" in str(exc):
                    anchors = []
                else:
                    raise
            new = parse_anchor(
                {
                    "activity": args.activity,
                    "name": args.name,
                    "x": args.x,
                    "y": args.y,
                    "landmark": args.landmark,
                    "screenshot": args.screenshot,
                },
                "new anchor",
            )
            anchors = [
                item
                for item in anchors
                if (item["activity"], item["name"])
                != (new["activity"], new["name"])
            ]
            anchors.append(new)
            anchors.sort(key=lambda item: (item["activity"], item["name"]))
            try:
                with open(args.store, "w", encoding="utf-8") as handle:
                    json.dump({"anchors": anchors}, handle, indent=2)
                    handle.write("\n")
            except OSError as exc:
                raise InputError(f"cannot write {args.store}: {exc}") from exc
            print(f"anchor {new['activity']}/{new['name']}: {new['x']},{new['y']}")
            return 0

        if args.command == "anchor-list":
            anchors = load_anchor_store(args.store)
            anchors.sort(key=lambda item: (item["activity"], item["name"]))
            if args.format == "json":
                print(json.dumps({"anchors": anchors}, indent=2))
            else:
                print(fmt_anchors(anchors), end="")
            return 0

        return 2
    except InputError as exc:
        print(f"tapcal: error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
