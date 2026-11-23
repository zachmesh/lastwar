---
title: Daily missions queue run 2208
created: 2026-11-23T06:13:00Z
modified: 2026-11-23T06:13:00Z
version: 1.0.0
description: Daily missions unit daily-missions-2026-11-22-1800, operator seat, nothing claimable in the Daily Tasks view, star 110 with the 40 and 80 chests open, rows below the fold unread
status: run-partial
grounded_in:
  - source: cu_bridge start, status poll and final result on run 20261123T060831Z-e25a07, 2026-11-23T06:08Z
  - source: run screenshots step-0001.png and step-0002.png under /Users/zhenchen/.computer-use/runs/20261123T060831Z-e25a07, final frame saved as _tools_/state/cu_missions_2208.png
  - source: lsappinfo front reading and killall of UserNotificationCenter and NotificationCenter before the start, 2026-11-23T06:08:31Z
  - source: queue.py token-acquire and claim on the live pool, 2026-11-23T06:08:31Z
---

# Daily missions queue run 2208

- Unit daily-missions-2026-11-22-1800, operator seat, assignment A-20261123-0607-operator.
  Leases are in the unit file, attempts 1. Measured rows are in the sidecar
  [2208-queue-run-detail.md](2208-queue-run-detail.md).
- Status: partial. Nothing was claimable in view, so nothing was claimed. The rows below
  the fold were not read, so the list is not checked top to bottom.
- Run `20261123T060831Z-e25a07`, model `claude-gateway/claude-sonnet-5-5`,
  max-steps 8, ended `completed` after 4 steps. Actions done 3, refused 0, failed 0,
  one action per turn. Model time 3.91 s per step. Cost 0.058985 USD. No local-input
  takeover.
- Front precondition held: `killall -9 UserNotificationCenter NotificationCenter`
  in the same shell, then `lsappinfo front` named LastWar. The first base frame had no
  "Boarding closes in" banner, so the boarding rule did not trigger.
- Route: the orange terminal opened MISSION on the Main Tasks tab, not Daily Tasks. One
  tap on Daily Tasks switched it. The panel's back arrow then returned to the base.
- Daily Tasks: no green Claim button in view and no red badge on the tab. The
  four rows in view are all incomplete Go rows, left untouched. A fifth row was cut off.
  The run did not drag the list, so the rest is unread.
- Star track: 110 points, with the 40 and 80 chests open and the 120, 160 and 200
  chests closed. The 120 chest is 10 points away.
- Reset: Next Refresh reads 19:51:19, which points at the 18:00 PT reset.
- Closing state: the base screen.
- Not touched: every Go button, the paid-purchase and Attack a Commander rows, the
  mid-base trophy bubble.
- Red lines held: no diamonds, no purchase, no speedup, no attack, rally, march or
  Arena, no Alliance Wars, no diplomacy.
- Follow-up: "Donate to Alliance Tech 5 times" is 0/5 and pays 10 points, which would
  carry the star to 120 and open that chest. A later pass should drag the list to read
  the rows below the fold.
