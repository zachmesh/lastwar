#!/usr/bin/env python3
"""Harvest tap verification - the tool slice of issue #250.

Issue #250 (ticker-2034 harvest unit harvest-2026-11-03-1803,
record _records_/2026-11-03/resource-collection/2034-queue-run.md):
visual grounding for "small circular resource bubble above a
building" returned factory-top markers as bubbles. Two taps at
(435,442) and (501,532) only selected Titanium Alloy Factory No.1
and No.3 (both Lv.30) and collected nothing, while the one verified
collection - the first-view teal bubble tap at (397,413) - moved
the second-row resource from 19.0M to 20.6M (+1.6M, HUD read live).
A fourth tap, the white bubble above the central house cluster at
(485,575), produced only the toast "Game season event not yet
started or has ended": a season entry icon, not a bubble.

The issue's suggested fix is what this tool implements: a harvest
tap counts as collected only when a per-tap HUD-movement check
(or bubble clearance on a follow-up screenshot) verifies it, and
grounding hits that select a building are flagged suspect-factory
and never counted. It does NOT tap, drive a device, capture
screenshots, or run visual grounding: that is game operation,
which this job does not do. It consumes the executor's tap log -
plain JSON the executor can write from the HUD reads and tap
outcomes it already records - and returns the verified count,
the per-resource deltas of verified taps only, and the re-probe
list the next harvest unit resumes from.

A tap log is a JSON list, or an object with a "taps" list.
Each tap carries:

  point            {"x": int, "y": int}, normalized 0..1000
                   coordinates, the convention already used in
                   execution records
  grounding_label  optional string, the grounding query that
                   produced the point, e.g. "small circular
                   resource bubble above a building"
  building         optional string, the building a selection
                   revealed, e.g. "Titanium Alloy Factory No.1"
  before           HUD dict {resource: value} read before the
                   tap, e.g. {"second-row": "19.0M"}
  after            HUD dict read after the tap, or null when
                   no post-tap HUD read was taken
  outcome          one of "cleared", "selected-building",
                   "toast", "still-present":
                     cleared           bubble gone on the
                                       follow-up screenshot
                     selected-building tap selected a building
                                       (panel or highlight)
                                       instead of collecting
                     toast             tap produced a toast
                                       and collected nothing
                                       (season/event icon)
                     still-present     bubble still on screen
                                       after the tap
  note             optional string, e.g. the toast text

HUD values are numbers or strings with a K/M/B suffix
("19.0M", "505.1K", "11.72K"). A key present in only one of
before/after has no baseline or no follow-up, so it cannot
prove movement and is excluded from the movement check.

Verdicts, in order (the first matching rule wins):

  not-a-bubble    outcome "toast": a season/event icon, never
                  counted and never re-probed as a bubble.
  suspect-factory outcome "selected-building": a grounding hit
                  over a factory row, never counted. No fixed
                  coordinate zone is encoded for this: camera
                  framing moves (the resource-collection location
                  map says coordinates are framing-specific), so
                  the suspect flag comes from the tap's observed
                  outcome plus the HUD check, not from a y band.
                  A bubble-icon template or colour check that
                  could reject these hits before tapping is
                  future work outside this stdlib JSON tool.
  unverified      after is null: no post-tap HUD read, so the
                  HUD-movement check was not performed; never
                  counted, even when the outcome says cleared -
                  the check the issue requires is the read
                  itself, and a missing read is not evidence.
  verified        outcome "cleared" with a post-tap HUD read:
                  a HUD resource also increased, the delta is
                  the evidence; when the rounded HUD is
                  unchanged, clearance is the evidence - the
                  2026-11-01 1149 record notes gains below the
                  0.1M display precision do not move the rounded
                  figures, so an unchanged rounded HUD alone is
                  not proof that nothing was collected. Only
                  verified taps contribute to the collected
                  count and to the reported deltas.
  suspect         outcome "still-present": the tap did not
                  collect. If a HUD resource moved anyway, the
                  movement is not attributable to this tap and
                  is reported as such, not counted.

An empty log is a valid empty result (exit 0); a malformed
entry is an input error (exit 2) naming the entry, never
silently skipped - a bad log must not masquerade as a clean
harvest, following tapcal.py and records_batch.py. A suspect
or unverified tap is a finding, not a tool failure, so the
exit code stays 0 when the log itself is well formed.

Usage:
  harvest_verify.py verify --log FILE [--format text|json]
"""

