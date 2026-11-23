---
title: 7. Perception points in the day part 2
created: 2026-11-23T09:03:33Z
modified: 2026-11-23T09:03:33Z
version: 0.1.0
sequence: 23
description: Post-reset full pass - the first pass of the reset day, staged at the trade-day reset
---
- **Post-reset full pass** - the first pass of the reset day,
  staged at the trade-day reset (absolute 02:00 UTC, about 18:00 PST in winter, 19:00 PDT in summer). It walks the whole checklist.
  This is the pass that builds the day - everything the reset
  made available is observed before the day routine settles into
  its windows.
- **Midday pass** - one more full pass at the middle of the
  reset day, 07:00 local. It exists for state-dependent
  availability the morning cannot show - trains entering
  preparation, Arms Race phases rotated, markets refreshed,
  trucks returned.
- **Change-triggered full pass** - a full pass fired by a
  detected state change between the anchors, under the rule
  above. It walks the whole checklist like an anchored pass and
  lands in the same observation file, marked with its trigger.
- **Rolling partitioned perception** - between full passes, the
  surface-group chains of section 8 re-walk their groups on the
  ticker heartbeat - base and HUD every tick, events and store
  on rotation-sensitive ticks, alliance and mail with their own
  traffic. Their sections append to the same observation file,
  each stamped with its pass time, so the diff always works
  from the freshest read of each surface.
- **Handover to the zero sweep.** The pre-reset zero sweep
  (queue design section 12) walks the merged list - the daily
  collection ledger plus the day observed items - so anything
  perception found during the day is swept by the same standard
  as the modelled lines. An observed item still open at the final
  sweep gets its fix-up unit enqueued by the sweep, exactly like
  a ledger line not at zero.

