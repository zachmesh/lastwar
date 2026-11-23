---
title: Truck plunder queue run 2058
created: 2026-11-23T05:01:00Z
modified: 2026-11-23T05:01:00Z
version: 1.0.0
description: Trucks unit trucks-2026-11-22-1857, operator seat, own trucks only, Reward Recovery claimed, no truck to collect, no dispatch reached, no plunder
status: run-partial
grounded_in:
  - source: cu_bridge start, status poll and final result on run 20261123T045827Z-ff3218, 2026-11-23T04:58Z to 04:59Z
  - source: run screenshots step-0003.png to step-0007.png under /Users/zhenchen/.computer-use/runs/20261123T045827Z-ff3218, final frame saved as _tools_/state/cu_trucks_2058.png
  - source: lsappinfo front reading and killall of UserNotificationCenter and NotificationCenter before the start, 2026-11-23T04:58:27Z
  - source: queue.py token-acquire and claim on the live pool, 2026-11-23T04:58:27Z
---

# Truck plunder queue run 2058

- Unit trucks-2026-11-22-1857, operator seat, assignment A-20261123-0457-operator.
  Own trucks only, no plunder. Measured rows are in the sidecar
  [2058-queue-run-detail.md](2058-queue-run-detail.md).
- Status: partial. The Reward Recovery record was claimed. No truck had returned,
  so nothing was collected. No truck was dispatched, because the step cap was
  reached.
- Run `20261123T045827Z-ff3218`, model `claude-gateway/claude-sonnet-5-5`,
  max-steps 8, ended `max_steps` with no final message, because the step-8 call
  was recorded and not executed.  Steps 8, actions done 20,
  refused 0, failed 0. Model time 4.31 s per step. Cost 0.095071 USD. No
  local-input takeover.
- Front precondition held: `killall -9 UserNotificationCenter NotificationCenter`
  in the same shell, then `lsappinfo front` named LastWar.
- Entry: the back arrow and a BASE tap reached the base, and the truck circle at
  the top of the left column opened Intercity Trade. It opened on the Others'
  Trucks tab, with its counter read in the sidecar.
  The run only looked at that tab. Its first tap there was the switch to Your
  Truck. No truck of another commander was tapped.
- Your Truck: Today's Trade Count 0/5, a new trade day. The yard is empty. Slots are in the sidecar. No returned truck was waiting.
- Reward Recovery: the Recover button carried a red dot. It opened the
  2026-11-22 18:00 record, (the record text is in the sidecar). One tap on Claim paid it. The
  tiles are in the sidecar.
- Not done: any dispatch. Trade Count stays 0/5. The 2026-11-21 18:00 record
  below was not opened or read.
- Closing state: the game was left on the Reward Recovery panel over the trade
  screen, not on the base. Close it with its X first.
- Red lines held: no plunder, no Quick Plunder, no Battle, no Mega Mode, no Trade
  Contract refresh, no speedup, no diamonds spent, no purchase, no attack, rally,
  march or Arena, no diplomacy. The mid-base trophy bubble was not tapped.
- Follow-up: a continuation or the next trucks unit closes the panel, reads the
  counters, and dispatches own trucks. That needs a ruling on Trade Contract
  refresh spending and Mega Mode for this duel day, which is Radar Training.
