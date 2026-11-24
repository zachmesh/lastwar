---
title: Shop claims scroll recipe
created: 2026-11-24T13:07:41Z
modified: 2026-11-24T13:07:41Z
version: 0.1.0
description: The composed press, hold, move, hold, release pan that moves a clipped page, with the nine drags measured and the first working result
---

# Shop claims scroll recipe

Dated 2026-11-24, from the Coach's drag table (`_records_/2026-11-22/coach/drag-distance-table.csv`) and record `_records_/2026-11-22/shop-claims/1301-queue-run.md`. Back to [how to enter](how-to-enter.md).

## The recipe

On a clipped page start from the blank right margin, in ONE message: mouse_move to the start, left_mouse_down, wait 1 s, ONE move of 175 px, wait 1 s, left_mouse_up, then the screenshot after the up; a malformed or missing wait refuses the whole batch and nothing runs. Then tap the now-visible claim once, only if it is a plain Claim with no price, gem or diamond icon.

## The evidence

Nine drags on the Weekly Pass page. Single drag events: three from a card (320 px) moved 0; from the blank right margin 70 px and 135 px moved 0, and 250 px flung the page out of view. The composed pan of experiment 007 (13:01:54.9Z, (685,650) to (685,475), holds of 1 s, 2,371 ms) moved it 150 px with no fling: the S1 Claim went from y 915 (clipped) to 765, and one tap paid Drone Parts x15 (the card then reads Already claimed today).

## Still open [G]

Why it works: 150 px moved for a 175 px pan (perhaps a touch slop). After the result the Coach weighs touch duration 0.56, distance threshold 0.22, movement duration 0.13. A clean one-variable test is not run, by Steer A's ruling.
