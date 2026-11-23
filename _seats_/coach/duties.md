---
title: Coach seat duties
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-23T06:08:00Z
level: L2
version: 0.2.0
description: The per-firing checklist for this seat
status: unverified
grounded_in:
  - source: TEAM.yaml 0.1.0 and continuous-play-team.md 0.1.0
---

# Duties - coach

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

## Record

Write the run at `_records_/<date>/<activity>/<HHMM>-run.md` and append the
day index. The record carries inputs, outputs, stats and follow-up.