import argparse
import json
import re
import sys

TOOL_VERSION = "1.0.0"
COORD_MIN = 0
COORD_MAX = 1000

OUTCOMES = ("cleared", "selected-building", "toast", "still-present")

_VALUE_RE = re.compile(r"^\s*([0-9]+(?:\.[0-9]+)?)\s*([KMB])?\s*$")
_SUFFIX_MULTIPLIER = {"K": 1e3, "M": 1e6, "B": 1e9}


class InputError(Exception):
    """A malformed input file or entry; reported, never skipped."""


def parse_value(value, where):
    """Parse a HUD value to base units (float)."""
    if isinstance(value, bool):
        raise InputError(f"{where}: boolean is not a HUD value")
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        match = _VALUE_RE.match(value)
        if match is None:
            raise InputError(f"{where}: unparseable HUD value {value!r}")
        number = float(match.group(1))
        suffix = match.group(2)
        if suffix:
            number *= _SUFFIX_MULTIPLIER[suffix]
        return number
    raise InputError(f"{where}: HUD value must be a number or string, got {type(value).__name__}")


def format_value(number):
    """Format base units back to a HUD-style figure."""
    if number >= 1e9:
        return f"{number / 1e9:g}B"
    if number >= 1e6:
        return f"{number / 1e6:g}M"
    if number >= 1e3:
        return f"{number / 1e3:g}K"
    return f"{number:g}"


def _parse_hud(hud, where):
    if not isinstance(hud, dict):
        raise InputError(f"{where}: HUD read must be an object, got {type(hud).__name__}")
    return {key: parse_value(value, f"{where}.{key}") for key, value in hud.items()}


def _validate_point(point, where):
    if not isinstance(point, dict) or "x" not in point or "y" not in point:
        raise InputError(f"{where}: point must be an object with x and y")
    for axis in ("x", "y"):
        value = point[axis]
        if isinstance(value, bool) or not isinstance(value, int):
            raise InputError(f"{where}: point {axis} must be an int, got {value!r}")
        if not COORD_MIN <= value <= COORD_MAX:
            raise InputError(f"{where}: point {axis} {value} outside 0..1000")
    return {"x": point["x"], "y": point["y"]}


def classify_tap(tap, index):
    """Classify one harvest tap. Returns a verdict dict."""
    where = f"tap {index}"
    if not isinstance(tap, dict):
        raise InputError(f"{where}: tap must be an object")
    point = _validate_point(tap.get("point"), where)
    outcome = tap.get("outcome")
    if outcome not in OUTCOMES:
        raise InputError(f"{where}: outcome must be one of {', '.join(OUTCOMES)}, got {outcome!r}")
    if "before" not in tap:
        raise InputError(f"{where}: missing required field 'before'")
    before = _parse_hud(tap["before"], f"{where}.before")
    after_raw = tap.get("after")
    after = None if after_raw is None else _parse_hud(after_raw, f"{where}.after")
    building = tap.get("building")
    if building is not None and not isinstance(building, str):
        raise InputError(f"{where}: building must be a string")
    label = tap.get("grounding_label")
    if label is not None and not isinstance(label, str):
        raise InputError(f"{where}: grounding_label must be a string")

    if outcome == "toast":
        return {
            "point": point, "verdict": "not-a-bubble", "counted": False,
            "reason": "tap produced a toast, not a collection (season/event icon)",
            "deltas": {}, "building": building, "grounding_label": label,
        }
    if outcome == "selected-building":
        reason = "tap selected a building instead of collecting (factory-row grounding hit)"
        if building:
            reason += f": {building}"
        return {
            "point": point, "verdict": "suspect-factory", "counted": False,
            "reason": reason, "deltas": {}, "building": building,
            "grounding_label": label,
        }
    if after is None:
        return {
            "point": point, "verdict": "unverified", "counted": False,
            "reason": "no post-tap HUD read, so the HUD-movement check was not performed",
            "deltas": {}, "building": building, "grounding_label": label,
        }
    deltas = {}
    for key in before:
        if key in after and after[key] > before[key]:
            deltas[key] = after[key] - before[key]
    if outcome == "cleared":
        if deltas:
            moved = ", ".join(f"{key} {format_value(delta)}" for key, delta in deltas.items())
            reason = f"bubble cleared and HUD moved: {moved}"
        else:
            reason = ("bubble cleared; rounded HUD unchanged, which does not "
                      "disprove a collection below display precision")
        return {
            "point": point, "verdict": "verified", "counted": True,
            "reason": reason, "deltas": deltas, "building": building,
            "grounding_label": label,
        }
    # outcome == "still-present"
    if deltas:
        moved = ", ".join(f"{key} {format_value(delta)}" for key, delta in deltas.items())
        reason = (f"bubble still on screen; HUD moved ({moved}) but the "
                  "movement is not attributable to this tap")
    else:
        reason = "bubble still on screen and HUD unchanged: tap did not collect"
    return {
        "point": point, "verdict": "suspect", "counted": False,
        "reason": reason, "deltas": {}, "building": building,
        "grounding_label": label,
    }


