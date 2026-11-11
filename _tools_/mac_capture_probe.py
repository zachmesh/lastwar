#!/usr/bin/env python3
"""Mac screen-capture failure probe for the Last War routine.

Classifies a capture failure from the device evidence a ticker pass
already collects, so a blocked pass stops after one cheap probe
instead of burning its whole unit budget re-proving the same
failure. The diagnosis this encodes is the settled one from
zachmesh/lastwar issue #284 (40 consecutive ticker passes,
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

Version 1.1.0 adds the second, worsened form of the same outage,
first seen at ticker-0904 on 2026-11-05 (the 40th consecutive
blocked pass): the device invoke channel itself stalls - every
invoke times out (computer.session start, list_apps,
connection.health, connection.repair, session end; eight
attempts, zero responses) while device.list still reports the Mac
online with a stale last_seen. That is a different fault from the
off-screen window stream, and the Dock-icon step does not address
it: the Mac-side agent gateway likely needs a restart. The probe
must not answer such evidence with "run the checklist", because
each checklist invoke costs another 120s timeout and cannot
succeed while the channel is stalled.

Version 1.3.0 adds the third form, first seen at ticker-1259 on
2026-11-11 (issue #648): the window is on-screen and the pixel
stream works, but the window sits in Zoom to Fit at 1920x1080 (not
the windowed 642x951) and the app is not frontmost, so the canvas
takes no background input - five grounded taps on the home button
and a base building produced no change, and no remote step
restores it (the View-menu Zoom to Fit toggle is ignored without
keyboard focus, resize to 642x951 is refused, Cmd-Tab is blocked
as a system command, activate selects for background input only).
The executor reached this state by clicking the green zoom button
as an activation step: the button changes window state instead of
bringing the app forward, so it must never be used for activation.
The probe classifies this evidence as ZOOMED_WINDOW_INPUT_BLOCKED:
stop the pass, do not tap, recover with one owner mouse action on
the Mac (click the LastWar Dock icon, or un-zoom the window), then
re-probe and expect windowed 642x951 and frontmost. Every unit
entry route carries the window-state precondition - windowed
642x951 AND frontmost - before any tap; a pass that finds the
window zoomed stops and escalates instead of tapping.

This tool touches no device and no game state. It only reads an
evidence JSON file the worker assembles from its own device calls
and prints the classification. The worker runs the probe calls;
this tool is the single source of truth for what they mean.

Evidence schema (every field optional; missing means unknown):
  {
    "window": {"app": "LastWar", "on_screen": false,
               "width": 1920, "height": 1080, "x": 0, "y": 0,
               "window_id": 160366, "app_active": false},
    "view_menu": ["Landscape Orientation", "Portrait Orientation",
                  "Zoom to Fit", "Enter Full Screen"],
    "app_active": false,
    "zoom_to_fit_checked": true,
    "canvas_taps_ignored": ["home (645,949) snapped, no change",
                            "home (645,949) unsnapped, no change"],
    "capture_errors": ["Failed to start stream due to audio/video capture failure"],
    "capture_attempts": 8,
    "chrome_observes_ok": true,
    "activate": {"on_screen": false, "brought_to_front": false},
    "open_app": "outcome_unknown",
    "space_keys_dispatched": true,
    "space_switched": false,
    "invoke_timeouts": ["computer.session start", "computer.control list_apps",
                        "connection.health", "connection.repair"],
    "invoke_offline": ["computer.session start", "connection.health"],
    "invoke_responses": 0,
    "invoke_attempts": 8,
    "device_list_online": true,
    "device_last_seen_stale": true
  }
Aliases accepted: top-level "window_on_screen" for
window.on_screen, "view_menu_items" for "view_menu", "errors"
for "capture_errors", "timeouts" for "invoke_timeouts".
"invoke_timeouts" accepts a list of timed-out call names or a
plain count; "invoke_offline" accepts the same shape for calls
that returned node_offline (the device is offline) and is the
only place those calls are recorded; "invoke_responses" is the
count of invokes that returned a response (0 in a full stall),
not counting node_offline returns. "app_active" is also read
from window.app_active, and "zoom_to_fit_checked" from
window.zoom_to_fit_checked; a view_menu entry of
"Zoom to Fit (checked)" records the same checked state.
"canvas_taps_ignored" accepts a bool, a count, or a list of tap
descriptions (each tap grounded on a control that produced no
change); "taps_ignored" is accepted as an alias.

Diagnoses:
  OFF_SCREEN_WINDOW   the game window is off-screen (inactive Space)
  CAPTURE_STREAM_DOWN the screen-recording stream itself is down
  CHANNEL_STALL       the device invoke channel stalls: invokes time
                      out with zero responses, so no evidence at all
                      could be collected
  DEVICE_OFFLINE      the device is offline: invokes return
                      node_offline and device.list reports it
                      offline with no wake-up path, so no invoke
                      can run until it is back
  ZOOMED_WINDOW_INPUT_BLOCKED the window is on-screen and the
                      capture stream works, but the window sits
                      in Zoom to Fit (1920x1080, not the
                      windowed 642x951) and the app is not
                      frontmost, so the canvas takes no input
  HEALTHY             window on-screen, capture works
  UNKNOWN             evidence too thin to tell; probe steps are owed

Usage:
  mac_capture_probe.py --evidence EVIDENCE.json [--json]
  mac_capture_probe.py --probe-checklist
  mac_capture_probe.py --version

Exit codes: 0 HEALTHY, 1 UNKNOWN, 10 OFF_SCREEN_WINDOW,
11 CAPTURE_STREAM_DOWN, 12 CHANNEL_STALL, 13 DEVICE_OFFLINE,
14 ZOOMED_WINDOW_INPUT_BLOCKED.
"""

