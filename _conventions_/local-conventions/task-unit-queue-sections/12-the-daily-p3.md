---
title: 12. The daily collection ledger and the pre-reset zero sweep part 3
created: 2026-11-23T08:37:05Z
modified: 2026-11-23T08:37:05Z
version: 0.1.0
sequence: 31
description: 2026-11-04 correction (organizer 0432, Refs 147) - the sweep geometry above replaces the wall-clock 1730/1830 slots
---
2026-11-04 correction (organizer 0432, Refs #147): the sweep geometry above replaces the wall-clock 17:30/18:30 slots expiring 19:00 local, which could not close a trade day after the 2026-11-02 DST end (the Nov 3 final slot staged at 18:30 local fell half an hour after the 18:00 PST reset). Other 19:00 mentions elsewhere in this design (VIP expiry, the scout anchor, quota checkpoints, the deadline list) are not rewritten in this pass and are flagged as follow-up on #147.
2026-11-07 follow-up (organizer 0432, Refs #147): the four flagged mentions are rewritten in version 0.16.0 - VIP expiry (section 4), the scout anchor and the deadline list (section 13), and the quota checkpoints (rule R3) - all now anchor at the absolute reset instant 02:00 UTC (about 18:00 PST in winter, 19:00 PDT in summer). The two dated 19:00 mentions that stay are history, not rules: the 2026-10-27 lapse (section 1) and the 2026-10-28 migration validation (section 9), both from the PDT era when the reset was 19:00 local.
2026-11-18 sync (organizer 1232, Refs #606): the sweep geometry above moves from [90, 30] to [120, 60] per PR #614 (merged 2026-11-11) - seq-1 at 16:00, fix-ups at the 16:30 midpoint, seq-2 at 17:00 PST in winter - so the final pass spans two ticker passes instead of expiring inside one. The 2026-11-04 correction note above stays as history: it records the geometry the 90/30 form replaced, not the current form.
2026-11-21 (tool-developer, Refs #748): the pair bodies now carry the ledger-walk task section (rule R20) - the production path appends it, first pass or final pass by chain_seq, so the pair no longer depends on the planner appending the text by hand.

