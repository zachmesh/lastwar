# Alliance donations queue run 0733 (ticker-0707)

Unit: donations-2026-11-11-1430. Status: partial.
Activity: alliance-donations. Computer session cc-576.

## What this unit was for

Re-read unit for the ticker-0604 donations unit (0635): re-read the
Donation Count live after its 00:15:49 cooldown (ended about
06:51), and verify whether its tap 2 from a live 1/30 count on
Rallied Attack landed.

## Profile freshness

This unit ran from the CURRENT main profile (alliance-donations
1.99.0, modified 2026-11-11T14:32:17Z), read via `git show main:`
before acting - the disk copy is the stale 1.5.0 that caused the
ticker-0434 changed-route deviation (Issue #631). The rules
applied here are the main ones: the changed route (stop at the
live-read 1/30, no tap from 1/30), the burst replenishment model,
and the hard closing rule (R1 - close only on a live Donation
Count read in the same unit; the footer is disqualified per
Issue #558).

## Entry

- The game was on the base screen in full framing. Alliance
  shield grounded fresh from the current screenshot via visual
  grounding (bbox 895-968 x 698-748, centre 931,723) - opened the
  Alliance menu first try. Alliance Techs tile at (678,689)
  opened ALLIANCE TECHS first try.
- Development tab: Auto Rally Max Level, Quick Construction
  8/10, Great Helper Max Level, bottom node 2/10. Tech Donation
  Today footer 3750 at entry (display only, disqualified).
- War tab, tree dragged upward twice (drag 500,550 to 500,300):
  Rallied HP, Rallied Attack, Rallied Defense 7/10, Expert Nurse
  1/10. The recommended marker (small round red-panda badge)
  sits on Rallied Attack - read fresh this unit, same node as
  the 0635 unit. The red thumbs-up above the Development tab
  is fixed and is NOT a node marker.

## Re-read and donations (Rallied Attack, live reads)

- Panel entry: Rallied Attack 7/10, Increased Hero Attack in
  Rallies for Allies, Tech EXP Required 25.2K/4.5M, Current +7%,
  Next Level +8%, Donation Reward EXP 50 + badge 50 per
  donation, coin Donate 800 (green), diamond Donate 2 (never
  used).
- Donation Count read live at entry: **3/30** (remaining).
- Tap 1 (coin Donate, from 3/30): landed, verified - count
  re-read live 2/30, Tech EXP 25.2K to 25.3K.
- Tap 2 (coin Donate, from 2/30): landed, verified - count
  re-read live 1/30, Tech EXP 25.3K to 25.4K.
- Stopped at the live-read 1/30 per the changed route. The coin
  button stayed GREEN with no cooldown timer visible - the
  changed route HELD (same end state as units 2249, 2354, 0024,
  0316, 0321, 0353). No tap was made from 1/30.
- The 1/30 remainder is handed to the next staged donations
  unit (donations-2026-11-11-1003, in inbox) after
  replenishment; no separate re-read unit is enqueued.

## The 0635 tap-2 question - NOT decided

- The count at this unit's entry read 3/30 live. The 0635 unit
  closed at 1/30 with tap 2 unverified behind its 00:15:49
  timer. Between the 0635 close (about 06:35) and this read
  (about 07:29) the count replenished: 1/30 to 3/30 is
  consistent with tap 2 eaten (+2 replenished) and with tap 2
  landed (0/30, +3 replenished). The Tech EXP bar cannot
  decide it either (25.2K at the 0635 close; a +50 move does
  not reliably move the 0.1K display at this value). The footer
  rose 3600 to 3750 in the same window, but it is disqualified
  as evidence (Issue #558) and cannot decide the tap. The
  landing of the 0635 tap 2 stays UNVERIFIED. No derived total
  is reported.

## Close

- Partial. Two coin donations verified live (count 3/30 to
  2/30 to 1/30, Tech EXP 25.2K to 25.4K), closing count read
  live at 1/30, changed route held, tracker untouched (partial
  units do not move the tracker). The day's remaining 1
  donation awaits replenishment and the next donations unit.
- No diamonds or money spent. No priced button, Renew, paid
  unlock or Legendary Claim All tapped. No login or
  verification demanded. No "active on a different device"
  dialog appeared. The game was left on the base screen.
  Computer session cc-576 ended.

## Result stats

- target re-read the Donation Count live after the 0635 cooldown and verify the 1/30 tap
- achieved live 3/30 read, 2 coin donations verified 3/30 to 1/30, stopped at 1/30 per the changed route
- resources_gained 100 Tech EXP, 100 contribution points (2 donations at 50 each)
- points 0
- costs about 7 minutes, 1600 coins
- verified partial - the re-read and both donations are live-verified; the 0635 tap-2 landing is unverified
- blocker_category h
- donations_made 2, donation_count_before 3, donation_count_after 1 (live), tech_exp_before 25.2K, tech_exp_after 25.4K, footer 3750 (display only), cooldown none (button green at close), device_takeovers 0
