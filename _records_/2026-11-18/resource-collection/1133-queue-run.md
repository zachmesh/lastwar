---
title: Queue run 1133 - harvest unit 1003 access failed
created: 2026-11-18T19:47:00Z
executor: ticker-1133
unit: harvest-2026-11-18-1003
status: failed
---

# Queue run 1133 - harvest unit 1003 (failed, game window will not open)

- Session window: 11:33-11:47 PT, 2026-11-18. Executor ticker-1133.
- Unit: harvest-2026-11-18-1003, regular harvest, activity
  resource-collection, priority 3, est 9 minutes. Claimed 11:35 PT,
  lease to 11:55 PT.
- Result: failed. No game state was observable, no input was sent,
  no bubbles collected, no Armed Truck loot claimed. Blocker
  category f (missing precondition - game window missing).
- This is the forty-fifth consecutive window-loss occurrence
  (ticker-1010 at 10:14 PT was the forty-fourth). No game unit has
  executed since ticker-0214 gifts at 02:14 PT Nov 17 - about
  thirty-three and a half hours of routine now missed.

## Device access - window probe, two computer sessions

Mac mini (device 1c817413-83e2-0545-cb90-36d5e096a6bd, Zhen's Mac
mini) is ONLINE per device.list, last_seen 2026-11-18T19:03:24Z,
about 30 minutes before this pass. The device channel works: all
15 invokes in this pass returned promptly, none timed out. The
game window does not exist:

1. computer.session cc-98 started (Last War harvest unit).
2. computer.control list_windows - 11 windows (Typeless, 2x
   ChatGPT, Calendar, 2x Finder, 3x Chrome, BlueBubbles,
   Calculator), no LastWar entry.
3. computer.control open_app "Last War" - failed, no installed
   app matching that name.
4. computer.control open_app "LastWar" - outcome_unknown (action
   05F3F5C4-A96D-4A8A-8400-EE4EF2D59869); launch result could not
   be verified, do not repeat without inspecting first.
5. computer.control list_windows again - still 11 windows, still
   no LastWar entry.
6. computer.control activate "LastWar" - dispatched,
   brought_to_front false, no bound window (ax_windows_empty).
7. computer.observe mode current - observation_unavailable, no
   current target window.
8. screen.snap - observation_unavailable, no current target.
9. After a 20-second wait, list_windows a third time - still 11
   windows, still no LastWar entry.
10. environment.describe (refresh) - LastWar IS in running_apps,
    alongside Google Chrome, ChatGPT and Finder; accessibility
    and screen recording granted; display 1920x1080;
    agent_window.available false with reason
    new_tab_in_existing_window, the sixteenth pass in a row.
11. computer.session cc-98 ended; computer.session cc-99 started.
12. computer.control open_app "Finder" in the fresh session -
    failed stale_observation/geometry_mismatch, target_bundle_id
    still com.lastwar.ios: the control channel is wedged on the
    stale LastWar target and cannot bind ANY window, the same
    symptom ticker-1010 reported as NEW. No further window
    selection was attempted.

No Escape, Return or Ctrl-Cmd-F was used; the green zoom button
stays untouched. No Touch ID, no password. The "active on a
different device" dialog never appeared (no window to show it).

Probe classification: tools/mac_capture_probe.py v1.2.0 on the
assembled evidence (/tmp/lw-probe-1133.json) returns
OFF_SCREEN_WINDOW, high confidence, stop_pass yes - the same label
as the 0616, 0733 and 1010 passes. Recovery stays the same owner
step (issue #284): click the LastWar Dock icon once (or run
_tools_/mac_lastwar_front.sh in Terminal), then re-probe.

## Ordering deviation - stated plainly

This pass ran sync and claimed this unit BEFORE re-reading the
newest queue-ticker record (1010's alliance-gifts record and the
day INDEX), against the ticker-0534 route change (claim no unit
until the window is recovered) and the explicit warnings in the
0004, 0733, 0834 and 1010 records. The deviation watch restarts
at zero a seventh time and two more consecutive honoring passes
are needed again before the route change counts as verified. The
claim should not have happened; the probe itself was still
required by the retry rule and sent no game input. The next pass
must re-read the newest queue-ticker record FIRST, before sync
and before any claim.

## Duel posture (read from tools/duel.py, not from the screen)

- Duel day 3, Age of Science, 6.3 hours left at the 11:40 read,
  day ends 18:00 PT Nov 18. Radar posture RELEASE. Day-3 scoring
  (research completions, valor badges, drone component chests,
  radar release) is all missed while the window is down.
