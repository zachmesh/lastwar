---
title: Alliance donations queue run 0154
created: 2026-11-08T09:54:00Z
executor: ticker-0137
unit: donations-2026-11-08-0618
status: partial
---

# Alliance donations - blocked by the Star Ceremony overlay, no count read

Unit donations-2026-11-08-0618 (priority 2, no chain). Session
window about 01:53-01:54 PST on the Mac mini Last War window
(computer session cc-71). Result: partial - no donation made, no
Donation Count read, no coin or diamond spent. The tracker is
untouched.

## Entry state, read live

- The game was found on the [AP3X] Alliance Star Ceremony
  (Event 40) bonus-rewards slide: purple gem 4.0K, "Here are
  your bonus rewards", "Send emotes to the winner to receive
  rewards" tooltip with a blue Go button, chest counter 0/1.
  The bottom row reads 10, 11, 12, 13, MVP and a glowing chest
  icon. This is the same overlay the scout unit of this pass
  (0150) walked in full and found looping: chest -> 10 -> 11
  -> 12 -> 13 -> MVP -> chest.
- The ceremony overlay covers the whole window, so the base
  screen - and with it the Alliance entry, the Alliance Techs
  panel and the Donation Count - is unreachable in this unit.
  No different-device dialog, no login demand. Nothing was
  tapped on the ceremony: the Go button is the ceremony's
  claim path and belongs to the star-ceremony regular, whose
  unit is already queued.

## Closing, per the hard closing rule

- No Donation Count figure is claimed anywhere in this record:
  the count was never read live in this unit, so the day's
  30-of-30 target is unverified for this unit and no
  arithmetic final is asserted. Donations landed in this unit:
  0.
- No re-read unit is enqueued from this unit: the blocker is
  not a donation cooldown but the ceremony overlay, and the
  tracker still shows donations due, so the next tick
  re-produces the regular once the overlay clears. The
  star-ceremony unit in the inbox (star-ceremony-2026-11-08-0230,
  -0630) is the unblocker; until it runs, every base-screen
  unit blocks on the same overlay.
- Queue note: the picker takes the earliest-expiring unit
  first, so while the ceremony is open it keeps handing out
  base-screen units that all block identically. Whether the
  picker should prefer the unit that clears a screen-blocking
  overlay is a tooling question, filed as GitHub Issue #436
  from this pass.

## Result statistics

- target 30 (daily coin donations), achieved 0, resources_gained
  none, verified no, blocker_category f (missing precondition:
  base screen unreachable behind the Star Ceremony overlay;
  exit is the Go/emote claim owned by the star-ceremony
  regular).