def verify_taps(taps):
    """Verify a whole tap log. Returns the summary dict."""
    if not isinstance(taps, list):
        raise InputError("log must be a JSON list or an object with a 'taps' list")
    results = [classify_tap(tap, index) for index, tap in enumerate(taps)]
    deltas = {}
    for result in results:
        if result["counted"]:
            for key, delta in result["deltas"].items():
                deltas[key] = deltas.get(key, 0.0) + delta
    counts = {}
    for verdict in ("verified", "suspect-factory", "suspect", "not-a-bubble", "unverified"):
        counts[verdict] = sum(1 for r in results if r["verdict"] == verdict)
    re_probe = [
        {"point": r["point"], "verdict": r["verdict"], "reason": r["reason"]}
        for r in results if r["verdict"] in ("suspect-factory", "suspect", "unverified")
    ]
    return {
        "tool": "harvest_verify",
        "version": TOOL_VERSION,
        "total": len(results),
        "collected": counts["verified"],
        "counts": counts,
        "deltas": deltas,
        "taps": results,
        "re_probe": re_probe,
    }


def load_log(path):
    try:
        with open(path, "r", encoding="utf-8") as handle:
            data = json.load(handle)
    except OSError as exc:
        raise InputError(f"cannot read {path}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise InputError(f"{path} is not valid JSON: {exc}") from exc
    if isinstance(data, list):
        return data
    if isinstance(data, dict) and isinstance(data.get("taps"), list):
        return data["taps"]
    raise InputError(f"{path}: log must be a JSON list or an object with a 'taps' list")


def render_text(summary):
    lines = [
        f"harvest verify: {summary['total']} taps, "
        f"{summary['collected']} verified collected, "
        f"{summary['counts']['suspect-factory']} suspect-factory, "
        f"{summary['counts']['suspect']} suspect, "
        f"{summary['counts']['not-a-bubble']} not-a-bubble, "
        f"{summary['counts']['unverified']} unverified",
    ]
    if summary["deltas"]:
        moved = ", ".join(f"{key} +{format_value(delta)}" for key, delta in summary["deltas"].items())
        lines.append(f"deltas (verified taps only): {moved}")
    else:
        lines.append("deltas (verified taps only): none")
    if summary["re_probe"]:
        lines.append("re-probe (not counted; prefer first-view teal bubbles next):")
        for item in summary["re_probe"]:
            point = item["point"]
            lines.append(f"  ({point['x']},{point['y']}) {item['verdict']}: {item['reason']}")
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(prog="harvest_verify.py")
    sub = parser.add_subparsers(dest="command", required=True)
    verify = sub.add_parser("verify", help="verify a harvest tap log")
    verify.add_argument("--log", required=True, help="JSON tap log file")
    verify.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args(argv)
    try:
        summary = verify_taps(load_log(args.log))
    except InputError as exc:
        print(f"harvest_verify: error: {exc}", file=sys.stderr)
        return 2
    if args.format == "json":
        print(json.dumps(summary, indent=2, sort_keys=True))
    else:
        print(render_text(summary))
    return 0


if __name__ == "__main__":
    sys.exit(main())
