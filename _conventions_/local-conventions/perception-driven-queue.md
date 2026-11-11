---
title: Perception-Driven Queue
created: 2026-11-01T05:10:00Z
modified: 2026-11-11T09:32:17Z
level: L2
version: 1.2.4
description: The scout layer - daily work is determined by what the game screen actually offers, perceived first and scheduled by observation triggers rather than fixed slots, with the regulars kept as a capability profile library and new tasks discovered, profiled and scheduled automatically
status: phase-2-landed
grounded_in:
  - source: owner direction of 2026-10-31 - daily tasks shall be determined by what is observed on screen, perceive the game first, see what is available to do, and place it into the queue dynamically
  - source: owner refinement of 2026-10-31 - no fixed schedule; check and perceive where tasks are needed and schedule them automatically; discover potentially new tasks, learn about them, create their task profile and metadata, and start scheduling executions for them
  - source: miss audit of 2026-10-31 - whole classes of work had no execution channel because no static model named them
  - source: reflection of 2026-10-31 in this folder
  - source: organizer 0432 run 2026-11-07 (Refs #147, #247) - the two standing 19:00 reset anchors rewritten to the absolute reset instant 02:00 UTC
---

# Perception-driven queue - the scout layer

## 1. Principle

Until now the day was defined by a static list - the 19 regulars
in `_tools_/regulars.json`. The planner staged one unit per regular
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

The owner refinement of 2026-10-31 sharpens the principle one
step further -

- **Scheduling is observation-triggered, not fixed-slot.** No
  execution unit exists because a clock slot said so. A unit is
  produced when perception fires a trigger from the list in
  section 5 - a badge turned claimable, a deadline approaching,
  a storage about to fill, a phase rotated, a train entering
  preparation, a quota behind pace, a new element on screen.
  Fixed time slots survive only as the safety net underneath -
  the cadence checks and the two anchored scout passes of
  section 7 are the floor that guarantees nothing modelled is
  ever left unchecked, never the primary mechanism and never
  the ceiling.
- **The regulars are a capability profile library.** Each known
  task is kept as a profile, not a timetable entry - its entry
  point, its rules, its red lines, the live read that verifies
  it, its trigger conditions, its deadline shape, its cooldown
  and its expected duration. Section 5 fixes the profile fields.
  The clock keeps only two jobs - the perception heartbeat (the
  ticker cadence that keeps perception rolling) and the game
  hard deadlines (the trade-day reset, absolute 02:00 UTC, Arms Race phase windows, the
  quota checkpoints of rule R3).
- **New tasks are discovered, not waited for.** Anything the
  screen shows that no profile owns enters the discovery
  protocol of section 6 - filed as a provisional candidate,
  learned by exploration units, promoted to an active profile
  and scheduled by the same triggers, or rejected with the
  reason kept. Discovery is part of comprehensiveness, not an
  exception path.

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

**The unmatched labels list.** Every full pass closes with an
explicit roster-out scan - the `unmatched_labels` list of every
label, icon and tab the pass met that no roster entry owns -
the regulars index, the ledger, the checklist, the candidate
register. The list is part of the coverage report of section 9,
printed even when it is empty, because an absent list and an
empty list are different claims - the first is a pass that did
not look, the second is a pass that looked and found nothing
outside the roster. Every entry on a non-empty list enters the
discovery protocol of section 6 in the same session; an
unmatched label that is neither filed as a candidate nor
recorded with a reason counts as an unexplained red dot under
the standard above.

## 4. The observed items schema

Every signal a scout records is one observed item, written in
the day observation file (section 8) as a structured block in
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

## 5. Trigger-based scheduling - profiles, triggers and the diff

### The capability profile

Under the owner refinement, `_tools_/regulars.json` is the index
of a profile library, and each regular profile - the index row
plus its `_activities_` metadata - carries these fields -

| Field | Meaning |
|---|---|
| entry point | where the task lives on screen, re-grounded at execution like every entry point |
| rules | how the task is worked - the standing method, quality rules and caps from its metadata |
| red lines | what must never be pressed or spent while working it |
| verification | the live read that closes it - the counter, balance or panel state of rule R1 |
| triggers | the observation conditions of the trigger list below that produce its units |
| deadline shape | when its value dies - the reset, a phase end, a preparation close, a displayed countdown, or none |
| cooldown | the wait after an attempt before a trigger may fire it again - a greyed button timer, a return trip, a phase length |
| expected duration | the learned estimate of section 5 of the queue design, used by the priority formula below |

A profile with no trigger written yet is a gap, not a default -
writing its triggers is part of keeping the library honest, and
a profile whose screen has died is closed by the modelled but
absent rule below, not left to fire forever.

### The trigger list

A unit is produced when one of these fires in an observation -

- **Claimable now** - a red dot, badge or counter turned
  claimable or doable since the last observation of that
  surface.
- **Deadline approaching** - a visible countdown, the reset, a
  phase end or a preparation close enters the window where one
  unit plus one retry still fits before it.
- **About to fill** - a bubble field, a warehouse, a gift or
  inbox badge count, or any capped store is at or near its cap,
  so uncollected value would stop accruing or overflow.
- **State rotation** - an Arms Race phase rotated, a duel day
  posture changed, a market refreshed, a pass day rolled.
- **Preparation opened** - a train entered preparation, a boss
  spawned, a limited activity opened its window.
- **Quota behind pace** - a quota counter (rule R3) reads behind
  the pace its cycle end demands at a checkpoint or at any
  observation that reads it.
- **New element** - a label, icon or tab no profile owns - this
  fires the discovery protocol of section 6, not an execution
  unit.
- **Floor check** - the cadence safety net - a profile not
  observed inside its cadence window is perceived and checked
  anyway, so silence never masquerades as nothing to do.

### Priority

Produced units are ordered by a score, not by the slot that
bore them -

```text
priority score = deadline pressure x value / expected duration
```

- **Deadline pressure** rises as the time left before the
  item deadline approaches one unit duration plus one retry -
  inside that band the unit is priority 1, expiry-critical.
  Items with no deadline carry the lowest pressure.
- **Value** is what the item visibly carries - duel or phase
  score first on scoring days, then resources, then progress -
  read from the observation, never assumed.
- **Expected duration** is the profile learned estimate, so a
  cheap quick claim outranks a long grind of equal value.
- Dependencies and cooldowns gate before the score applies - a
  unit whose precondition is unmet (no empty truck slot, a drill
  ground still full) is not produced until the observation shows
  the precondition met, and a profile inside its cooldown does
  not refire.
- The score maps onto the queue priority classes of the queue
  design (1 expiry-critical, 2 windowed, 3 standard, 4
  background); ties break by deadline, then by age, exactly as
  the executor pick already does.

### The diff rules

After each pass, the observation is diffed against three
references - the regulars, the daily collection ledger, and the
pool in all three states.

- **Known item, triggered.** When a trigger from the list above
  fires for a profiled item, a unit of its regular is produced
  through the shared (regular, planned_for) invariant - already
  queued, claimed or done for that trigger window means no
  duplicate. When the same item is already queued and a later
  observation raises its deadline pressure, the queued unit is
  raised in priority instead of duplicated - priority 2
  normally, priority 1 inside the expiry band of the priority
  formula.
- **Known item, already done.** When the observation shows a
  modelled line already satisfied - collected, claimed, boarded -
  no unit is produced, and the observation stands as the day
  evidence for that ledger line.
- **Unknown item.** An item whose suggested_unit is `new` enters
  the discovery protocol of section 6 - it is filed as a
  candidate and gets its exploration unit from there, never an
  execution unit directly. No unknown item ages unnamed - rule
  R5 applies to it from its first day.
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

## 6. The new task discovery protocol

Comprehensiveness cannot rest on the checklist alone - the game
adds surfaces the checklist has never seen. Discovery is the
protocol that turns an unknown element into owned work, in four
steps.

### Discovery - where candidates come from

- **Roster matching.** Every scout traversal compares each
  label, icon and tab it meets against the known roster - the
  regulars index, the ledger lines, the traversal checklist
  itself and the candidate register below. Anything on screen
  that matches nothing is registered as a **candidate** in that
  pass observation, with its surface and the on-screen text
  transcribed exactly.
- **Announcement signals.** System mail and update notices are a
  discovery source in their own right, read as signals, not
  noise. The precedent is the Crystal Shop - the maintenance
  mail of 2026-10-21 announced the new Store tab days before any
  pass walked the Building section. A mail or notice that names
  a feature, tab, shop or activity no roster owns files a
  candidate the same day it is read, pointing at the surface the
  notice names.
- **Mail residue.** Unclaimed-reward mail from an unworked
  source - the Glittering Market Unclaimed mail is the standing
  case - is a discovery signal for its source, under the mail
  rule of section 2. The residue is claimed by the mail unit;
  the source still goes through this protocol.

### Filing - the provisional profile

A candidate is filed automatically, in the same session that
discovers it -

- A provisional metadata file under `_activities_`, in the
  candidate register the activities index keeps, carrying only
  what is known - discovery time, the surface it was seen on,
  the on-screen text transcribed, and every clue already in hand
  (the announcing mail, the residue mail, a ledger near-match).
- Its state, one of the state machine below, starting at
  `candidate`.

The state machine -

```text
candidate -> exploring -> active
                       -> rejected (reason recorded)
```

### Learning - exploration units

A candidate gets exploration units, ahead of any execution -

- The first exploration unit is read-only about the task
  itself - it enters by the discovered surface, and learns and
  records the entry point, the mechanism, the rewards, the
  cost, the cycle, the deadline shape, whether it scores
  anywhere, and the live read that would verify it.
- Where acting on the candidate would touch a price, diamonds,
  or any red line - or where the rules are still unclear after
  the read - exploration stays learn-only. The candidate is
  named in that day round summary for the owner, and no
  execution unit is produced until the mechanism is clear.
- A candidate that one exploration pass cannot resolve stays
  `exploring` and is re-perceived on the next pass - it does not
  age in silence (rule R5 applies from its first day).

### Promotion and scheduling

- When the mechanism is clear and the task sits inside the free
  and safe envelope - no price, no diamond spend, no red line -
  the profile is completed with its trigger conditions (section
  5) and the candidate turns `active`. From that moment the
  trigger-based scheduler produces its execution units like any
  profiled task, with no per-item owner approval - the owner
  approves the envelope, not each task inside it.
- A candidate that turns out priced, red-lined, owner-only or
  not a task at all is `rejected`, and its file and reason are
  kept - a rejected candidate is never rediscovered and
  re-explored from zero; a later observation that contradicts
  the rejection reopens it explicitly, with the contradiction
  recorded.
- Promotion is reported in the round summary of the day it
  happens - what was found, what it turned out to be, and the
  triggers it now schedules under.

## 7. Perception points in the day

Perception is a heartbeat, not an appointment. The two anchored
passes below are the guaranteed floor - the minimum perception a
day ever gets - and they are not the ceiling. A full pass also
fires whenever the layer detects a state change it cannot price
from partial views - a phase rotation boundary crossed, a reset
of any sub-cycle, an announcement mail read - and partitioned
perception rolls with every ticker heartbeat, each tick
re-perceiving the surface groups whose state is volatile or
whose last observation is stale, so a trigger rarely waits for
the next anchored pass to be seen.

- **Post-reset full pass** - the first pass of the reset day,
  staged at the trade-day reset (absolute 02:00 UTC, about 18:00 PST in winter, 19:00 PDT in summer). It walks the whole checklist.
  This is the pass that builds the day - everything the reset
  made available is observed before the day routine settles into
  its windows.
- **Midday pass** - one more full pass at the middle of the
  reset day, 07:00 local. It exists for state-dependent
  availability the morning cannot show - trains entering
  preparation, Arms Race phases rotated, markets refreshed,
  trucks returned.
- **Change-triggered full pass** - a full pass fired by a
  detected state change between the anchors, under the rule
  above. It walks the whole checklist like an anchored pass and
  lands in the same observation file, marked with its trigger.
- **Rolling partitioned perception** - between full passes, the
  surface-group chains of section 8 re-walk their groups on the
  ticker heartbeat - base and HUD every tick, events and store
  on rotation-sensitive ticks, alliance and mail with their own
  traffic. Their sections append to the same observation file,
  each stamped with its pass time, so the diff always works
  from the freshest read of each surface.
- **Handover to the zero sweep.** The pre-reset zero sweep
  (queue design section 12) walks the merged list - the daily
  collection ledger plus the day observed items - so anything
  perception found during the day is swept by the same standard
  as the modelled lines. An observed item still open at the final
  sweep gets its fix-up unit enqueued by the sweep, exactly like
  a ledger line not at zero.

## 8. Budget, chain splitting and the observation file

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
`_tools_/queue.py complete` like any unit. Its result must carry -

- `evidence` - the day observation file.
- `stats` - surfaces_walked, items_observed, red_dots_seen,
  red_dots_explained, unexplained_red_dots, unknown_items.
- `follow_up` - the units the diff enqueued or raised, or the
  unknowns awaiting their exploration unit, named - never a bare
  `none` while the pass holds an open signal.

## 9. Tool - _tools_/scout_diff.py (Phase 2, implemented)

Implemented 2026-11-01 as `_tools_/scout_diff.py` (standard library
only), to the design this section fixed in Phase 1. The tool is
the diff of section 5 as a program, so the step from observation
to queue stops depending on an executor remembering to do it.

**CLI usage**

```text
_tools_/scout_diff.py --observation FILE [--date YYYY-MM-DD]
                    [--out DIR] [--root POOL] [--repo DIR]
                    [--regulars FILE] [--ledger FILE]
                    [--now ISO] [--apply] [--format text|json]
```

- The observation is the day observation file, or any file in the
  same shape - a Markdown or YAML text carrying `observed_items`
  blocks (frontmatter, fenced or body blocks all count, because
  every pass of the day appends to one file) plus any
  `unmatched_labels` lists, or a JSON document with the same keys
  at any depth.
- Without `--apply` the tool is a dry run - it writes its three
  outputs and changes no pool. With `--apply` it writes the
  enqueue plan into the pool through `_tools_/queue.py enqueue`,
  one call per unit, so every unit it creates passes the same
  validation as a manual enqueue - the cap check, the chain
  homogeneity check, the file layout. `--apply` refuses to run
  unless the pool root is named explicitly with `--root`; pool
  reads for the dedupe checks and the learned estimates likewise
  happen only against a named root.
- Outputs land in `--out` (default - a `scout-diff-output` folder
  beside the observation file), named with the date - the enqueue
  plan as JSONL (one `queue.py enqueue` argument set per line,
  each entry carrying its action - enqueue, already-queued or
  raise - and its source items), the candidate filings, and the
  coverage report.
- `--now` pins the clock for the priority formula and the
  production windows; it exists for tests and replays. Production
  runs leave it unset.

**Inputs**

- The day observation file,
  `_records_/<date>/perception-scout/observation.md`, parsed for
  its observed items.
- The observation `unmatched_labels` list - every label the
  passes met that no roster entry owns (section 3), the raw
  material of discovery.
- The candidate register - the provisional profiles under
  `_activities_` and their states (section 6), so a candidate
  already filed is recognised, not rediscovered.
- `_tools_/regulars.json` - the profile library index, read for
  its trigger conditions and deadline shapes, not only its
  cadences - the planner evolution of section 5 consumes
  observations plus profile triggers, and this tool is that
  consumer in program form.
- The daily collection ledger - its lines and the regular that
  produces each.
- The pool itself, read through the queue tool list and stats
  functions - what is already queued, claimed or done.

**Outputs**

1. **The enqueue plan** - one entry per unit to create or raise,
   in the exact field shape `_tools_/queue.py enqueue` consumes -
   regular, activity, priority computed by the formula of
   section 5, expires_at from the item deadline, not_before,
   window text naming the observation and the trigger it came
   from, and a chain id `scout-followup-<date>` for exploration
   units. Known items map to their regular when one of their
   profile triggers fired.
2. **The unknown items list** - every observed item with no
   owning model, with its surface, label and state, formatted
   for the round summary naming rule R5 requires.
3. **The coverage report** - the perception scoreboard for the
   day - items observed, items queued, items already done, red
   dots seen, red dots explained, unexplained red dots, and the
   day `unmatched_labels` list printed in full - totalled and
   split by surface. Narrative observations also carry
   their per-pass red-dot accounting sections, reconciled
   section total against frontmatter counter in the same
   report, so a narrative-only day's dots are checked,
   not just carried. The unexplained count is the headline -
   the day perception is judged by it reaching zero.
4. **The candidate filings and exploration plan** - one entry
   per unmatched label not already in the candidate register -
   the provisional profile to file under `_activities_` (surface,
   transcribed text, clues in hand) and the exploration unit to
   enqueue for it at priority 2 under chain id
   `scout-discovery-<date>`. Candidates already exploring get
   their next exploration unit here instead of a duplicate
   filing; candidates whose exploration completed get their
   promotion or rejection recorded as a proposed metadata edit,
   never applied silently.

**Idempotency** - the tool obeys the pool invariant it feeds.
Produced units dedupe on (regular, planned_for) exactly as sync
and plan do. Dynamic units carry their source in their window
text and chain id, and the tool checks the pool for an existing
unit from the same observation item - same date, surface and
label - before enqueueing. A second run over the same
observation produces an empty enqueue plan and an unchanged
pool. The tool never completes, claims or deletes a unit - it
only proposes and, with `--enqueue`, enqueues.

**Priority support from the queue tool** - produced scout units
stage at priority 2, windowed work. The queue tool takes
production priority from its SYNC_PRIORITY table; the Phase 2
change landed `scout` and `scout-midday` there at priority 2,
with SYNC_EST_MINUTES seeds of 10 minutes each until the pool
learns better, instead of silently defaulting scout production
to priority 3. The tool reads its expected durations through
the queue tool learned estimates, so its priority formula and
the planner seeds never drift apart.

## 10. Learning and knowledge hardening

Discovery files a task; execution works it. Neither, alone,
makes the routine know the task - and the audit showed the cost
of shallow knowledge as plainly as the cost of missing tasks:
units repeated a wrong entry belief for days, because nothing
forced what was learned to be written down, checked and
hardened. Every task therefore carries a learning loop beside
its execution loop. The loop binds candidates in their
exploration stage and known tasks whose executions keep failing
alike - a repeated failure is treated as a knowledge defect
first and an execution defect second.

### In-game learning

An execution or exploration unit reads the task's own interface
in full - the rules and help text, the reward table, the costs,
the timers, the preconditions, and every sub-tab, not only the
screen the work itself touches. What can be tested safely is
tested, and the value is recorded as measured. What cannot be
tested is recorded as untested, never presented as known - the
distinction is part of the record, under constitution C4.

### Web research

The game is not the only source, and memory of the game is the
weakest one. For each task under hardening, the official
announcements, the wiki, mature guides and community sources
are checked, with at least two independent sources
cross-checked against each other. Where the sources disagree
with each other or with the in-game read, the in-game live read
wins, and the disagreement and the choice are written into the
profile with the sources and their dates - a later unit must be
able to see why the profile believes what it believes.

### Knowledge hardening - the profile and its proficiency

What is learned is written back into the task's `_activities_`
profile the same session, with the profile version raised -
entry point, mechanism, cost, rewards, cycle and deadline
shape, scoring rules, red lines, the live read that verifies
it, and the open questions still outstanding. The profile
carries a proficiency state -

- **proficient** - every key field (mechanism, cost, rewards,
  deadline shape) is supported by a measured in-game read or by
  two independent sources in agreement.
- **learning** - anything less. A profile in this state is a
  work order, not a reference: its execution units learn first
  and execute second, filling the missing fields before or
  while they work, and a unit that cannot close the gap says so
  instead of executing on a guess.

### The feedback loop

When an execution finds the profile wrong - a count, a
mechanism, a state the profile asserts - the profile is
corrected in the same session and its version raised. No second
unit may spend itself on a belief already known to be wrong.
This is the learning form of rule R2: the pivot is recorded
knowledge, not only a changed tap.

### Visual-grounding coordinate conversion (2026-11-11)

The visual grounding tool returns coordinates in the 0-1000
NORMALIZED range of the image it is given, not pixels. Convert
a grounding return to a tap point as: original pixel = crop
origin + (returned / 1000) * crop size / upscale, then
normalize to the 642x951 window. Do NOT divide a grounding
return by the upscale factor. The 2026-11-11 0117 harvest unit
made exactly that error on its first three taps: the food and
coin taps still collected (bubbles are large), but the iron tap
missed by about 48 in x and 45 in y in normalized units and
most likely hit the mine building instead of the bubble, and
its top-row disappearance without a HUD credit is recorded
unverified, not as a collection. The same error explains in
part the 2042 unit's iron no-credit tap. A tap that misses its
bubble by this error is a method failure, not a game mechanic -
the next unit re-grounds with the normalized conversion.
Recorded in resource-collection 1.58.0.

### The exploration closing standard

Under this protocol, an exploration unit for a candidate does
not close on "the surface was visited". It closes when the
profile fields are filled far enough to decide - the candidate
can be completed as a profile and turned active, or it is
explicitly rejected with the reason kept (section 6). A pass
that ends with the fields still open ends as partial with the
missing fields named, and the candidate stays in exploring.

### First retrospective hardening target - radar-tasks

The first profile named for retrospective hardening under this
protocol is radar-tasks. Its failure history in the audited
days is specific: on a stack day a radar unit never entered the
radar screen at all (the rotating base entry icon pointed at
the wrong target and the pass closed without the screen); on
the release day the map pins - the subtask rule R7 now protects
- went untapped while claims were worked; and the special pin
tasks that Quick Execute does not cover were left without a
closing read. The hardening goal is a complete radar profile:
the task types and their refresh, the exact coverage of Quick
Execute and its exceptions, the handling of each pin task type,
the stack and release scoring rules, and the inventory cap
management that keeps stored tasks refreshing. The completion
standard is not this document's say-so - later execution units
verify the profile field by field against the game, under the
feedback loop above, and the profile rises to proficient only
when the key fields carry measured or dual-source support.

Execution results under this protocol are also the data of the
retro review mechanism (task unit queue design, section 14) -
what units measured, gained and were blocked by is aggregated
there, and its execution-knowledge actions land back here as
profile hardening. The aggregation tool of that mechanism,
`_tools_/retro_report.py`, is implemented (2026-11-01) to the
section 14 specification and writes its metrics appendix into
`_records_/retro/`.

## 11. Phased roadmap

- **Phase 1 - this document and the modelling (landed with this
  change).** This design, the perception layer section of the
  task unit queue design, the observed items schema, the
  traversal checklist, and the scout regulars in
  `_tools_/regulars.json` with their activity metadata. Scout
  passes run as executor-produced chains under the existing
  planner; the diff of section 5 is applied by the executor
  from the observation file, by hand, under the rules above.
  Version 1.1.0 of this design, landed the same day under the
  owner refinement, re-based the layer on trigger-based
  scheduling - profiles instead of timetable entries, the
  trigger list and priority formula of section 5, the discovery
  protocol of section 6, and the anchored passes demoted to a
  guaranteed floor under rolling and change-triggered
  perception. The executor applies those rules by hand in this
  phase exactly as it applies the diff.
- **Phase 2 - the diff tool and the planner hookup
  (implemented 2026-11-01).** `_tools_/scout_diff.py` is
  implemented to the design of section 9 - dry run by default,
  `--apply` only against an explicitly named pool root - and
  the queue tool priority entries for the scout regulars are
  landed (SYNC_PRIORITY and SYNC_EST_MINUTES in
  `_tools_/queue.py`). The tool was validated on a scratch pool
  against a synthetic observation covering a known actionable
  item, known items blocked by state and by red line, an unknown
  candidate and unmatched labels - classification, the priority
  formula, apply and rerun idempotency (second run zero new)
  all asserted. What remains of this phase is operational, not
  design: the planner pass runs the tool after each scout chain
  completes, so dynamic units land in the pool without waiting
  for an executor to transcribe them; wiring that invocation
  into the scheduled planner's instructions is an operations
  step outside this document. This is also where the planner
  changes species - from staging units by time slot to
  consuming observations plus profile trigger conditions and
  producing units when triggers fire, with the slot staging
  kept only as the floor check of section 5. Version 1.2.0 of
  this design, landed the same day, adds the learning and
  knowledge hardening protocol of section 10.
- **Phase 3 - reporting and promotion automated.** The coverage
  report, unmatched labels included, joins the round summary as
  a standing section, the unknown items naming becomes
  automatic, candidate filings and exploration units are
  produced by the tool from the unmatched labels, and the
  promotion of a proven candidate into an active profile is
  proposed by the tool from its exploration record - free and
  safe promotions land under the envelope of section 6, the
  rest still come to the owner with the evidence.

## 12. Standing rules this layer inherits

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
- The discovery duty - an unmatched label met by any unit, scout
  or executor, is filed as a candidate in the same session under
  section 6. Seeing a new surface and walking past it is the
  failure this layer exists to end.
- The retro duty - every unit, scout or executor, closes with
  the measurement stats the retro review mechanism aggregates
  (task unit queue design, section 14). Perception that is not
  measured cannot be reviewed, and what cannot be reviewed
  repeats.
