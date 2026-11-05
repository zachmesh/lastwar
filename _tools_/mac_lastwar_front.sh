#!/bin/bash
# Bring the LastWar app to the active Space on the Mac mini.
#
# Owner recovery for zachmesh/lastwar issue #284 (Mac screen capture
# failure): the game window sits windowed 1920x1080 on an inactive
# Space, so the capture stream cannot start - list_windows reports
# window_on_screen false and the View menu still lists "Enter Full
# Screen". No background control route moves it: Space keys sent in
# the background do not switch Spaces, open_app returns
# outcome_unknown, and set_window_frame needs a fresh observation
# of the window, which is exactly what the failure prevents.
#
# Run on the Mac mini in Terminal:
#   bash _tools_/mac_lastwar_front.sh
#
# This is the scripted form of the known reliable step - clicking
# the LastWar Dock icon once. Activating the app moves its Space to
# the front; it does not tap, claim or change anything inside the
# game. After running, re-probe with:
#   python3 _tools_/mac_capture_probe.py --evidence <evidence.json>
# and expect window_on_screen true and a working observation.
#
# Never uses Control-Command-F or Escape on this app (both crash
# it); fullscreen, if wanted, is the green zoom button / View menu
# only after the window is back on the active Space.
set -euo pipefail
osascript -e 'tell application "LastWar" to activate'
