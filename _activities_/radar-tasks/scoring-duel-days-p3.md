---
title: Scoring - duel days part 3
created: 2026-11-23T06:25:33Z
modified: 2026-11-23T06:25:33Z
version: 0.1.0
sequence: 21
description: Stale window label across the duel-day rollover, 2026-11-10 2107 - the unit's window text said 'duel
---
- Stale window label across the duel-day rollover, 2026-11-10 2107: the unit's window text said 'duel day 2 - radar stack', stamped at production (06:42 PT) for an 18:03 slot, but the duel day rolled over at 18:00 PT, so by execution time (20:58) the live posture was day 3 release. The live duel.py read governed, not the label: the stack was released, not stacked. A unit produced before a duel-day rollover carries a stale posture label - the next unit must re-read duel.py live before acting, as this one did. Filed as tooling Issue #603 by the unit; the fix belongs to the tool developer, not this profile.
- Stale window label across the duel-day rollover, 2026-11-16 2102 (third instance): the unit's window text said "duel day 1 - radar release", stamped at production (14:22Z) while day 1 was still running, but the rollover (about 18:00 PST after the DST end) had moved the duel to day 2 Base Expansion before execution at 21:04 PT. The live duel.py read governed - STACK posture, nothing claimed, no pins tapped - and the unit closed done on the stack standard. On entry a Monica dialog announced "Champion Duel has begun"; one tap at the bottom of the dialog dismissed it. A unit produced before a duel-day rollover carries a stale posture label - the next unit must re-read duel.py live before acting, as this one did.

