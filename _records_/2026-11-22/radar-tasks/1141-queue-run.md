---
title: Radar queue run 1141
created: 2026-11-22T19:41:00Z
modified: 2026-11-22T19:41:00Z
version: 1.0.0
description: Radar unit radar-2026-11-22-1003, ticker-1104, done, stack posture
status: unverified
grounded_in:
  - source: live game screens on the owner Mac mini, 2026-11-22 11:35-11:41 PT
  - source: tools/duel.py --json, 2026-11-22 11:35 PT
---

# Radar queue run 1141

- Executor: ticker-1104, unit radar-2026-11-22-1003, 11:35-11:41 PT.
- Status: done. Stack posture, duel day 7 (off day, settlement).
- Duel posture (tools/duel.py, 11:35 PT, live re-read): duel_day 7, theme "Off day - settlement", radar_posture stack. Day ends 18:00 PT. Gate: stack radar for Day 1, complete, do not claim; never sit at the cap across a 6 hour refresh; power freeze caution for the Sunday assessment window.
- Entry verified on the radar screen itself: Lv.13, radar points 533, stored 23/40, stamina 120. Restore line: "12 Radar Task(s) will be restored in 01:01:27". Dish grounded fresh at norm (53,718) from the live base screenshot and opened on the first tap with move-wait-click. Entry route note: NO open_app was called this unit - the game was already running, so the pass listed windows and activated the original window 127196 with raise=true (see the harvest unit's Issue #822 finding); the duplicate window 127250 was left untouched.
- Blocker, named per the stack standard: the bottom bar presented Claim All only ("11 task rewards can be claimed") with NO Quick Execute offer, at entry and after a 60 second wait. Claim All was NOT tapped (stack day; claims score on release days only). No ordinary task was executable in this unit.
- Restore observation: stored moved 23/40 to 28/40 during the 60 second wait - the restore lands in chunks, not as one batch at the timer end. The restore line's "12 tasks in 01:01:27" did not match a +5 move in one minute; the trickle mechanism is still open (profile open question).
- Closing reads: stored 28/40 (headroom kept, not at the cap), pending rewards 11, radar points 533 (unchanged - points move only on claim), stamina 120 (unchanged - nothing spent).
- Pin inventory (stack day - inventoried, none tapped): blue person pin and purple skull pin with red dots (top centre), blue oil-barrel pin with red dot (right), green skull pin with red dot (lower left), blue oil pin with red dot (lower centre), grey handshake pin with red dot (lower right). Six pins standing, all with red dots - the same six the 0524 unit inventoried.
- Exit: home button tapped once, base screen verified (coin 109.2M, power 147,972,169).
- No diamonds or money spent, no paid button tapped, no pin tapped, nothing claimed. No red line touched.
- Tracker: radar marked done for this slot.
- Follow-up: none.
