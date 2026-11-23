---
title: Queue Planning Sweep Pair And Alliance Exercise Watch 2216 2026-11-22
created: 2026-11-22T22:16:00-08:00
modified: 2026-11-22T22:16:00-08:00
level: L0
version: 1.0.0
description: Planner staging pass for assignment A-20261123-0611 - sweep pair and 12 fix-ups staged for 2026-11-24 by queue.py sweep, Alliance Exercise watch minted, Winter Battlefield held, and a finding that the siege watch outranks the sweep once actionable
status: done
activity: queue-planning
run_id: queue-planning-2026-11-22-2216-sweep-and-ae
trigger: coordinator assignment A-20261123-0611-planner
started_at: 2026-11-22T22:11:19-08:00
finished_at: 2026-11-22T22:16:00-08:00
verified: validate exit 0 after the sweep; sweep-status read for 11-23; pick order simulated with the tool's own pick_key over the live inbox
grounded_in:
  - source: _records_/2026-11-22/queue-planning/2216-sweep-and-ae-rows.json
  - source: _tools_/queue.py cmd_sweep, _stage_sweep_fixups, pick_key and cmd_next, read before running
  - source: _records_/2026-11-22/queue-planning/2210-watch-unit.md, the units this pass builds on
---

# Sweep pair and Alliance Exercise watch, 2216

Rows, commands and the simulation are in [the sidecar](2216-sweep-and-ae-rows.json).

## 1. Done

- **Brief sentence added** to `scout-midday-2026-11-23-0609`: the sweep pair has priority; if the stage has ended, read the result mail first.
- **Sweep pair staged** by `queue.py sweep --regular zero-sweep --date 2026-11-23`, exit 0, reset 2026-11-24T02:00:00Z. Both are priority 1, 15 minutes, `expires_at` 2026-11-24T02:00:00Z:
  - `zero-sweep-2026-11-23-1600`, `not_before` 2026-11-24T00:00:00Z, chain seq 1.
  - `zero-sweep-2026-11-23-1700`, `not_before` 2026-11-24T01:00:00Z, chain seq 2.
- **Alliance Exercise watch minted:** `scout-midday-2026-11-23-0612`, priority 2, 15 minutes, `not_before` 2026-11-23T22:55:00Z, `expires_at` 2026-11-23T23:35:00Z, brief in the body.
- **Winter Battlefield held, not minted:** 5v5 PvP, OD-20261123-03 open. A yes on that decision releases the command drafted in `2210-watch-unit-rows.json`.

## 2. Two things you did not ask for

**The same `sweep` call staged 12 fix-ups.** They are priority 1, `not_before` 00:30Z, expiring 02:00Z, with estimates summing to 67 minutes. The tool stages them by design, so the pair alone is not available from `sweep`.

**The queue order does not put the pair before the watch.** I simulated `next` with the tool's `pick_key` over the live inbox, worst case with nothing done yet. At 01:10Z the siege watch ranks 3rd, ahead of all 12 fix-ups and both passes. A priority 2 unit older than two hours counts as priority 1, and the watch was created three minutes before the sweep units. The alliance watch ranks first at 22:56Z, as intended.

Two ways to restore your sequence:
- **A.** Dispatch the final pass by name before the watch. No queue change.
- **B.** Withdraw `...-0609` and mint its replacement after the sweep units. That gives it a new id, so I did not do it without your word.

## 3. Load

By estimates, the fix-ups, final pass and watch need 97 minutes in the 90 from 00:30Z. At the observed pace of about 3.0 minutes per unit (13 runs, 20:13 to 20:49 PT) the fix-ups take about 36 minutes and it fits. That is a projection, unverified for the passes. The older `vip-2026-11-22-1800` and `scout-2026-11-22-1800` rank first for as long as they stay in the inbox.

## 4. Proof

- `validate`: exit 0, after the sweep.
- `sweep-status` for 11-23: exit 1. Both passes are in the inbox, pending, `geometry_ok` true; exit 1 means not yet executed.
- Counts: inbox 18 to 32 (14 sweep units), claimed 0, done 2,633.
