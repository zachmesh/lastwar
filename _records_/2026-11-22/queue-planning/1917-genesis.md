---
title: Queue Planning Genesis Reset 1917 2026-11-22
created: 2026-11-22T19:17:00-08:00
modified: 2026-11-22T19:17:00-08:00
level: L0
version: 1.0.0
description: Genesis reset of this checkout's stale queue snapshot - 300 expired by reap, 412 stale copies dropped, 15 duplicates dropped by sync, 2 no-expiry units repaired and expired, inbox 766 to 37, done 2310 to 2612, validate 0 / slot-coverage 1 / sweep-status 1; the old live pool's done units are a data gap, not zero
status: done
activity: queue-planning
run_id: queue-planning-2026-11-22-1917-genesis
trigger: coordinator directive 2026-11-22 about 19:14 PT - genesis reset, not a live-pool recovery
started_at: 2026-11-22T19:15:01-08:00
finished_at: 2026-11-22T19:17:00-08:00
verified: measured before/after counts by file count and by queue.py list_units; reap/sync/validate/slot_coverage/sweep-status exit codes captured this pass; git status on _queue_ clean at HEAD before the pass and 1,031 changed paths after it (729 inbox deletions, 302 done additions)
grounded_in:
  - source: coordinator directive 2026-11-22 - one genesis reset pass because this checkout's _queue_ is a stale snapshot, not the previous host's live pool; first 19:11 PT pass was reverted by the coordinator
  - source: measured 2026-11-22 19:15:01 PT - inbox 766, claimed 0, done 2310, git status _queue_ clean at HEAD
  - source: _records_/2026-11-22/queue-planning/1440-run.md - live pool (previous host, /home/hatch/workspace/lastwar) inbox 96, claimed 0, done 2884 at 2026-11-22T22:44:51Z
  - source: coordinator statement - records/2026-11-22 branch holds 636 inbox / 2259 done
---

# Queue planning - genesis reset, 2026-11-22 1917

Genesis timestamp: **2026-11-22T19:15 PT (now)**, not the snapshot
date. This pass is a genesis reset of a stale queue snapshot, not a
live-pool recovery: the previous host's live pool was not migrated
with this clone. No game input, no device token, no computer-use run,
no claim/done execution. This pass only managed queue files.

## Migration finding

This checkout's `_queue_` is a stale snapshot. Evidence:

- Pre-pass `git status --porcelain _queue_` was empty (clean at HEAD),
  and the pool held inbox 766 / claimed 0 / done 2310.
- The 2026-11-22 day index and the 1440 queue-planning record measure
  the live pool on the previous host at, respectively, inbox 96 /
  done 2884 and inbox 96 / claimed 0 / done 2884 at 22:44:51Z.
- The coordinator states the records/2026-11-22 branch holds 636
  inbox / 2259 done - a third divergent state.

The live pool therefore lives outside this tree; this tree's queue is
a snapshot whose content dates from 2026-11-10 to 2026-11-21. A first
19:11 PT pass moved 300 units to done; the coordinator reverted it
because it was a live-pool recovery aimed at the wrong pool. This pass
re-measured the reverted tree and re-ran as a genesis reset.

## Freeze snapshot (before)

| State | Count | Note |
|---|---|---|
| inbox | 766 | unit windows 2026-11-10 to 2026-11-21 |
| claimed | 0 | device token only, no unit |
| done | 2310 | snapshot history, not the account's full history |

Oldest inbox unit at freeze: `scout-scout-2026-11-10-010`, id/window
date 2026-11-10, `created_at` 2026-11-12. Content split: 12 units
dated 2026-11-10, 3 dated 2026-11-11, 59/134/134/114/110/108 dated
2026-11-12 to 2026-11-17, plus 73 dated 2026-11-22 and 14 dated
2026-11-23 (current and next windows).

## Recovery actions and exit codes

1. **freeze** - counted the pool and recorded the migration finding
   above (no tool; file counts and `git status`).
2. **reap** - `python3 _tools_/queue.py reap`, exit **0**:
   `reaped 0 expired claim(s), expired 300 stale unit(s)`. The 300 had
   a passed `expires_at` and no done record, so each moved to done with
   result status `expired` and `stats_missing` set. A further **412**
   stale inbox copies were dropped, every one with reason "already has
   a done record" (the done record was kept, the duplicate copy
   removed). After reap: inbox 54 / claimed 0 / done 2610.
3. **sync** - `python3 _tools_/queue.py sync`, exit **0**:
   - `reaped` 0, `expired` 0, `stale_done_dropped` 15 (all with an
     existing done record: 6 `scout-scout-2026-11-10-*`, 2
     `scout-scout-2026-11-20-013/017`, 6
     `zombie-invasion-zombie-2026-11-10-*`, `donations-2026-11-22-0921`)
   - `branch_done_reconciled` [], `branch_done_reconcile_warning`
     null, `blockers_reaped` [], `completion_markers_reaped` [],
     `completion_markers_lost` []
   - `due` 24, **`produced` 0** (the <=20 staging guard did not fire;
     0 new units staged), `already_queued` 23 (every due non-fixed-slot
     regular already had its current-window unit staged),
     `skipped_closed` [], `expired_window_refusals` [],
     `chain_seq_refusals` [], `roster_stale_regulars` []
   - After sync: inbox 39 / claimed 0 / done 2610.
