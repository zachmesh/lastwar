---
title: Radar tasks queue run 2317
created: 2026-11-04T07:17:00Z
modified: 2026-11-04T07:17:00Z
status: partial
executor: ticker-2304
unit: radar-2026-11-03-2203
---

# Radar tasks - 2317 queue run

Session window: 2026-11-03 about 23:05 to 23:17 local. Unit
radar-2026-11-03-2203, executor ticker-2304. Status: partial.
Posture: release (live duel.py at entry: duel day 3, Age of
Science, radar posture release; the unit window text reads
"duel day 3 - radar release", matching the live posture).

## Entry

- Radar entry on the first tap at norm (57,715), the proven
  dish cluster from the 0636, 1010, 1450 and 1913 units.
  Entry verified by its own reads: Lv.13, radar points 183,
  stored 2/40, stamina 120, restore line "12 Radar Task(s)
  will be restored in 04:24:25" at entry (later frames read
  04:23:18 down to 04:15:18, and the full-restore line
  "Fully restore at 11-5 03:31:43 local time" once stored
  hit 0/40).
- Bottom-bar buttons in this window respond at norm
  (500,952) (confirmed by two successful Quick Execute
  taps and two successful Claim All taps at that point).

## Pins first (rule R7, from the 1913 unit)

- The 1913 unit's first-action pin was the purple
  question-mark story pin top left. This unit worked it
  first, before any Quick Execute batch:
  - Pin tap at norm (231,323) opened the card: "A
    Distressed Survivor", "Look for survivors after the
    cold wave...", "Break the ice to view rewards",
    countdown 04:03:28.
  - Go at norm (500,946) jumped to the world map task
    location: "Thawing Soon 00:02:51", snowflake bar
    1,000/1,000.
  - Hammer contextual button: a tap at (449,548) did
    nothing; a visually grounded tap at (490,600)
    opened the deploy panel. Lesson carried forward:
    ground contextual buttons, never estimate them.
  - Deploy panel: Squad 1, 25.17M vs Unknown, Evenly
    Matched, Unit Count 2,231/2,231, march 8 seconds,
    stamina cost shown as -5.
  - March button: taps at (500,691), (500,715) and
    (500,730), a 1 second long-press at (500,700) and
    a double-click at (500,691) all left the panel open
    with stamina unchanged. A visually grounded tap at
    (500,751) closed the panel. The March button's
    true centre is (500,751) in this window geometry,
    matching the zombie-invasion March lesson
    (500,755) - the visual centre estimate sits above
    the button's active area.
  - March verification: the panel closed and March
    Queues read 0/4, but the radar stamina read stayed
    120, so dispatch was not proven by stamina alone.
    Proof came from the pin itself: back on the radar,
    the same pin's card now showed the revealed rewards
    (survivor x1, paw print x200, black rock 207.3K),
    exactly the verified story flow's step 4. The
    march did dispatch and resolve; the radar stamina
    figure did not move with it, an unresolved read
    discrepancy recorded here, not smoothed over.
  - Go again at (500,946) returned to the task
    location with the simplified card; the green
    magnifier button grounded at (499,599) (an
    estimate tap at (449,553) did nothing) opened the
    story dialog ("Are you Violet?"). Tapping the
    bottom of the dialog advanced it through "...and
    helped delay CL-7." to the closing line "Take me
    to your base. I'll prove it through my actions!"
    and the top banner "...th the treasure map -
    congrats!". One more bottom tap closed the dialog.
  - Back on the radar, the story pin is gone in the
    closing frames: the pin completed and its reward
    was paid through the Claim All below.

## What was done

- Quick Execute 1: 2 tasks, stamina 120 to 100, stored
  stayed 2/40. Bar flipped to Claim All: "9 task
  rewards can be claimed".
- Claim All 1: 9 rewards claimed, no TIPS dialog (as in
  the 1913 unit; contrast the 1450 unit's pre-rollover
  TIPS dialog - see the Issue #235 note below). Popup:
  radar item 80, paw print 200, blue triangle 948,
  EXP 7.6M, drone item 1.6K, black rock 207.3K, coin
  1.9M, iron 2.0M, food 1.5M, Lv.1 chest 1, survivor
  portrait 1. Radar points 183 to 192 (+9, exactly
  the claim count), stored 2/40 to 0/40. Bar flipped
  to Quick Execute: "You can complete 1 tasks,
  requires 10 Stamina."
- Quick Execute 2: 1 task, stamina 100 to 91 (10 spent,
  1 regenerated), stored stayed 0/40. Bar flipped to
  Claim All: "2 task rewards can be claimed".
- Claim All 2: 2 rewards claimed, again with no TIPS
  dialog. Popup: radar item 20, EXP 3.3M, drone item
  800, food 1.2M, coin 319.2K, iron 316.8K. Radar
  points 192 to 194 (+2, exactly the claim count),
  stored 0/40. The bottom bar then showed no offer
  at all: no Quick Execute, no Claim All.
- No diamonds or money spent, no Buy tapped, no
  stamina item used, no free stamina claim taken
  (stamina never blocked execution), no other
  activity worked from this unit.

## Totals in this unit

- Rewards claimed: 11 (9 + 2). Radar points 183 to
  194 (+11, exactly the claim count).
- Tasks executed: 3 via Quick Execute (2 + 1), plus
  the story pin task completed through its full flow.
- Popup resources summed: radar items 100, EXP 10.9M,
  drone items 2.4K, blue triangles 948, coin 2.2192M,
  iron 2.3168M, food 2.7M, plus paw prints 200, black
  rock 207.3K, Lv.1 chest 1, survivor 1.
- Stamina: 120 to 91 net (-29: 30 spent on Quick
  Execute, 1 regenerated; the story march's shown -5
  never moved the radar stamina read, see above).
- Duel points: NOT read in this unit. No VS panel
  read was taken, and no duel-points figure is
  claimed. Both Claim All taps ran with no TIPS
  dialog, matching the 1913 post-rollover unit and
  continuing the evidence for Issue #235 (duel.py
  says radar claims score on day 3; the 1450 unit's
  pre-rollover TIPS dialog said they do not); it is
  noted here, not settled here.

## Closing state (live reads, same unit)

- Radar Lv.13, radar points 194, stored 0/40,
  stamina 91, restore line "Fully restore at 11-5
  03:31:43 local time", bottom bar with no offer.
- Pin inventory at close (visible frames only, not
  a whole-map census): a blue axe pin top left, a
  purple arrow pin centre, and a blue skull pin top
  centre carrying a red dot (seen in the frame
  before Claim All 2; the closing frame's map view
  had shifted and showed only the axe and arrow
  pins, both with no red dot visible). The story
  question-mark pin is gone, completed in-unit.
- Per the release standard, pins left unattempted
  make this unit partial, never done. The axe and
  skull pins are the same standing pins carried
  since the 1450 and 1913 units, so this is the
  third consecutive partial carrying the same pin
  blocker. Under rule R7 the pins become the FIRST
  action of the next radar unit, starting with the
  red-dotted blue skull pin (a finished-task pin
  pays instantly on tap, per the activity
  metadata) and then the axe pins, whose class is
  still unidentified - the next unit must tap them
  under the release handling rule rather than
  inventory them again. The map-view shift between
  the pre-claim and closing frames means the next
  unit must re-ground every pin point on its own
  current screenshot, never reuse the positions
  recorded here blindly.
- Tracker untouched for partial, per the queue rules.
