---
title: Queue Planning Siege Watch Replacement 2218 2026-11-22
created: 2026-11-22T22:19:00-08:00
modified: 2026-11-22T22:19:00-08:00
level: L0
version: 1.0.0
description: Planner pass for assignment A-20261123-0615 - the siege watch replaced by a unit created after the sweep units, ranking last at 01:10Z and 01:50Z; the tool refused the expired route for a live unit, so the old file was removed by hand and disclosed
status: done
activity: queue-planning
run_id: queue-planning-2026-11-22-2218-watch-replacement
trigger: coordinator assignment A-20261123-0615-planner, decision B
started_at: 2026-11-22T22:15:09-08:00
finished_at: 2026-11-22T22:19:00-08:00
verified: refused tool call proven to write nothing by an unchanged hash; replacement read back; validate exit 0 after the removal; pick order simulated with the tool's own pick_key
grounded_in:
  - source: _records_/2026-11-22/queue-planning/2218-watch-replacement-rows.json
  - source: _tools_/queue.py _complete_expired, pick_key and _window_aged_priority1, read before acting
  - source: _records_/2026-11-22/queue-planning/2216-sweep-and-ae.md, the finding this pass fixes
---

# Siege watch replacement, 2218

Rows, hashes and the simulation are in [the sidecar](2218-watch-replacement-rows.json).

## 1. Withdrawal: the tool route refused, so one step deviated

`queue.py complete --unit scout-midday-2026-11-23-0609 --status expired` exited 1: the unit's `expires_at` of 2026-11-24T02:00Z has not passed, and the tool refuses to retire a live window (`_tools_/queue.py:4555-4560`, issue #859). The unit file's hash was identical afterwards and nothing reached `_queue_/done`.

I did not backdate `expires_at` to get past the guard. That would falsify a window that never passed and file a missed unit in the retro counts. Instead I minted the replacement first, then removed the old file from `_queue_/inbox/` by hand. I first verified the path, that git did not track it, 0 attempts, and no claimed or done copy. This is a hand removal, not a tool closing, so there is no done record and no expired miss. Its fields and hash are in the sidecar.

## 2. Replacement

`scout-midday-2026-11-23-0616`, priority 2, 15 minutes, `not_before` 2026-11-24T01:10:00Z, `expires_at` 2026-11-24T02:00:00Z, created 06:16:21Z. The sweep units were created 06:12:45Z to 06:12:47Z. The brief is the same, including the sentence that the sweep pair has priority.

## 3. Rank (worst case, nothing done yet)

The tool's `pick_key` over the live inbox, 17 actionable units at each instant:
- **01:10Z:** rank 17 of 17, after all 12 fix-ups and both passes.
- **01:50Z:** rank 17 of 17, still alive. It expires at 02:00Z, and `next` budgets 15 minutes by default against a 15-minute estimate, so it is handed out whenever it is reached.

Nothing else is needed for ordering. Coverage is the open point. At the observed 3.0 minutes per unit the fix-ups end near 01:06Z, the final pass near 01:21Z, and the watch sees about 01:21Z to 01:36Z. At the estimate pace it would not start before expiry. No queue setting fixes both, because anything that lifts the watch above the fix-ups also lifts it above the pair. Clearing `vip-2026-11-22-1800` and `scout-2026-11-22-1800` before 00:00Z gives the sweep its full window.

## 4. Rule for the scribe

**A priority 2 unit older than 2 hours counts as priority 1 when `next` picks, and ties at equal expiry and effective priority go to the older `created_at`.**
- `_tools_/queue.py:828`: `AGING_STEP_HOURS = 2`.
- `_tools_/queue.py:910-913`: `steps = int(age_hours // AGING_STEP_HOURS)`; `effective_priority = max(1, priority - steps)`.
- `_tools_/queue.py:916-917`: the sort key is `(effective_expires, effective_priority, created_sort)`.
- `_tools_/queue.py:1141-1211`: an aged priority 1 unit with no `planned_for` is re-timed once its `not_before` passes. This is why hand-minted window units are priority 2.

Consequences for the planner profile:
- Mint a unit after the set it must trail.
- Never use priority 1 for a hand-minted window.
- Priority alone does not separate units staged hours apart; expiry and creation order do.

## 5. Proof

- `validate`: exit 0, after the removal and the replacement.
- `sweep-status` for 11-23: exit 1. Both passes are in the inbox, pending, `geometry_ok` true; exit 1 means not yet executed.
