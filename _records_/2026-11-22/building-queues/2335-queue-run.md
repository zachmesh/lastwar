---
title: Building queues queue run 2335
created: 2026-11-23T07:40:00Z
modified: 2026-11-23T07:40:00Z
version: 1.0.0
description: Building queues unit building-queues-2026-11-23-0720, operator seat, all four builders busy on Training Base Lv.25 upgrades, nothing started, earliest finish 2026-11-24T09:20:13Z
status: run-done
grounded_in:
  - source: cu_bridge start, status polls, events and final result on run 20261123T073552Z-31ee06, 2026-11-23T07:35Z to 07:36Z
  - source: frames step-0002.png (Building Queue panel) and step-0004.png (base) read by the operator, panel saved as _tools_/state/cu_buildq_2335.png (untracked)
  - source: lsappinfo front reading and killall of UserNotificationCenter and NotificationCenter before the start, 2026-11-23T07:35:52Z
  - source: building-queues rule digest, rules 1 to 5
---

# Building queues queue run 2335

- Unit building-queues-2026-11-23-0720, operator seat, assignment A-20261123-0735-operator,
  attempt 1, claimed 07:35:46Z. Rows are in the sidecar
  [2335-queue-run-detail.md](2335-queue-run-detail.md).
- Run `20261123T073552Z-31ee06`, model `claude-gateway/claude-sonnet-5-5`, max-steps 8,
  ended `completed` after 5 steps. Actions done 7, refused 0. Model time 5.6 s per step.
  Cost 0.068898 USD. No takeover. No account dialog, no boarding banner.
- Route: the game began on the Secret Command Post. The back arrow reached the base, the
  hammer icon (4/4) opened the BUILDING QUEUE panel, and the panel's own X closed it.
- Read at 07:36:04Z (rule 1): all four builders are busy. Each slot reads "Lv.25 Training
  Base upgrade in progress", progress bar a little under half, and one button,
  "Speed Up", not tapped. Time left, slot 1 to 4: 1d 01:44:09, 01:44:12, 01:44:15,
  01:44:19.
- Finish times by arithmetic from the frame time: 2026-11-24T09:20:13Z, 09:20:16Z,
  09:20:19Z and 09:20:23Z. The **earliest finish is 2026-11-24T09:20:13Z**, about 25.7
  hours from now. That is the time for the planner's next build unit. A base countdown tag
  read 1d 01:44:01 at 07:36:23Z, which agrees.
- No idle builder, so the Builders Hut decision (rules 2 and 3) was not reached. Nothing
  was started, no Construct button exists, and no stock was spent.
- Stocks at the top bar, unchanged by the run: food 638.0M, iron 1.0G, coin 9.6M,
  diamonds 11,136. Banner quest still "Build: Oil Well (0/1)".
- Who started the four Training Base upgrades is not recorded. The account state
  changed since 04:24Z, when all four slots were idle, and play on the other device is the
  likely source. This seat did not start them.
- Red lines held: no speed-up, no Finish Now, no diamonds, no purchase, no green up arrow,
  no building tapped, no PvP, no diplomacy.
- Closing state: the base screen, panel closed, hammer 4/4.
- Follow-up: schedule the next builder check for 2026-11-24T09:20Z, or earlier only for
  a Builders Hut start if the owner frees a builder.
