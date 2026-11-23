---
title: 4. Unit schema part 2
created: 2026-11-23T09:03:48Z
modified: 2026-11-23T09:03:48Z
version: 0.1.0
sequence: 9
description: 1 expiry-critical - vip (expires at the next reset after its slot, absolute 0200 UTC -
---
- **1 expiry-critical** - vip (expires at the next reset after its slot, absolute 02:00 UTC - the slot opens its reset day, so expires_at is planned_for + 24h), passes when
  a free pack carries its own countdown, events on a check-in day
  boundary.
- **2 windowed** - arms-race (points only count inside the live phase),
  radar on release days (claims score at claim time), donations before
  the daily settlement, trucks on a duel UR day.
- **3 standard** - everything else.
- **4 background** - continuation chains that soak up idle quanta
  and always yield at the next boundary (Zombie Invasion units).

