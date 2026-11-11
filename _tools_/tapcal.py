#!/usr/bin/env python3
"""Tap calibration, scoring and the tap-verify loop decision - the measurement half of issue #123 plus the loop-decision half (verification clause 2).

Issue #123 (IMP-20261101-08, owner direction of 2026-11-01) asked
for screenshot-grounded tap calibration and verification tooling:
measured coordinates instead of eye estimates, a tap-verify loop,
per-activity visual reference anchors, and a per-session systematic
offset measured against a fixed anchor and stored as compensation.
The 2026-11-01 urgent harvest that prompted it needed five owner
corrections inside one unit, and no first-try tap rate was measured
anywhere yet.

This tool is the measurement half plus the tap-verify loop
decision, in the same way earlier tool-developer PRs shipped a
measurement half first (stall_expired triage, PR 146;
stall-evidence stats, PR 163). It does NOT tap, drive a device,
or capture screenshots: that is game operation, which this job
does not do. It consumes the executor's tap log and anchor
observations - both plain JSON the executor can write from the
grounding coordinates it already records - and returns measured
numbers the retro can read:

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
  verify       - one step of the tap-verify loop for a single
               target: given the attempts so far (aim, where the
               tap landed, whether the state changed, where
               grounding found the element afterwards), decide
               verified / retry with a compensated next aim /
               exhausted / unverified / input-blocked. A tap
               that lands exactly on the target and changes
               nothing is "ignored", not a miss: a retry would
               re-aim at the same point, so the loop verdict
               is input-blocked and the recovery is to re-front
               the app and re-probe (issue #575). The loop
               itself still runs with the executor; this
               subcommand is the decision the loop feeds on, so
               a miss is measured and the retry aim is computed,
               never eye-estimated again.

Window geometry (issue #475, 2026-11-08): five taps on the
Alliance button in fullscreen (1920x1080) never opened the
panel, while the same button in the 642x951 window opened at
once - the taps land somewhere other than the requested point
in fullscreen, or the app ignores them there. Until the
verification unit measures it, do NOT enter fullscreen for
tap work; stay in the 642x951 windowed geometry. This tool
carries that measurement: every tap attempt and every anchor
observation may name its window geometry, `score` breaks the
first-try rate and the median miss down by geometry, and
`calibrate` refuses to mix geometries - a single offset across
windowed and fullscreen observations would hide exactly the
fullscreen-only shift #475 is about. The two geometries seen
so far are "windowed-642x951" and "fullscreen-1920x1080";
any other non-empty string is accepted and grouped as-is.
A 2026-11-10 session (issue #575) measured the fullscreen
offset by three agreeing cursor reads at about +70 right,
-14 up, and a tap aimed at the compensated point worked, so
a fullscreen offset is real and compensable through
`calibrate` / `compensate`. The same session also had taps
landing exactly on target ignored in both geometries: that
is input-blocked, not geometry, and `verify` names it so
instead of retrying the same aim.

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
  geometry          optional string, the window geometry the tap
                    was placed in, e.g. "windowed-642x951" or
                    "fullscreen-1920x1080"; absent means the log
                    predates geometry recording and the tap is
                    grouped under "unspecified" in the
                    by-geometry breakdown

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
  geometry  optional string, the window geometry the observation
            was made in (see the tap log above); calibrating
            observations that span more than one geometry without
            --geometry is an error, so a fullscreen-only shift is
            never averaged away into a windowed offset

Calibrating from zero observations is an error: no observations
means no offset, not a zero offset.

Usage:
  tapcal.py score --log FILE [--format text|json]
  tapcal.py calibrate --observations FILE [--format text|json]
                      [--out FILE] [--geometry G]
  tapcal.py compensate --comp FILE --x N --y N [--format text|json]
  tapcal.py anchor-add --store FILE --activity A --name N
                       --x X --y Y [--landmark L] [--screenshot S]
  tapcal.py anchor-list --store FILE [--format text|json]
  tapcal.py verify --case FILE [--format text|json]
  tapcal.py variant --control CLASS [--format text|json]
  tapcal.py variant --list [--format text|json]

A verification case for `verify` is a JSON object:

  activity          string, e.g. "resource-collection"
  target            {"x": int, "y": int}, the grounded target
  geometry          optional string, the window geometry of this
                    target's attempts; one case covers one
                    geometry only, so a fullscreen-only shift is
                    never averaged into a windowed loop (issue
                    #475)
  compensation      optional {"dx": .., "dy": ..} session offset
                    from `calibrate`
  control           optional string, the control class of the
                    target, e.g. "top-bar-icon" or
                    "collect-button" (issue #646); names the
                    first-try variant for a not-started case
  max_retries       optional int >= 0, default 2; the loop allows
                    1 + max_retries attempts in total
  attempts          list, in order, of:
    attempt         int, consecutive from 1
    aim             {"x": int, "y": int}, where the executor aimed
    tapped          {"x": int, "y": int} or null, where the tap
                    actually landed (null when no tap was placed)
    changed         bool, whether the game state changed
    variant         optional "snapped" or "unsnapped", the
                    background-click variant the tap used
                    (issue #646)
    observed        {"x": int, "y": int} or null, where grounding
                    found the element after the tap (null when
                    it was not re-grounded)

A verified attempt ends the loop, so no attempt may follow one.
The verdict is verified when any attempt changed the state;
not-started when no attempt exists yet (the next aim is the
target under the session compensation, when one is given);
input-blocked when the last attempt landed exactly on the
target and changed nothing (issue #575): no next aim is
given, because a retry would re-aim at the same point - the
recovery is to re-front the app and re-probe instead;
exhausted when 1 + max_retries attempts all missed; unverified
when the last attempt carries no measurement at all (no tap
placed and no re-grounding) and no retry aim can be computed;
otherwise retry, with the next aim shifted by the measured
landing error: aim + (observed - tapped) when both ends were
measured, aim + (target - tapped) when the element was never
re-grounded, and the re-grounded element under the session
compensation when no tap was placed. A next aim is rounded to
integers and clamped to 0..1000, with clamped axes named.

Per-control tap variant (issue #646): the background-click
variant that works flips by control type inside one unit -
resource top-bar icons open on an unsnapped tap (snapped taps
did nothing twice on the coin icon), panel Collect buttons
collect on a snapped tap (an unsnapped Collect did not
register). `variant` reports the measured first-try variant
for a control class; `verify` takes an optional control class
and an optional variant per attempt. When the last attempt
landed exactly on the target and changed nothing, the verdict
is retry-variant-flip instead of input-blocked when the other
variant has not yet been tried on target: the next aim is the
same point with the flipped variant, because a wrong-variant
tap is not input-blocked (issue #575 names the state only
once both variants have been tried on target with no change).
A variant flip is a changed method under R2, not a retry of
the same method, so it outranks the count-based exhausted
verdict, and it can fire at most once per target. The rows
are provisional: one unit of evidence (ticker-1104 harvest
1155, session cc-600, 2026-11-11); a second confirming unit
promotes a row to confirmed. `changed` must come from the
post-tap read (Owned/Available), not the receipt verdict -
the coin Collect receipt said no change while Owned had moved.

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

TOOL_VERSION = "1.4.0"
COORD_MIN = 0
COORD_MAX = 1000

# Window geometries seen in execution records (issue #475).
# Taps and observations carry one of these labels, or any other
# non-empty string; a missing geometry groups under UNSPECIFIED.
GEOMETRY_UNSPECIFIED = "unspecified"
GEOMETRY_WINDOWED = "windowed-642x951"
GEOMETRY_FULLSCREEN = "fullscreen-1920x1080"

# Background-click variants (issue #646). A tap is delivered
# either snapped to the control (snap_to_control true) or
# unsnapped (exact pointer). Which one works flips by control
# type inside one unit, so the loop must never repeat the same
# variant after a no-change tap.
VARIANT_SNAPPED = "snapped"
VARIANT_UNSNAPPED = "unsnapped"

# Measured first-try variant per control class (issue #646).
# One unit of evidence so far: ticker-1104 harvest unit 1155,
# session cc-600, 2026-11-11, windowed 642x951. Both rows are
# provisional until a second unit confirms them; the tool
# reports the status and the unit count so no executor treats
# a single-unit finding as established. The 0909 harvest unit
# the same day found panel X buttons ignoring both variants,
# and the 0541 donations unit found a back arrow ignoring
# three variants, so the table claims nothing beyond the two
# measured classes.
CONTROL_VARIANTS = {
    "top-bar-icon": {
        "first_try": VARIANT_UNSNAPPED,
        "status": "provisional",
        "units": 1,
        "issue": 646,
        "evidence": (
            "two snapped taps on the coin icon (575,55) did "
            "nothing; one unsnapped tap at the same point "
            "opened the panel at once; food (248,55) and iron "
            "(414,55) opened on the first unsnapped tap"
        ),
    },
    "collect-button": {
        "first_try": VARIANT_SNAPPED,
        "status": "provisional",
        "units": 1,
        "issue": 646,
        "evidence": (
            "coin Collect did not register on an unsnapped "
            "tap at (751,584); a snapped tap at (751,580) "
            "collected at once (Owned 130,716,351 to "
            "131,920,128); food and iron Collects landed on "
            "the first snapped tap"
        ),
    },
}


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


def check_geometry(value, where):
    if value is None:
        return None
    if not isinstance(value, str) or not value:
        raise InputError(f"{where}: expected a non-empty string, got {value!r}")
    return value


def check_variant(value, where):
    if value is None:
        return None
    if value not in (VARIANT_SNAPPED, VARIANT_UNSNAPPED):
        raise InputError(
            f"{where}: variant must be 'snapped' or 'unsnapped', "
            f"got {value!r}"
        )
    return value


def check_control(value, where):
    if value is None:
        return None
    if not isinstance(value, str) or not value:
        raise InputError(f"{where}: expected a non-empty string, got {value!r}")
    if value not in CONTROL_VARIANTS:
        known = ", ".join(sorted(CONTROL_VARIANTS))
        raise InputError(
            f"{where}: unknown control class {value!r}; "
            f"known classes: {known}"
        )
    return value


def variant_advice(control):
    """Measured first-try variant advice for a control class."""
    row = CONTROL_VARIANTS[control]
    return {
        "tool": "tapcal",
        "version": TOOL_VERSION,
        "control": control,
        "first_try": row["first_try"],
        "status": row["status"],
        "units": row["units"],
        "issue": row["issue"],
        "evidence": row["evidence"],
        "rule": (
            "on a no-change tap that lands on target, flip the "
            "variant before re-aiming; never repeat the same "
            "variant after a no-change"
        ),
        "note": (
            "changed must come from the post-tap read "
            "(Owned/Available), not the receipt verdict"
        ),
    }


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
    geometry = check_geometry(entry.get("geometry"), f"{where} geometry")
    return {
        "activity": activity,
        "target": target,
        "tapped": tapped,
        "changed": changed,
        "attempt": attempt,
        "owner_correction": owner_correction,
        "geometry": geometry,
    }


def rate(successes, total):
    if total == 0:
        return None
    return successes / total


def new_bucket():
    return {
        "taps": 0,
        "first_try_taps": 0,
        "first_try_successes": 0,
        "owner_corrections": 0,
        "first_try_misses_with_vector": 0,
        "miss_dx": [],
        "miss_dy": [],
    }


def finalize_bucket(bucket):
    bucket["first_try_rate"] = rate(
        bucket["first_try_successes"], bucket["first_try_taps"]
    )
    bucket["median_miss_dx"] = (
        statistics.median(bucket["miss_dx"]) if bucket["miss_dx"] else None
    )
    bucket["median_miss_dy"] = (
        statistics.median(bucket["miss_dy"]) if bucket["miss_dy"] else None
    )
    del bucket["miss_dx"]
    del bucket["miss_dy"]
    return bucket


def score_taps(taps):
    per_activity = {}
    by_geometry = {}
    first_try = 0
    first_try_success = 0
    retries = 0
    owner_corrections = 0
    miss_dx = []
    miss_dy = []
    for tap in taps:
        activity_bucket = per_activity.setdefault(tap["activity"], new_bucket())
        geometry_key = tap["geometry"] or GEOMETRY_UNSPECIFIED
        geometry_bucket = by_geometry.setdefault(geometry_key, new_bucket())
        for bucket in (activity_bucket, geometry_bucket):
            bucket["taps"] += 1
            if tap["owner_correction"]:
                bucket["owner_corrections"] += 1
            if tap["attempt"] == 1:
                bucket["first_try_taps"] += 1
                if tap["changed"]:
                    bucket["first_try_successes"] += 1
                elif tap["tapped"] is not None:
                    bucket["first_try_misses_with_vector"] += 1
                    bucket["miss_dx"].append(
                        tap["tapped"]["x"] - tap["target"]["x"]
                    )
                    bucket["miss_dy"].append(
                        tap["tapped"]["y"] - tap["target"]["y"]
                    )
        if tap["owner_correction"]:
            owner_corrections += 1
        if tap["attempt"] == 1:
            first_try += 1
            if tap["changed"]:
                first_try_success += 1
            elif tap["tapped"] is not None:
                miss_dx.append(tap["tapped"]["x"] - tap["target"]["x"])
                miss_dy.append(tap["tapped"]["y"] - tap["target"]["y"])
        else:
            retries += 1
    for bucket in per_activity.values():
        finalize_bucket(bucket)
    for bucket in by_geometry.values():
        finalize_bucket(bucket)
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
        "by_geometry": dict(sorted(by_geometry.items())),
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
    geometry = check_geometry(entry.get("geometry"), f"{where} geometry")
    return {
        "anchor": anchor,
        "dx": observed["x"] - expected["x"],
        "dy": observed["y"] - expected["y"],
        "geometry": geometry,
    }


def calibrate_observations(observations, geometry=None):
    if not observations:
        raise InputError("calibrate: no observations, cannot compute an offset")
    if geometry is not None:
        matched = [item for item in observations if item["geometry"] == geometry]
        if not matched:
            raise InputError(
                f"calibrate: no observations for geometry {geometry!r}"
            )
        observations = matched
    else:
        seen = sorted(
            {item["geometry"] for item in observations if item["geometry"]}
        )
        if len(seen) > 1:
            raise InputError(
                "calibrate: observations span more than one geometry "
                f"({', '.join(seen)}); pass --geometry to calibrate one "
                "geometry at a time, so a fullscreen-only shift is never "
                "averaged away into a windowed offset (issue #475)"
            )
        geometry = seen[0] if seen else None
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
        "geometry": geometry,
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
    if result["by_geometry"]:
        lines.append("by geometry:")
        for geometry, bucket in result["by_geometry"].items():
            rate_text = (
                f"{bucket['first_try_rate']:.3f}"
                if bucket["first_try_rate"] is not None
                else "none"
            )
            miss_text = (
                f"{bucket['median_miss_dx']},{bucket['median_miss_dy']}"
                if bucket["median_miss_dx"] is not None
                else "none"
            )
            lines.append(
                f"  {geometry}: first-try {bucket['first_try_successes']}/"
                f"{bucket['first_try_taps']} ({rate_text}), "
                f"owner corrections {bucket['owner_corrections']}, "
                f"median miss {miss_text}"
            )
    return "\n".join(lines) + "\n"


def fmt_calibrate(result):
    lines = [
        f"offset dx: {result['dx']}",
        f"offset dy: {result['dy']}",
        f"observations: {result['n']}",
        f"anchors: {', '.join(result['anchors'])}",
        f"spread dx: {result['spread_dx']}",
        f"spread dy: {result['spread_dy']}",
    ]
    if result["geometry"] is not None:
        lines.append(f"geometry: {result['geometry']}")
    return "\n".join(lines) + "\n"


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


def fmt_num(value):
    """Render a coordinate or offset without a trailing .0."""
    return str(int(value)) if float(value).is_integer() else str(value)


def shift_aim(aim, dx, dy):
    """Aim shifted by (dx, dy), rounded to integers, clamped to 0..1000.

    Returns (point, clamped_axes).
    """
    shifted = {
        "x": int(round(aim["x"] + dx)),
        "y": int(round(aim["y"] + dy)),
    }
    clamped_axes = []
    for axis in ("x", "y"):
        if shifted[axis] < COORD_MIN:
            shifted[axis] = COORD_MIN
            clamped_axes.append(axis)
        elif shifted[axis] > COORD_MAX:
            shifted[axis] = COORD_MAX
            clamped_axes.append(axis)
    return shifted, clamped_axes


def parse_verify_attempt(entry, index):
    where = f"verify attempt {index}"
    if not isinstance(entry, dict):
        raise InputError(f"{where}: expected an object")
    attempt = entry.get("attempt")
    if isinstance(attempt, bool) or not isinstance(attempt, int) or attempt < 1:
        raise InputError(f"{where}: attempt must be an integer >= 1")
    if "aim" not in entry:
        raise InputError(f"{where}: missing required field 'aim'")
    aim = check_point(entry["aim"], f"{where} aim")
    tapped = entry.get("tapped")
    if tapped is not None:
        tapped = check_point(tapped, f"{where} tapped")
    if entry.get("changed") is None:
        raise InputError(f"{where}: missing required field 'changed'")
    changed = check_bool(entry.get("changed"), f"{where} changed")
    variant = check_variant(entry.get("variant"), f"{where} variant")
    observed = entry.get("observed")
    if observed is not None:
        observed = check_point(observed, f"{where} observed")
    return {
        "attempt": attempt,
        "aim": aim,
        "tapped": tapped,
        "changed": changed,
        "variant": variant,
        "observed": observed,
    }


def parse_verify_case(data, path):
    if not isinstance(data, dict):
        raise InputError(f"{path}: expected a verification case object")
    activity = data.get("activity")
    if not isinstance(activity, str) or not activity:
        raise InputError(f"{path}: activity must be a non-empty string")
    if "target" not in data:
        raise InputError(f"{path}: missing required field 'target'")
    target = check_point(data["target"], f"{path} target")
    geometry = check_geometry(data.get("geometry"), f"{path} geometry")
    control = check_control(data.get("control"), f"{path} control")
    compensation = data.get("compensation")
    if compensation is not None:
        compensation = parse_comp(compensation, f"{path} compensation")
    max_retries = data.get("max_retries", 2)
    if (
        isinstance(max_retries, bool)
        or not isinstance(max_retries, int)
        or max_retries < 0
    ):
        raise InputError(f"{path}: max_retries must be an integer >= 0")
    attempts_data = data.get("attempts", [])
    if not isinstance(attempts_data, list):
        raise InputError(f"{path}: attempts must be a list")
    attempts = [
        parse_verify_attempt(entry, i) for i, entry in enumerate(attempts_data)
    ]
    for position, attempt in enumerate(attempts):
        if attempt["attempt"] != position + 1:
            raise InputError(
                f"verify attempt {position}: attempt must be "
                f"{position + 1}, got {attempt['attempt']} "
                "(attempts are consecutive from 1)"
            )
    for position, attempt in enumerate(attempts[:-1]):
        if attempt["changed"]:
            raise InputError(
                f"verify attempt {position}: changed is true before the "
                "last attempt - a verified tap ends the loop, later "
                "attempts must not exist"
            )
    return {
        "activity": activity,
        "target": target,
        "geometry": geometry,
        "control": control,
        "compensation": compensation,
        "max_retries": max_retries,
        "attempts": attempts,
    }


def next_aim_for(last, target, compensation):
    """Compensated next aim from the last attempt, or (None, None, []).

    `last` is None before the first tap: aim at the target under the
    session compensation. Otherwise the measured landing error is
    what the retry corrects, so a session offset is never applied
    twice: both ends measured -> aim + (observed - tapped); only
    the element re-grounded -> that element under the session
    compensation; only the tap landed -> aim + (target - tapped).
    With neither end measured there is nothing to correct from.
    """
    if last is None:
        if compensation is not None:
            result = compensate_point(compensation, target["x"], target["y"])
            return result["compensated"], "compensated-target", result["clamped_axes"]
        return dict(target), "target", []
    tapped = last["tapped"]
    observed = last["observed"]
    if tapped is not None and observed is not None:
        point, clamped = shift_aim(
            last["aim"],
            observed["x"] - tapped["x"],
            observed["y"] - tapped["y"],
        )
        return point, "measured", clamped
    if observed is not None:
        if compensation is not None:
            result = compensate_point(
                compensation, observed["x"], observed["y"]
            )
            return result["compensated"], "grounded-target", result["clamped_axes"]
        return dict(observed), "grounded-target", []
    if tapped is not None:
        point, clamped = shift_aim(
            last["aim"],
            target["x"] - tapped["x"],
            target["y"] - tapped["y"],
        )
        return point, "target-miss", clamped
    return None, None, []


def flip_variant(variant):
    """The other background-click variant (issue #646)."""
    if variant == VARIANT_SNAPPED:
        return VARIANT_UNSNAPPED
    return VARIANT_SNAPPED


def verify_case(case):
    target = case["target"]
    compensation = case["compensation"]
    attempts = case["attempts"]
    max_retries = case["max_retries"]
    control = case.get("control")
    advice = variant_advice(control) if control is not None else None
    attempt_results = []
    for attempt in attempts:
        if attempt["changed"]:
            verdict = "verified"
        elif attempt["tapped"] is not None and attempt["tapped"] == target:
            # Landed exactly on the target and changed nothing:
            # the tap reached the right pixel and the game
            # ignored it (issue #575). That is input-blocked,
            # not a miss - a retry would re-aim at this same
            # point, so it must not be scored as a miss.
            verdict = "ignored"
        elif attempt["tapped"] is not None:
            verdict = "miss"
        elif attempt["observed"] is not None:
            verdict = "re-grounded"
        else:
            verdict = "unverified"
        miss = None
        if attempt["tapped"] is not None:
            # Same convention as score: where the tap landed
            # relative to the expected target.
            miss = {
                "dx": attempt["tapped"]["x"] - target["x"],
                "dy": attempt["tapped"]["y"] - target["y"],
            }
        ground = None
        if attempt["observed"] is not None:
            # Where grounding found the element relative to the
            # expected target: the grounding error, distinct from
            # the landing error above.
            ground = {
                "dx": attempt["observed"]["x"] - target["x"],
                "dy": attempt["observed"]["y"] - target["y"],
            }
        attempt_results.append(
            {
                "attempt": attempt["attempt"],
                "verdict": verdict,
                "aim": attempt["aim"],
                "tapped": attempt["tapped"],
                "observed": attempt["observed"],
                "changed": attempt["changed"],
                "variant": attempt["variant"],
                "miss_dx": miss["dx"] if miss else None,
                "miss_dy": miss["dy"] if miss else None,
                "ground_dx": ground["dx"] if ground else None,
                "ground_dy": ground["dy"] if ground else None,
            }
        )
    # Variants already tried on target with no change: only an
    # on-target tap tests its variant (issue #646) - a tap that
    # missed the point says nothing about its variant.
    tried_on_target = {
        attempt["variant"]
        for attempt in attempts
        if attempt["variant"] is not None
        and attempt["tapped"] is not None
        and attempt["tapped"] == target
        and not attempt["changed"]
    }
    next_variant = None
    if any(result["verdict"] == "verified" for result in attempt_results):
        verdict = "verified"
        next_aim, basis, clamped = None, None, []
    elif not attempts:
        verdict = "not-started"
        next_aim, basis, clamped = next_aim_for(None, target, compensation)
        if advice is not None:
            next_variant = advice["first_try"]
    elif attempt_results and attempt_results[-1]["verdict"] == "ignored":
        last_variant = attempts[-1]["variant"]
        if (
            last_variant is not None
            and flip_variant(last_variant) not in tried_on_target
        ):
            # The last tap hit the target exactly with the wrong
            # variant and the game ignored it (issue #646): the
            # recovery is to flip the variant, not to declare
            # the input blocked. A flip is a changed method
            # under R2, not a retry of the same method, so it
            # outranks the count-based exhausted verdict, and
            # it can fire at most once per target - after the
            # flip both variants are tried and the branch below
            # names the state input-blocked.
            verdict = "retry-variant-flip"
            next_variant = flip_variant(last_variant)
            next_aim, basis, clamped = dict(target), "variant-flip", []
        else:
            # Both variants tried on target with no change, or
            # no variant recorded: the tap reached the right
            # pixel and the game ignored it (issue #575). A
            # retry would re-aim at the same point, so the loop
            # stops here whatever the retry budget: this
            # outranks the count-based exhausted verdict,
            # which would hide the cause.
            verdict = "input-blocked"
            next_aim, basis, clamped = None, None, []
    elif len(attempts) >= 1 + max_retries:
        verdict = "exhausted"
        next_aim, basis, clamped = None, None, []
    elif attempt_results[-1]["verdict"] == "unverified":
        verdict = "unverified"
        next_aim, basis, clamped = None, None, []
    else:
        verdict = "retry"
        next_aim, basis, clamped = next_aim_for(
            attempts[-1], target, compensation
        )
        # A miss is a landing error: the variant was never
        # tested on target, so the retry keeps it.
        next_variant = attempts[-1]["variant"]
    return {
        "tool": "tapcal",
        "version": TOOL_VERSION,
        "activity": case["activity"],
        "target": target,
        "geometry": case["geometry"],
        "control": control,
        "variant_advice": advice,
        "verdict": verdict,
        "attempts_used": len(attempts),
        "retries_remaining": max(0, 1 + max_retries - len(attempts)),
        "attempts": attempt_results,
        "next_aim": next_aim,
        "next_aim_basis": basis,
        "next_variant": next_variant,
        "clamped": bool(clamped),
        "clamped_axes": clamped,
    }


def fmt_verify(result):
    lines = [
        f"verdict: {result['verdict']}",
        f"attempts used: {result['attempts_used']} "
        f"(retries remaining: {result['retries_remaining']})",
    ]
    for attempt in result["attempts"]:
        detail = attempt["verdict"]
        notes = []
        if attempt["miss_dx"] is not None:
            notes.append(
                f"miss {fmt_num(attempt['miss_dx'])},"
                f"{fmt_num(attempt['miss_dy'])}"
            )
        if attempt["ground_dx"] is not None:
            notes.append(
                f"ground {fmt_num(attempt['ground_dx'])},"
                f"{fmt_num(attempt['ground_dy'])}"
            )
        if attempt["variant"] is not None:
            notes.append(f"variant {attempt['variant']}")
        if notes:
            detail += " (" + "; ".join(notes) + ")"
        lines.append(f"attempt {attempt['attempt']}: {detail}")
    if result["next_aim"] is not None:
        aim = result["next_aim"]
        lines.append(
            f"next aim: {aim['x']},{aim['y']} "
            f"(basis: {result['next_aim_basis']})"
        )
        if result["clamped"]:
            lines.append(f"clamped axes: {', '.join(result['clamped_axes'])}")
    if result["next_variant"] is not None:
        lines.append(f"next variant: {result['next_variant']}")
    if result["verdict"] == "retry-variant-flip":
        lines.append(
            "recovery: re-tap the same point with the flipped "
            "variant; verify by the post-tap read, not the receipt"
        )
    if result["verdict"] == "input-blocked":
        lines.append(
            "recovery: re-front the app (Dock icon / "
            "mac_lastwar_front.sh), then re-probe; do not retry "
            "the same aim"
        )
    return "\n".join(lines) + "\n"


def fmt_variant(advice):
    lines = [
        f"control: {advice['control']}",
        f"first-try variant: {advice['first_try']}",
        f"status: {advice['status']} "
        f"(units: {advice['units']}, issue #{advice['issue']})",
        f"evidence: {advice['evidence']}",
        f"rule: {advice['rule']}",
        f"note: {advice['note']}",
    ]
    return "\n".join(lines) + "\n"


def fmt_variant_list(rows):
    lines = []
    for advice in rows:
        lines.append(
            f"{advice['control']}: first-try {advice['first_try']} "
            f"({advice['status']}, units {advice['units']}, "
            f"issue #{advice['issue']})"
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
    calib.add_argument(
        "--geometry",
        default=None,
        help="calibrate only observations in this window geometry",
    )

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

    verify = sub.add_parser("verify", help="tap-verify loop decision for one target")
    verify.add_argument("--case", required=True)
    verify.add_argument("--format", choices=("text", "json"), default="text")

    variant = sub.add_parser(
        "variant", help="first-try tap variant for a control class"
    )
    variant.add_argument("--control", default=None)
    variant.add_argument("--list", action="store_true")
    variant.add_argument("--format", choices=("text", "json"), default="text")

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
            result = calibrate_observations(observations, args.geometry)
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

        if args.command == "verify":
            data = load_json(args.case)
            case = parse_verify_case(data, args.case)
            result = verify_case(case)
            if args.format == "json":
                print(json.dumps(result, indent=2, sort_keys=True))
            else:
                print(fmt_verify(result), end="")
            return 0

        if args.command == "variant":
            if args.list and args.control is not None:
                raise InputError("variant: pass --control or --list, not both")
            if args.list:
                rows = [
                    variant_advice(control)
                    for control in sorted(CONTROL_VARIANTS)
                ]
                if args.format == "json":
                    print(json.dumps({"variants": rows}, indent=2, sort_keys=True))
                else:
                    print(fmt_variant_list(rows), end="")
                return 0
            if args.control is None:
                raise InputError("variant: pass --control CLASS or --list")
            advice = variant_advice(
                check_control(args.control, "variant --control")
            )
            if args.format == "json":
                print(json.dumps(advice, indent=2, sort_keys=True))
            else:
                print(fmt_variant(advice), end="")
            return 0

        return 2
    except InputError as exc:
        print(f"tapcal: error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
