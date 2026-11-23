---
title: Activity profile loop audit - 2026-11-22 20:34 PT
created: 2026-11-22T20:34:00-08:00
modified: 2026-11-22T20:38:00-08:00
level: L3
version: 0.1.0
description: Per-activity audit of the 37 folders under _activities_ - which have a record, fold, open-questions, issue and target loop, and whether the folders are grouped
status: done
activity: team-operations
run_id: team-operations-2026-11-22-2034-activity-loop-audit
trigger: owner question 2026-11-23T04:30Z - is there a self-improvement loop for each task type, and are the _activities_ grouped recursively
started_at: 2026-11-22T20:30:00-08:00
finished_at: 2026-11-22T20:38:00-08:00
duration_seconds: 480
verified: measured by script over _activities_/*/INDEX.md, _records_/*/<activity>/*.md, improvements.md and owner-decisions.md at 2026-11-23T04:36Z
---

# Activity profile loop audit - 2026-11-22 20:34 PT

Unit of analysis: the 37 folders under `_activities_` (not queue regulars).

## Measured

| Loop element | Activities | Reading |
|---|---|---|
| Execution records exist | 37 of 37 | fewest 1 (decoration-gallery-overview-ur) |
| Profile folded on or after its newest record date | 31 of 37 | stale: pr-integration, tool-development, knowledge-organization, alliance-gifts, alliance-help, retro-review |
| An "Open questions" section | 32 of 37 | learning prompts, no owner, no deadline |
| Cites at least one GitHub issue | 30 of 37 | none: tool-development, season-warming, retro-review, pr-integration, hidden-treasures, hero-recruitment, decoration-gallery-overview-ur |
| A dedicated improvement target or metric section | 0 of 37 | the only target heading, alliance-duel "3.6M target", is a game target, not an improvement target |
| Named in `_records_/retro/improvements.md` | 1 of 37 | knowledge-organization only; per-type improvements live in GitHub issues |
| Status `unverified` | 28 of 37 | |
| Profile frontmatter not valid YAML | 2 of 37 | alliance-gifts, zombie-invasion |
| Profiles over 1,000 lines | 17 of 37 | 36,866 lines in total; alliance-donations 4,221, perception-scout 4,159 |
| Subfolders inside any activity | 0 | `_activities_` is flat: 37 folders, one `INDEX.md` each, no grouping |

The three meta-activities that run the improvement loop are the thinnest and
stalest: pr-integration (1,275 records, profile 58 lines, folded 2026-11-01),
tool-development (321 records, 58 lines, 2026-11-01), knowledge-organization
(299 records, 75 lines, 2026-11-04).

## Reading

A per-type learning loop exists for most types (record, fold, open question,
issue). A closed improvement loop does not: no type states a target metric, a
current value, an owner, a review date, or the verification that closes a change.
Improvement is driven by the global retro's top leaks, so a type that is not a
top leak gets none.

## Corrections to earlier chat claims

- "5 of 37 profiles have a target section" was a loose heading count; the strict
  count is 0 of 37. A first rerun matched 17 because log headings contain
  "measured" and "target found"; that number is not a finding.

## Follow-up

- Improvement `IMP-20261123-02` filed.
- No folder or profile was changed in this pass.
