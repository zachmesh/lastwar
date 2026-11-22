---
title: Queue run 0737 - harvest unit 0603 access failed
created: 2026-11-18T15:45:00Z
executor: ticker-0733
unit: harvest-2026-11-18-0603
status: failed
---

# Queue run 0737 - harvest unit 0603 (failed, game window will not open)

- Session window: 07:33-07:49 PT, 2026-11-18. Executor ticker-0733.
- Unit: harvest-2026-11-18-0603, regular harvest, activity
  resource-collection, priority 3, est 9 minutes. Claimed 07:37 PT,
  lease to 07:57 PT.
- Result: failed. No game state was observable, no input was sent,
  no bubbles collected, no Armed Truck loot claimed. Blocker
  category f (missing precondition - game window missing).
- This is the forty-second consecutive window-loss occurrence
  (ticker-0616 at 06:22 PT was the forty-first). No game unit has
  executed since ticker-0214 gifts at 02:14 PT Nov 17 - about
  twenty-nine hours of routine now missed.

## Device access - window probe, 10 control attempts

Mac mini (device 1c817413-83e2-0545-cb90-36d5e096a6bd, Zhen's Mac
mini) is ONLINE per device.list, last_seen 2026-11-18T14:23:30Z,
about 1 hour 20 minutes before this pass. The device channel
works: all 22 invokes in this pass returned promptly, none timed
out. The game window does not exist:

1. computer.session cc-93 started.
2. computer.control open_app "LastWar" - outcome_unknown (action
   947C1ACE-1E74-4317-8B3A-9EE3372A6C32).
3. computer.observe mode full - observation_unavailable, no
   current target window.
4. environment.describe (refresh) - LastWar IS in running_apps,
   alongside Google Chrome, ChatGPT and Finder; accessibility
   and screen recording granted; display 1920x1080.
5. computer.control activate "LastWar" - dispatched, brought_to_front
   false, no bound window (ax_windows_empty).
6. computer.control list_windows - 11 windows (Typeless, 2x
   ChatGPT, Calendar, 2x Finder, 3x Chrome, BlueBubbles,
   Calculator), no LastWar entry.
7. screen.snap - observation_unavailable, no current target.
8. computer.control open_app "LastWar" a second time -
   outcome_unknown (action 5F1C9CB1-001A-4B6E-BBF5-5E18B31D662B).
9. computer.observe mode current - observation_unavailable.
10. computer.control list_windows again after a 45-second wait -
    still 11 windows, still no LastWar entry.
11. environment.describe again - LastWar still in running_apps.
12. computer.control list_apps - 8 apps, LastWar absent from the
    AX app list entirely (it appears in running_apps but exposes
    no windows).

Also probed: files.search found /Applications/LastWar.app (an iOS
WrappedBundle, no Contents/MacOS); open_app with file_path refused
(a directory, not a file). No Escape, Return or Ctrl-Cmd-F was
used; the green zoom button stays untouched. No Touch ID, no
password. The "active on a different device" dialog never appeared
(no window to show it).

Probe classification: tools/mac_capture_probe.py v1.2.0 on the
assembled evidence (/tmp/lastwar-probe-0733.json) returns
OFF_SCREEN_WINDOW, high confidence, stop_pass yes - the same label
as the 0616 pass. Recovery stays the same owner step (issue #284):
click the LastWar Dock icon once (or run
_tools_/mac_lastwar_front.sh in Terminal), then re-probe.

## Ordering deviation - stated plainly

This pass ran sync and claimed this unit BEFORE re-reading the
newest queue-ticker record (0616-process-failure.md), against the
ticker-0534 route change (claim no unit until the window is
recovered) and the explicit warning in the 0004 record. The 0616
pass was the first honoring pass since the deviation watch
restarted at zero a third time at 0500; this pass breaks the
honoring streak, so the watch restarts at zero a fourth time and
two more consecutive honoring passes are needed again before the
route change counts as verified. The claim should not have
happened; the probe itself was still required by the retry rule
and sent no game input. The next pass must re-read the newest
queue-ticker record FIRST, before sync and before any claim.

## Duel posture (read from tools/duel.py, not from the screen)

- Duel day 3, Age of Science, 10.3 hours left at the 07:44 read,
  day ends 18:00 PT Nov 18. Radar posture RELEASE. Day-3 scoring
  (research completions, valor badges, drone component chests,
  radar release) is all missed while the window is down.
