---
title: Brief - two read-only count reads that straddle the 02:00Z reset
created: 2026-11-23T16:45:00-08:00
modified: 2026-11-23T16:52:00-08:00
level: L0
version: 1.1.0
description: Unit brief for two read-only donation count reads before and after the 02:00Z daily reset, separating no reset, reset to zero and refill to 30 without the elsewhere-use confound of the 03:30Z pass
status: unverified
grounded_in:
  - source: coach registration refill-reset-test-prereg.csv, anchor 00:37:57.17Z
  - source: _records_/2026-11-22/alliance-donations/2115-queue-run.md, pass 003 anchor series and the 02:00Z reset in the shop and duel records
---

# Two reads across 02:00Z

**Leaves the game: none. No tap on Donate; read only; nothing spent.** If any other app comes to the front, stop and touch nothing.

**Why.** A 4 at the 03:30Z pass is either a reset to 0 or no reset plus 5 elsewhere taps. Two reads 20 minutes apart leave almost no room for elsewhere use, and spend no counts, so the pass 004 anchor stays 00:37:57.17Z.

**Do, twice (about 5 steps each).**
1. Confirm LastWar is frontmost; Alliance shield (ground fresh), Techs tile, the recommended node (Quick Construction 9/10).
2. Read the count, or the grey timer if the count is hidden; read the UTC time to the second.
3. Close with the panel X and back arrow. No Donate tap.

**Read A: 01:48 to 01:55Z** (before the 01:57:57 grid point). Predicted 4 [1 + floor((entry - 00:37:57.17) / 20 min)].
**Read B: 02:03 to 02:12Z** (after 02:00, before the 02:17:57 grid point; the 01:57:57 point falls between the reads).

| Read B shows | Reading |
|---|---|
| 5 (A + 1) | no reset; the refill clock ignores 02:00Z |
| grey timer ending 02:17:57 within 3 s | reset to 0, grid kept |
| grey timer ending about 02:20:00 | reset to 0 and the grid restarted at 02:00:00Z; the old grid is dropped, re-anchor on the end |
| 30 | refilled to 30 |
| A exactly | one elsewhere tap or one missed refill; flag, ask the owner |
| any other value | flag; log the owner-activity check |

A count above A + 1 flags the model at any size; elsewhere use only lowers it.

**Record:** both read times to the second, the counts; if grey, the timer value and its read time, so the end (read time plus timer) is computed to the second, not only the count.

**Risk and spend.** Nothing spent; both screens are in game. Each read costs about one short unit.
