---
title: Research queue queue run 2022
created: 2026-11-23T04:23:30Z
modified: 2026-11-23T04:23:30Z
version: 1.0.0
description: Research unit research-2026-11-22-1803, operator seat, both slots read live and busy, nothing to complete and nothing started
status: run-done
grounded_in:
  - source: cu_bridge start, status polls and final result on run 20261123T042206Z-60e1a0, 2026-11-23T04:22Z
  - source: run trajectory events.jsonl and the final screenshot saved as _tools_/state/cu_research_2022.png, trajectory under /Users/zhenchen/.computer-use/runs/20261123T042206Z-60e1a0
  - source: lsappinfo front reading and killall of UserNotificationCenter and NotificationCenter before the start, 2026-11-23T04:22:06Z
  - source: queue.py token-acquire and claim on the live pool, 2026-11-23T04:22:06Z
---

# Research queue queue run 2022

- Executor: operator seat (top-level session), unit research-2026-11-22-1803,
  assignment A-20261123-0421-operator. Token lease 04:37:06Z, claim lease
  04:42:06Z, attempts 1.
- Status: done. Both research slots were read live. Both are busy, so there was
  nothing to complete and no idle slot to start.
- Run: `20261123T042206Z-60e1a0`, desktop, apps `com.lastwar.ios`, model
  `claude-gateway/claude-sonnet-5-5`, max-steps 8, max-minutes 15, max-cost
  1.0 USD. Started 04:22:07Z, ended 04:22:26Z with status `completed`. Active
  18.7 s, model time 13.4 s, so 4.48 s of model time per step. Steps 3, actions
  done 6, refused 0, blocked 0, failed 0. Cost 0.030943 USD.
- Front precondition: `killall -9 UserNotificationCenter NotificationCenter`
  ran in the same shell immediately before the start, and `lsappinfo front`
  named `"LastWar" ... (in front)`. Both clicks carried
  `frontmostBundleId: com.lastwar.ios`. There was no local-input takeover.
- What the run did, from its trajectory: step 1 click (175,930), the Events
  back arrow, which returned to the base. Step 2 click (110,262) on the flask
  queue icon. It opened the RESEARCH QUEUE list panel on the first try, which
  matches the 1010 and 1310 units. Step 3 only read and reported.
- Live read on the final screenshot (RESEARCH QUEUE panel):
  - Slot 1: "Lv.0 Unlock Oil Well upgrade in progress", Time Left 07:20:35,
    the bar about 80 percent full.
  - Slot 2: "Lv.7 Defense Training VIII upgrade in progress", Time Left
    3d 02:56:42, the bar about 30 percent full.
  - No green Complete button on either slot, and no Idle slot. Each slot shows
    a blue Speed Up button, and neither was tapped.
- Power: 150,080,120 before the queue was opened, read by the run on the base
  HUD at step 2. The panel covers the HUD on the final screenshot, so no
  after-value was read. No Complete was pressed, so no power change was
  expected. The agent reported it unchanged. That is the agent's statement,
  not a second screenshot read.
- CONTRADICTION with the profile, recorded and not reconciled. The 1310 read
  carried slot 1 as Lv.3 Advanced Armor VIII (finishing about 16:43 PT) and
  slot 2 as Lv.6 Defense Training VIII (finishing about 02:03 PT on
  2026-11-23). The live names and timers now differ: slot 1 is the Lv.0
  Unlock Oil Well research and slot 2 is Lv.7 Defense Training VIII with
  3d 02:56 left. Advanced Armor VIII is no longer in the queue. This unit
  started nothing and completed nothing. Who completed the earlier research
  and who started the two current ones is not known from this unit. Neither
  the 1310 carried names nor the live names are asserted beyond the screenshot.
  The next research unit reads the names live and does not carry these.
- Arms Race relevance: the Unlock Oil Well research finishes in 07:20:35, which
  is about 11:43Z. That is after the Base Building phase ends (about 06:00Z),
  so no research completion lands inside the live phase.
- Red lines: no speedup, no diamonds, no purchase, no new research started, no
  item used. No confirmation dialog appeared.
- Game left with the RESEARCH QUEUE panel open over the base screen.
- Follow-up: the next research unit closes the panel first and re-reads both
  slots. The slot 1 completion is due about 11:43Z, so it falls to a unit
  after that time. The Lv.7 Defense Training VIII timer is 3d 02:56:42, so it
  is not due for days.
