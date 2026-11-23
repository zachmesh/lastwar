---
title: F. Knowledge organiser impact
created: 2026-11-23T09:02:25Z
modified: 2026-11-23T09:02:25Z
version: 0.1.0
sequence: 11
description: Per organiser run, rolled up weekly.
---
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

