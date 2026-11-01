---
title: Perception Scout
created: 2026-11-01T05:10:00Z
modified: 2026-11-01T10:45:00Z
level: L1
version: 1.1.0
description: The scout passes - walking the whole game interface to observe what is available to do, recording it as observed items, and handing the work to the owning regulars
status: active
grounded_in:
  - source: owner direction of 2026-10-31 - perceive the game first, see what is available, place it into the queue dynamically
  - source: perception-driven queue design in the local conventions
  - source: task unit queue design section 13
  - source: perception-scout execution record 2026-11-01 0215 PST, first day observation
---


# Perception scout

## What this activity is

The perception layer of the routine. A scout pass walks the
game interface systematically - base screen, HUD, Events hub,
Store by section, markets, alliance panel and station, mail,
duel and radar, world map, VIP, passes, daily missions - and
records what is actually available to do as structured observed
items. It exists because the miss audit of 2026-10-31 proved
that work no static model named was never done - the scout is
how the day finds out what it contains before the day is worked.

Executions are recorded in `_records_/<date>/perception-scout/`,
one observation file per reset day, appended to by every scout
unit of that day. The full design - traversal checklist,
completeness standard, observed items schema, diff rules - is
the [perception-driven queue](../../_conventions_/local-conventions/perception-driven-queue.md)
document in the local conventions. Section 13 of the task unit
queue design fixes the unit contract.

## The job

1. Walk the surface group the unit owns - scout-base,
   scout-events, scout-store or scout-alliance - opening every
   tab and sub-page in the traversal checklist, re-grounding
   entry points fresh.
2. Record every signal as an observed item in the day
   observation file - surface, label, state, deadline and value
   where visible, the owning regular or `new`, and the red-line
   check.
3. Close no signal on silence. Every red dot or badge resolves
   to an action or to a recorded reason. Unexplained red dots
   close the unit as partial and are named in the round summary.
4. Never do the work. A scout observes only - no claim, fight,
   dispatch, donation or purchase, and no map pin tap on a radar
   stack day. The work belongs to the owning regular own unit,
   produced or raised by the diff.
5. Append, never rewrite. The observation file is append-only
   inside its day - the midday pass adds its sections after the
   post-reset pass, it does not edit them.

## Cadence

Two passes per reset day, both regulars in _tools_/regulars.json -

- `scout` - the post-reset full pass, daily-reset cadence
  anchored at the 19:00 local reset.
- `scout-midday` - the midday full pass, daily-reset cadence
  anchored at 07:00 local, for state-dependent availability the
  morning cannot show.

Each pass is a homogeneous chain of scout units split by surface
group - the staged unit is the chain head, the executor extends
the chain under the queue chain rules.

## What is known from 2026-11-01

First day observation file, from the 0215 unit (ticker-0204,
unit scout-midday-2026-10-31-0700, group scout-base, status
partial). Evidence in `_records_/2026-11-01/perception-scout/`,
observation file plus queue-run file.

- Entry correction, rule R2 - the game was found open on the
  Secret Command Post Hidden Treasure screen, left there by an
  earlier unit, not on the base screen. Two taps near norm 83 to
  86,938 to 941 on the back arrow changed nothing; a third tap at
  norm 112,946, the centre of the blue arrow, returned to the
  base screen. The earlier points had clipped the overlapping
  portrait icon at the arrow left edge. The next unit re-grounds
  the back arrow at norm 112,946, not 83,938. The encountered
  Secret Command Post surface counts as encountered, not as a
  walked group.
- Base screen and HUD read live about 02:15 local - level 30,
  power 148,957,193 as displayed; HUD top row 289.2M, 477.2M,
  10.6M, 2,366 beside the cart icon; second row lightning 135
  and 11.72K with a plus button, labels for the second row not
  legible in the downscaled capture and recorded as displayed
  only, not asserted. Left column top to bottom - zombie face,
  train, truck, radio with red badge 4, magnifier, survivor
  portrait, building icon, HEROES button at the bottom. Right
  column - Halloween Check-In with a 7 badge, Events with an x2
  badge, Faction Duel, VS, Season II, Alliance with a red dot,
  Mail with a red dot, Inventory, BASE. Centre - base with
  aircraft, one building carrying a badge 5. Bottom - a NEW!
  speech bubble over a chest icon with a badge 3, unexplained
  in this unit, not opened.
- Red dot accounting - seen 7, explained 4, unexplained 3.
  Explained - radio badge 4 to the help regular, Mail dot to
  the mail regular, Events x2 to the events regular,
  Halloween Check-In 7 to the check-in surface, with help,
  mail and events units already queued for the current slots.
  Unexplained - Alliance dot, building badge 5, NEW! chest
  badge 3. Unknown items 2 - the furnace overdrive toast line
  ("Furnace total overdrive time (in sec)", furnace observed
  only, never touched, a red-line surface) and the exact
  resource labels of the second HUD row.
- Partial by design, not a failure - the unit cap of 15 minutes
  closed the group with the base screen and HUD read only.
  Unwalked and carried to the successor unit (chain
  scout-mid-2026-10-31) - scout-base remainder (building
  badges building by building, Armed Truck state, gate and
  wall signals, resource bubbles re-read) plus the
  scout-events, scout-store and scout-alliance groups in full.
  Result statistics as written - surfaces walked 1, items
  observed 12, red dots seen 7, explained 4, unexplained 3,
  unknown items 2, resources gained none, observation only.
- Cross-check inside the same pass - the Hidden Treasure read
  on entry matched the treasures unit of ticker-0136 exactly
  (M1 x13, M2 x11, M3 x0, M4 x9, M5 x0, M6 x4, M7 x13,
  chest 1 of 15), and the Rewards Preview panel was read only
  (single dig chest rates UR 10.0 percent, SSR 30.0 percent,
  SR 60.0 percent, panel closed with its X, nothing claimed).
  The treasure counts are therefore confirmed by two live reads
  the same morning; the dig odds confirm the hidden-treasures
  profile figure.
- Staged-unit filing question, left open for the queue rules,
  not decided by this unit - ticker-0136 deliberately left
  this unit unexecuted, reasoning its window belongs to the
  2026-10-31 reset day which closed at 19:00 on 2026-10-31,
  and that a pass then would append current-day observations
  to a closed day file. Ticker-0204 executed it anyway on a
  different filing ground - every observation in the unit is
  a 2026-11-01 early-hours live read, filed under 2026-11-01,
  not under the closed day. Whether stale staged scout units
  should execute or expire is a queue-rule question for the
  queue design owners, recorded here, not settled by a scout
  unit. Resource bubbles - none clearly standing on the base
  in this capture, recorded as none seen, not as none present.

## Open questions

- The three unexplained red dots above (Alliance dot, building
  badge 5, NEW! chest badge 3) and the two unknown items (furnace
  overdrive toast, second HUD row labels) - carried to the
  successor scout unit, not closed on silence.
- Whether stale staged scout units execute or expire - see the
  filing question in the 2026-11-01 section; a queue-rule
  decision, not a scout-unit decision.
