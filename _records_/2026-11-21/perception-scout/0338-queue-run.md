---
title: Scout unit seq 14 queue run 0338
created: 2026-11-22T11:38:00Z
modified: 2026-11-22T11:42:00Z
level: L0
version: 1.0.0
description: Perception-scout unit scout-scout-2026-11-20-014, chain scout-2026-11-20 seq 14, executed by ticker-0334
status: unverified
---

# Scout 0338 queue run (ticker-0334, partial)

- Session about 03:38 to about 03:42 local, computer session cc-91, window
  105986 (window mode, never brought to front; background input
  working). Observe-only throughout. Token held 03:37 to 03:52.
- Entry: the game was still on MY PROFILE, left open by seq 13
  (ticker-0304). Closed it with the panel X at (823,46), first try,
  back to the base view. MY PROFILE re-read unchanged: Lv.30
  [AP3x]owner account, 149.4M, 48.6K, Lv.63, Lv.2, [AP3x]The Apex,
  VIP13 (red dot - the Daily Freebie, belongs to the VIP regular),
  #2110; flower 12, gift box 88, trophy 11; Moments "No posts
  found."; Record red dot still present (persistent per seq 13).
- Base re-reads (entry about 03:40, close about 03:42): power
  149,417,850 (unchanged); food 760.8M, iron 1.1G, coins 103.9M,
  diamonds 6,436 (unchanged); hammer 1/4 (red dot), flask 2/2;
  Events badge 1, VS red dot; Build: Oil Well (0/1); two survivor
  "?" icons at the front door; WORLD badge 43 at close (chat count,
  still rising with new chat lines); chat icon badge 3; trucks
  icon red dot; "Breaking News: Intense battle..." ticker;
  "Neural Hunter: [Alliance Recruiti..." and "System: Pinenipp1e
  Received..." chat lines; banner "The rumor turns out to be
  true!" and a Lucky Star banner line.
- Lightning counter discrepancy, unresolved: entry screenshot
  reads 120, close OCR reads 114. Both reads are reported; the
  6-point difference is NOT asserted as a spend - it may be an
  OCR misread. No lightning-spending action was taken in this
  unit. Successor: re-read the counter live twice before treating
  any change as real.
- Right-edge long timer re-read live: 14:20:40 at about 03:40,
  14:20:04 at about 03:41, 14:19:4x at the about 03:42 close
  (OCR). Against seq 13's 14:38:52 (read during its 03:22-03:30
  session), the drop is about 18 to 19 minutes over about 14 to
  18 minutes of wall time - near-real-time ticking within the
  read-time uncertainty. Model check, with the corrected clock:
  the rocket model (zero near the 18:00 reset) predicts about
  14:20 at 03:40, within a minute of the 14:20:40 read; the
  green-clock model (seq 12's 15:17:27 at about 02:19, real-time)
  predicts about 13:56, about 24 minutes off. The rocket
  identification is STRONGLY favored, still NOT proven - the
  green-clock timer was not re-located and re-read in this unit,
  so the two timers are still not discriminated from the base
  view. (Correction, same pass before commit: the first draft of
  this record attached the wrong wall times, about 03:48-03:52,
  to these reads; the VM clock shows the unit ran about
  03:38-03:42, and the model check above uses the corrected
  times.)
- Blue-building count-up timer NOT identified. The tap at the
  small clock icon at (609,519) opened TRAIN UNITS (a barracks),
  not the blue building: Power 1352, Morale 625.0, Squad Load
  Capacity 2000, Unit HP 4121.49, Unit Attack 33.87, Unit Defense
  6.89; tiers Lv.6, Lv.7 (1,116), Lv.8 (1,998), Lv.9 (1,878,
  selected), Lv.10 (34.8K, locked); training in progress Lv.9,
  726 units, "Training in progress 1d 08:16:33" - a countdown,
  not the count-up timer. Speed Up NOT tapped (red line). The
  "09:38" seen at the right edge behind the MY PROFILE panel was
  NOT re-found on the base view after closing the panel (the
  camera re-centred; the element's position is view-dependent).
  The count-up timer's building identity stays open for seq 15.
- NOT seen this unit: the Mall floating chest and orange balloon
  carried open from seq 8 (not re-checked, unit cap); the
  green-clock timer's location.
- Red dots seen this unit: 11 (Record, VIP13, hammer 1/4, Events
  badge 1, VS, Alliance, Mail, Inventory, trucks, chat badge 3,
  WORLD badge 43), explained 11, unexplained 0 - the sixth
  zero-unexplained close of this chain. Mail and Inventory dots
  are explained by category (unread mail / new items) and were
  not opened - opening them belongs to the mail and shop-claims
  regulars, not to a scout.
- No diamonds or money spent. Nothing claimed, fought, dispatched,
  donated, dug or bought. The TRAIN UNITS panel was closed with
  its X at (797,255), first try, back to the base view; the game
  was left on the base screen.
- Unit cap reached with 2 of 3 targets unfinished (blue-building
  timer identity; green-clock / rocket discrimination). The chain
  continues (scout-2026-11-20, successor seq 15 enqueued).
