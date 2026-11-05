#!/usr/bin/env python3
"""Mac screen-capture failure probe for the Last War routine.

Classifies a capture failure from the device evidence a ticker pass
already collects, so a blocked pass stops after one cheap probe
instead of burning its whole unit budget re-proving the same
failure. The diagnosis this encodes is the settled one from
zachmesh/lastwar issue #284 (27 consecutive ticker passes,
2026-11-04/05): the LastWar window sits windowed 1920x1080 on an
inactive Space - list_windows reports window_on_screen false and
the View menu still lists "Enter Full Screen", so the app is not
in native fullscreen and the capture stream cannot start because
it is the pixel stream of an off-screen window. Chrome windows
observe normally in the same sessions, so the channel itself is
fine. Background-sent Space keys (Ctrl+arrows, Mission Control)
do not switch Spaces, open_app returns outcome_unknown, and
set_window_frame is gated on a fresh observation of the window,
so no background control route unblocks this state: recovery is
one owner step on the Mac mini - click the LastWar Dock icon once
(or run _tools_/mac_lastwar_front.sh in Terminal) - then re-probe.

This tool touches no device and no game state. It only reads an
evidence JSON file the worker assembles from its own device calls
and prints the classification. The worker runs the probe calls;
this tool is the single source of truth for what they mean.

Evidence schema (every field optional; missing means unknown):
  {
    "window": {"app": "LastWar", "on_screen": false,
               "width": 1920, "height": 1080, "x": 0, "y": 0,
               "window_id": 160366},
    "view_menu": ["Landscape Orientation", "Portrait Orientation",
                  "Zoom to Fit", "Enter Full Screen"],
    "capture_errors": ["Failed to start stream due to audio/video capture failure"],
    "capture_attempts": 8,
    "chrome_observes_ok": true,
    "activate": {"on_screen": false, "brought_to_front": false},
    "open_app": "outcome_unknown",
    "space_keys_dispatched": true,
    "space_switched": false
  }
Aliases accepted: top-level "window_on_screen" for
window.on_screen, "view_menu_items" for "view_menu", "errors"
for "capture_errors".

Diagnoses:
  OFF_SCREEN_WINDOW   the game window is off-screen (inactive Space)
  CAPTURE_STREAM_DOWN the screen-recording stream itself is down
  HEALTHY             window on-screen, capture works
  UNKNOWN             evidence too thin to tell; probe steps are owed

Usage:
  mac_capture_probe.py --evidence EVIDENCE.json [--json]
  mac_capture_probe.py --probe-checklist
  mac_capture_probe.py --version

Exit codes: 0 HEALTHY, 1 UNKNOWN, 10 OFF_SCREEN_WINDOW,
11 CAPTURE_STREAM_DOWN.
"""

import argparse
import json
import sys

TOOL_VERSION = "1.0.0"

CAPTURE_ERROR = "Failed to start stream due to audio/video capture failure"

EXIT_HEALTHY = 0
EXIT_UNKNOWN = 1
EXIT_OFF_SCREEN = 10
EXIT_STREAM_DOWN = 11

DIAGNOSIS_EXIT = {
    "HEALTHY": EXIT_HEALTHY,
    "UNKNOWN": EXIT_UNKNOWN,
    "OFF_SCREEN_WINDOW": EXIT_OFF_SCREEN,
    "CAPTURE_STREAM_DOWN": EXIT_STREAM_DOWN,
}

PROBE_CHECKLIST = [
    '1. computer.control list_windows with app "LastWar" (the name '
    '"Last War" returns 0 windows): record on_screen, size, position, '
    'window_id.',
    '2. computer.control inspect_menu on the View menu: record whether '
    '"Enter Full Screen" is listed (listed means windowed, not native '
    'fullscreen) or "Exit Full Screen" is listed (native fullscreen).',
    '3. One computer.observe attempt (compact) and note the exact error.',
    '4. One control observation of a Chrome window in the same session: '
    'record whether it succeeds (channel works for other apps).',
    '5. If on_screen is false, one computer.control activate for '
    'LastWar: record on_screen and brought_to_front.',
    'Stop after the checklist. Do not repeat capture attempts: with '
    'the off-screen signature, further attempts cannot succeed.',
]

RECOVERY_OWNER_STEP = (
    "Recovery is one owner step on the Mac mini: click the LastWar Dock "
    "icon once (or run _tools_/mac_lastwar_front.sh in Terminal), then "
    "re-probe with this tool and expect window_on_screen true. Never "
    "use Control-Command-F or Escape on this app (both crash it); "
    "fullscreen, if wanted, is the green zoom button / View menu only "
    "after the window is back on the active Space."
)

RECOMMENDATIONS = {
    "OFF_SCREEN_WINDOW": (
        "Stop the pass. Do not burn further capture attempts: the pixel "
        "stream of an off-screen window cannot start. " + RECOVERY_OWNER_STEP
    ),
    "CAPTURE_STREAM_DOWN": (
        "Stop the pass; the screen-recording stream itself is down "
        "(other apps fail too). Check connection.health, then "
        "connection.repair on the web gateway, then the Mac's Screen "
        "Recording permission for the control channel; re-probe."
    ),
    "HEALTHY": "Proceed: the window is on-screen and capture works.",
    "UNKNOWN": (
        "Probe incomplete - run the checklist "
        "(--probe-checklist) and classify again with the new evidence."
    ),
}


