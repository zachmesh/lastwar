---
title: Secret missions claim run 2129
created: 2026-11-23T05:33:00Z
modified: 2026-11-23T05:33:00Z
version: 1.0.0
description: Claim run, continuation of secrets-2026-11-22-1857, operator seat, one ally assist taken, the four finished tasks seen with Claim buttons but not claimed
status: run-partial
grounded_in:
  - source: cu_bridge start, status poll and final result on run 20261123T052924Z-5ba84f, 2026-11-23T05:29Z to 05:30Z
  - source: run screenshots step-0004.png and step-0007.png under /Users/zhenchen/.computer-use/runs/20261123T052924Z-5ba84f, final frame saved as _tools_/state/cu_secrets_2129.png
  - source: lsappinfo front reading and killall of UserNotificationCenter and NotificationCenter before the start, 2026-11-23T05:29:23Z
  - source: queue.py token-acquire and token-release around the run, no unit claimed
---

# Secret missions claim run 2129

- Claim run, continuation of secrets-2026-11-22-1857, assignment
  A-20261123-0528-operator. It is not a queue unit. No unit was claimed, the closed
  partial unit file is untouched, and the device token was held for the run only.
  Measured rows are in the sidecar [2129-queue-run-detail.md](2129-queue-run-detail.md).
- Status: partial. One ally assist was taken. The finished tasks were NOT claimed.
- Run `20261123T052924Z-5ba84f`, model `claude-gateway/claude-sonnet-5-5`,
  max-steps 8, ended `max_steps` with no final message. Steps 8, actions done 18,
  refused 6, failed 0. Model time 5.22 s per step. Cost 0.106715 USD. No
  local-input takeover.
- Front precondition held: `killall -9 UserNotificationCenter NotificationCenter`
  in the same shell, then `lsappinfo front` named LastWar.
- Why the claim did not run. In turn 5 the run put a `zoom` action into a batch
  with two clicks. The harness does not support zoom, so it refused the whole
  batch, which counts as 6 refused actions. Nothing in that turn executed. The
  run redid the dismiss click in turn 6 and the Your Tasks tab in turn 7. The
  Claim tap was its turn-8 request, which is never executed.

- Ally assist: one tap on Ally Tasks, one on Assist. ASSIST SUCCESSFUL for
  an ally. Assist Allies now reads 3/5, and the Ally Tasks badge reads 2, so
  two more assists are waiting.
- Finished tasks: four SR Lv.5 cards on Your Tasks each show a green Claim
  button, the 30-minute tasks. They finished at about 05:20Z and are still
  unclaimed on the last frame, so they are exposed to plunder. The 1-hour tasks
  are not due yet.
- Not touched: Plunder Others (0/5), Mega Refresh, the Others' Tasks tab, ally
  exchange, the mid-base trophy bubble.
- Closing state: the game was left on the Secret Command Post screen, Your Tasks
  tab, with the Claim buttons showing.
- Red lines held: no plunder, no diamonds, no purchase, no speedup, no diplomacy.
- Lesson: never put zoom in a batch. One unsupported action refuses all of it.
- Follow-up: a short run of three steps claims the four tasks with one tap on
  Claim, and takes the two assists. It should go at once.
