---
title: Alliance donations queue run 0545
created: 2026-11-02T13:45:00Z
modified: 2026-11-02T13:45:00Z
version: 1.0.0
description: Ticker unit donations-2026-11-02-0354, coin donations to Garrison Defense, closing count hidden by timer
status: partial
---

# Alliance donations queue run 0545

- Unit: donations-2026-11-02-0354, executor ticker-0534.
- Entry: Alliance button at norm (935, 706) and the Alliance
  Techs tile at norm (687, 690), both first time, matching
  the 0259 groundings.
- Target: Garrison Defense (recommended marker), War tab,
  7/10, +7% toward +8%, Tech EXP 126.7K/4.5M at entry,
  Donation Reward +20%, per donation 50 EXP + 50 badge
  item by panel. Tech Donation Today footer read live
  2,750 at entry (above the 1,000 reward threshold).
- Entry correction: the first coin-button tap at
  (732, 710) landed above the button and changed nothing
  (count stayed 8/30). The button centre re-grounded by
  crop measurement is (732, 760); every tap there landed.
  Next units ground the coin button at y 760, not 710.
- Donations, coin button only (800 coin each): Donation
  Count read live 8/30 at entry, then 7/30, 6/30, 5/30,
  4/30, 3/30, 2/30 (image-verified at 2/30) and 1/30 in
  sequence, one counted donation per tap, eight in
  total, 6,400 coin spent. The panel also showed a
  "Hold down for easier continuous donations" hint
  after one tap; single taps were kept, no long-press
  used. No diamond button was used.
- Final donation: 1/30 remaining, one coin tap landed,
  Tech EXP 127.5K to 127.6K. The coin button then
  greyed with a 00:09:54 timer that hides the count
  label, so the closing 0/30 was NOT read live in this
  unit. Per the hard closing rule in the activity
  metadata, this unit does not claim the day done on
  arithmetic: status partial, verified no, tracker
  untouched.
- Cross-check that does NOT close the unit: the tree
  footer after the donations read Tech Donation Today
  3,500, up 750 from the 2,750 entry read. That delta
  does not divide cleanly by the 8 counted donations,
  so the footer is not a per-donation counter and is
  not used as a closing figure. The same footer moved
  1,900 (0259 entry) to 2,750 (this entry) with no
  intervening done donations unit, so it moves for
  reasons beyond one unit's own coin donations.
- Replenishment observation, new against the metadata
  model: unit 0259 ended greyed at about 02:59 with its
  count arithmetically at 0, yet this unit read 8/30
  live at 05:41. The Donation Count therefore
  replenishes after reaching 0 (about 8 back over
  about 2 hours 40 minutes), and "0 remaining" is a
  momentary state, not a day-done state. The metadata
  closing rule (day done only at a live 0 read) still
  binds this unit, but the replenishment model belongs
  in the activity metadata; filed as GitHub Issue #174
  (knowledge) rather than edited here, since tier-2
  edits do not ride a records commit. Correction found
  after filing: the replenishment question is already
  tracked as Issue #160 (from the 2348 record); the
  new evidence was added as a comment on #160 and
  #174 is noted there as a duplicate for the retro
  to consolidate, not self-closed.
- Follow-up: a re-read donations unit is enqueued with
  not-before 2026-11-02T13:55:00Z, after the 00:09:54
  timer read at about 05:42 local expires, to read the
  count live and donate further if it reopened above
  zero. If it reads 0, that unit may close the day.
- Result stats: target 30, achieved unverified,
  verified no, blocker_category d (closing count hidden
  by timer, not a live read). Donations landed in this
  unit: 8 coin donations, 6,400 coin spent, node Tech
  EXP 126.7K to 127.6K as displayed.
