---
title: Alliance donations queue run 2220
created: 2026-11-02T22:20:00-08:00
executor: ticker-2204
unit: donations-2026-11-02-2203
status: partial
---

# Alliance donations - 2026-11-02 2220 queue run (ticker-2204)

## Outcome

- Status: partial. The entry blocker is broken: the game was
  relaunched and the Alliance menu opened from a verified
  base view, Alliance Techs opened, and a live Donation
  Count was read. But no donation landed: the green coin
  Donate button on the Rallied HP panel ignored five tap
  variants (see Method notes). Donations made 0, tracker
  untouched, day target not closed.

## Live reads

- Alliance: [AP3x] The Apex, Leader Abuss Apex, Power
  12,969,422,116, Members 94/100, Language English.
- Alliance Techs, War tab: Troop Movement 5/10, Rallied
  HP 6/10, Rallied Attack 7/10, Rallied Defense 7/10,
  next node below 1/10.
- Panel: Rallied HP, Increased Hero HP in Rallies for
  Allies, Donation Reward +20%, Tech EXP Required
  200/3.0M, Current +6%, Next Level +7%, Donation
  Reward 50 and 50.
- Donation Count: 10/30, read live at panel entry and
  again after every tap variant, unchanged. Under the
  hard closing rule this is the remaining count, so 10
  coin donations remain today and the day is not done.
- Coin button: Donate 700 coin, green, enabled-looking.
  Coin balance on the HUD reads 5.9M (rounded), so cost
  is not the blocker. Diamond button (Donate 2) was
  never touched.
- Tech EXP stayed 200/3.0M through all attempts, which
  proves no donation landed (a landed donation pays
  Tech EXP and moves the count).

## Method notes (rule R2)

- Entry route changed and worked: the pass started
  stranded on the Arms Race page (left open by the
  arms-race unit, whose back arrow again did not
  navigate). The app was quit with Cmd+Q (menu Quit
  confirmed) and relaunched (new pid, same window
  geometry), restoring the base view with no
  different-device dialog. The Alliance shield was
  then tapped at its fresh measured centre on the
  relaunch screenshot, norm 907,731, and the Alliance
  menu opened on the first tap. The 2026-11-02 entry
  blocker (camera panning to Drill Ground) is broken
  by this route; the metadata hypothesis about the
  grounding point above the button is consistent with
  the miss but the relaunch-plus-fresh-centre route
  is what is verified here.
- Donate button, five variants, all no-change:
  (1) snapped click at norm 678,731; (2) repeat
  snapped click after a 5 second wait; (3) exact
  pointer click at the same point with snap off;
  (4) long-press (mouse down, 1 second, up);
  (5) double-click at the same point. After each,
  the count still read 10/30 and Tech EXP still
  200/3.0M. Navigation taps worked in this same
  session (Alliance shield, Alliance Techs tile),
  and a claim-style tap worked in the previous
  unit (ranking chest preview), so this is a
  button-specific failure, matching open issue #171
  (green buttons unresponsive to background input).
  This unit is commented on #171 rather than filed
  as a new issue.
- Handover for the next donations unit: try a
  different point on the same button first (the
  coin icon at its left end, away from the small
  portrait badge at its right edge), then a
  foreground click if the route allows it. Do not
  repeat the five variants above unchanged. Do not
  touch the diamond button.

## Correction (appended same pass)

- The 2220 time in this file's name and frontmatter
  overstates the close: the unit actually completed at
  22:16 PST. All game reads above are from the
  22:10-22:16 window.

## Red lines

No diamonds or money spent, no speedup item burned,
no other activity's work done from this unit. The
Assemble tile was visible in the Alliance menu and
was not opened.

## Result stats

- target 30, achieved 0 (donations made by this unit;
  the live remaining count 10 is carried separately
  and is never converted into an achieved figure),
  donations_made 0, donation_count_remaining 10,
  donation_count_read true, verified yes for the
  count read and no for any donation, blocker_category
  c (tap method, Donate button unresponsive).
