---
title: treasures 2026-11-08 ticker-2235 queue run
created: 2026-11-09T06:55:00Z
modified: 2026-11-09T06:56:00Z
version: 1.0.0
description: Hidden treasures unit treasures-2026-11-08-1857 executed by ticker-2235
status: done
grounded_in:
  - source: game screens observed live on the owner Mac mini, 2026-11-08 about 22:54 to 22:55 PT
---

# treasures 2026-11-08 ticker-2235 queue run

- Unit: treasures-2026-11-08-1857 (regular treasures, activity hidden-treasures)
- Executor: ticker-2235
- Session window: about 22:54 to 22:55 PT, 2026-11-08 (device session cc-186)
- Status: done

## Performed

- One treasure dig executed (Dig 1 time, Skip Animation on).
  Congratulations panel rewards, read live from its six tiles:
  chest stack x24, coin sacks x12, gold coins x24, medal 600,
  blue triangle 400, silver ingots 100. The chest tier won was
  not displayed on the panel.
- Fragment stocks verified live before and after the dig. Before:
  M1 x17, M2 x14, M3 x3, M4 x7, M5 x5, M6 x7, M7 x13. After:
  M1 x16, M2 x13, M3 x2, M4 x6, M5 x4, M6 x6, M7 x12 - exactly
  one of each fragment consumed. Chest progress 7/15 before,
  8/15 after. The Dig button now reads "Dig 2 time(s)": 2 digs
  remain by stock, capped by M3 x2.

## Not performed

- The remaining 2 possible digs were not taken: one dig per
  unit is the activity's standing pattern, and the stock stays
  for the next treasures unit.

## Notes

- The Hidden Treasures tab badge read 1 both before and after
  the dig, while the stock allowed 3 digs before and 2 after,
  so the badge does not count digs possible by stock. Its
  meaning stays open.
- No fragment exchange was opened or executed (needs owner
  approval).

## Red lines

- No diamonds or money spent. No speedups burned. No paid
  button tapped. No fragment exchange. No login or
  verification was demanded, and no different-device dialog
  appeared.

## Delivery note

- The local working tree sits on branch
  work/ops-execution-records and holds another job's
  in-flight state (unrelated modifications and deletions),
  so this pass's outputs are delivered through a temporary
  worktree onto the records/2026-11-08 branch, leaving
  that state undisturbed. PR 460 already covers the
  branch, so no new PR is opened.

## Outcome

Done. One treasure dig executed and verified: one of each
fragment M1-M7 consumed, chest progress 8/15, 2 digs remain
by stock. No diamonds or money spent, no speedups burned,
no paid button tapped. No alliance diplomacy, no assembly,
no teleport.

## Result stats

- target 1, achieved 1, resources_gained (chest-stack x24,
  coin-sacks x12, gold-coins x24, medal 600, blue-triangle
  400, silver-ingots 100), costs 2min-no-items-spent,
  verified yes, device_takeovers 0, follow_up none
