---
title: Truck plunder second continuation run 2105
created: 2026-11-23T05:09:00Z
modified: 2026-11-23T05:09:00Z
version: 1.0.0
description: Second continuation of trucks-2026-11-22-1857, operator seat, two own trucks dispatched at SR on free refreshes, Trade Count 2/5, game left on the trade screen
status: run-partial
grounded_in:
  - source: cu_bridge start, status poll and final result on run 20261123T050551Z-036490, 2026-11-23T05:05Z to 05:06Z
  - source: run screenshots step-0002.png to step-0007.png under /Users/zhenchen/.computer-use/runs/20261123T050551Z-036490, final frame saved as _tools_/state/cu_trucks_2105.png
  - source: lsappinfo front reading and killall of UserNotificationCenter and NotificationCenter before the start, 2026-11-23T05:05:51Z
  - source: queue.py token-acquire and token-release around the run, no unit claimed
---

# Truck plunder second continuation run 2105

- This is the second continuation of trucks-2026-11-22-1857, assignment
  A-20261123-0505-operator. It is not a queue unit. No unit was claimed, the closed
  partial unit file is untouched, and the device token was held for the run only.
  Measured rows are in the sidecar [2105-queue-run-detail.md](2105-queue-run-detail.md).
- Status: partial. Two own trucks were dispatched. The game was not returned to
  the base.
- Run `20261123T050551Z-036490`, model `claude-gateway/claude-sonnet-5-5`,
  max-steps 8, ended `max_steps` with no final message. Steps 8, actions done
  14, refused 0, failed 0. Model time 4.21 s per step. Cost 0.094737 USD. No
  local-input takeover.
- Front precondition held: `killall -9 UserNotificationCenter NotificationCenter`
  in the same shell, then `lsappinfo front` named LastWar.
- Rule applied: non-UR day, Radar Training. SR or above only, a diamond refresh
  never, Mega Mode skipped.
- Truck 1: opened on slot 1, rolled R with a Free tag, so the run took the free
  refresh and it landed SR, arriving in 03:45:28. Let's Go sent it, and Trade
  Count rose to 1/5.
- Truck 2: opened on slot 2, rolled R again, took the free refresh and landed SR,
  arriving in 03:36:43. Let's Go sent it, and Trade Count rose to 2/5.
- Cost of the refreshes: two free refreshes, no Trade Contract spent, no diamond.
  
- Final state, verified on step-0007.png: Trade Count 2/5, two trucks on the
  road, one open slot, one locked slot. The Recover button no longer carries a
  red dot.
- Budget finding: the reserved step 8, the back arrow, was recorded and not
  executed, as every capped run's last request has been today. A run capped at 8
  steps executes 7, so the game was left on the Intercity Trade screen, not the base.
- Not touched: Others' Trucks and every plunder control, Mega Mode, the mid-base
  trophy bubble.
- Red lines held: no plunder, no diamonds, no purchase, no speedup, no diplomacy.
- Follow-up: the third open slot is free for another truck. The 05:21Z claim run
  starts on the trade screen and must tap the back arrow first. The dispatch
  quota stands at 2 of 5 until these trucks return.
