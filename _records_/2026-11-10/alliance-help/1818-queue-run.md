---
title: Alliance help queue run 1818
created: 2026-11-11T02:21:00Z
modified: 2026-11-11T02:21:00Z
level: L0
version: 1.0.0
description: Help unit help-2026-11-10-1430, Help All pressed twice, 3 ally requests helped
status: unverified
---

# Alliance help 18:18 to 18:21 - ticker-1806

Unit help-2026-11-10-1430 (planned for the 14:30 cycle,
expires 02:30). Executor ticker-1806. Session cc-488 on the owner
Mac mini. Background input reached every button on the first tap;
no foreground repair was needed.

## Live reads

- Entry: from the Alliance Gifts screen, back arrow to the
  Alliance panel, then the Help tile (norm 698,510).
- Help dialog at entry: header "Today's points gained from
  Alliance Help: 0/1,000". Four rows: own Bears Lair "Need help
  with Missile Mastery II research" and "Need help with
  building Lv.30 Aircraft Center", specialist Donut "Need help
  with Oil Output I research", Teemo "Need help with Missile
  Vehicle - Defense II research".
- First Help All (norm 498,764): both ally rows cleared live -
  only the two own Bears Lair rows remained. Header still
  0/1,000 in-session, the known lag.
- Close and reopen: header read live at 40/1,000 - the two
  helps moved the counter, 20 points each. A new ally row had
  arrived in the meantime: Teemo "Need help with Missile
  Vehicle - Damage II research".
- Second Help All: Teemo's row cleared live, only the two own
  rows remain. Header still 40/1,000 in-session; the third
  help's +20 follows the same lag pattern and will be read by
  the next help unit's header.

## Outcome

- Done. 3 ally requests helped (Donut Oil Output I, Teemo
  Missile Vehicle - Defense II, Teemo Missile Vehicle -
  Damage II). Header verified 0 to 40/1,000 after close and
  reopen; the third help's points are pending the next
  unit's header read.
- No diamonds or money spent, no red line touched. The game
  was left on the Help dialog with only own requests visible.
