---
title: 3. Pool layout
created: 2026-11-23T08:37:05Z
modified: 2026-11-23T08:37:05Z
version: 0.1.0
sequence: 5
description: queue_/ INDEX.md - the type index, points here unit-template.md - the unit file template inbox/ -
---
## 3. Pool layout

```text
_queue_/
  INDEX.md          - the type index, points here
  unit-template.md  - the unit file template
  inbox/            - pending units, one file per unit
  claimed/          - units under execution, plus the device token
  done/             - finished units with their result blocks
  completed/        - completion markers for units closed in a detached worktree (live-only state, never committed; see below)
```

Unit file names are `<unit-id>.md` where the id is
`<regular-id>-<cycle>` and cycle is the local date and hour of the
producing cycle, for example `vip-2026-10-28-1900.md`. Names stay
unique across days without a central counter.

