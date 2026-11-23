---
title: Changelog part 1
created: 2026-11-23T06:45:27Z
modified: 2026-11-23T06:45:27Z
version: 0.1.0
sequence: 37
description: 1.48.0 (2026-11-22) - 2124, 0134 and 0958 training units folded, plus the 1005 arms-race cross-read.
---
## Changelog

- 1.48.0 (2026-11-22): 2124, 0134 and 0958 training units folded, plus the 1005 arms-race cross-read. CONTRADICTION corrected: T10 stats are now Attack 38.87 / Defense 7.87 (2026-11-22 0958 live read), superseding the profile's 38.45 / 7.79. Drill Ground Full blocker did NOT reproduce in either 0134 (Lv.27 T9 x726 requeued first try, food 764.9→760.8M exact) or 0958 (Lv.30 T10 x793 requeued, food 766.1→760.6M exact, 1d 17:14:37) — the standing-blocker run is broken as a live blocker, though the Drill Ground screen is still unread and its capacity unmeasured; 2124 is the fifth consecutive partial on the same cause (formation-flag tap selects 2nd Squad Lv.20, not a Drill Ground screen; pistol deliberately NOT tapped; commented on #678 2026-11-22T05:39:29Z) and the 0134 non-reproduction was commented on #678 2026-11-22T09:41:43Z. Lv.24 finished batch of 143 Lv.8 collected in the 1005 cross-read (+152,009 power, exactly 143 x 1,063; count does not match the carried T8 x666 batch, recorded as observed, not reconciled); Lv.24 now idle, requeue not done. Button-row lesson (0134): tap point must be precise — one tap opened Building Details when TRAIN UNITS was intended, one stray tap opened the world map. Lv.30 Details Training Count +793 (0134), instructors Marcus, Taylor, Daniel, Michael. Process note: the 0134 `complete` call closed without the five always-required result stats keys and without blocker_category (recorded as stats_missing; the tool refuses a second `complete`) — a tooling note, not a game claim.
- 1.47.0 (2026-11-21): 1340 training unit folded (partial, Drill Ground still unlocated - portrait tent at the lower left (152, 671) tapped, no button row, most likely a hospital tent not a barracks, do not re-tap as a barracks; Drill Ground not identifiable in the current framing and the view cannot be panned, so its screen stays unread; 0 batches collected, 0 requeued; blocker_category c; Issue #678 commented by the ticker pass 2026-11-21T21:32:29Z; the queue should not keep paying a unit to re-prove the same unlocated building without a new route). Follows #773's 1.46.0 on main.
