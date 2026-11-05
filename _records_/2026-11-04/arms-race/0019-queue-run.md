---
title: Arms Race queue run 0019
created: 2026-11-04T00:19:00-08:00
modified: 2026-11-04T00:19:00-08:00
version: 1.0.0
description: Ticker unit arms-race-2026-11-03-2203, Hero Advancement phase, score 0, tier 3 not met, hero-card tap blocked
status: partial
grounded_in:
  - source: live game screens on the owner Mac mini, 2026-11-04 00:04 to 00:19 PST
---

# Arms Race queue run 0019

Unit: arms-race-2026-11-03-2203, executor ticker-0004.
Session window: 2026-11-04 00:04 to 00:19 PST, device session cc-395.
No different-device dialog appeared. No diamonds or money spent,
no speedup burned, no stage swap, no research or building started,
no recruitment made, no hero levelled, no chest claimed.

## Session start state

The game was already running, left on an Alliance Techs detail
panel (Rallied Attack 7/10, Tech EXP 16.6K/4.5M, Donation Count
3/30). The detail panel and the tech list were closed without
donating: donations belong to their own unit under the
one-unit-one-type rule. The Alliance screen back arrow needed
two taps before it returned to the base.

## Live phase reading

- Phase: Hero Advancement, Contest Segment Lv.29-30.
- Time left at entry: 01:52:03; phase ends about 02:04 PST.
- Score read live: 0 (top star display). Chest thresholds read
  live: 2,000, 4,000 and 12,000, ruby tags 2,360, 4,800, 11,800.
- Scoring rows read live: 1 Hero Recruitment +400; Use at least
  2,000 Hero EXP at a time +1; Buy Packs containing Diamonds
  +30 per diamond (red line, not used).
- Cumulative counter chest at the top left read 3/8, partial,
  not claimable.
- Ranking row read: segment rank 10, combined #2110
  [AP3x]Bears Lair, row figure 10,000. The row figure is NOT
  used as the score: all three point chests showed locked and
  one tap on the tier 1 chest produced no change, consistent
  with a live score of 0. The row figure's meaning is
  unexplained and is recorded as such, not as a closing count.
- Events hub tabs seen at entry: Arms Race, Desert Battlefield,
  General's Trial, and a further tab cut off at the right edge.
  No Zombie Invasion tab, consistent with the chain close of
  2026-10-30. No zombie chain was seeded: the event is not
  available now.

## Navigation blockers and pivots (rule R2)

- The Events screen back arrow took two background taps with
  no change, and the Recruit screen back arrow likewise took
  two taps plus a re-centred tap with no change. Both methods
  ended inside this unit per R2.
- Pivot that worked: a left-edge swipe drag (from x 15 to x 500
  at mid height) returned from the Recruit screen to the base.
  This swipe-back is the changed method for the next unit when
  a back arrow does not respond.
- Wrong-row tap, no action taken: one tap intended for the
  Hero EXP scoring row arrow opened the Recruit screen instead
  (Recruitment Timer 3d 17:50, Recruit x1 Free shown). Nothing
  was recruited; the screen was left via the swipe above.

## Hero level-up not executed

- From the base, HEROES opened the Hero List. The bottom-right
  card read Lv.124 (the level Adam reached in the 2026-11-02
  Hero Advancement unit); the list shows no names, so the card
  is not confirmed as Adam.
- Two taps on that card at its measured centre produced no
  change, and one long-press variant also produced no change.
  The hero detail was never opened, so no EXP was spent and no
  level-up was executed. This is the unit's closing blocker.
- Tier 3 (12,000) therefore stays unmet: gap 12,000, score 0.

## Completion sweep

- No point chest was claimed; no bouncing chest or reward red
  dot was visible on the Arms Race page apart from the
  not-yet-full cumulative counter at 3/8.
- The ranking-row chest was not tapped: while the phase is live
  it opens a preview only, and its reward is claimed by the
  run after the phase ends.

## Follow-up

- Next arms-race unit in this phase (ends about 02:04 PST)
  should retry the hero detail with a changed method: a class
  tab filter, a different card, or a foreground tap path, and
  then level one hero with EXP only, per the 2026-11-02
  precedent (Adam Lv.123 to Lv.124 scored 40,500 and cleared
  the 12,000 top chest). If the hero detail still does not
  open, the blocker must be written into the activity metadata
  per rule R2.
- Status: partial. Tracker left untouched; the next tick
  re-produces the regular.
- Result stats: target 12000, achieved 0, points 0, verified yes,
  blocker_category c (tap method, hero card and back arrows).
