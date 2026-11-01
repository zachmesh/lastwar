---
title: Perception-Driven Queue
created: 2026-11-01T05:10:00Z
modified: 2026-11-01T05:10:00Z
level: L2
version: 1.0.0
description: The scout layer - daily work is determined by what the game screen actually offers, observed first and enqueued dynamically, with the static regulars as the baseline
status: phase-1-landed
grounded_in:
  - source: owner direction of 2026-10-31 - daily tasks shall be determined by what is observed on screen, perceive the game first, see what is available to do, and place it into the queue dynamically
  - source: miss audit of 2026-10-31 - whole classes of work had no execution channel because no static model named them
  - source: reflection of 2026-10-31 in this folder
---

# Perception-driven queue - the scout layer

## 1. Principle

Until now the day was defined by a static list - the 19 regulars
in `tools/regulars.json`. The planner staged one unit per regular
per window, and the executor worked the list. The miss audit of
2026-10-31 showed the structural cost of that definition - work
the list did not name did not exist. Daily missions were modelled
but never scheduled. The Crystal Shop and the Glittering Market
sat outside the list entirely. State-dependent availability - a
train in preparation, a phase that just rotated, a market whose
contents changed - was discovered late or never, because nothing
looked at the game before deciding what the day contained.

The owner direction of 2026-10-31 inverts the flow -

- **Perceive first.** Scout units walk the game interface
  systematically and record what is actually available to do, as
  a structured observation.
- **Diff, then enqueue.** The observation is compared against
  the modelled work - the regulars, the daily collection ledger
  and the pool. Execution units are generated, updated or closed
  from what was seen, not from what the static list assumed.
- **The static list is the baseline, not the day.** The regulars
  still guarantee the floor - every modelled line is checked on
  its cadence whether or not a scout saw it. The scout layer adds
  the two things the list cannot do - discovering work outside
  the models, and confirming the real availability of work inside
  them.

A scout unit never does the work it finds. It observes, records
and hands over. Execution stays one unit, one task type, under
the queue design - the scout layer changes where units come
from, not how they run.

## 2. The traversal checklist

A scout pass walks every surface below. The checklist is the
definition of "the whole game" for perception purposes, and it
is append-only - the first time any scout or executor meets a
new surface, tab or entry point, it is added here in the same
session, with the date it was found. The checklist only grows.

### Base screen

- Resource bubbles standing on the base - food, iron, coin, EXP,
  titanium - each noted as its own signal, never merged.
- The Armed Truck state - progress, the fully loaded notice.
- Building badges and red dots, building by building, including
  queue states a badge points at.
- The left column entry icons, re-grounded fresh - their points
  drift, and a scout pass re-measures them like any executor.
- Gate and wall signals - the survivor line at the gate, help
  bubbles over buildings.

### HUD and counters

- Resource totals as displayed - food, iron, coin, diamonds,
  rubies.
- Stamina, and every counter or timer visible on the HUD.
- The duel score widget and the day progress it shows.
- Inbox and gift icons with their badge counts.

### Events hub

- Every tab in the hub, opened, and every activity sub-page
  inside it expanded - check-in calendars, Wanted Boss and its
  Goals, Arms Race entry state, seasonal activities, limited
  activities with their own claim and progress states.
- Every activity records its own state - claimable rewards,
  doable work, progress, and any visible deadline.

### Store

- Every Store section, walked by name, not only the storefront -
  the Building section and the Crystal Shop tab inside it, the
  pass pages, Hot Deals, Daily Pickup and Free Supply, and any
  section added since the last pass.
- The Alliance Store is read for state only - its Buy button is
  a red line and is never pressed.

### Markets

- Market-class entry points - the Glittering Market above all,
  and any market, exchange or trading surface a pass encounters,
  wherever its entry turns out to live.

### Alliance panel

- Gifts on both tabs, the help state, donation state and count.
- Alliance technology state.
- The station panel, train by train - each service in
  preparation, boardable or departed, read on the panel itself.
  A banner-only read does not count as perception of the train.

