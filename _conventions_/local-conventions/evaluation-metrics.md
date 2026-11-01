---
title: Evaluation Metrics
version: 1.1.0
status: active
created: 2026-10-31
description: How the play system measures itself - execution efficiency per task type, perception completeness and discovery generalisation, retro effectiveness, and the measured impact of the tool developer and the knowledge organiser
---

# Evaluation metrics

Owner direction, 2026-10-31 - the system that plays the account
must be able to measure its own progress, not only the account's.
Section 14 of the [task unit queue design](task-unit-queue-design.md)
measures the work - what each unit reached. This specification
measures the system that does the work - whether execution is
getting faster and richer per task type, whether perception sees
everything and recognises what it has never seen, whether the
retro proposes improvements that actually close and stay closed,
and how much the tool developer and the knowledge organiser each
improve the step or the system they touch.

Three standing rules govern every metric below.

- **A metric names its source.** Every figure is computed from a
  named repository file and field. A figure that cannot be
  computed from repository data is emitted as a data-gap entry
  with its reason - never estimated, never silently dropped.
- **Association is not causation.** Before-and-after comparisons
  around a tool landing or a profile fix are reported as
  associated movement, with the confounders named. The game
  changes, the duel posture changes, the owner plays by hand;
  none of that is the system's doing, in either direction.
- **Thresholds are alarms, not targets.** A threshold breach is
  named so a human-grade judgement can look at it. Optimising a
  metric against its own threshold (closing improvements
  cheaply, splitting units to flatter durations) is a defect the
  retro itself must call out when it sees it.

Cadence shorthand - **daily** means the daily retro computes it
for its rolling 7 day window and the day just ended; **weekly**
means the first retro of a week additionally compares the window
against the previous week's, from the dated data files, which
are the immutable series these trends read.

## A. Execution efficiency, per task type

Per regular, per day and rolling 7 days. Source - the unit
results in `_queue_/done` (fields `result.status`,
`result.duration_seconds`, `result.attempts`,
`result.stats.target`, `result.stats.achieved`,
`result.stats.resources_gained`, `result.stats.points`,
`result.stats.costs`, `result.stats.verified`,
`result.stats.blocker_category`), read through the canonical
appendix `_records_/retro/<date>-data.json` - the per-regular
`rolling` and `by_day` summaries under `regulars.<regular>`.

- **Duration median and p90** - median and 90th percentile of
  `duration_seconds` over the window's executions. Median is
  computed today (`duration_median_seconds`); p90 is not yet
  emitted and joins with the tool extension filed below.
- **Attempts** - mean and maximum of `result.attempts`, and the
  share of executions that needed more than one attempt. The
  field exists in every result; the aggregation does not read
  it yet - same tool extension.
- **Done rate** - done over executions, from `statuses`.
- **Target attainment** - `attainment_summed` (summed achieved
  over summed target) and `attainment_mean_ratio`, over the
  units that carried both keys (`attainment_units` is the
  denominator and is always reported beside the ratio).
- **Resource yield** - `resources_gained` itemised by resource,
  per execution and per minute (`resources_per_minute`). Free
  text that does not parse is counted in
  `resources_unparsed_count`, never dropped silently.
- **Points per minute** - `points_per_minute`, for the scoring
  types that report `points`.
- **Unverified rate** - `unverified` over executions, with
  `unverified_reasons` split (verified not yes, missing
  required stats, missing result) and `missing_key_counts`
  naming which keys the pool is failing to produce.

Thresholds - no universal attainment line; attainment is read
per type against its own history. For the quota types with a
hard daily target (trucks, donations) a rolling attainment
under 0.8 is named. The unverified rate is thresholded under
Monitoring below.

Known defects - units executed before the section 14 stats
specification landed (2026-11-01) are legacy-shaped and count
as unverified almost by definition; early windows are dominated
by them, so every unverified figure is read together with the
legacy share of its window. Attainment is undefined for types
whose units carry no numeric target; those types report
attainment_units 0 and are judged on done rate and yield.

## B. Perception completeness

Per perception day. Sources - the day observation file
`_records_/<date>/perception-scout/observation.md`, the scout
diff coverage output `scout-coverage-<date>.md` (and its JSON
form) written beside it, the zero sweep records under
`_records_/<date>/daily-activities/`, and the 23 lines of the
[daily collection ledger](daily-collection-ledger.md).

- **Ledger coverage** - ledger lines closed on a live read that
  day, over 23. A line closed as explicitly unverified under
  the ledger standard counts as read; a line never walked
  counts as not covered. The two pre-reset sweeps are the
  primary walk; scout and producing-unit reads close lines the
  same way when they carry the closing read.
- **Unexplained red dots** - `unexplained_red_dots` from the
  coverage report. The completeness standard of the perception
  design (its section 3) already fixes the target - zero, every
  day, no exceptions averaged away.
