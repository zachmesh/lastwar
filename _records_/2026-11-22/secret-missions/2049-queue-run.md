---
title: Secret missions queue run 2049
created: 2026-11-23T04:55:00Z
modified: 2026-11-23T04:55:00Z
version: 1.0.0
description: Secrets unit secrets-2026-11-22-1857, operator seat, nine tasks deployed with Mega Deploy, ally assists not reached at the step cap
status: run-partial
grounded_in:
  - source: cu_bridge start, status poll and final result on run 20261123T044950Z-b921b9, 2026-11-23T04:49Z to 04:50Z
  - source: run screenshots step-0001.png to step-0007.png under /Users/zhenchen/.computer-use/runs/20261123T044950Z-b921b9, final frame saved as _tools_/state/cu_secrets_2049.png
  - source: lsappinfo front reading and killall of UserNotificationCenter and NotificationCenter before the start, 2026-11-23T04:49:50Z
  - source: queue.py token-acquire and claim on the live pool, 2026-11-23T04:49:50Z
---

# Secret missions queue run 2049

- Unit secrets-2026-11-22-1857, operator seat, assignment A-20261123-0453-operator.
  Leases in the sidecar, attempts 1.
- Status: partial. The Mega Deploy half is done and verified. The ally assists
  were not reached, so Assist Allies still reads 0/5. Measured rows are in the
  sidecar [2049-queue-run-detail.md](2049-queue-run-detail.md).
- Run `20261123T044950Z-b921b9`, model `claude-gateway/claude-sonnet-5-5`,
  max-steps 8, ended `max_steps` with no final message because the step-8 call
  was recorded but not executed. Active 48.2 s. Steps 8, actions done 22,
  refused 0, failed 0. Model time 3.90 s per step. Cost 0.085764 USD. No
  local-input takeover.
- Front precondition held: `killall -9 UserNotificationCenter NotificationCenter`
  in the same shell, then `lsappinfo front` named LastWar.
- Entry: the jeep icon in the left column opened SECRET COMMAND POST, and the
  title was read before anything else was tapped. At entry Assist Allies 0/5,
  Other counters in the sidecar. No card carried a
  Claim button, so nothing was due to claim.
- Mega Deploy: one tap on Mega Deploy opened the MEGA DEPLOY REMINDER. UR Only
  was unchecked and all nine tasks were ticked, checked by scrolling the list.
  One tap on Perform Now sent them. The squads left over the world map.
- Verified on re-entry (step-0007.png): the Your Tasks badge cleared, Mega
  Refresh and Mega Deploy are greyed, and the cards show running countdowns, countdowns in the sidecar. The remaining cards were
  not individually re-read.
- Claim timing matters. Finished tasks left unclaimed for hours get plundered
  (the 1104 lesson). Finish times are in the sidecar.
- Not done: the 5 ally assists. The Ally Tasks badge shows 5 waiting. They are
  a free step and need a follow-up unit soon.
- Not touched: Plunder Others (PvP), Mega Refresh, Others' Tasks, Hidden
  Treasures, Ghost Ops, Recover. The mid-base trophy bubble was not tapped.
- Closing state: the game was left on the Secret Command Post screen, not the
  base. Diamonds unchanged.
- Red lines held: no speedup, no diamonds, no purchase, no attack, rally,
  march or Arena, no diplomacy.
- Follow-up: dispatch the assists now, then claim units on the finish times in the sidecar.