### Mail

- All six categories, badge counts first, then the unclaimed
  state per category. Mail that evidences an unworked source -
  the Glittering Market Unclaimed mail is the standing case - is
  recorded as a signal pointing at that source, never as the
  source worked.

### Duel, radar, world map

- The duel page - the personal daily total, read live, with the
  day target gap, plus the day scoring state.
- The Arms Race page - live phase, phase score, chest states.
- The radar panel - task state, claim state, the stack or
  release posture of the duel day.
- World map pins and the loot gift box - pins are observed,
  never tapped on a stack day; tapping is an execution act, not
  perception.

### Account surfaces

- The VIP page - points, the Daily Freebie state, the login
  chest state, each read as its own item.
- The passes pages - weekly and monthly pass daily states.
- The daily missions panel - activity points, chest states,
  completed unclaimed tasks.

## 3. The completeness standard - zero unexplained red dots

A scout pass is complete only when every signal it met is
accounted for. Every red dot, badge, counter and timer observed
must resolve to exactly one of -

- **(a) an action** - the signal maps to work that can be done,
  and a unit for it is generated or already queued under the
  diff rules of section 5; or
- **(b) a recorded reason** - the signal cannot be acted on, and
  the observation records why - a red line, a locked feature, a
  purchase price, a phase not yet open, a state that needs the
  owner.

A signal that was seen but not classified is an unexplained red
dot, and it is a defect of the pass, counted in the pass result
and named in the round summary. A scout unit that closes with
unexplained red dots closes as partial, however much it walked.
This standard is the perception form of rule R1 - nothing closes
on silence.

## 4. The observed items schema

Every signal a scout records is one observed item, written in
the day observation file (section 7) as a structured block in
the same frontmatter style the queue already uses - values
colon-free except timestamps.

```yaml
observed_items:
  - surface: events/wanted-boss
    label: Wanted Boss Code 39 goals
    state: doable
    deadline: 2026-11-02T03:00:00Z
    est_value_or_score: best hit 1097397868, next goal tier unread
    suggested_unit: events
    redline_check: clear - fighting the boss spends stamina only
  - surface: store/building/crystal-shop
    label: Crystal Shop tab
    state: claimable
    deadline: ""
    est_value_or_score: daily free crystal, amount as displayed
    suggested_unit: new
    redline_check: claim only - any priced exchange stays unpressed
```

| Field | Meaning |
|---|---|
| `surface` | where it was seen, as a path of screen, section and sub-page |
| `label` | the item as the game names it, transcribed |
| `state` | one of claimable, doable, in-progress, locked, info-only |
| `deadline` | the visible expiry or reset it dies at, when the screen shows one |
| `est_value_or_score` | the visible value, amount or score it carries, when shown |
| `suggested_unit` | the regular id that should work it, or `new` when no model owns it |
| `redline_check` | what the red lines say about acting on it - clear, blocked and why, or owner-needed |

State vocabulary -

- **claimable** - a reward or pickup is ready to take now.
- **doable** - work can be done now - a fight, a dispatch, a
  donation, a boarding.
- **in-progress** - under way with a visible state or timer - a
  truck on the road, a train in preparation, a building queue.
- **locked** - visible but not open - level, phase, unlock or
  preparation gates.
- **info-only** - read for the record - a total, a ranking, a
  notice with nothing to claim or do.

## 5. Diff and dynamic enqueue rules

After each pass, the observation is diffed against three
references - the regulars, the daily collection ledger, and the
pool in all three states.

- **Known item, actionable.** A unit of its regular is produced
  for the current window through the shared (regular,
  planned_for) invariant - already queued, claimed or done means
  no duplicate. When the item carries a deadline nearer than its
  window end, the queued unit is raised in priority instead -
  priority 2 normally, priority 1 when the deadline falls inside
  the current window.
- **Known item, already done.** When the observation shows a
  modelled line already satisfied - collected, claimed, boarded -
  no unit is produced, and the observation stands as the day
  evidence for that ledger line.
