---
title: Open questions part 2
created: 2026-11-23T06:25:33Z
modified: 2026-11-23T06:25:33Z
version: 0.1.0
sequence: 40
description: Bottom bar offer selection - the bar presents one offer at a time; why did the
---
- Bottom bar offer selection - the bar presents one offer
  at a time; why did the 2026-10-31 10:40 unit get Quick
  Execute despite 7 pending rewards, when the 06:12, 14:15,
  18:38 and 22:06 units got Claim All and no Quick Execute?
  Candidate factors to test - completable task count at
  entry, pending count, restore timer state. (2026-11-10 1555 update: no Quick Execute offer at entry with 11 pending rewards - the bar presented Claim All only, and the state is unchanged since the 1146 close (stored 23/40, pending 11, points 348, stamina 120, same 4 skull pins). The offer flipped since 1146, which was offered 1 Quick Execute at 11:44 and then flipped to Claim All-only; the selecting rule stays open.) (2026-11-22 0524 update: the bar offered Quick Execute despite pending rewards again - stored 11/40 with 11 pending and a 1-task Quick Execute offer, against the 00:57 unit the same day finding stored 14/40 with 8 pending and no Quick Execute offer; a further counter-observation to the 2026-10-31 single-offer behaviour. 0901 and 1141 the same day presented Claim All only with 11 pending and no Quick Execute offer, so the selecting rule stays open.)
- Standing pin types - identify the orange arrow, purple
  axe, orange axe and portrait pins (class, cost, reward)
  on the next release day, by tapping them under the
  release handling rule. (2026-11-08 2335 update: the standing
  inventory now also includes blue arrow pins (one with a red
  dot), purple arrow pins and orange skull pins, none yet
  identified - the blue arrow, purple arrow and orange skull
  classes join the orange arrow, purple axe, orange axe and
  portrait pins awaiting identification under the release
  handling rule.) (2026-11-09 0852 update: pin inventory at close - portrait pin top left, blue skull pin top left, blue skull pin top centre, green skull pin right middle, two grey skull pins bottom, gold/pink pin cluster left centre (the 0335 Rare Iron Mine gathering pin, claim NOT checked this unit); per rule R7 the Iron Mine gathering claim is the first action of the next radar unit, then the skull pins and the portrait pin, each to a closing read.) (2026-11-09 1253 update: pin inventory at close - 3 grey skull pins with red dots, 1 green skull, 1 purple skull, 1 blue teardrop, 1 brown animal-face pin, 1 orange skull, 1 portrait pin, at least 6 distinct pins unworked; per the record the same standing set deferred from the 2026-11-08 2335 unit;