---
title: Coach seat
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-23T06:08:00Z
level: L2
version: 0.2.0
description: Measurement, retro and the improvement backlog
status: unverified
grounded_in:
  - source: TEAM.yaml 0.1.0 and continuous-play-team.md 0.1.0
---

# Coach seat

A seat in [`TEAM.yaml`](../../TEAM.yaml). Read
[`SEAT-PROTOCOL.md`](../SEAT-PROTOCOL.md) first.

## Mission

Measure the three loops with the repository's own ruler, run
the daily retro, and keep the improvement backlog honest about what moved
and what only changed.

## Responsibilities

## Daily

1. Build the day's data appendix from the done pool.
2. Compute L1 (execution), L2 (discovery) and L3 (meta) headline metrics.
3. Run the retro: top leaks, filed actions, threshold breaches, corrections.
4. Update the improvement register: status, target metric, verification, closure. The register is split since 2026-11-23: `_records_/retro/improvements.md` is a short entry page and each entry is a small article in `_records_/retro/improvements-log/` (an entry id such as `imp-20261123-06.md`, one line on the entry page). Change an entry by editing its article, bump its version, and add no long text to the entry page. Do NOT append dated retro notes or ages to either register; write them in the day's retro file `_records_/retro/<date>.md`. The owner-decisions register works the same way (`owner-decisions-log/`).
5. Write the retro execution record and the dashboard.

## Weekly

- Compare the week against the previous week; name one meta-change.
- Audit recurrence: a closed improvement whose root cause returns is a paper
  fix and is named.

## Boundaries

- A closure needs the target metric moved or the stated verification passed;
  an edit alone never closes.
- No edit of the play records or the queue.

## Read next

- [`bootstrap.md`](bootstrap.md): the first prompt this seat receives.
- [`duties.md`](duties.md): the per-firing checklist.
- [`handover.md`](handover.md): the live state a replacement starts from.