def _get(evidence, *names, default=None):
    for name in names:
        if name in evidence and evidence[name] is not None:
            return evidence[name]
    return default


def classify(evidence):
    """Classify capture-failure evidence into a diagnosis dict.

    Pure function of the evidence: classifying the same evidence
    twice returns an identical dict.
    """
    evidence = dict(evidence or {})
    window = _get(evidence, "window", default={}) or {}
    on_screen = _get(window, "on_screen",
                     default=_get(evidence, "window_on_screen"))
    view_menu = _get(evidence, "view_menu", "view_menu_items", default=[])
    capture_errors = _get(evidence, "capture_errors", "errors", default=[])
    chrome_ok = _get(evidence, "chrome_observes_ok")
    activate = _get(evidence, "activate", default={}) or {}
    missing = []
    lines = []

    if on_screen is False:
        lines.append("LastWar window_on_screen false")
    elif on_screen is True:
        lines.append("LastWar window_on_screen true")
    else:
        missing.append("list_windows with app LastWar (on_screen)")

    enter_fullscreen = any(
        isinstance(item, str) and item.strip() == "Enter Full Screen"
        for item in (view_menu or []))
    exit_fullscreen = any(
        isinstance(item, str) and item.strip() == "Exit Full Screen"
        for item in (view_menu or []))
    if enter_fullscreen:
        lines.append('View menu lists "Enter Full Screen": windowed, '
                     "not native fullscreen")
    elif exit_fullscreen:
        lines.append('View menu lists "Exit Full Screen": native fullscreen')
    elif view_menu:
        lines.append("View menu read, no fullscreen entry named")
    else:
        missing.append("View-menu inspect (Enter/Exit Full Screen)")

    if capture_errors:
        lines.append("capture error: %s (x%d)"
                     % (capture_errors[0], len(capture_errors)))
    else:
        missing.append("one observe attempt with its exact error")

    if chrome_ok is True:
        lines.append("Chrome window observes normally in the same session")
    elif chrome_ok is False:
        lines.append("Chrome window observation also fails")
    else:
        missing.append("one control observation of a Chrome window")

    activate_on_screen = _get(activate, "on_screen")
    brought_to_front = _get(activate, "brought_to_front")
    if activate:
        lines.append("activate reports on_screen=%s brought_to_front=%s"
                     % (activate_on_screen, brought_to_front))

    diagnosis = "UNKNOWN"
    confidence = "low"
    if on_screen is False and enter_fullscreen:
        diagnosis = "OFF_SCREEN_WINDOW"
        confidence = "high"
    elif on_screen is False and brought_to_front is False:
        diagnosis = "OFF_SCREEN_WINDOW"
        confidence = "high"
    elif on_screen is False:
        diagnosis = "OFF_SCREEN_WINDOW"
        confidence = "medium"
    elif on_screen is True and not capture_errors:
        diagnosis = "HEALTHY"
        confidence = "high"
    elif capture_errors and chrome_ok is False and on_screen is True:
        diagnosis = "CAPTURE_STREAM_DOWN"
        confidence = "high"
    elif capture_errors and chrome_ok is False:
        diagnosis = "CAPTURE_STREAM_DOWN"
        confidence = "medium"

    return {
        "tool_version": TOOL_VERSION,
        "diagnosis": diagnosis,
        "confidence": confidence,
        "stop_pass": diagnosis in ("OFF_SCREEN_WINDOW",
                                   "CAPTURE_STREAM_DOWN"),
        "evidence": lines,
        "missing_probe_steps": missing,
        "recommendation": RECOMMENDATIONS[diagnosis],
    }


def format_text(result):
    out = ["diagnosis: %s (%s confidence)"
           % (result["diagnosis"], result["confidence"]),
           "stop_pass: %s" % ("yes" if result["stop_pass"] else "no")]
    if result["evidence"]:
        out.append("evidence:")
        out.extend("  - %s" % line for line in result["evidence"])
    if result["missing_probe_steps"]:
        out.append("missing probe steps:")
        out.extend("  - %s" % step
                   for step in result["missing_probe_steps"])
    out.append("recommendation: %s" % result["recommendation"])
    return "\n".join(out) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence", default="",
                        help="JSON file with the probe evidence")
    parser.add_argument("--json", action="store_true",
                        help="print the classification as JSON")
    parser.add_argument("--probe-checklist", action="store_true",
                        help="print the ordered device-call checklist")
    parser.add_argument("--version", action="store_true",
                        help="print the tool version and exit")
    args = parser.parse_args(argv)

    if args.version:
        print(TOOL_VERSION)
        return 0
    if args.probe_checklist:
        print("\n".join(PROBE_CHECKLIST))
        return 0
    if not args.evidence:
        parser.error("--evidence is required (or use --probe-checklist)")

    with open(args.evidence, "r", encoding="utf-8") as handle:
        evidence = json.load(handle)
    if not isinstance(evidence, dict):
        parser.error("evidence file must hold one JSON object")

    result = classify(evidence)
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(format_text(result), end="")
    return DIAGNOSIS_EXIT[result["diagnosis"]]


if __name__ == "__main__":
    sys.exit(main())
