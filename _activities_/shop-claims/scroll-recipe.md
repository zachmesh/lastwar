---
title: Shop claims scroll recipe
created: 2026-11-24T13:07:41Z
modified: 2026-11-24T23:37:20Z
version: 0.2.0
description: The composed press, hold, move, hold, release pan that moves a clipped page, with the nine drags measured and the first working result
---

# Shop claims scroll recipe

Dated 2026-11-24, from the Coach's drag table (`_records_/2026-11-22/coach/drag-distance-table.csv`). Back to [how to enter](how-to-enter.md).

## The recipe

On a clipped page send ONE message: mouse_move to the start point, left_mouse_down, wait 1 s, ONE move of 175 px, wait 1 s, left_mouse_up, then the screenshot after the up. A malformed or missing wait refuses the whole batch and nothing runs. The page moves about 150 px (12 pans on the Weekly Pass page: 150 or 149). Then tap a now-visible claim once, only if it is a plain Claim with no price, gem or diamond icon.

## The start point is page-specific

| Page | Start | Moved |
|---|---|---|
| Weekly Pass (shop) | blank right margin, x 685 | 150 px (`_records_/2026-11-22/shop-claims/1301-queue-run.md`, `1327`) |
| History list, Dispatch tab | blank right margin, x 670 | 150 px (`_records_/2026-11-22/truck-plunder/1850-queue-run.md`) |
| Backpack grid, Speed-up then Resources tab | margin, x 665 | 0 px twice (`_records_/2026-11-22/perception-scout/1601-queue-run.md`) |
| Thanksgiving Store list | strip right of the rows, x 639 | 0 px (`_records_/2026-11-22/event-claims/1927-queue-run.md`) |
| Backpack grid, Special tab | centre of a tile-gap crossing, (274,448) | 143 px, no tile selected (`_records_/2026-11-22/perception-scout/2315-queue-run.md`) |
| Backpack grid, Resources tab | the same pixel | 150 px, no selection (`_records_/2026-11-22/perception-scout/2328-queue-run.md`) |

On a Backpack grid start at the CENTRE of the crossing of a gap between tiles; the gap is about 20 px wide, so there is no 60 px rule (n = 2). A card start moved nothing (three drags of 320 px).

## Still open [G]

Why the margin works on some pages only, and why 150 px moves for a 175 px pan. A single drag event moved nothing at 70 and 135 px and flung at 250 px.
