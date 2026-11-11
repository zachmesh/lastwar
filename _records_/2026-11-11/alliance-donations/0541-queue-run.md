---
title: Alliance donations queue run 0541
created: 2026-11-11T13:41:00Z
modified: 2026-11-11T14:02:00Z
version: 1.0.0
description: Ticker-0534 donations unit - 4 coin donations to Rallied Attack, burst cooldown hit, closing count derived not live-read, partial
status: unverified
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-11 05:41-06:01 PT
---

# Alliance donations queue run 0541 (ticker-0534)

Unit: donations-2026-11-11-0203. Status: partial.
Activity: alliance-donations. Computer session cc-564.

## What happened

- Entry detour (new finding): the unit started on the Arms Race
  page from the previous unit, and its back arrow ignored three
  background-click variants - snapped tap at (110,905), re-measured
  centre (112,907), exact-pointer tap (snap_to_control false) -
  with the receipt guidance that background clicks do not reach
  some controls. The detour that worked: switch to the Desert
  Battlefield tab (tap worked at once), whose back arrow at the
  fresh measured centre (164,931) returned to the base at once.
  Back-arrow behaviour differs per Events page; the Arms Race
  page arrow is the unresponsive one. The next unit starting on
  the Arms Race page should use the Desert detour, not repeat
  the three dead taps.
- Alliance entry (R2 fix validated): the Alliance shield icon
  fresh measured centre (919,694) on this session's base screen
  opened the Alliance menu on the first tap. Note: the metadata's
  recorded centre (903,787) does not match this layout - the
  shield sits at about (590,660)px here, and the (903,787) point
  would land near Mail. Measure fresh every unit; do not reuse
  the stored point blindly.
- Alliance Techs: Development tab - Auto Rally Max Level, Quick
  Construction 8/10, Great Helper Max Level, a 2/10 node below
  (cut off). War tab, scrolled by drag - Unit Load Capacity 2/10,
  Quick Training 1/10, Expert Trainer 2/10, World Interception
  5/10, Rapid Siege 5/10, Quick Garrison 5/10, Troop Movement
  5/10, Rallied HP 7/10, Rallied Attack 7/10, Rallied Defense
  7/10, a 1/10 node below (name unread). A red thumbs-up marker
  sits fixed near the Development tab in every War screenshot
  and does not move with the tree scroll - which node it marks
  is still unclear, recorded as observed.
- Rallied Attack panel, read live: 7/10, Increased Hero Attack
  in Rallies for Allies, Tech EXP Required 24.9K/4.5M, Current
  +7%, Next Level +8%, Donation Reward 50 EXP + 50, Donation
  Count 3/30 live at entry, coin Donate 800 (green), diamond
  Donate 2 (yellow, never used).
- Donations: five batched taps on the coin Donate button. Four
  landed - Tech EXP 24.9K to 25.1K (+200, 4 x 50) and Tech
  Donation Today footer 3400 to 3600 (+200), both read live. The
  fifth tap hit the burst limit: toast "...count has reached its
  limit, please wait." The coin button then greyed with a green
  00:19:31 cooldown timer, which hides the Donation Count label
  - the exact R1 trap documented for this activity.
- Panel hint observed: "Hold down for continuous donations" -
  the coin button supports hold-to-donate. Worth trying in the
  next unit (faster than batched taps); the burst limit stops
  it, so it cannot overshoot.

## Correction (appended 05:48, same pass)

- The duration stated above is wrong. The unit ran about 6
  minutes (claimed 05:41:13, token released 05:47:18), well
  inside the 15 minute cap - not "about 20 minutes", and it did
  not run over the cap. The "about 20 minutes" in the costs
  stat and the "over the 15 minute cap" sentence are withdrawn;
  they were a misjudged wall-time estimate, contradicted by the
  tool timestamps. The entry detour cost about 2 minutes, not
  7. Everything else in this record stands as written.

## Close

- Partial. Four coin donations made and verified by two live
  reads (Tech EXP and the footer). The closing Donation Count
  7/30 is DERIVED (3 live at entry + 4 verified), not live-read,
  because the cooldown timer hides the label; per R1 the
  tracker stays untouched and the next unit re-reads the count
  after the cooldown (ends about 06:19). 23 donations remain
  (derived). The daily 30/30 target is not met yet.
- Unit ran about 20 minutes, over the 15 minute cap - the entry
  detour (three dead back-arrow taps plus the tab switch) cost
  about 7 minutes. The pass budget, not the unit, ended the run.
- No diamonds or money spent. No login or verification demanded.
  No "active on a different device" dialog appeared.

## Result stats

- target donate coin donations to Rallied Attack until the button greys, read Donation Count live
- achieved 4 coin donations, button greyed on burst cooldown, footer 3400 to 3600
- resources_gained 200 Tech EXP, 200 contribution points
- points 0
- costs about 20 minutes, 3200 coins
- verified partial - donations verified by two live reads (Tech EXP 24.9K to 25.1K, footer 3400 to 3600); closing Donation Count 7/30 derived, not live-read
- blocker_category h
- donations_made 4, donation_count_before 3, donation_count_after_derived 7, tech_exp_before 24.9K, tech_exp_after 25.1K, footer_before 3400, footer_after 3600, cooldown 00:19:31, device_takeovers 0
