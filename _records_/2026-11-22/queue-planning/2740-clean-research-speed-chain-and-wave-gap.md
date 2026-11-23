---
title: Queue Planning Clean Research Speed The 17:30Z Chain And The Missing Wave 2740 2026-11-23
created: 2026-11-23T06:14:00-08:00
modified: 2026-11-23T06:14:00-08:00
level: L0
version: 1.0.0
description: Planner pass after the clean research speed read - the 17:30Z unit rewritten for the 550 minute tech spend and Oil Output I, obsolete units retired, the route card given the tree route, and the finding that the 14:03Z wave is not staged
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0614-research-chain-wave-gap
trigger: coordinator message 14:07Z with the clean research speed read
started_at: 2026-11-23T06:04:00-08:00
finished_at: 2026-11-23T06:14:00-08:00
verified: Iron Output V end time recomputed from 14:00:54.5Z plus 131,879 s; unit states read before each edit; the inbox searched for wave units; validate exit 0
grounded_in:
  - source: coordinator message 14:07Z (operator run 20261123T140004Z-ea602f)
  - source: _queue_/done/secrets-2026-11-23-0742.md and 0944
---

# Clean research speed, the 17:30Z chain and the missing wave, 2740

## 1. The 17:30Z unit

Iron Output V was started at 14:00:54.5Z for 131,879 s, so it ends at about 2026-11-25T02:38:53Z, 549 minutes after Food Output V (2026-11-24T17:29:58Z). The divisor is 3.678 [M]; the blue Research button reads about 11 percent longer than the lab ran, so units read the Finish Now clock. `research-complete-2026-11-24-002` (17:30:10Z to 19:30Z) now: Complete Food Output V; then the second tech spend on Iron Output V, about 550 minutes (8h x1, 1h x1, 5m x2), approved if the preview shows the finish time before confirming, skipped with a reason otherwise; Complete Iron Output V if it finishes; then Oil Output I level 1 (iron 3.7M, food 3.7M, coin 11.2M, 60,000 oil, base 679,140 s) with the coin formula and the Diamonds-tile hazard, a Special Forces +15K node with no speed-up as the idle-lab fallback. The separate Iron Output V speed-up unit I was asked to stage is therefore folded in. Retired and closed: the speed-up fallback `-002` and the 14:59:30Z Complete unit (the speed-up unit `-001` completed the chain; the item-5 survey is also done).

## 2. Route card and oil

The route card is 1.3.0 with the Age of Oil tree route: the running node's icon at (456,925), never the fast-forward button at (603,925), and the Finish Now clock rule. Today's Oil Depot units were retired: the Oil Depot secret is the UR Capture the Oil Depot task, whose 30K oil was claimed at 08:51:08Z, and at 12:50Z all eight Secrets cards read PERFECT with no countdown, so no later claim exists that day. Tomorrow's pair stays.

## 3. Expiries and the missing wave

Three plan-minted units expired unrun at 14:03Z (arms-race, building-queues, donations of the 10:03Z wave), more than two in an hour. My own 14 expired units were closed with a real summary each. The 14:03Z wave is NOT STAGED: no wave unit exists, and the next window to open is the 14:20Z trucks settle. Until `plan` or `sync` runs there is no routine claim in the queue; after 2026-11-24T00:05Z both will refuse a unit whose serves is not valid, which the roster default upkeep satisfies.
