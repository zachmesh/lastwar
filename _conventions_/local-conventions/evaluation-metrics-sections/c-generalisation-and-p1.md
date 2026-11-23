---
title: C. Generalisation and discovery part 1
created: 2026-11-23T09:02:25Z
modified: 2026-11-23T09:02:25Z
version: 0.1.0
sequence: 6
description: Per week, with daily counts kept.
---
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

