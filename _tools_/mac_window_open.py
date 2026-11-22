#!/usr/bin/env python3
"""Decide the session-open step from list_windows evidence.

A pass must never call open_app while the game is already running:
open_app spawns a SECOND LastWar window whose canvas takes no input,
and every tap sent to that duplicate is a no-op (zachmesh/lastwar
issue #822: ticker-1104 harvest-2026-11-22-1003 - the game was
already running in window 127196 on the Secret Command Post screen;
open_app opened window 127250 showing the same screen; 2 back-arrow
clicks, 1 double-click, 1 left_click, 1 dimmed-area tap and 2
background drags on 127250 all produced no change, while activating
the ORIGINAL window 127196 with raise=true restored input at once).
This also explains the standing Secret Command Post back-arrow
blocker (2026-11-11 0909 unit: the back arrow did not respond to
two background clicks).

This tool touches no device and no game state. It only reads an
evidence JSON file the worker assembles from its own
computer.control list_windows call and prints the exact next step.
The worker runs the device call; this tool is the single source of
truth for what the window list means.

Evidence schema (every field optional; missing means unknown):
  {
    "windows": [
      {"window_id": 127196, "app": "LastWar", "on_screen": true,
       "width": 642, "height": 951, "app_active": true,
       "focused": true},
      {"window_id": 127250, "app": "LastWar", "on_screen": true,
       "width": 642, "height": 951, "app_active": false,
       "focused": false}
    ],
    "canvas_taps_ignored": ["back arrow snapped, no change",
                            "back arrow unsnapped, no change"]
  }
A single "window" object is accepted as an alias for a one-element
"windows" list, for evidence assembled by hand. Per-window focus is
read from any of "focused", "is_focused", "frontmost", "has_focus",
"has_keyboard_focus" or "app_active" being true. Entries whose app
is not "LastWar" are ignored (list_windows must be called with app
"LastWar" - the name "Last War" returns 0 windows); entries with no
app field are counted as LastWar windows. "canvas_taps_ignored"
accepts a bool, a count, or a list of tap descriptions, and is only
used for the stuck-on-a-panel-exit reading (R2 below).

Decisions:
  OPEN_APP                  no LastWar window exists: open_app is
                            the only case it is used
  ACTIVATE_EXISTING         exactly one LastWar window: activate
                            THAT window with raise=true, never
                            open_app while it exists
  ACTIVATE_LIVE_DUPLICATE   two or more LastWar windows and the live
                            one is identified: the window holding
                            keyboard focus is live; activate it with
                            raise=true. The newer duplicate is a dead
                            input target - close it or ignore it,
                            never send canvas input to it
  DUPLICATE_UNKNOWN_LIVE    two or more LastWar windows but no focus
                            signal names the live one: stop, do not
                            tap, re-list with focus per window
  UNKNOWN                   no usable window evidence at all

R2: a pass stuck on a panel exit (grounded taps ignored) must check
list_windows for a duplicate before concluding the control is
unresponsive. When the evidence carries both a duplicate and
ignored taps, the recommendation names the duplicate as the likely
cause: the taps went to the dead window, so activate the live one
and retry the exit there.

Usage:
  mac_window_open.py --evidence EVIDENCE.json [--json]
  mac_window_open.py --open-checklist
  mac_window_open.py --version

Exit codes: 0 a session-open action is decided (OPEN_APP,
ACTIVATE_EXISTING, ACTIVATE_LIVE_DUPLICATE), 1 UNKNOWN, 2
DUPLICATE_UNKNOWN_LIVE.
"""

import argparse
import json
import sys

TOOL_VERSION = "1.0.0"

EXIT_DECIDED = 0
EXIT_UNKNOWN = 1
EXIT_DUPLICATE_UNKNOWN = 2

DECISION_EXIT = {
    "OPEN_APP": EXIT_DECIDED,
    "ACTIVATE_EXISTING": EXIT_DECIDED,
    "ACTIVATE_LIVE_DUPLICATE": EXIT_DECIDED,
    "DUPLICATE_UNKNOWN_LIVE": EXIT_DUPLICATE_UNKNOWN,
    "UNKNOWN": EXIT_UNKNOWN,
}

