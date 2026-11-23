---
title: Alliance duel queue run 2037
created: 2026-11-23T04:41:00Z
modified: 2026-11-23T04:41:00Z
version: 1.0.0
description: Star ceremony unit star-ceremony-2026-11-22-1830, operator seat, no ceremony trophy beside the Alliance shield, nothing tapped, checked only; Event 42 left unfinished at step 7 of 13 and its two successor units expired
status: run-done
grounded_in:
  - source: cu_bridge start, status poll and final result on run 20261123T043746Z-f3a97f, 2026-11-23T04:37Z to 04:38Z
  - source: run screenshots step-0000.png, step-0001.png and step-0002.png under /Users/zhenchen/.computer-use/runs/20261123T043746Z-f3a97f, final frame saved as _tools_/state/cu_ceremony_2037.png
  - source: operator crops of the 04:34Z train-run screenshot and of this run's frames, saved as _tools_/state/cu_trophy_crop_0436.png, cu_tan_bubble_0000.png to 0002.png and cu_midbase_crop_0000.png and 0002.png
  - source: lsappinfo front reading and killall of UserNotificationCenter and NotificationCenter before the start, 2026-11-23T04:37:45Z
  - source: queue.py token-acquire and claim on the live pool, 2026-11-23T04:37:45Z
  - source: _queue_/done unit files star-ceremony-2026-11-22-1030, 1430 and 1630, and _records_/2026-11-22/alliance-duel/1415-queue-run.md, read for the Event 42 history
---

# Alliance duel queue run 2037

- Executor: operator seat (top-level session), unit star-ceremony-2026-11-22-1830,
  assignment A-20261123-0436-operator. Token lease 04:52:46Z, claim lease
  04:57:46Z, attempts 1.
- Status: done, checked only. No Star Ceremony is waiting by the profile's
  indicator, so there was nothing to play or claim.
- Run: `20261123T043746Z-f3a97f`, desktop, apps `com.lastwar.ios`, model
  `claude-gateway/claude-sonnet-5-5`, max-steps 8, max-minutes 15, max-cost
  1.0 USD. Started 04:37:47Z, ended 04:38:04Z with status `completed`. Active
  17.3 s, model time 14.3 s, so 4.75 s of model time per step. Steps 3. The
  result counts 3 actions done and they were a screenshot, a 2-second wait and a
  screenshot, so the run sent NO click, drag or key to the game. Refused 0,
  blocked 0, failed 0. Cost 0.047021 USD.
- Front precondition: `killall -9 UserNotificationCenter NotificationCenter`
  ran in the same shell immediately before the start, and `lsappinfo front`
  named `"LastWar" ... (in front)`. There was no local-input takeover.
- The indicator, read three times. The profile's ceremony icon is a gold
  trophy cup in a tan bubble immediately left of the Alliance shield. That
  bubble holds a green fist bump, which is the Alliance Help bubble. Three
  evidence points agree: the run read it so on all three frames, my own zoomed
  crops of this run's step 1 and step 2 are identical, and a crop of the 04:34Z
  train-run frame shows the same fist. It never alternated to a trophy. The
  rest of the right rail reads Events (red 4), the Warzone Duel VS medallion
  (countdown about 21:22), Alliance (red dot), Mail and Inventory (red dot).
  The run had plain screenshots and no zoom, so the zoomed reads are mine, made
  on the run's own frames.
- Open question, stated plainly. A second trophy exists on the base screen: a
  white speech bubble with a gold trophy cup, alternating with a gold "NEW" tag,
  over a large circular building near the middle of the base, about (568,217).
  My crops (cu_midbase_crop_0000.png and _0002.png) show both states. It is a
  building bubble, not the tan bubble beside the Alliance shield that the
  profile and the 1415 record describe, so it was not counted as the ceremony.
  What it belongs to is NOT established. It was visible in base frames
  throughout this session, including before and after the Help unit. I have not
  tapped it: the building may be the Arena, which is a PvP surface, so a tap
  needs a decision. If the profile's icon can be hidden behind the Help bubble,
  that is also untested.
- Event 42 history, from the repository. The 1030 unit played Event 42 to step 7
  of 13 at about 14:15 PT with 3 hearts sent, and left the finale golden chest
  and the Participation Prize unclaimed. Its successors star-ceremony-2026-11-22-1430
  and 1630 both closed `expired`, window passed before execution, so no unit
  resumed it. The trophy beside the Alliance shield is gone at 20:34 and 20:37 PT.
  Same shape as Event 40 on 2026-11-08, when the ceremony was left at step 10 of
  13 and the trophy later vanished with no record of the finale (Issue #488).
  Whether Event 42 expired at the duel-day rollover, or was finished by someone
  else, is unobserved. The finale chest and the Participation Prize for Event 42
  are most likely lost. That is a loss to report, not something this unit can
  repair.
- Hearts, finale, claims: none this unit. No ceremony screen was opened.
- Closing frame, `_tools_/state/cu_ceremony_2037.png`: base screen unchanged. No
  panel opened, nothing tapped.
- Red lines: no speedup, no diamonds, no purchase, no attack, rally or march, no
  diplomacy. No confirmation dialog appeared.
- Follow-up: the next ceremony unit is star-ceremony-2026-11-23-0230, not before
  2026-11-23T10:30:00Z. A new ceremony would appear after the next weekly
  settlement, so that unit is most likely another check. Two decisions are owed
  by the coordinator or owner: what the mid-base trophy bubble is, and whether a
  ceremony left unfinished should be resumed by the very next unit instead of
  waiting for slots that can expire.
