---
title: Alliance donations queue run 1923
created: 2026-11-02T19:23:00-08:00
executor: ticker-1904
unit: donations-2026-11-02-1803
status: failed
---

# Alliance donations - 2026-11-02 19:23 queue run (ticker-1904)

## Outcome

- Status: failed. Execution was impossible in this unit:
  the game was stranded on the Arms Race page left open by
  the previous unit, and its back arrow did not navigate
  in four attempts, so the base screen (and therefore the
  Alliance menu and Alliance Techs) was never reached.
- Tracker: untouched. No donation was made and no live
  Donation Count was read, so nothing is claimed about
  the day's donation state.
- No live count, no target technology, no donation in
  this unit - all unverified by this unit.

## What was tried

- Back arrow on the Arms Race page, bottom-left blue
  button, four attempts with fresh observations each
  time: single tap at norm 90,947 (arms-race unit),
  double-click at norm 90,947 (arms-race unit), single
  tap at norm 89,949, single tap at norm 58,945 (the
  coordinate that worked for the radar screen's back
  arrow earlier this pass). Every attempt dispatched
  with no observed change; the Arms Race page stayed
  open with its timer running (02:45:21 down to about
  02:40:15 across the attempts), proving the game was
  live and responsive to the clock but not to these
  back-arrow taps.
- The pass budget (about 25 minutes from the first
  token) did not leave room for a full app relaunch
  plus Alliance entry inside this unit, so the relaunch
  route was not attempted here.

## Blocker (named, per rule R2)

- Back-arrow unresponsive on the Arms Race page under
  background input, fourth consecutive failure counting
  the arms-race unit's two attempts. This is the same
  stranded-page family as the 2026-11-02 donations
  entry blocker (camera panned to Drill Ground), but
  the mechanism here is different: the page is the
  Arms Race page itself, and its back button ignores
  background taps.
- Handover for the next donations unit: relaunch the
  app first (the 14:39 radar handover notes a relaunch
  restores the base overview), then open the Alliance
  menu from a verified base view, then Alliance Techs.
  Do not start from a stranded event page. If the
  relaunch shows the different-device dialog, that is
  the pass's next allowed takeover (this pass used
  one, in the radar unit).

## Red lines

Nothing spent, no diamond button touched, no other
activity's work done from this unit.

## Result stats

- donations_made 0, donation_count_read false,
  entry_blocker back-arrow-unresponsive.
