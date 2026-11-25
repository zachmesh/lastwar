---
title: Zero Sweep Rules For The Pre Reset Sweeps 2543 2026-11-25
created: 2026-11-25T14:20:00-08:00
modified: 2026-11-25T14:20:00-08:00
level: L0
version: 1.0.0
description: The rules the pre-reset zero sweep units apply to the ledger walk - the bubble lines, the Main Tasks claims, the VIP lines and the tram lines - moved out of the units to keep them under 450 words
status: done
activity: queue-planning
run_id: queue-planning-2026-11-25-1420-zero-sweep-rules
trigger: the 22Z plan, the zero sweep units over the word gate
started_at: 2026-11-25T14:12:00-08:00
finished_at: 2026-11-25T14:20:00-08:00
verified: each rule copied from note 3120 and the ledger articles 20261125-01 and 20261125-02, and from the older zero sweep unit text for the VIP and tram lines
grounded_in:
  - source: _records_/2026-11-22/queue-planning/3120-next-plan-specifics.md
  - source: _conventions_/local-conventions/daily-ledger-sections/entry-20261125-01.md
---

# Zero sweep rules, 2543

Apply these in both zero sweeps (the first pass and the final pass).

## Bubble lines (ledger 20261125-01)

The food, iron and coin bubble lines are 'structural, not counted': a bubble line is at zero if the harvest unit's last collect is within 3 hours and 'available' after it is under 1 percent. The denominator is 20. Both definitions go in the report header every day.

## Main Tasks (ledger 20261125-02)

A green Claim found on the Main Tasks tab is a priority-1 fix-up (`--serves upkeep`): a plain Claim, once per row, never Go.

## VIP lines

The avatar is NEVER tapped (Steer A 00:40Z): read a VIP line only through a VIP entry in the left column or the HUD, else 'unreadable'.

## Tram lines (armed truck, train)

No badge at the first read: WORLD then BASE (one tap each on the standing corner button, no icon), read the tram icon once more. Write its state (absent, bare, badge N) and the UTC times (the Coach's control: it should stay absent).