- **Unknown item.** An item whose suggested_unit is `new` gets an
  exploration unit at priority 2, enqueued manually in Phase 1
  (the diff tool of section 8 automates it in Phase 2). The
  unknown is named in that day round summary. Its first execution
  backfills activity metadata for the item and decides its fate -
  promoted to a modelled regular or ledger line, kept as a
  recurring exploration, or recorded as info-only with the reason.
  No unknown item ages unnamed - rule R5 applies to it from its
  first day.
- **Modelled but absent.** When the models expect something the
  screen does not have - an activity that has ended, a tab that
  is gone, a pass that expired - the diff closes the expectation
  instead of staging empty units against it. The closure is
  recorded in the observation and in the activity metadata, so
  the next planner run stops producing for a dead surface.
- **Contradiction.** When the screen contradicts a standing
  record - a count, a mechanism, a state the metadata asserts -
  the screen wins, the observation records the contradiction,
  and the metadata is corrected in the same session. Perception
  never defers to the file against the game.

## 6. Perception points in the day

- **Post-reset full pass** - the first pass of the reset day,
  staged at the 19:00 local reset. It walks the whole checklist.
  This is the pass that builds the day - everything the reset
  made available is observed before the day routine settles into
  its windows.
- **Midday pass** - one more full pass at the middle of the
  reset day, 07:00 local. It exists for state-dependent
  availability the morning cannot show - trains entering
  preparation, Arms Race phases rotated, markets refreshed,
  trucks returned.
- **Handover to the zero sweep.** The pre-reset zero sweep
  (queue design section 12) walks the merged list - the daily
  collection ledger plus the day observed items - so anything
  perception found during the day is swept by the same standard
  as the modelled lines. An observed item still open at the final
  sweep gets its fix-up unit enqueued by the sweep, exactly like
  a ledger line not at zero.

## 7. Budget, chain splitting and the observation file

A scout pass is bound by the same 15 minute unit cap as all
work. A full traversal does not fit in one unit, so a pass is a
homogeneous chain of scout units, one per surface group -

- `scout-base` - base screen, HUD and counters.
- `scout-events` - the Events hub, the duel page, Arms Race,
  radar.
- `scout-store` - the Store by section, the markets, VIP, the
  passes, the daily missions panel.
- `scout-alliance` - the alliance panel, the station, mail, the
  world map pins and the loot box.

The chain carries one chain id per pass - `scout-<reset date>`
for the post-reset pass, `scout-mid-<reset date>` for the midday
pass - and its units run in order inside the pass window. Each
unit observes only its own surface group and appends its section
to the day observation file. A unit that cannot finish its group
inside the cap closes partial with the unwalked surfaces named,
and the chain continues with a successor for the remainder -
perception is never silently truncated.

**The observation file** lives with the day execution records -
`_records_/<local date>/perception-scout/observation.md`. One
file per reset day, append-only inside the day (constitution
C1) - the post-reset pass writes its sections first, the midday
pass appends its own, and the zero sweep reads it as it stands
at sweep time. Its frontmatter carries the day counters -
passes completed, items observed, red dots seen, red dots
explained, unexplained red dots - and its body carries the
observed items per pass and per surface, in the schema of
section 4. The file is the single input the diff works from,
and the evidence every scout unit result points at.

**Scout unit results.** A scout unit completes through
`tools/queue.py complete` like any unit. Its result must carry -

- `evidence` - the day observation file.
- `stats` - surfaces_walked, items_observed, red_dots_seen,
  red_dots_explained, unexplained_red_dots, unknown_items.
- `follow_up` - the units the diff enqueued or raised, or the
  unknowns awaiting their exploration unit, named - never a bare
  `none` while the pass holds an open signal.

## 8. Tool design - tools/scout_diff.py (Phase 2)

Design only in this phase - no code is written here. The tool is
the diff of section 5 as a program, so the step from observation
to queue stops depending on an executor remembering to do it.

