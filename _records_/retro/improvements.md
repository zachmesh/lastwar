---
title: Improvements backlog
created: 2026-11-01T05:42:09Z
modified: 2026-11-01T07:58:31Z
version: 1.1.1
description: The standing backlog of improvement tasks for the play system - filed by retros and by owner instruction, worked by the tool developer and the knowledge organizer, closed by the retro only when the target metric moves or the stated verification passes
status: active
grounded_in:
  - source: task unit queue design section 14 - the retro review mechanism and its closure rule
  - source: evaluation metrics in _conventions_ local-conventions - the metric families each target metric belongs to
  - source: owner instruction of 2026-10-31 - add or modify steps so every open item has a closed loop
---

# Improvements backlog

The register of improvement tasks for the improvement loop.
Every entry carries the leak it addresses, one target metric
with its current value, and the verification that closes it.
An entry is the unit of work between retros - the retro files
and closes entries, the hourly tool developer and knowledge
organizer work them, and the integrator's merges move tooling
entries to implemented.

## Entry fields

- id - IMP-<YYYYMMDD>-<n>, assigned at filing, never reused.
- source - the retro date that filed it, or the owner
  instruction it serves.
- class - execution-knowledge, meta-knowledge, tooling or
  knowledge-organization.
- leak - the observed loss or gap, with its evidence.
- target metric and current value - one metric from the
  evaluation metrics families, with the value read at filing.
- verification - the check a later retro runs to close it.
- status - open, in-progress, implemented or closed.

## Maintenance rules

- The daily retro updates statuses every run and is the only
  role that closes an entry. An entry closes only when its
  target metric actually moved, or its stated verification
  passes. Merged code or an edited document alone never
  closes an entry.
