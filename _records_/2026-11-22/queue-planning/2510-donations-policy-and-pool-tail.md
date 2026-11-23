---
title: Queue Planning Donations Policy And Pool Tail 2510 2026-11-23
created: 2026-11-23T02:35:00-08:00
modified: 2026-11-23T02:35:00-08:00
level: L0
version: 1.0.0
description: Planner pass on the donations tracker policy - the 2-hour cadence checked against what is staged, the policy close rules added to the two unclaimed donations units, and a pool gap found around 13:10Z before the 14:03Z wave
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0235-donations-policy
trigger: coordinator message with the donations tracker policy 2532
started_at: 2026-11-23T02:33:00-08:00
finished_at: 2026-11-23T02:35:00-08:00
verified: the pool simulated at 5 minutes per growth read; unit files read back; validate exit 0
grounded_in:
  - source: _records_/2026-11-22/team-operations/2532-donations-tracker-policy.md
  - source: _tools_/queue.py pick_key
---

# Donations policy and pool tail, 2510

## 1. Cadence

The policy keeps the 2-hour cadence until two refill reads exist. The last pass finished at about 10:13Z. Staged after it are the 10:03Z wave unit `donations-2026-11-23-0203` (window to 14:03Z) and the midnight fix-up. Simulated at 5 minutes per growth read, the wave unit runs at about 12:40Z, 2.5 hours after the last pass, so the cadence is about kept and I stage no new donations unit. The next one is the 14:03Z wave unit, which is not staged yet.

## 2. Units

Both unclaimed donations units now carry the policy close rules beside the logging block: spend the live count and stop; DONE when the count is spent or already spent at entry; PARTIAL when it stops early; FAILED when the panel is never reached; an entry at 1/30 closes flagged uncalibrated; only witnessed taps count; coin only. Units minted later by `plan` and `sync` carry neither block, so the scribe's digest must.

## 3. Pool tail

The same simulation shows an idle gap from about 13:09Z to 13:30Z: the pool drains before the 14:03Z wave opens. The wave needs `plan` or `sync` to stage it by about 13:30Z; I do not run those commands unprompted.