- **Conversion** - observed to actionable to enqueued:
  `actionable_items` over `items_observed`, and (`to_enqueue`
  plus `already_queued` plus `raises`) over `actionable_items`.
  `already_satisfied` and `not_actionable` are reported with
  their reasons so a falling conversion is diagnosable - a drop
  caused by more items being read as already satisfied is
  health, a drop caused by red-line blocks is information, a
  drop with neither is a diff defect.
- **Perception latency** - for each enqueued unit, its
  `created_at` in the pool minus the time of the observation
  pass that saw its item. Reported as median and maximum per
  day where both timestamps exist.

Known defects - observed items carry no per-item timestamp; the
observation file is appended pass by pass, so latency is
computable at pass granularity only. Where a pass time cannot be
recovered, latency for that day is a data-gap, not a zero. Until
the scout diff auto-invocation lands (loop review open link 1),
conversion measures a hand-run tool and must be read as such.

## C. Generalisation and discovery

Per week, with daily counts kept. Sources - the candidate
register the activities index keeps and the `status` field of
each `_activities_/<slug>/INDEX.md` (the state machine of the
perception design section 6: candidate, exploring, active,
rejected), the coverage report fields `candidates_filed`,
`candidates_registered` and `unknown_items`, and the exploration
units in the pool under chain id `scout-discovery-<date>`.

- **New types discovered** - profiles reaching `active` in the
  period that began as candidates, counted separately from
  owner-named types (an owner-named type is intake, not
  discovery, and the two are never merged into one count).
- **Candidates filed** - new candidate profiles per period,
  from the coverage reports and the register.
- **Conversion and dwell** - candidate to exploring to active
  conversion rate, and the median days a candidate spends in
  each state, from profile created and modified dates and the
  first exploration unit's `created_at`.
- **Unmatched labels trend** - the day `unmatched_labels` count
  from each coverage report, as a series. A healthy system
  trends this down as the roster learns the game; a spike is
  either a game update or a perception regression, and the
  retro says which it believes and why.
- **False discoveries** - candidates rejected with the reason
  that the element is not a task at all. Rejections for priced,
  red-lined or owner-only elements are correct filtering and
  are counted separately - the false discovery rate is
  not-a-task rejections over all candidates filed.

Thresholds - none hard in the first weeks; discovery is new and
a quota would reward filing noise. A median candidate dwell
over 3 days in `exploring` is a watch item, named at the weekly
comparison.

Known defects - state dwell depends on profile `modified`
timestamps, which also move for unrelated edits; dwell is an
approximation and is labelled as one until the register carries
explicit state-change dates.

## D. Retro effectiveness

Per retro and rolling. Sources - the retro's own execution
records at `_records_/<date>/retro-review/` are the
authoritative source for the run itself (that it ran, when,
what it filed), under the
[ops execution records](ops-execution-records.md) standard;
the improvements backlog `_records_/retro/improvements.md`,
one entry per improvement task carrying its id, its class
(execution-knowledge, meta-knowledge, tooling,
knowledge-organization), the leak it addresses, its target
metric with the value at filing, its verification method, its
opened date, its status and its closing date, is the source
for entry state. Commit and PR traces are cross-check only,
never the source. The backlog file is created by the first
retro that files into it; entry-state metrics are data-gaps
until it exists, while run metrics read from the execution
records from 2026-10-31 onward (period 0 reconstructed).

- **Critical improvements proposed** - entries filed per retro,
  split by class. Critical means the entry addresses a named
  top leak of its retro; the retro marks them, the count is not
  inferred later.
- **Filing rate** - of the top leaks a retro names, the share
  that became backlog entries. A leak named twice with no entry
  is a filing failure and is itself named.
- **Closure rate and dwell** - entries closed over entries
  opened, per week, and the median days from opened to closed.
  Closure keeps the standing rule - the target metric moved, or
  the stated verification passed; an edit alone never closes.
- **Recurrence rate** - the core quality metric of this family.
  Of the improvements closed in a period, the share whose root
  cause class (the miss audit classes a to i, carried in the
  entry and in unit `blocker_category`) reappears in the done
  pool within 7 days of closure. A closed improvement whose
  problem comes back was a paper fix, and this metric is how
  the system knows.
- **Open roll-forward** - entries still open at each retro,
  counted and aged; the oldest open age feeds family G.

Thresholds - any recurrence is named (target zero). Closure
dwell has no threshold yet; two weeks of baseline come first.

Known defects - recurrence reads `blocker_category`, which
depends on executors filling it - family A's enforcement gap is
this family's data risk, and the queue tool validation filed in
the tool-developer backlog is the fix both families wait on.

## E. Tool developer impact

