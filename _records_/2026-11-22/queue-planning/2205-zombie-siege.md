---
title: Queue Planning Zombie Siege Timing 2205 2026-11-22
created: 2026-11-22T22:08:00-08:00
modified: 2026-11-22T22:08:00-08:00
level: L0
version: 1.0.0
description: Planner answer to assignment A-20261123-0601 - server time reads UTC-2, so the Zombie Siege 23:15 item is 01:15Z and already past, not 07:15Z; no unit for the closed event, one read-only To-do List unit drafted
status: done
activity: queue-planning
run_id: queue-planning-2026-11-22-2205-zombie-siege
trigger: coordinator assignment A-20261123-0601-planner
verified: offset from four recorded readings plus the reset anchor; the event time rests on one fold of a branch-side record; nothing run against the game or the queue
grounded_in:
  - source: _records_/2026-11-22/queue-planning/2205-zombie-siege-rows.json rows 1 to 14
  - source: issue 814 as quoted in the assignment and in _records_/2026-11-21/perception-scout/0604-queue-run.md
---

# Zombie Siege (issue #814) - when, and does the queue need a unit?

File-only; nothing enqueued, staged or played. Rows, commands and the unit brief are in [the sidecar](2205-zombie-siege-rows.json).

## Answer

The siege most likely already ran. Server time reads about two hours behind UTC, so "23:15" is 01:15Z on 2026-11-23 (17:15 PT on 11-22), not 07:15Z. Nothing supports server time equal to Pacific time.

## 1. Offset: UTC-2, verified

- 2026-11-08: Server Time 10:17:10 at about 04:18 PT (12:18Z); the same screen shows the weekly refresh "Monday 00:00 server" 13:43:38 away, which is 02:00Z (rows 1, 2, 4).
- 2026-11-21: To-do List header 12:09:10 at about 06:14 PT, labels 4 to 7 minutes late (row 3).
- Daily reset 02:00Z is ruled, so server midnight is the reset (row 5).

Residual, unverified: two Wanted Boss countdowns to "server 00:00" end at 01:00Z, which alone implies UTC-1 (row 7). The siege is past either way (00:15Z).

## 2. Candidate times

- A, supported (UTC-2): 2026-11-23 01:15Z, stage 01:15-01:45Z, ended about 4h20 before 06:05Z.
- B, assumed (server = PT): 2026-11-23 07:15Z, stage 07:15-07:45Z, opens in about 1h10.

Check on A (row 6): a harvest unit at 17:09-17:24 PT saw "Zombie Siege is about to attack: 00:02:49" with the clock at 23:12-23:15. Fold only; the raw record is on the records branch.

## 3. What it is and pays

Alliance Events tab Zombie Siege, mode Alliance Exercise: 30-minute Battle Stage, top alliance damage pays everyone, the top Commander may multiply rewards 10x, Offline Participation auto-joins allied rallies and is already on (row 8, text verified, outcome unverified). The Alliance Exercise reward mail paid EXP 105.8M, coin 12.1M, food 19.0M, iron 19.0M and about 120 five-minute speedups (row 9, verified 11-03). The To-do List lists the two events separately, so crediting that pay to the siege is unverified. Siege Reports carried no attachments; the siege's own pay, cost and cadence are unresolved (rows 10-12).

## 4. Does the queue need a unit?

Not for the closed occurrence, and not as play: rally and attack are a red line, and auto-join already covers it. No regular until two occurrences are time-stamped. One read-only unit is worth minting: a To-do List read that settles the offset and times the next siege. Both cases have a command in the sidecar, each with `--not-before` and `--expires-at`. `enqueue` cannot carry a brief (free text only in `--window`), so the red-line brief rides in the operator assignment.

## 5. Settling observation

Operator opens the To-do List and reads Server Time beside UTC: about 04:05 at 06:05Z confirms A, about 22:05 confirms B. It also checks Alliance mail for a Siege Report dated about 01:15-02:00Z.
