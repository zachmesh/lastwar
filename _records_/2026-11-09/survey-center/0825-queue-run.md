---
title: Survey Center exploration
created: 2026-11-09T16:37:00Z
modified: 2026-11-09T16:37:00Z
version: 1.0.0
description: Scout discovery exploration of the Survey Center tab - read-only learning
status: done
grounded_in:
  - source: live game screens on the owner Mac mini, 2026-11-09 08:24-08:28 PT
---

# Survey Center - 0825 queue run

Unit scout-scout-discovery-2026-11-09-005, executor ticker-0804.
Session cc-243, LastWar window 489932, no device dialog, no
contention, no login demand. Token held until 08:39:31 PT; the
session was ended at about 08:28, inside the window, and no
game input ran after expiry.

## What was learned

Survey Center is the feedback-survey hub in the Events hub (tab
bar: ...Battlefield, Desert Battlefield, Wanted Boss with a red
dot, Survey Center). Its page reads "Survey Center - We'd love
to hear from you!" and carries one live entry: "Season II:
Polar World Experience Survey", with a blue chest icon and a
button that first read Go, then Proceed after one tap, with a
red dot appearing on the card. No countdown is shown on the
card.

The info button opens INSTRUCTIONS, read in full:

1. When there are available surveys, the Survey Center will
   appear in Special Ops.
2. Click to proceed and fill out the survey through the provided
   link, then return to the Survey Center to claim rewards.
3. If you exit midway through the survey, you can return to the
   Survey Center and click "Continue" to resume.
4. Note that each survey can only be submitted once. If you
   revisit, it will show as completed.
5. Timed surveys will disappear when the countdown ends.
6. Surveys without a countdown will disappear 3 hours after
   completion.
7. If you complete the survey but do not claim the reward
   before it disappears, it will be sent via mail.

Mechanism: the survey itself is filled out through an external
link; the reward is claimed back in the Survey Center after
completion (or mailed if unclaimed before the entry disappears).
The live entry shows no countdown, so under rule 6 it is
untimed before completion.

Blocker, recorded for the next unit: the Proceed button did not
respond to background input - two coordinate taps at (763,762),
one click_element on the Proceed OCR control and one
click_foreground attempt (rejected: no Accessibility Action ID
for an OCR control) all produced no change, and the survey link
never opened. The reward content for the Season II survey is
therefore unmeasured. The first tap did change the button label
from Go to Proceed and raised a red dot on the card.

Correction, observed 08:29 in the next unit's session: the
Proceed tap HAD worked, with a delay - at the next activation
the frontmost app was Chrome showing "Season II: Polar World
Experience Survey", i.e. the survey link opened in the owner's
browser after the session ended. Nothing was filled in or
submitted there; the page was left open for the owner.

## Result

Done - the mechanism is explained: Survey Center is a
feedback-survey hub, one live survey (Season II: Polar World
Experience Survey), no countdown, reward claimed in-center
after an external-link completion. No price, diamonds or red
line attaches to reading it. Candidate REJECTED as a routine
task, same verdict class as units 001 and 003: completing a
survey means answering feedback in the owner's voice, which
is the owner's own action, not queue work - the agent's role
is at most to notice a new survey. No survey was submitted,
no reward claimed, nothing spent. The unmeasured reward and
the unresponsive Proceed button are named here for the next
unit that revisits this page.

- Follow-up: none for this candidate. If the owner fills the
  Season II survey, the reward claim in the Survey Center (or
  its arrival by mail) is worth one check; no unit is staged
  for that.
- Note: the news ticker during the unit reported warzone
  president appointments (HawksMav appointed Agricola as
  Secretary of Interior); unrelated to this exploration, not
  acted on.

## Stats

- target: explain-survey-center-mechanism
- achieved: 1
- resources_gained: none
- costs: about 4 minutes, no items spent
- verified: yes (same-unit live reads)
- blocker_category: none
