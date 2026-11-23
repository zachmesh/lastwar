---
title: How it is done
created: 2026-11-23T07:24:49Z
modified: 2026-11-23T07:24:49Z
version: 0.1.0
sequence: 4
description: The gifts screen has two tabs, Regular and Premium.
---
## How it is done

- The gifts screen has two tabs, Regular and Premium. Each tab has a
  Claim All button. Claim All on BOTH tabs every round - the owner
  confirmed this explicitly on the evening of 2026-10-25.
- Claim All pays the whole tab in one tap and shows a summary dialog
  naming the count claimed.
- Gifts keep arriving as allies play, so a tab can show new gifts
  minutes after a claim - one extra Regular gift arrived and was
  claimed during the same evening visit. The Alliance Gifts entry
  keeps its red dot while any gift waits.
- Record the claim in the summary and resources_gained (counts
  claimed on each tab, Gift Level progress before and after).
  Never write the Gift Level progress gain into stats.points:
  gifts is not a scoring type - points is score gained, for
  scoring types only - so a gifts closing carries no points
  key at all (issue #300).
- The back-arrow button sits at different x positions per screen (0346: about norm x 62 on the gifts screen, about x 156 on the Alliance panel and the Events screen) - ground it fresh per panel, never reuse one screen's point on another.