OPEN_CHECKLIST = [
    '0. Before any open_app: computer.control list_windows with app '
    '"LastWar" (the name "Last War" returns 0 windows). Record '
    'window_id, on_screen, size, and which window holds keyboard '
    'focus (focused / frontmost / app_active) per window.',
    '1. No LastWar window: open_app LastWar. This is the only case '
    'that opens the app.',
    '2. Exactly one LastWar window: activate that window_id with '
    'raise=true and work in it. Never open_app while it exists - '
    'open_app spawns a second window whose canvas takes no input '
    '(issue #822).',
    '3. Two or more LastWar windows: the window holding keyboard '
    'focus is the live one; activate it with raise=true. The newer '
    'duplicate is a dead input target - close it or ignore it, never '
    'send canvas input to it.',
    '4. A panel exit (e.g. the back arrow) that ignores grounded '
    'taps does not prove the control unresponsive: re-list windows '
    'first (R2). A duplicate window explains ignored taps - the '
    'taps went to the dead window, so activate the live one and '
    'retry the exit there.',
    '5. Never click the green zoom button as an activation step: it '
    'changes window state instead of bringing the app forward '
    '(issue #648).',
    'Stop after the checklist. Decide with this tool '
    '(--evidence EVIDENCE.json) before opening or tapping.',
]

FOCUS_FIELDS = ("focused", "is_focused", "frontmost", "has_focus",
                "has_keyboard_focus", "app_active", "is_active")

RECOMMENDATIONS = {
    "OPEN_APP": (
        "No LastWar window is running: open_app LastWar. This is the "
        "only case that opens the app."
    ),
    "ACTIVATE_EXISTING": (
        "The game is already running: activate the existing window "
        "with raise=true and work in it. Never open_app while it "
        "exists - open_app spawns a second window whose canvas "
        "takes no input (issue #822)."
    ),
    "ACTIVATE_LIVE_DUPLICATE": (
        "Activate the live window with raise=true and work in it. "
        "The newer duplicate is a dead input target - close it or "
        "ignore it, never send canvas input to it."
    ),
    "DUPLICATE_UNKNOWN_LIVE": (
        "Stop. Do not tap: two or more LastWar windows exist but no "
        "focus signal names the live one, so any tap may land in the "
        "dead duplicate. Re-list windows recording focus / frontmost "
        "per window, then decide again."
    ),
    "UNKNOWN": (
        "No usable window evidence - run the checklist "
        "(--open-checklist) and decide again with fresh list_windows "
        "evidence."
    ),
}


def _get(evidence, *names, default=None):
    for name in names:
        if name in evidence and evidence[name] is not None:
            return evidence[name]
    return default


def _ignored_tap_count(value):
    """Count ignored taps from a bool, a count, or a list of taps."""
    if isinstance(value, bool):
        return 1 if value else 0
    if isinstance(value, list):
        return len(value)
    if isinstance(value, int):
        return value
    return 0


def _is_focused(window):
    """True when any focus signal on this window entry is true."""
    return any(window.get(field) is True for field in FOCUS_FIELDS)


def _window_id(window):
    value = window.get("window_id")
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, str) and value.isdigit():
        return int(value)
    return None


def _describe(window):
    parts = []
    wid = _window_id(window)
    parts.append("window %s" % (wid if wid is not None else "?"))
    app = window.get("app")
    if app is not None:
        parts.append("app=%s" % app)
    on_screen = window.get("on_screen")
    if on_screen is not None:
        parts.append("on_screen=%s" % on_screen)
    width = window.get("width")
    height = window.get("height")
    if width is not None and height is not None:
        parts.append("geometry %sx%s" % (width, height))
    if _is_focused(window):
        parts.append("holds keyboard focus")
    return " ".join(parts)


