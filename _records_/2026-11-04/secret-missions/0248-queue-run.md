---
title: Secrets Queue Run 0248
created: 2026-11-04T10:48:00Z
modified: 2026-11-04T10:48:00Z
status: partial
executor: ticker-0234
unit: secrets-2026-11-03-2257
---

# Secret missions - 0248 queue run

Session window: 2026-11-04 02:46 to 02:48 PST. Unit
secrets-2026-11-03-2257, executor ticker-0234.
Status: partial - post entered and read live, but its
Claim buttons did not respond to input, so nothing was
claimed or dispatched. Tracker untouched, per the
partial rule.

## Entry - worked this time

- Computer session cc-404 dropped between the events
  unit and this unit and was restarted as cc-407 with
  no game state lost (the same session-drop pattern
  as the 2026-11-03 12:23 unit).
- Base view left column grounded fresh on the same
  screenshot it was tapped from: white pickup icon at
  norm 53,650. One tap opened SECRET COMMAND POST on
  the Secret Tasks tab, verified by title. This
  answers the 2026-11-03 12:23 unit's entry blocker:
  measure and tap from the same screenshot.

## Live post state read

- Assist Allies: 5/5 (full - no assists needed or
  made today).
- Plunder Others: 4/3 (not touched - PvP, forbidden
  without owner instruction).
- Your Tasks: four finished SSR tasks, each with a
  green Claim button, none yet claimed:
  1. Protect Refugee Camp (Lv.5), rewards including
     Hero EXP (tooltip read live: Owned 824.4M, "It
     grants EXP to a specific Hero").
  2. Search for Missing Refugees (Lv.5).
  3. Provide Tech Support to Refugees (Lv.5).
  4. Train Refugees (Lv.5).
- Per the standing rule, claiming any one finished
  task should collect all finished tasks at once -
  that claim never landed (see blocker).

## Blocker - Claim buttons unresponsive to background input

Five attempts, all no-change, all verified by fresh
screenshot after each:

1. Single tap, row 1 Claim centre norm 810,436.
2. Single tap, row 1 Claim centre norm 833,436.
3. Double-click, row 1 Claim centre norm 833,436.
4. Exact-pointer tap (snap_to_control false), row 1
   Claim centre norm 833,436 - the control doc's
   exact-input variant, still no change.
5. Single tap, row 2 Claim centre norm 833,542 -
   a different row, still no change.
- A click_element attempt on the OCR 'Claim' element
  instead opened the Hero EXP reward tooltip for row
  1 (closed afterwards by tapping the banner area;
  no reward was taken, no setting changed).
- Background input is not dead in general this
  session: shop tabs, trade tabs, Events tabs and the
  post entry tap itself all landed. The failure is
  specific to the Claim buttons on this panel (and to
  the post back arrow at norm 86,952, which also did
  nothing; the working back-arrow centre, as in the
  Events hub, is norm 132,952, which returned to the
  base screen on the first tap).
- Nothing was claimed, nothing was dispatched (no
  Mega Deploy was attempted - dispatching on top of
  unclaimed finished tasks would stack work behind
  the same blocker), no diamonds or items spent, no
  ally task touched, no Plunder Others touched.
- Next secrets unit: try the Claim buttons again
  first (the blocker may be session-specific); if
  they still do not respond, the foreground-input
  variant from the queue design's retro note is the
  remaining route, since background input is the
  only route tried here. If this Claim blocker
  repeats in a second consecutive secrets unit, it
  must be written into the secret-missions activity
  metadata under rule R2 and named in the round
  summary.

## Result statistics

- target claim 4 finished tasks, achieved 0,
  resources_gained none, costs about 2 minutes no
  stamina or items, verified no (no live claim read;
  the post state above is a live read, the claim
  outcome is not), blocker_category c (tap method /
  input route).