4. **residual repair (disclosed direct edit)** - exactly two units had
   no `expires_at` and so could never be retired by the expiry path:
   `donations-2026-11-22-1241` (not_before 13:05Z, window closed well
   before the 18:00 PT reset) and `scout-scout-2026-11-20-019` (chain
   `scout-2026-11-20` day ended at its 18:00 PT reset). Both had no
   done record and no completion marker. `queue.py complete` cannot
   write status `expired` (its choices are done/partial/failed/
   skipped-needs-owner), so the only supported expiry path is
   `expires_at` + sync. Repair: set `expires_at` on the two inbox
   copies only - `donations-2026-11-22-1241` to
   `2026-11-23T02:00:00Z` (the current reset instant) and
   `scout-scout-2026-11-20-019` to `2026-11-21T02:00:00Z` (its chain
   day's reset); both original values were empty. This is the only
   direct unit-file edit in this pass; no play data was invented, and
   the miss records themselves were written by sync below.
5. **sync again** - exit **0**: `expired` 2 (the two repaired units,
   closed as `expired` with `stats_missing`), `produced` 0,
   `already_queued` 23, `stale_done_dropped` 0,
   `branch_done_reconcile_warning` null. After: inbox 37 / claimed 0 /
   done 2612.

## After state

| State | Count |
|---|---|
| inbox | 37 |
| claimed | 0 |
| done | 2612 |

- No inbox unit has an empty `expires_at`; no inbox unit has
  `expires_at` at or before now.
- The 37 = 22 current-window units (local 18:00/18:03/18:30/18:57
  slots, planned_for 02:00/02:03/02:30/02:57Z) + 1 `scout-midday`
  07:00 window still open to 07:00 tomorrow + 14 upcoming units
  (2026-11-23 02:03/02:30 local windows).
- Oldest remaining inbox unit: `scout-midday-2026-11-22-0700` (id date
  2026-11-22, window still open). No inbox unit is id-dated before
  2026-11-22.
- Change set in the working tree, left uncommitted for the coordinator:
  1,031 paths - 729 inbox deletions and 302 done additions. 729 = 766
  before - 37 after; 302 = 2612 - 2310.

## Tool proof

| Command | Exit | Reading |
|---|---|---|
| `queue.py validate` | **0** | `pool valid` |
| `slot_coverage.py check --date 2026-11-22` | **1** | 0 covered, 38 recordless past-window, 10 future (slots 0004 to 1834) |
| `queue.py sweep-status` | **1** | zero-sweep pre-reset pair for 2026-11-22 missing (1600 first pass, 1700 final pass), executed 0 of 2, pair_complete false, geometry_ok false |

The slot-coverage and sweep-status failures are snapshot facts, not
this pass's regressions: the snapshot never ticked today, so 38 past
slots have no record, and today's sweep pair was never staged here.
This checkout's zero-sweep roster is `reset_utc 02:00` with
`slots_before_reset_minutes [120, 60]` (16:00/17:00 local), while the
1440 record's live pool held a 1630/1730 pair (90/30 geometry) - issue
#606/#410 class geometry drift between hosts. No sweep pair was staged
now; the next plan pass must reconcile the roster before staging a new
pair, and no missed pair is backfilled.

## Data gap - explicit

The old live pool's done units are a **data gap, not zero**. This
checkout's done count (2,612 after this pass; 2,310 before) is not the
account's execution history: the live pool held 2,884 done at
22:44:51Z and the records/2026-11-22 branch holds 2,259. Three
divergent states exist and none was imported, merged or reconstructed
this pass; the live pool was not migrated with the clone.

Historical retro metrics come from the delivered data files, not from
this pool: `_records_/retro/<date>.md` and its canonical appendix
`_records_/retro/<date>-data.json` are the evidence of record. The 300
+ 2 `expired` records written this pass are genesis miss records for
snapshot duplicates and stale units; they are not evidence that the
live account missed that play.

## No backfill

`sync` produced 0 new units in both runs. No missed cycle was staged,
no catch-up flood was created, and no slot was backfilled with a
stillborn unit. The 22 current-window units were already staged in the
snapshot; staging the next window belongs to the next plan pass.

## Follow-up

1. Coordinator: decide delivery for this record and the 1,031-path
   queue change set (commit/push with the action log; the day index
   entry is outside this seat's write scope). Left uncommitted here.
2. Coordinator/scribe: file the migration finding (live pool not
   migrated with the clone) in the improvements backlog; any attempt to
   recover the previous host's pool or the branch's 2,259 done is an
   owner decision, not a planner action.
3. Toolsmith: `enqueue` with `--not-before` and no `--expires-at` mints
   a unit the expiry path can never retire
   (`donations-2026-11-22-1241`), and a scout chain successor for an
   ended chain day still slips through
   (`scout-scout-2026-11-20-019`, chain `scout-2026-11-20`) - issue
   #818 class. Both are now retired as genesis misses.
4. Next planner pass: run a normal plan pass from a fresh main
   worktree (issue #694 guard), reconcile the zero-sweep roster
   geometry before staging tomorrow's pair, and treat the current 37
   inbox units as the only playable set.
5. Carry the 38 recordless past-window slots and the missing sweep pair
   into the retro as missed - never backfilled.

## Stats

- expired 302 (300 by reap, 2 by the disclosed repair); dropped
  duplicate copies 427 (412 by reap, 15 by sync); reaped claims 0
- produced 0; already_queued 23 in each sync; due 24
- inbox 766 -> 37; done 2310 -> 2612; claimed 0 throughout
- validate 0 / slot_coverage 1 / sweep-status 1
- genesis timestamp 2026-11-22T19:15 PT; no game input, no device
  token, no computer-use run
