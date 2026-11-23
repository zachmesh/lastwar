---
title: Forecast ledger schema
created: 2026-11-23T09:00:00Z
modified: 2026-11-23T09:20:00Z
version: 1.0.0
level: L3
description: The four kinds of forecast row, how the coach scores each, the source tags and the rule that a row is immutable once its action has run
status: unverified
grounded_in:
  - source: Steer A red team round 2 of 2026-11-23 08:57Z on the ledger schema
  - source: _records_/2026-11-22/strategy/forecast-ledger.csv
---

# Forecast ledger schema

The ledger is [forecast-ledger.csv](forecast-ledger.csv). A row is written before its action. Once the action has run, the row is never edited; a note goes in `amendment_note` and a correction is a new row. The coach fills the actual columns.

## Kinds

- **binary**: the action realizes or it does not. Columns `p_success` (my probability) and `value_if_success`. Scored with a Brier score and a reliability table by probability band.
- **continuous**: `predicted_low`, `predicted_point`, `predicted_high` are an 80 percent interval, point strictly inside, high over low at most about 3 unless the note states why. Scored by interval hit rate against 80 percent and by bias.
- **deterministic**: arithmetic on a known quantity, tolerance 3 percent in `tolerance_pct`. Excluded from calibration.
- **retired**: dropped before it ran, with the reason in the amendment note. Excluded.

A forecast whose honest answer is "zero or a lot" is two rows: a binary row for whether it happens and a continuous row for the size given that it does (F-006 with F-024, F-007 with F-025, F-017 with F-028).

## Source tags

`value_source` and `p_source`: M measured on this account, D derived from M, S sourced from a guide, G guess. `g_flag` marks a row with a G in either. The coach splits the error by tag; the lever table's `evidence_basis` names the G rows each rank rests on.

## Pairs and correlation

F-013 and F-014 share one mechanism and are scored as one pair. F-025 and F-028 are conditional on F-007 and F-017 and are scored only when the condition holds.

## Known weaknesses

Rows F-003 and F-004 were created after a first failed attempt at 08:30Z. F-001 was restored after an edit that followed its action. Thirty rows are too few for a reliable hit rate; read the first calibration as a drift signal, not a grade.
