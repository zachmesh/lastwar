---
title: Alliance donations queue run 2340
created: 2026-11-23T07:46:00Z
modified: 2026-11-23T07:46:00Z
version: 1.0.0
description: Donations unit donations-2026-11-23-0709, operator seat, two coin donations to Quick Construction, count 4 of 30 to 2 of 30, step cap reached one tap short of the 1 of 30 floor
status: run-partial
grounded_in:
  - source: cu_bridge start, status polls, events and final result on run 20261123T074058Z-7f1217, 2026-11-23T07:40Z to 07:42Z
  - source: frames step-0003.png (count 4 of 30) and step-0006.png (count 2 of 30) read by the operator, the latter saved as _tools_/state/cu_donations_2340.png (untracked)
  - source: lsappinfo front reading and killall of UserNotificationCenter and NotificationCenter before the start, 2026-11-23T07:40:58Z
  - source: alliance-donations rule digest, rules 1 to 6
---

# Alliance donations queue run 2340

- Unit donations-2026-11-23-0709, operator seat, assignment A-20261123-0740-operator,
  attempt 1, claimed 07:40:53Z. Rows are in the sidecar
  [2340-queue-run-detail.md](2340-queue-run-detail.md).
- Run `20261123T074058Z-7f1217`, model `claude-gateway/claude-sonnet-5-5`, max-steps 8,
  ended `completed` after 7 steps. Actions done 11, refused 0. Model time 5.2 s per step.
  Cost 0.092926 USD. No takeover. First frame was the base: no account dialog, no
  boarding banner.
- Route: Alliance button, Alliance Techs tile, the node with the red-panda recommended
  badge, no drag needed. The badge sat on Quick Construction, level 9/10.
- Counts, each read on a frame (rule 4): 4/30 at entry, 3/30 after the first tap, 2/30
  after the second. The first tap's reward animation hid the count for one frame, and the
  run waited 2 s before reading it, so the first donation was confirmed only then.
- Cost per donation 1000 coin, so 2000 coin spent. Coin stayed 9.6M and diamonds 11,136
  on the top bar. The diamond Donate button (2 diamonds) was never touched.
- No cooldown timer and no greyed button, so the burst was not exhausted. Per rule 5 one
  donation was still allowed (2/30 to 1/30). The step cap stopped the unit one tap short,
  so it closes partial, not by a cooldown.
- Status: partial. Target 1/30, reached 2/30.
- Closing state, not the base: the node panel is open over the Alliance Techs tree. The
  next run must back out with the blue back arrow until the base shows, and read its first
  base frame for a boarding banner then.
- Not touched: Help, Gifts, Store, Events, any daily reward, the trophy bubble.
- Red lines held: no diamonds, no purchase, no diplomacy, no march, no PvP.
- Follow-up: one donation from 2/30 reaches the floor; the refill is about 20 minutes per
  step (rule 8, unsettled), so a later donations unit finds more room and can start from
  the base.