**Interface sketch**

```text
tools/scout_diff.py [--root DIR] [--date YYYY-MM-DD] [--enqueue]
                    [--format text|json]
```

- Without `--enqueue` the tool is a dry run - it prints its three
  outputs and changes nothing. With `--enqueue` it writes the
  enqueue plan into the pool through `tools/queue.py enqueue`,
  one call per unit, so every unit it creates passes the same
  validation as a manual enqueue - the cap check, the chain
  homogeneity check, the file layout.

**Inputs**

- The day observation file,
  `_records_/<date>/perception-scout/observation.md`, parsed for
  its observed items.
- `tools/regulars.json` - the modelled regulars and their
  cadences.
- The daily collection ledger - its lines and the regular that
  produces each.
- The pool itself, read through the queue tool list and stats
  functions - what is already queued, claimed or done.

**Outputs**

1. **The enqueue plan** - one entry per unit to create or raise,
   in the exact field shape `tools/queue.py enqueue` consumes -
   regular, activity, priority, expires_at from the item
   deadline, not_before, window text naming the observation it
   came from, and a chain id `scout-followup-<date>` for
   exploration units. Known items map to their regular; unknown
   items map to exploration units at priority 2.
2. **The unknown items list** - every observed item with no
   owning model, with its surface, label and state, formatted
   for the round summary naming rule R5 requires.
3. **The coverage report** - the perception scoreboard for the
   day - items observed, items queued, items already done, red
   dots seen, red dots explained, unexplained red dots - totalled
   and split by surface. The unexplained count is the headline -
   the day perception is judged by it reaching zero.

**Idempotency** - the tool obeys the pool invariant it feeds.
Produced units dedupe on (regular, planned_for) exactly as sync
and plan do. Dynamic units carry their source in their window
text and chain id, and the tool checks the pool for an existing
unit from the same observation item - same date, surface and
label - before enqueueing. A second run over the same
observation produces an empty enqueue plan and an unchanged
pool. The tool never completes, claims or deletes a unit - it
only proposes and, with `--enqueue`, enqueues.

**Priority support it needs from the queue tool** - produced
scout units should stage at priority 2, windowed work. The
queue tool takes production priority from its SYNC_PRIORITY
table, which has no scout entries yet. Adding `scout` and
`scout-midday` at priority 2, with learned-estimate seeds, is a
named part of the Phase 2 change, landed with this tool rather
than silently defaulting scout production to priority 3.

## 9. Phased roadmap

- **Phase 1 - this document and the modelling (landed with this
  change).** This design, the perception layer section of the
  task unit queue design, the observed items schema, the
  traversal checklist, and the scout regulars in
  `tools/regulars.json` with their activity metadata. Scout
  passes run as executor-produced chains under the existing
  planner; the diff of section 5 is applied by the executor
  from the observation file, by hand, under the rules above.
- **Phase 2 - the diff tool and the planner hookup.** `tools/scout_diff.py`
  implemented to the design of section 8, the queue tool priority
  entries for the scout regulars, and the planner pass running
  the diff after each scout chain completes, so dynamic units
  land in the pool without waiting for an executor to transcribe
  them.
- **Phase 3 - reporting and promotion automated.** The coverage
  report joins the round summary as a standing section, the
  unknown items naming becomes automatic, and the promotion of a
  proven unknown into a regular or a ledger line is proposed by
  the tool from execution history - the owner still approves
  promotions, the tool only brings the evidence.

## 10. Standing rules this layer inherits

- The red lines bind perception exactly as they bind execution -
  a scout reads a priced button, it never presses it. Reading
  the Alliance Store is perception; its Buy button stays
  unpressed.
- One unit, one task type - a scout unit observes; the work it
  finds belongs to the owning type own unit, counted under that
  type statistics.
- Rule R1 - a scout closes on live reads or as unverified, like
  every unit. An unwalked surface is named, never smoothed over.
- The ledger standard - an observed line and a ledger line close
  by the same evidence, a live read from that day.
