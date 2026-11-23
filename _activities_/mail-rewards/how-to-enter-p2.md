---
title: How to enter part 2
created: 2026-11-23T07:24:19Z
modified: 2026-11-23T07:24:19Z
version: 0.1.0
sequence: 4
description: The back arrow sits at the bottom left of the mail screens, both in the category
---
- The back arrow sits at the bottom left of the mail screens, both in
  the category list and inside an open mail. (2026-11-10 1259 update: the mail-list back arrow's true centre in the 642x951 window is (62,948) - taps at (57,902), (40,900), (55,925) and (40,955) all missed high, the button sits at about y 869-935 px, centre about y 902 px; measure the centre fresh from a screenshot crop in each unit. The AX tree carries no back-button element (game canvas), so coordinate taps at the freshly measured centre are the working route; keyboard input is unavailable in this app - focus belongs to the other LastWar window.) (2026-11-11 1456 update: the mail-DETAIL back arrow in the 1920x1080 fullscreen framing ignored four tap variants at (301,958) - snapped, snapped-explicit, left-edge swipe drag, unsnapped - and click_element label "Back" found no enabled control; but those taps aimed at the arrow's centre would have landed near (278,968) under the measured -23 x, +10 y tap offset (tooling Issue #652), so the failure is consistent with an offset miss and does NOT prove the control input-blocked - the #575 comment filed mid-unit was corrected by a follow-up comment. Re-test the mail-detail back arrow with offset-compensated taps (+23 x, -10 y) aimed at the freshly measured centre before concluding anything about it. Claim All auto-advances: a Claim All tap after the list is claimed opens the next unread mail's detail, so do not tap Claim All twice in a row without checking what opened.)

