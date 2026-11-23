---
title: 8. Budget, chain splitting and the observation file part 1
created: 2026-11-23T09:03:33Z
modified: 2026-11-23T09:03:33Z
version: 0.1.0
sequence: 24
description: A scout pass is bound by the same 15 minute unit cap as all work.
---
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

