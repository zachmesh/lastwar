---
title: Alliance donations queue run 2354
created: 2026-11-10T23:54:00-08:00
modified: 2026-11-10T23:54:00-08:00
version: 1.0.0
description: Donations unit donations-2026-11-11-0650, re-read after the 2319 cooldown, 1 coin donation verified live 2/30 to 1/30, stopped at the 1/30 floor per the changed route
status: partial
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-10 23:54-23:59 PST
---

# Alliance donations queue run 2354

- Unit: donations-2026-11-11-0650, executor ticker-2334, session
  cc-524 (same session as the zombie unit this pass).
- Window: 23:54-23:59 PST. Status partial - 1 coin donation
  verified live, stopped at the 1/30 floor per the changed route;
  the last donation goes to a named re-read unit after the
  cooldown. Tracker untouched.

## Entry

- Base screen at entry in full-base framing, shortcut columns
  visible. Alliance shield tapped at the fresh measured centre
  (930,720) on the current screenshot - opened the Alliance
  menu on the first try. Alliance Techs tile at (724,689)
  opened ALLIANCE TECHS on the first try.
- Development tab at entry: Auto Rally Max Level, Quick
  Construction 8/10, Great Helper Max Level, one node 2/10
  below. Tech Donation Today footer 1600 at entry, display
  only, never a closing figure.

## The donation

- Quick Construction node tapped at (288,515) opened the tech
  panel on the first try. Donation Count read live 2/30 at
  entry - replenished +1 since the 2319 close (1/30 at 23:16),
  about 40 minutes later, with no landed donation in between.
  One more replenishment data point for the burst allowance.
- One coin donation: green Donate 900 button tapped at
  (643,774). The yellow Donate 2 button (diamond) was never
  tapped. Donation Count re-read live 1/30 on the screenshot
  after the tap - the donation landed. Coin HUD 110.2M
  unchanged at this rounding (900 coin is below the 0.1M
  display step). Contribution counter top bar 406.1K to 406.2K,
  footer corroboration only.
- Stopped at the live-read 1/30 floor per the changed route
  (retro action A-2026-11-10-02). No tap was made from 1/30.
  No cooldown timer was visible on this panel after the tap.

## Result

- donations_made 1 (verified: Donation Count 2/30 to 1/30,
  same-unit live reads).
- count_before 2/30, count_after 1/30, both read live.
- Target: re-read the count after the 2319 cooldown and donate
  the replenished allowance; achieved: 1 coin donation verified
  live, stopped at the 1/30 floor. Verified yes. Blocker
  category h (by-design partial - changed route hands the last
  donation to a re-read unit).
- Follow-up: named re-read unit donations-2026-11-11-0757
  enqueued with not_before 00:15 PT (about 15 minutes after
  this donation, the usual cooldown span) to test whether the
  count has replenished past 1/30 again.
- No diamonds or money spent. No priced button tapped. No
  other activity's rewards touched.
