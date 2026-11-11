---
title: Alliance donations queue run 0323
created: 2026-11-10T11:23:00Z
modified: 2026-11-10T11:23:00Z
version: 1.0.0
description: Ticker-0304 donations unit - entry blocked, Alliance shield not visible in current camera state, partial
status: unverified
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-10 03:22-03:23 PT
---

# Alliance donations queue run 0323 (ticker-0304)

Unit: donations-2026-11-10-0203. Status: partial.
Activity: alliance-donations.

## Entry - blocked, Alliance shield not visible

- The Alliance shield icon is not visible in the current
  base view. The base camera is in the same zoomed/panned
  state that blocked the radar unit this pass (the dish
  icon was likewise off-frame): the screen edges show map
  content, not the fixed UI shortcut columns.
- Visual grounding returned norm 916,387 for the shield.
  Checked against the screenshot before tapping: the
  point sits on a hero portrait MAP pin (red-cap figure
  standing on the road, enlarged crop confirms), not a
  UI shield. No tap was made on it - the grounding
  result was rejected on the visual check, the same
  failure mode as the radar grounding point this pass
  (34,324), which was a map bubble.
- The R2 changed route (2026-11-02) names the fresh
  measured Alliance centre 903,787, but that centre was
  measured in a different camera state: in the current
  view norm 903,787 sits on map troops at the right
  edge, not on any shield. Tapping it blind would repeat
  the 11-02 failure (camera pan to the Drill Ground
  cluster). No blind tap was made.
- The remaining entry routes for the next unit: reset the
  base camera zoom/framing first (the shortcut columns
  return with it), or tap the Alliance HQ building on
  the map itself (R2 candidate route). Do not repeat the
  grounding-tool point or the inherited 903,787 centre
  without a fresh visual check.

## What was done

- Nothing donated, no count read. The Alliance Techs
  screen was never entered, so there are NO live reads
  from this unit: Donation Count, Tech Donation Today
  footer and the coin-button state are all unread.
- Last-known state from the 0234 re-read unit (02:49-
  02:53 PT, explicitly not a live read): Quick
  Construction count 6/30 remaining, 6 coin donations
  made at 900 coin each, count closing 0/30, footer
  4800 to 5100 (+300), coin button greyed with a
  00:13:05 cooldown. The cooldown has expired since,
  and the count replenishes in bursts, so the live
  count now is unknown.
- No diamonds or money spent. No other activity's
  rewards touched.

## Closing reads

- Alliance Techs entered: no. Donation Count: unread
  (0/30 remaining last-known, 02:53 PT). Tech Donation
  Today: unread (5100 last-known). Coin button: unread
  (greyed on 00:13:05 cooldown last-known). Donations
  made: 0. Coins spent: 0.

## Outcome

Partial. The donations unit never reached the donation
panel, so the daily 30-coin quota cannot be verified
from this unit. The tracker is left untouched, so the
next tick re-produces the donations regular and the
work resumes as a fresh unit with a changed entry
method (camera reset or Alliance HQ building tap).
The quota checkpoint rule R3 still applies - the
remaining count must be read live six hours and two
hours before the 19:00 reset.

## Red lines

- No diamonds or money spent. No priced button tapped.
  No blind tap on the grounding point or the inherited
  centre. No other activity's rewards touched.

## Result stats

- target 1, achieved 0, resources_gained none, costs 0
  stamina plus about 1 minute, verified no,
  blocker_category c, donations_made 0,
  donation_count_before unknown,
  donation_count_after unknown, coin_spent 0,
  device_takeovers 0, entry_attempts 0