- The fixer roles (tool developer, knowledge organizer, and
  this retro's own write-backs) may move an entry to
  implemented with the commit or PR that carries the fix -
  never to closed.
- A closed entry whose root cause recurs within 7 days is
  reopened by the retro and counted in the recurrence metric
  of evaluation metrics family D.
- New entries are inserted in leak-size order within their
  status group - the largest leak first - so the top of the
  open list is always the next thing to work on.
- Owner-decision items are not improvement entries. They live
  in the companion register `owner-decisions.md` in this
  folder and are maintained by the retro alongside this file.

## Open

### IMP-20261031-04 - result stats validation on unit completion

- source: owner instruction of 2026-10-31 (standing tool queue)
- class: tooling
- leak: unit closings can omit the required result.stats
  fields and still complete, so the retro can only count the
  damage after the fact - closings that lack same-unit
  verified numbers were the largest single data-quality leak
  of the 2026-10-31 audit window.
- target metric: unverified rate of units closed under the
  new rules (evaluation metrics family A). Current value -
  pre-rule baseline only: 428 of 428 units in the 2026-10-31
  retro window count as unverified, because the field rule
  dates from 2026-10-31; no post-rule value exists yet.
- verification: queue.py complete warns or flags a closing
  whose required stats keys are missing, demonstrated on an
  isolated fixture pool; the retro then reads the post-rule
  unverified rate falling week over week.
- status: implemented - PR 11 (squash merge 8f3e8053, 2026-11-01; branch work/queue-complete-stats-validation, commit 1b2dd38d252fca74eaa20ef49c4187607675b2d1), warning in queue.py complete; fixture validation 9/9 plus retro cross-check passed on an isolated scratch pool.

### IMP-20261031-09 - queue aging boost against starvation

- source: loop review of 2026-10-31 (open link 4)
- class: tooling
- leak: queue.py next picks by expires_at, then priority,
  then age as tiebreak only, so a no-expiry low-priority
  chained unit can starve indefinitely behind expiring work.
  Precedent - the 2026-10-30 zombie chain successor was
  crowded out for five beats by expiring units.
- target metric: oldest unit age in the pool (evaluation
  metrics family G). Current value - not yet snapshotted;
  family G defines the metric and the first value lands with
  the next retro data appendix.
- verification: an aging rule in queue.py raises a waiting
  unit's effective priority with wait time, demonstrated on
  an isolated fixture pool replaying the 2026-10-30
  starvation pattern without starving the chain.
- status: implemented - PR 23 (branch work/queue-aging-boost, commit e30a588b74fb9f5e48ca4f222ece820abd3f8a7c), effective priority plus 1 per 2 hours waited floored at 1 and a 2 hour soft deadline for no-expiry units in queue.py pick_key; fixture validation passed on isolated scratch pools including a starvation replay first picking the chain at beat 3 (90 minutes)

### IMP-20261031-03 - retro report extensions, p90, attempts, system metrics

- source: owner instruction of 2026-10-31 (evaluation metrics)
- class: tooling
- leak: retro_report.py aggregates medians but not p90
  durations or attempt counts, and emits no system_metrics
  object, so parts of evaluation metrics families A and G
  stay data-gap even though the underlying unit results
  carry the raw values.
- target metric: data-gap share of families A and G
  (evaluation metrics). Current value - the 2026-10-31 data
  appendix carries no p90 and no attempts fields; those
  metric rows read data-gap.
- verification: a regenerated appendix on an isolated
  fixture pool shows p90 and attempts values that match hand
  calculation, byte-identical on re-run, and a system_metrics
  object the retro file can cite.
- status: open


### IMP-20261101-01 - reconcile activity verification and metadata coverage

- source: owner instruction of 2026-11-01 to retire the standalone task list; legacy open items 2 and 5, preserved in the task intake workflow migration table.
- class: knowledge-organization
- leak: verification of every activity against this account and backfilling the entry, cadence, scope and availability sections were two overlapping legacy obligations with no reconciled coverage ledger.
- target metric and current value: profile coverage (evaluation metrics family F). Current inventory is 32 activity profiles; the legacy obligations have no complete profile-by-profile verification map, so verified coverage is a data gap rather than assumed zero.
- verification: the knowledge organizer audits all current activity profiles, links each required section to existing dated evidence or an explicitly unverified gap, and routes missing game observations into bounded execution work. New profiles enter the same audit. Reuse existing profile-hardening entries instead of duplicating them.
- status: open

### IMP-20261101-02 - document the account's three squads

- source: legacy open item 3, retained by the owner-directed task-list retirement.
- class: execution-knowledge
- leak: the heroes-and-squads article still says the owned roster has not been recorded; generic team recommendations do not establish this account's three formations.
- target metric and current value: squad evidence coverage, an explicit acceptance measure for this one-off investigation. Current value is unverified for all three complete formations, not a claim that no hero observations exist elsewhere.
- verification: bounded game observations record all three squads' heroes, levels, stars where shown, gear and troop types, with dated evidence and unknown fields marked. The knowledge organizer reconciles the evidence into `_knowledge_/heroes-and-squads/`. No resource spending or squad changes are authorized by this item.
- status: open

### IMP-20261101-03 - verify device-switch behavior on both devices

- source: legacy open item 4, retained by the owner-directed task-list retirement.
- class: execution-knowledge
- leak: the account-and-platforms article records the Mac-side takeover but explicitly leaves the iPhone-side outcome unobserved.
- target metric and current value: device-switch evidence coverage. Mac takeover is observed; the corresponding iPhone behavior and safe switch sequence remain unverified.
- verification: an owner-coordinated observation records what both devices display during a switch and writes the supported sequence into `_knowledge_/account-and-platforms/`, preserving the old observation as dated evidence. Until then the conservative existing device-switch rule remains in force; no disruptive test is performed merely because this backlog item exists.
- status: open

### IMP-20261101-04 - reconcile HUD labels and resource definitions

- source: legacy open item 6, retained by the owner-directed task-list retirement.
- class: execution-knowledge
- leak: headquarters-and-resources still leaves the six-figure 2026-10-25 HUD mapping unverified, while `_tools_/resources.json` already contains some named resource definitions. The two sources have not been explicitly reconciled.
- target metric and current value: resource-label verification coverage. The six-figure historical mapping remains unverified in the knowledge article; current resource definitions are partial inputs, not proof of that old screen.
- verification: read the HUD labels and relevant detail panels in a bounded observation, link each supported mapping to dated evidence, and reconcile the article with `_tools_/resources.json`. If the historical screen cannot be reconstructed, retain its mapping as unverified and add a separately dated current mapping rather than assigning old figures by inference.
- status: open

### IMP-20261101-05 - reconcile the remaining guide-claim checks

- source: legacy open item 7, retained by the owner-directed task-list retirement.
- class: execution-knowledge
- leak: the counter triangle, HQ 31 requirements and radar storage-cap behavior were named for live spot-checking, but the old task list never linked the three claims to verified completion evidence.
- target metric and current value: claim verification coverage across those three checks. The first two knowledge articles remain unverified; radar has later observations and the existing IMP-20261031-05 follow-up, which must be reviewed before any new test is created.
- verification: the knowledge organizer first reuses existing evidence, including radar profile/playbook findings and IMP-20261031-05. Remaining gaps get bounded, non-spending observation units. Each claim ends with a dated supported statement, a corrected statement, or an explicit unresolved limitation in its canonical article; this item does not authorize spending or changing the account to create a test.
- status: open

## In progress

### IMP-20261031-10 - ops execution records standard landed

- source: owner instruction of 2026-10-31 (executions, not sessions)
- class: meta-knowledge
- leak: the loop's own activities - retro, tool development,
  knowledge organization, PR integration, planning - left no
  structured execution records in the repo, so evaluation
  metrics families D to G had to infer their runs from
  commits and PR traces or read data-gap.
- target metric: data-gap share of families D to G
  (evaluation metrics). Current value - baseline execution
  records exist for 2026-10-31 only, reconstructed and
  labelled as such; no live-written records exist yet.
- verification: PR number 2 (branch work/ops-execution-records)
  reviewed and merged by the integrator, and the next runs of
  the standing jobs each leave a live execution record under
  _records_ in the standard's shape.
- status: in-progress

## Implemented, awaiting retro verification

### IMP-20261031-01 - perception to queue auto-wiring

- source: owner instruction of 2026-10-31, approved in chat
- class: tooling
- leak: scout_diff.py existed and was validated, but nothing
  ran it after scout units produced an observation, so the
  perception-to-queue link worked only when an operator ran
  the tool by hand - open link 1 of the loop review.
- target metric: observed to enqueued conversion rate
  (evaluation metrics family B). Current value - not yet
  measured; no planner execution record carrying diff counts
  exists yet.
- verification: planner execution records under
  _records_/queue-planning show scout_diff counts (observed,
  actionable, enqueued) for the current trade day.
- status: implemented - the planner job body gained the
  perception consumption step and the queue cleanup step on
  2026-10-31, and its cadence moved to hourly at the owner's
  direction the same day.

### IMP-20261031-02 - retro report tool

- source: owner instruction of 2026-10-31 (retro mechanism)
- class: tooling
- leak: the daily retro's 7 day aggregation had no tool, so
  the first retro would have been aggregated by hand - slow,
  error-prone, and not repeatable byte for byte.
- target metric: retro aggregation produced by
  _tools_/retro_report.py from _queue_/done (evaluation
  metrics family A inputs). Current value - the tool is live
  and produced the 2026-10-31 appendix from 428 done units
  with zero parse errors.
- verification: fixture validation passed before landing
  (hand-checked aggregates, idempotent re-runs) in commit
  ee6544a; the retro cites the tool's appendix as its data
  source.
- status: implemented - commit ee6544a, pushed and verified.

### IMP-20261031-05 - radar tasks knowledge hardening

- source: owner instruction of 2026-10-31 (learning protocol)
- class: knowledge-organization
- leak: the radar profile was too thin to execute against -
  repeated entry failures (the rotating shortcut opening the
  Secret Command Post), unworked map pins on release days,
  and a stack day closing at 21 of 40 stored with tasks left
  undone, all traced to missing mechanism knowledge rather
  than game difficulty.
- target metric: radar profile proficiency (evaluation
  metrics family F). Current value - profile at version
  1.6.0, proficiency still learning; the fields below remain
  unmeasured in game.
- verification: the profile carries entry verification, the
  Quick Execute coverage and exception list, the pin
  taxonomy and handling, and checkable stack and release
  completion standards - landed in commit 9eae833.
- follow_up: three field tests still owed, to be verified by
  later execution units one by one before the retro closes
  this entry - the duel points delta test (read score, claim
  a batch, read again on a release day); the bottom-bar offer
  selection rule (when the bar shows Claim All instead of
  Quick Execute); the categories and costs of the
  unidentified arrow and axe map pins.
- status: implemented - profile 1.6.0, commit 9eae833.

### IMP-20261031-06 - pre-reset zero sweep production automated

- source: owner instruction of 2026-10-31 (loop completion)
- class: meta-knowledge
- leak: the 17:30 and 18:30 pre-reset zero sweeps were
  produced by hand every reset day because the planner could
  not express fixed time slots - the 2026-11-02 pair was
  hand-enqueued again on 2026-10-31 (chain
  pre-reset-sweep-2026-11-02).
- target metric: sweep pairs staged by the planner rather
  than by hand (loop health, evaluation metrics family G).
  Current value - zero planner-staged pairs so far; the
  standing pairs in the pool are hand-enqueued.
- verification: a planner execution record shows the sweep
  chain staged by the planner, and the next reset day's two
  sweep units are in the pool without any hand enqueue.
- status: implemented - the planner job body gained a sweep
  production step on 2026-10-31.

### IMP-20261031-07 - planner run records moved into the repo

- source: owner instruction of 2026-10-31 (executions, not sessions)
- class: meta-knowledge
- leak: the planner's run log lived outside the repo in the
  goal workspace hidden files, so the repo could not prove
  the planner ran, and the retro's loop-health check had to
  take its cadence on faith.
- target metric: planner runs with an in-repo execution
  record (loop health, evaluation metrics family G). Current
  value - none yet; the first hourly planner run under the
  new body writes the first one.
- verification: _records_/queue-planning holds a run record
  per planner run, and the hidden-files planner log is
  retired as a record of record.
- status: implemented - the planner job body was rewritten
  on 2026-10-31 to write its execution record under
  _records_/queue-planning; the outside-repo log is retired
  as the record body.

### IMP-20261031-08 - owner decisions register

- source: owner instruction of 2026-10-31 (loop completion)
- class: meta-knowledge
- leak: items that only the owner can decide (skipped-needs-
  owner outcomes, one-off in-game choices) surfaced once in a
  round summary or a chat line and then sank - no register
  aged them, so a pending decision could age invisibly until
  it expired in game.
- target metric: age of the oldest open owner decision
  (companion register owner-decisions.md). Current value -
  the oldest open item was opened 2026-10-31, age 0 days at
  filing.
- verification: owner-decisions.md exists beside this file,
  the retro job body carries a maintenance step for it, and
  each retro reports the open items with their ages until
  the owner decides.
- status: implemented - the register was created in the same
  batch as this backlog, and the retro job body gained the
  maintenance step on 2026-10-31.

## Closed

None yet. The first closures are expected at the 2026-11-01
retro, when the implemented entries above meet their
verification against live records.
