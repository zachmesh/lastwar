---
title: Hidden treasures queue run 2056
created: 2026-11-23T04:59:00Z
modified: 2026-11-23T04:59:00Z
version: 1.0.0
description: Treasures unit treasures-2026-11-22-1857, operator seat, fragment stock read live, M5 at zero so no dig possible, checked only
status: run-done
grounded_in:
  - source: cu_bridge start, status poll and final result on run 20261123T045630Z-0d4324, 2026-11-23T04:56Z
  - source: run screenshot step-0001.png under /Users/zhenchen/.computer-use/runs/20261123T045630Z-0d4324, final frame saved as _tools_/state/cu_treasures_2056.png
  - source: lsappinfo front reading and killall of UserNotificationCenter and NotificationCenter before the start, 2026-11-23T04:56:30Z
  - source: queue.py token-acquire and claim on the live pool, 2026-11-23T04:56:30Z
---

# Hidden treasures queue run 2056

- Unit treasures-2026-11-22-1857, operator seat, assignment A-20261123-0455-operator.
  Leases in the unit file, attempts 1. Measured rows are in the sidecar
  [2056-queue-run-detail.md](2056-queue-run-detail.md).
- Status: done, checked only. The stock was read live and allows no dig, so
  nothing was dug and nothing was exchanged.
- Run `20261123T045630Z-0d4324`, model `claude-gateway/claude-sonnet-5-5`,
  max-steps 8, ended `completed` after 2 steps. Active 10.2 s. Actions done 3,
  refused 0, failed 0. Model time 3.65 s per step. Cost 0.025268 USD. No
  local-input takeover.
- Front precondition held: `killall -9 UserNotificationCenter NotificationCenter`
  in the same shell, then `lsappinfo front` named LastWar.
- The game was already on the Secret Command Post screen from the previous
  work. One tap on the second tab opened the Hidden Treasure screen, which was
  read on the screenshot. The tab carries no badge.
- Fragment stock: M5 reads x0, so the stock allows 0 digs. M3 is thin at x1 and
  M4 at x2. The other four kinds hold four or more. The full row is in the
  sidecar.
- Chest progress track 5/15. Skip Animation was already ticked. Dig 1 time and
  Dig 2 time(s) are both greyed out, and neither was tapped.
- Not touched: the blue exchange control at the bottom right. A fragment
  exchange with allies needs the owner's approval, and M5 is the scarce kind.
  Plunder Others, Mega Refresh and the mid-base trophy bubble were not touched.
- Closing state: the game is on the Hidden Treasure screen, not the base.
- Red lines held: no speedup, no diamonds, no purchase, no attack, rally, march
  or Arena, no diplomacy. No exchange.
- Follow-up: M5 income comes from secret missions. The nine tasks deployed in
  the 2049 run pay fragments when claimed, so the next treasures unit should run
  after those claims and re-read the stock.
