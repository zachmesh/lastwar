---
title: Quick Execute - coverage and exceptions part 2
created: 2026-11-23T06:25:33Z
modified: 2026-11-23T06:25:33Z
version: 0.1.0
sequence: 15
description: Bottom-bar hitbox, measured 2026-11-03 1450 - taps at norm y 890, 905, 910 and 912 on
---
- Bottom-bar hitbox, measured 2026-11-03 1450: taps at norm y
  890, 905, 910 and 912 on the Claim All button did NOTHING
  (five taps across two attempts, including a double-click);
  the taps landed on the map/label area above the button's
  true hitbox. A tap at norm (498,925) opened the button.
  Next units: tap the bottom-bar buttons at y 925, not at
  their visual centre (~910). CORRECTION 2026-11-03 1913:
  the y-925 lesson does NOT transfer to every window
  geometry - in the 1913 window the bottom-bar buttons
  responded at norm (500,952), confirmed by three Quick
  Execute and three Claim All taps at that point. The
  grounded point governs in each window; never carry a
  y value across windows unverified.
- With too little stamina, tapping Quick Execute opens the
  Regain Stamina panel instead of failing - use the free
  claim there and continue.

