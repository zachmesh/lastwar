---
title: Test T2 - is the donation coin cost 100 times level plus 1
created: 2026-11-23T01:52:00-08:00
modified: 2026-11-23T01:52:00-08:00
level: L0
version: 1.0.0
description: One-unit read-only falsification test for the alliance-donations digest item that coin cost per tap is 100 x (node level + 1)
status: unverified
grounded_in:
  - source: panel readings in donation records of 2026-10-30, 2026-11-07, 2026-11-11 and 2026-11-22 under _records_/
  - source: alliance-donations rule digest, unverified item on coin cost, in the scribe pilot worktree
---

# T2 - coin cost against node level

**Rule tested:** digest unverified item, "coin cost per tap is 100 x (node level + 1)".

**State.** Clean panel pairs fit: level 2 costs 300 (Quick Gathering, 11-22), 5 costs 600 (Rallied HP, 10-30), 7 costs 800 (Rallied Attack), 8 costs 900, 9 costs 1000 (Quick Construction). No counter-example in the records. Untested: levels 1, 3, 4, 6, 10. A node level-up is slow (Quick Construction needs 8.0M Tech EXP), so read every level the tree shows in one unit.

**Do (read-only, 8 steps).**
1. Confirm LastWar is frontmost; Alliance shield (ground fresh), Techs, War tab.
2. Tap a node showing 1/10 (Expert Nurse, Quick Training or Food Output). Read level and the coin Donate number. Close with the panel X.
3. Drag the tree up once; open a node showing 5/10 (World Interception, Rapid Siege, Quick Garrison or Troop Movement). Read, close.
4. Read any node showing 3, 4, 6 or 10 the same way; at 10/10 note what the panel offers.

**Predictions:** 1/10 shows 200; 5/10 shows 600; 10/10 shows no coin Donate or 1100.

**Record:** node, level, coin cost, diamond cost, reward text; one line per panel.

**Refuted:** any panel whose coin cost is not 100 x (level + 1). One mismatch is enough; write the pair down and the item stays unverified. **Supported:** all fit, so the formula holds at six or more levels and the scribe may promote it.

**Risk and spend.** Nothing spent. A stray tap on Donate costs one donation, at most 1000 coin. Never the diamond button.