Per tool landing, rolled up weekly. Sources - the tool
developer's execution records at
`_records_/<date>/tool-development/` are authoritative for
deliveries, validation and timing, under the
[ops execution records](ops-execution-records.md) standard;
the tooling entries of the improvements backlog carry the
filed dates and target metrics; the target metric series
lives in the dated retro data files. The git history of
`tools/` is cross-check only - a landing with no execution
record is treated as not proven to have happened.

- **Tools delivered** - tooling entries reaching implemented
  per period, and the median days from filed to implemented.
- **Target metric movement** - every tooling entry must name,
  at filing time, the one metric it exists to move (from any
  family in this specification) and its value at filing. Impact
  is the metric's 7 day window before the landing commit
  against the 7 day window after it, reported as the pair of
  values with the landing date between them - never as a single
  improvement percentage with the windows hidden. Standing
  examples - the unverified rate (family A) around the queue
  tool stats validation; the perception conversion rate
  (family B) around the scout diff auto-invocation; the p90 and
  attempts availability itself around the extension filed
  below.
- **No-target landings** - a tool that lands with no target
  metric named at filing is counted here, by name. It may still
  be worth building; it is not allowed to claim impact.

Known defects - windows are small and the game is not a
laboratory; duel posture, event calendars and the owner's own
play all move the same metrics. The before and after pair is
evidence for the retro's judgement, not a proof, and is written
that way in the retro file.

## F. Knowledge organiser impact

Per organiser run, rolled up weekly. Sources - the
organiser's execution records at
`_records_/<date>/knowledge-organization/` are authoritative
for the run counts (profiles updated, contradictions
resolved, stale items marked, carried in the record stats),
under the
[ops execution records](ops-execution-records.md) standard;
the frontmatter of `_activities_/*/INDEX.md` (`version`,
`modified`, `proficiency`), and the execution records that
name a profile error. The pre-standard note series at
`_records_/knowledge-organizer/` is history and cross-check,
not a source.

- **Consolidation volume** - profiles updated per run,
  contradictions resolved per run, stale markings per run,
  straight from the organiser note.
- **Proficiency distribution** - profiles at `proficient` over
  profiles at `learning` (and any at candidate or exploring,
  counted in family C instead), over all profiles that carry
  the field.
- **Stale-profile blockers** - executions whose record names the
  profile as the problem - a stale tap point, a wrong mechanism,
  a superseded rule - counted from the records' own words, per
  week. The trend is the metric: as consolidation works, the
  game should stop being lost to the files.

Thresholds - none numeric yet. A week in which stale-profile
blockers rise while consolidation volume also rises is named -
it means the organiser is writing, but not where it matters.

Known defects - only the radar-tasks profile carries an
explicit `proficiency` field today; the distribution is a
data-gap until the organiser backfills the field across
profiles, which is an organiser backlog item this specification
files by reference. Stale-profile attribution is conservative
by design - only records that explicitly name the profile count
- so the metric understates, and says so.

## G. Loop health

Daily snapshot at the retro, from the records the loop itself
leaves. Sources - the queue run records under `_records_/<date>/`,
the ops execution records of the loop activities under the
[ops execution records](ops-execution-records.md) standard,
the retro files under `_records_/retro/`, the improvements
backlog, and the pool itself through `tools/queue.py stats`
and the unit frontmatter. The git log is cross-check only.

- **Standing job run rate** - for each standing job, runs that
  left their execution record over runs expected: ticker passes
  (queue run records against the 30 minute cadence), planner
  cycles (units produced and the planner log - the one job
  still proxied, below), the daily retro (its dated file and
  its execution record), the organiser and the tool developer
  and the PR integrator (their execution records, no-op runs
  included - a recorded no-op is a run, an absent record is a
  miss). Each job's rate is reported separately; an average
  across jobs would hide exactly the failure this family
  exists to see.
- **Backlog depth and oldest open age** - open entries in the
  improvements backlog, and the age in days of the oldest.
- **Queue depth and oldest unit age** - units waiting in inbox
  and claimed at snapshot time, and the age of the oldest
  waiting unit from its `created_at`, with any unit past its
  `expires_at` still unexecuted counted and named. These two
  are the capacity metrics the 2026-10-31 loop review found
  missing (its open link 4); the snapshot is persisted into the
  retro data output so the series is historical, not a number
  that evaporates when the pool drains.

Thresholds - the oldest open backlog entry over 7 days is
named. Any expired-but-unexecuted unit is named. A daily job
(retro, organiser) missing its artifact on any day is named the
next day; the ticker shortfall is named when a day's passes fall
under 90 percent of the cadence expectation.

