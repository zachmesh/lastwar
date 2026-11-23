---
title: Harvest and pool tools
created: 2026-11-23T04:53:59Z
modified: 2026-11-23T04:53:59Z
version: 1.0.0
description: Verbatim index rows for harvest_verify.py, pool_gap.py
---

# Harvest and pool tools

Moved verbatim from the former `_tools_/INDEX.md` table; only link destinations are adjusted for this folder. Back to the [tool index](../INDEX.md).

| Tool | Purpose | Data |
|---|---|---|
| [harvest_verify.py](../harvest_verify.py) | Verify a harvest tap log, the tool slice of issue #250: a tap counts as collected only when a per-tap HUD-movement check or bubble clearance on the follow-up screenshot proves it, and a grounding hit that reveals a selected building is flagged suspect-factory and never counted (the #250 failure was factory-top markers read as resource bubbles); consumes the executor's JSON tap log - normalized 0..1000 points, grounding label, building, before and after HUD reads with K/M/B suffixes, outcome cleared/selected-building/toast/still-present - and returns the verified count, the per-resource deltas of verified taps only and the re-probe list the next harvest unit resumes from, excluding a HUD key present in only one of before/after for having no baseline or no follow-up; it never taps, drives a device, captures screenshots or runs visual grounding; `verify --log` with `--format text` or `json` | executor tap log JSON and the harvest unit record |
| [pool_gap.py](../pool_gap.py) | Measure the branch-versus-live queue pool gap at one snapshot so a retro never hand-counts two pools out of bundles, the measurement slice of issue #251: reports done units in the rolling window, the per-date difference, inbox total, inbox past-expiry and inbox ids already closed in done, dating every unit by result.finished_at, else started_at, else planned_for, else its file-name date (the retro_report.py rule applied identically to both pools, with no records-INDEX fallback, so a pool is measured purely by the files it holds); the #251 closure verdict is PASS when the absolute done-in-window gap is under 10 units and the branch inbox past-expiry count is 0, exit 0 PASS, 1 FAIL, 2 usage or pool error, and a pool root holding no state directory is an error rather than a silent zero; `--days`, `--end`, `--now` and `--format text` or `json` | two pool roots, a branch checkout and the live working tree, each read at `<root>/_queue_` |