import argparse
import json
import sys

TOOL_VERSION = "1.3.0"

CAPTURE_ERROR = "Failed to start stream due to audio/video capture failure"

EXIT_HEALTHY = 0
EXIT_UNKNOWN = 1
EXIT_OFF_SCREEN = 10
EXIT_STREAM_DOWN = 11
EXIT_STALL = 12
EXIT_OFFLINE = 13
EXIT_ZOOMED = 14

DIAGNOSIS_EXIT = {
    "HEALTHY": EXIT_HEALTHY,
    "UNKNOWN": EXIT_UNKNOWN,
    "OFF_SCREEN_WINDOW": EXIT_OFF_SCREEN,
    "CAPTURE_STREAM_DOWN": EXIT_STREAM_DOWN,
    "CHANNEL_STALL": EXIT_STALL,
    "DEVICE_OFFLINE": EXIT_OFFLINE,
    "ZOOMED_WINDOW_INPUT_BLOCKED": EXIT_ZOOMED,
}

PROBE_CHECKLIST = [
    '0. If device invokes time out with no response at all, or '
    'return node_offline, do not repeat them: record each timed-out '
    'call under invoke_timeouts with invoke_responses 0, record each '
    'node_offline call under invoke_offline, and classify '
    'CHANNEL_STALL or DEVICE_OFFLINE instead of running the steps '
    'below (each one costs another timeout, and none can run while '
    'the device is offline).',
    '1. computer.control list_windows with app "LastWar" (the name '
    '"Last War" returns 0 windows): record on_screen, size, position, '
    'window_id, and whether the app is frontmost (app_active).',
    '2. computer.control inspect_menu on the View menu: record whether '
    '"Enter Full Screen" is listed (listed means windowed, not native '
    'fullscreen) or "Exit Full Screen" is listed (native fullscreen), '
    'and whether "Zoom to Fit" is checked (checked means the window '
    'is zoomed, not the windowed 642x951 layout).',
    '3. One computer.observe attempt (compact) and note the exact error.',
    '4. One control observation of a Chrome window in the same session: '
    'record whether it succeeds (channel works for other apps).',
    '5. If on_screen is false, one computer.control activate for '
    'LastWar: record on_screen and brought_to_front.',
    '6. Before any tap: the window-state precondition is windowed '
    '642x951 AND frontmost. If the window is zoomed (Zoom to Fit '
    'checked) or the app is not frontmost, do not tap: record '
    'zoom_to_fit_checked and app_active, and classify '
    'ZOOMED_WINDOW_INPUT_BLOCKED instead of tapping. Never click '
    'the green zoom button as an activation step: it changes window '
    'state instead of bringing the app forward.',
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
    "CHANNEL_STALL": (
        "Stop the pass. Do NOT re-run the probe checklist: every invoke "
        "times out while the channel is stalled, so each checklist step "
        "costs another 120s timeout and returns nothing. The Dock-icon "
        "step does not address this fault (it addresses the off-screen "
        "window stream, not a stalled invoke channel). The Mac-side "
        "agent gateway likely needs a restart; re-probe only after "
        "device.list last_seen refreshes. Record the timed-out calls "
        "under invoke_timeouts with invoke_responses 0."
    ),
    "DEVICE_OFFLINE": (
        "Stop the pass. Do NOT re-run the probe checklist: the device "
        "is offline and does not advertise a wake-up path, so no "
        "invoke can run until it is back. The Dock-icon step and the "
        "gateway restart both need the Mac reachable first. Recovery "
        "is to bring the Mac mini back online (power, wake, network), "
        "then restart the Mac-side agent gateway if invokes still "
        "stall, and re-probe only after device.list reports the "
        "device online with a fresh last_seen. Record the node_offline "
        "calls under invoke_offline."
    ),
    "ZOOMED_WINDOW_INPUT_BLOCKED": (
        "Stop the pass. Do not tap: the canvas takes no input in this "
        "state, so every further tap burns budget and cannot land, and "
        "never click the green zoom button as an activation step - it "
        "changes window state instead of bringing the app forward, "
        "and is how the window got here. Recovery is one owner step "
        "on the Mac mini, a real mouse action: click the LastWar Dock "
        "icon once, or un-zoom the window (View menu, uncheck Zoom to "
        "Fit), then re-probe and expect windowed 642x951 and "
        "frontmost (app_active true). Never use Control-Command-F or "
        "Escape on this app (both crash it). Every unit entry route "
        "carries the window-state precondition - windowed 642x951 AND "
        "frontmost - before any tap."
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


def _timeout_count(value):
    """Count invokes from a list of call names or a count."""
    if isinstance(value, list):
        return len(value)
    if isinstance(value, int) and not isinstance(value, bool):
        return value
    return 0


def _ignored_tap_count(value):
    """Count ignored taps from a bool, a count, or a list of taps."""
    if isinstance(value, bool):
        return 1 if value else 0
    if isinstance(value, list):
        return len(value)
    if isinstance(value, int):
        return value
    return 0


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
    app_active = _get(window, "app_active",
                      default=_get(evidence, "app_active"))
    zoom_checked = _get(evidence, "zoom_to_fit_checked",
                        default=_get(window, "zoom_to_fit_checked"))
    if zoom_checked is None:
        # A view_menu entry of "Zoom to Fit (checked)" records the
        # same checked state for evidence assembled by hand.
        zoom_checked = any(
            isinstance(item, str)
            and item.strip().lower() == "zoom to fit (checked)"
            for item in (view_menu or []))
    taps_ignored = _get(evidence, "canvas_taps_ignored", "taps_ignored")
    ignored_tap_count = _ignored_tap_count(taps_ignored)
    timeouts = _get(evidence, "invoke_timeouts", "timeouts")
    timeout_count = _timeout_count(timeouts)
    offline = _get(evidence, "invoke_offline", "offline")
    offline_count = _timeout_count(offline)
    responses = _get(evidence, "invoke_responses")
    device_online = _get(evidence, "device_list_online")
    last_seen_stale = _get(evidence, "device_last_seen_stale")
    missing = []
    lines = []

    if timeout_count:
        if isinstance(timeouts, list) and timeouts:
            lines.append(
                "%d device invokes timed out with no response "
                "(%s)" % (timeout_count, ", ".join(str(t) for t in timeouts)))
        else:
            lines.append(
                "%d device invokes timed out" % timeout_count)
    if offline_count:
        if isinstance(offline, list) and offline:
            lines.append(
                "%d device invokes returned node_offline "
                "(%s)" % (offline_count, ", ".join(str(t) for t in offline)))
        else:
            lines.append(
                "%d device invokes returned node_offline" % offline_count)
    if responses is not None:
        lines.append("device invokes that returned a response: %d"
                     % responses)
    if device_online is True:
        lines.append("device.list still reports the device online")
    elif device_online is False:
        lines.append("device.list reports the device offline")
    if last_seen_stale is True:
        lines.append("device.list last_seen is stale")

    if on_screen is False:
        lines.append("LastWar window_on_screen false")
    elif on_screen is True:
        lines.append("LastWar window_on_screen true")
    else:
        missing.append("list_windows with app LastWar (on_screen)")

    width = _get(window, "width")
    height = _get(window, "height")
    if width is not None and height is not None:
        lines.append("LastWar window geometry %sx%s" % (width, height))
    if app_active is True:
        lines.append("LastWar is the frontmost app (app_active true)")
    elif app_active is False:
        lines.append("LastWar is not the frontmost app (app_active false)")

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

    if zoom_checked is True:
        lines.append('View menu shows "Zoom to Fit" checked: the window '
                     "is zoomed, not the windowed 642x951 layout")

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

    if ignored_tap_count > 0:
        if isinstance(taps_ignored, list) and taps_ignored:
            lines.append(
                "%d grounded canvas tap(s) produced no change "
                "(%s)" % (ignored_tap_count,
                          ", ".join(str(t) for t in taps_ignored)))
        else:
            lines.append(
                "%d grounded canvas tap(s) produced no change"
                % ignored_tap_count)

    diagnosis = "UNKNOWN"
    confidence = "low"
    if offline_count > 0 and device_online is False:
        diagnosis = "DEVICE_OFFLINE"
        confidence = "high"
    elif (offline_count > 0 and responses is None
            and on_screen is None and not capture_errors
            and chrome_ok is None):
        diagnosis = "DEVICE_OFFLINE"
        confidence = "medium"
    elif timeout_count > 0 and responses == 0:
        diagnosis = "CHANNEL_STALL"
        confidence = "high"
    elif (timeout_count > 0 and responses is None
            and on_screen is None and not capture_errors
            and chrome_ok is None):
        diagnosis = "CHANNEL_STALL"
        confidence = "medium"
    elif on_screen is False and enter_fullscreen:
        diagnosis = "OFF_SCREEN_WINDOW"
        confidence = "high"
    elif on_screen is False and brought_to_front is False:
        diagnosis = "OFF_SCREEN_WINDOW"
        confidence = "high"
    elif on_screen is False:
        diagnosis = "OFF_SCREEN_WINDOW"
        confidence = "medium"
    elif (on_screen is True and not capture_errors and zoom_checked
            and (app_active is False or ignored_tap_count > 0)):
        # Zoom to Fit with the app not frontmost, or with grounded
        # taps already ignored: the canvas takes no input in this
        # state, so this is not a healthy window even though the
        # pixel stream works. High only when both halves of the
        # signature are present; without tap evidence the pass
        # stops on the zoomed state alone at medium confidence.
        diagnosis = "ZOOMED_WINDOW_INPUT_BLOCKED"
        confidence = ("high" if app_active is False
                      and ignored_tap_count > 0 else "medium")
    elif on_screen is True and not capture_errors:
        diagnosis = "HEALTHY"
        confidence = "high"
    elif capture_errors and chrome_ok is False and on_screen is True:
        diagnosis = "CAPTURE_STREAM_DOWN"
        confidence = "high"
    elif capture_errors and chrome_ok is False:
        diagnosis = "CAPTURE_STREAM_DOWN"
        confidence = "medium"

    if diagnosis in ("CHANNEL_STALL", "DEVICE_OFFLINE"):
        # No probe steps are owed: the checklist assumes invokes
        # return, and none can run while the channel is stalled
        # or the device is offline.
        missing = []

    return {
        "tool_version": TOOL_VERSION,
        "diagnosis": diagnosis,
        "confidence": confidence,
        "stop_pass": diagnosis in ("OFF_SCREEN_WINDOW",
                                   "CAPTURE_STREAM_DOWN",
                                   "CHANNEL_STALL",
                                   "DEVICE_OFFLINE",
                                   "ZOOMED_WINDOW_INPUT_BLOCKED"),
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
