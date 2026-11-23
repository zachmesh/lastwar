---
title: Queue Planning The Plunder Count Full And The Shop Facts 2930 2026-11-23
created: 2026-11-23T08:45:00-08:00
modified: 2026-11-23T08:45:00-08:00
level: L0
version: 1.0.0
description: Planner pass after four plunder fights filled the daily count - the remaining plunder units retired, tomorrow's eight scans staged from the 02:00Z reset, and the passes units corrected with the measured shop facts
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0845-count-full-shop
trigger: coordinator message 16:33Z
started_at: 2026-11-23T08:32:00-08:00
finished_at: 2026-11-23T08:45:00-08:00
verified: the inbox searched before and after each edit; the fight records 1600 and 1623 read; word counts under 450; validate exit 0
grounded_in:
  - source: _records_/2026-11-22/truck-plunder/1600-queue-run.md and 1623-queue-run.md
  - source: _records_/2026-11-22/shop-claims/1629-queue-run.md (as relayed)
---

# The plunder count full and the shop facts, 2930

## Plunder

The count reached 4 of 4 with four fights that paid 9, 3, 0 and 6 shards, no troops wounded. Closed as expired with that reason: scans `trucks-plunder-scan-2026-11-23-005` to `-009` and the session `trucks-plunder-2026-11-23-002`. Tomorrow `trucks-plunder-scan-2026-11-24-001` to `-008` run from 02:30Z, 30 minutes apart to 06:00Z, each expiring 40 minutes after it opens and all before the 08:00Z quiet window. Each looks once, reads the count first and stops at 4 of 4, takes the card with the most shards, fights at most once, applies the casualty guard and keeps the per-fight record block (shards won, share of the cargo per item, the card's shard count and stack slots, troops wounded, the count, Total Power). The briefs carry what the records show: a UR stack in either half qualifies, the half does not decide the payout (x9 from four stacks, x3 of 6, 0 of 6, x6 of 9), and a red item marked Reclaimed cannot be won.

## Shop

From record 1629: seven tabs (Official Event, Weekly Deal, Super Monthly Pass, Weekly Pass, Diamond, G, Hot Sale Packs); G is the Gold Brick Mall, a purchase page, never tapped; Hot Sale Packs, the last tab, reads 'Packs sold out'; no Claim anywhere. The passes units for 06:57, 10:57 and 16:30 and the daily pickup of 2026-11-24 now read the Weekly Pass tab only and skip Hot Sale Packs until it shows a pack. Two of them still carried the pre-incident wording that the check-in Go was unverified and the Researcher's test covered it; they now say never click Go, it opens the web store.