def decide(evidence):
    """Decide the session-open step from list_windows evidence.

    Pure function of the evidence: deciding the same evidence
    twice returns an identical dict.
    """
    evidence = dict(evidence or {})
    windows = _get(evidence, "windows")
    if windows is None:
        single = _get(evidence, "window")
        if isinstance(single, dict):
            windows = [single]
    if isinstance(windows, dict):
        windows = [windows]
    if not isinstance(windows, list):
        windows = None

    taps_ignored = _get(evidence, "canvas_taps_ignored", "taps_ignored")
    ignored_tap_count = _ignored_tap_count(taps_ignored)

    lines = []
    missing = []
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

    if windows is None:
        missing.append('list_windows with app "LastWar"')
        return {
            "tool_version": TOOL_VERSION,
            "decision": "UNKNOWN",
            "confidence": "low",
            "action": "none",
            "live_window_id": None,
            "duplicate_window_ids": [],
            "stop_pass": False,
            "evidence": lines,
            "missing_probe_steps": missing,
            "recommendation": RECOMMENDATIONS["UNKNOWN"],
        }

    lastwar = []
    ignored_other = 0
    for entry in windows:
        if not isinstance(entry, dict):
            continue
        app = entry.get("app")
        if app is not None and app != "LastWar":
            ignored_other += 1
            continue
        lastwar.append(entry)
    for entry in lastwar:
        lines.append(_describe(entry))
    if ignored_other:
        lines.append("%d non-LastWar window(s) ignored"
                     % ignored_other)

    if not lastwar:
        decision = "OPEN_APP"
        confidence = "high"
        action = "open_app LastWar"
        live_window_id = None
        duplicates = []
        stop_pass = False
        recommendation = RECOMMENDATIONS["OPEN_APP"]
    elif len(lastwar) == 1:
        only = lastwar[0]
        wid = _window_id(only)
        decision = "ACTIVATE_EXISTING"
        confidence = "high"
        action = ("activate %s raise=true" % wid
                  if wid is not None else "activate the window raise=true")
        live_window_id = wid
        duplicates = []
        stop_pass = False
        recommendation = RECOMMENDATIONS["ACTIVATE_EXISTING"]
        if only.get("on_screen") is False:
            recommendation += (
                " The window reports on_screen false: if activation "
                "leaves it off-screen, the capture probe's "
                "OFF_SCREEN_WINDOW recovery applies (one owner step "
                "on the Mac mini, then re-probe).")
    else:
        focused = [entry for entry in lastwar if _is_focused(entry)]
        if not focused:
            decision = "DUPLICATE_UNKNOWN_LIVE"
            confidence = "low"
            action = "none"
            live_window_id = None
            duplicates = [_window_id(entry) for entry in lastwar]
            duplicates = [wid for wid in duplicates if wid is not None]
            stop_pass = True
            missing.append(
                're-list windows recording focus / frontmost per '
                'window (which window holds keyboard focus)')
            recommendation = RECOMMENDATIONS["DUPLICATE_UNKNOWN_LIVE"]
        else:
            # The focused window is the live one. Several focused
            # windows is contradictory evidence: take the first
            # focused entry in list order and say so.
            live = focused[0]
            live_window_id = _window_id(live)
            duplicates = [_window_id(entry) for entry in lastwar
                          if entry is not live]
            duplicates = [wid for wid in duplicates if wid is not None]
            decision = "ACTIVATE_LIVE_DUPLICATE"
            confidence = "high" if len(focused) == 1 else "medium"
            action = ("activate %s raise=true" % live_window_id
                      if live_window_id is not None
                      else "activate the live window raise=true")
            stop_pass = False
            recommendation = RECOMMENDATIONS["ACTIVATE_LIVE_DUPLICATE"]
            if len(focused) > 1:
                recommendation += (
                    " (%d windows claim focus, which is contradictory "
                    "evidence: the first focused entry in list order "
                    "is taken as live at medium confidence.)"
                    % len(focused))
            if ignored_tap_count > 0:
                # R2: the ignored taps likely went to the dead
                # duplicate, so the exit control is not proven
                # unresponsive - retry it on the live window.
                recommendation += (
                    " The ignored tap(s) likely went to the dead "
                    "duplicate window (issue #822, R2): do not "
                    "conclude the control is unresponsive - retry "
                    "the exit on the live window after activating it.")
            newest = max(duplicates) if duplicates else None
            if newest is not None:
                lines.append(
                    "newest duplicate window %s is a dead input target"
                    % newest)

    return {
        "tool_version": TOOL_VERSION,
        "decision": decision,
        "confidence": confidence,
        "action": action,
        "live_window_id": live_window_id,
        "duplicate_window_ids": duplicates,
        "stop_pass": stop_pass,
        "evidence": lines,
        "missing_probe_steps": missing,
        "recommendation": recommendation,
    }


def format_text(result):
    out = ["decision: %s (%s confidence)"
           % (result["decision"], result["confidence"]),
           "action: %s" % result["action"]]
    live = result["live_window_id"]
    out.append("live window: %s" % (live if live is not None else "none"))
    if result["duplicate_window_ids"]:
        out.append("dead duplicate window(s): %s"
                   % ", ".join(str(wid)
                               for wid in result["duplicate_window_ids"]))
    out.append("stop_pass: %s" % ("yes" if result["stop_pass"] else "no"))
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
                        help="JSON file with the list_windows evidence")
    parser.add_argument("--json", action="store_true",
                        help="print the decision as JSON")
    parser.add_argument("--open-checklist", action="store_true",
                        help="print the ordered session-open checklist")
    parser.add_argument("--version", action="store_true",
                        help="print the tool version and exit")
    args = parser.parse_args(argv)

    if args.version:
        print(TOOL_VERSION)
        return 0
    if args.open_checklist:
        print("\n".join(OPEN_CHECKLIST))
        return 0
    if not args.evidence:
        parser.error("--evidence is required (or use --open-checklist)")

    with open(args.evidence, "r", encoding="utf-8") as handle:
        evidence = json.load(handle)
    if not isinstance(evidence, dict):
        parser.error("evidence file must hold one JSON object")

    result = decide(evidence)
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(format_text(result), end="")
    return DECISION_EXIT[result["decision"]]


if __name__ == "__main__":
    sys.exit(main())
