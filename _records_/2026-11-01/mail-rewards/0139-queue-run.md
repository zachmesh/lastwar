---
title: Mail rewards queue run 0139
created: 2026-11-01T08:39:00Z
modified: 2026-11-01T08:42:00Z
status: partial
executor: ticker-0134
unit: mail-2026-10-31-2230
---

# Mail rewards - 0139 queue run

Session window: 2026-11-01 01:39 to 01:42 PDT. Unit
mail-2026-10-31-2230, executor ticker-0134. Status: partial.

## What was done

- From the Alliance menu left open by the previous unit, the Help
  panel was closed and the Alliance menu back arrow returned to
  the base screen. The base screen showed the Mail envelope button
  on the right rail with a red dot, so claimable mail may exist.
- Mail entry failed in this unit. Four input variants at the
  freshly measured Mail point (normalised 920-929, 755-760) all
  showed no change on a second observation each time: two
  standard clicks, one exact-pointer click with control snapping
  off, and one 1-second long press. The game stayed on the base
  screen and no Mail panel opened.
- Contrast: in the same pass, background input to panel screens
  worked (Alliance Gifts back arrow, Alliance menu Help tile,
  Help All, panel close and menu back arrow). The blocker is
  specific to the base-screen right rail in this background-input
  mode, not to game input in general.
- No mail was claimed, nothing was deleted, no other task type
  touched. The tracker is left untouched, so the next tick
  re-produces this regular as a fresh unit.
- Blocker for the next mail unit (queue rule R2): the base-rail
  Mail entry method is exhausted for this unit. The next unit
  must arrive with a changed method - a foreground game window
  or a different entry route - before repeating the rail tap.
  Incidental observation, not part of this unit: while this unit
  opened, the Help panel header read 360/1,000, up from the
  160/1,000 live re-read that closed the previous help unit;
  the rise came from allies helping this account's requests
  between units, not from any action in this unit.
