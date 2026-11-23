---
title: Enforcement
created: 2026-11-23T09:06:47Z
modified: 2026-11-23T09:06:47Z
version: 0.1.0
sequence: 8
description: tools_/duel.py prints today's duel day, theme, gate and radar posture.
---
## Enforcement

- `_tools_/duel.py` prints today's duel day, theme, gate and radar
  posture. Every scheduled run reads it first and follows the gate:
  on preserve days the radar regular is marked skip with the duel
  reason instead of being emptied; on Day 1 it is worked first.
- `_tools_/regulars.py` remains the per-day ledger of what was done;
  the gates change how a regular is worked, never whether it is
  accounted for.
- `_tools_/resource_map.py check` output rides along in run reports
  whenever a flag is raised.