Known defects - the planner's own log lives outside the
repository (in the goal workspace), so its run rate is proxied
by produced units until the log is mirrored in as execution
records - the migration item the ops standard names. The
retro's own run rate has the one-day blind spot the loop
review accepted - a retro that never ran leaves neither file
nor record, and is only visible to the next one. Device
locks and maintenance distort the ticker expectation; the retro
annotates known distortions rather than treating the raw rate
as a verdict.

## Monitoring

- **Daily** - the daily retro computes the core set: family A
  rolling and by-day, family B for the perception day, family D
  snapshot and recurrence check, family G snapshot. The figures
  land in the day's data appendix and the headline movements in
  the retro file's dashboard - top leak, the metric that moved
  most, every threshold breach by name.
- **Weekly** - the first retro of a week compares the window
  against the previous week's data files for every family,
  including the slow ones (C, E, F), and files improvement
  entries for what the comparison shows.
- **Naming** - a threshold breach is named in the retro's Slack
  summary and in the chat report of that retro, by metric and
  value, the same day it is computed. A metric that goes
  data-gap for two consecutive computations is also named -
  silence about a blind metric is how the loop lost whole task
  lines before this specification existed.

First threshold set (each may be revised by a retro, with the
reason written into that retro file):

- unexplained red dots over 0 on any perception day;
- recurrence of any closed improvement's root cause within 7
  days of its closure;
- the unverified rate of post-specification units failing to
  fall week over week, or standing over 20 percent after the
  first full week of post-specification execution;
- oldest open backlog entry over 7 days old;
- any unit expired and unexecuted, or a daily standing job's
  artifact missing;
- ledger coverage under 23 of 23 lines read on a sweep day.

## Tool route

The computation extends `tools/retro_report.py`; it does not
become a second tool. Reasons - the families that read the done
pool (A, the recurrence half of D, the series E reads) must
share one scan and one unit-date attribution with the retro
aggregation, or the system gets two truths about the same units;
the output contract already exists - one canonical appendix per
window end at `_records_/retro/<date>-data.json` with its
Markdown rendering, its derived-from hash and its
byte-identical re-run - and these metrics ride it as an
additional top-level `system_metrics` object, versioned by the
tool's own version field; and the daily retro already runs the
tool, so no new scheduled step appears. The families that read
outside the pool (B from coverage reports, C from the candidate
register, F from profiles and organiser notes, G from a pool
snapshot) are separate input readers inside the same tool, each
emitting its section or its data-gap independently - a missing
coverage report degrades family B, never the run.

Filed into the tool-developer backlog, in the backlog's own
terms:

> IMP tooling - extend tools/retro_report.py with the system
> evaluation metrics of
> _conventions_/local-conventions/evaluation-metrics.md. Add a
> top-level system_metrics object to
> _records_/retro/<date>-data.json and its Markdown rendering,
> covering families A to G as specified there - the done pool
> aggregates (adding the attempts distribution and the duration
> p90 to family A in the same change), the scout coverage
> reports, the candidate register in _activities_, the
> improvements backlog, the ops execution records of the loop
> activities, and a pool snapshot for queue depth and oldest
> unit age. Target metric - the
> share of the specification's metrics emitted as figures
> rather than data-gaps in the daily appendix, from its current
> value (family A only, partially) toward the full set.
> Every metric that cannot be computed from repository data is
> emitted as a data-gap entry with its reason, never estimated.
> Re-running over unchanged inputs stays byte-identical.
> Validated on a fixture pool and scratch records in /tmp
> against hand-computed figures before it writes the live
> series.

The queue tool's stats validation (the standing tooling backlog
item the loop review calls item b) stays a separate entry -
several metrics above read fields that only its enforcement
makes trustworthy, and the retro names that dependency rather
than merging the two jobs into one unmeasurable lump.

## Changelog

- 1.1.0, 2026-11-01 - families D to G re-sourced onto the ops
  execution records of the
  [ops execution records](ops-execution-records.md) standard:
  the retro's, tool developer's, organiser's and integrator's
  own runs are now measured from their structured execution
  records under `_records_/<date>/<ops-activity>/`, and commit
  and PR traces are demoted to cross-check only. The
  data-gap statements move accordingly - run metrics exist
  from 2026-10-31 (period 0 reconstructed), entry-state
  metrics still wait on the improvements backlog, and the
  planner remains proxied until its log migrates in. The
  tool-route backlog text is aligned (ops execution records
  among its readers).
- 1.0.0, 2026-10-31 - first version, under the owner direction
  of 2026-10-31 to create evaluation metrics for the system
  itself and monitor them - seven families (execution
  efficiency, perception completeness, generalisation and
  discovery, retro effectiveness, tool developer impact,
  knowledge organiser impact, loop health), the monitoring
  cadence and first threshold set, and the tool route extending
  tools/retro_report.py, filed into the tool-developer backlog.
