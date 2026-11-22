---
title: Harvest queue run 0049
created: 2026-11-21T09:01:00Z
executor: ticker-0048
unit: harvest-2026-11-20-2203
status: partial
---

# Harvest - 0049 queue run (partial)

Session 00:49-01:03 PT (08:49-09:03Z), executor ticker-0048, unit
harvest-2026-11-20-2203 (planned for 2026-11-21 06:03Z, expires
2026-11-21 10:03Z). First game unit since ticker-0214 gifts on
2026-11-17 02:14 PT - about a 94 hour gap; the Mac mini is back
online (device list: online, last seen 2026-11-21T07:00:54Z).

## What happened

- Last War was not running. Opened it from the Mac; the game showed
  a TIPS dialog "Update complete, please restart the game." with a
  Confirm button. Tapped Confirm (coordinate 488,569); the game
  restarted cleanly into the base view. No login was demanded, no
  "active on a different device" dialog appeared, no verification
  code was asked.
- Resource panel at entry (read live from the top bar): food 665.3M,
  iron 1.0G, coin 47.4M, diamonds 17.72K, total power 149,653,371.
- Resource panel at close: food 665.3M, iron 1.0G, coin 50.2M.
  Coin moved +2.8M during the unit. Attribution is UNVERIFIED: no
  bubble tap in this unit was verified to move a total, so the
  +2.8M may be a login auto-collect after the update restart rather
  than a bubble collection. Food and iron did not move.
- Four bubble taps, none verified as a collection:
  - Tap 1 at (344,410) on the pre-shift framing: visual change in
    the tap region; coin read 50.2M afterwards.
  - Tap 2 at (441,556) selected Farmland Lv.28 instead of a bubble
    (no collection); deselected by tapping empty ground.
  - Tap 3 at (309,358) selected Component Factory Lv.20 instead of
    a bubble (no collection).
  - Tap 4 at (344,410) re-grounded on a fresh screenshot: visual
    change in the bubble area, but food and coin totals unchanged
    afterwards - collection NOT verified.
- The "Time to board!" train bubble was visible on the left edge;
  that is the alliance-train unit's work, not this unit's, and was
  left alone.
- The Armed Truck was not located or checked in this unit.

## Remaining work

- Many green and white resource bubbles remain visible over the
  farmland and the gold buildings; the Armed Truck loot state is
  still unchecked. The next tick re-produces this regular as a
  fresh unit (partial: tracker untouched).

## Blocker - tap method (R2, second consecutive miss of this kind)

- Bubble taps keep falling through to the buildings underneath
  (Farmland, Component Factory), and tapping a building re-centers
  the camera on it, shifting every coordinate grounded earlier.
  The next unit must pivot: re-ground each tap on a fresh
  screenshot taken immediately before that tap, verify the tap's
  effect on the resource totals before the next tap, and prefer a
  cropped/zoomed grounding of the bubble center. Do not repeat
  blind re-taps on stale coordinates.

## Delivery

- VPS SSH still Permission denied (publickey) - the outage since
  2026-11-12 continues (about 204 hours). Push and PR delivery
  are impossible this pass; the commit sits on the local
  records/2026-11-21 branch (from main 22601972), push pending
  VPS recovery.
- NEW (found while committing): the live tree's
  `_logs_/repo-actions/action-log.jsonl` has DIVERGED from main's
  lineage - live 533 lines (starting at the 2026-10-25 repo
  creation) vs main's 1964 lines (2026-10-29 to 2026-11-12).
  The branch commit therefore carries main's log plus this pass's
  entry only (1965 lines), NOT the live tree's copy - copying the
  live copy would have deleted about 1400 log lines. The live
  log's missing entries (including today's other passes' entries,
  which exist only in the live file) need a recovery-time
  reconciliation; file as a GitHub Issue (records/tooling class)
  when the gh route is back. Do NOT copy the live action-log
  over a main-lineage copy.
- The action-log check reports 3 pre-existing bad lines (374,
  380, 381 - concatenated Nov 3 ticker entries plus one blank
  line, the #422 tail shape). The live `log_append.py` is 1.0.0
  and has no `gate` command (gate is PR #425, unmerged), and
  1.0.0 `repair` refuses the file, so no repair was attempted;
  this pass's own entry appended cleanly at the tail.
- Device token released at pass end; computer session cc-1 ended
  with the game left on the base view (Component Factory
  selected, harmless).

## Stats

- coin_before 47.4M, coin_after 50.2M, food_before 665.3M,
  food_after 665.3M, iron_before 1.0G, iron_after 1.0G
- verified no, blocker_category c (tap method)
- bubbles_remaining many, truck_checked no
