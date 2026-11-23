---
title: Audit
created: 2026-11-23T08:37:00Z
modified: 2026-11-23T08:37:00Z
version: 0.1.0
sequence: 11
description: The daily retro's loop-health check scans every commit that landed on main since the previous retro
---
## Audit

The daily retro's loop-health check scans every commit that
landed on main since the previous retro and classifies each
one: a pull request squash merge (pull request reference in
the subject), a records PR merge commit, a retro-named
break-glass commit - or a violation. Every violation is named
in the retro file, counted in the evaluation metrics'
loop-health family, and filed as an improvement task. Under
this policy there is no fourth legitimate class.

The same check covers ownership: every PR merged in the
window must show its owner on record - the `Owner:` line in
its body, or an integrator reassignment comment where the
line was missing or wrong. A merged PR with no owner named
anywhere is reported in the retro by number, counted in the
loop-health family, and filed as an improvement task like
any other violation. The standing target is an ownership
coverage of 100 percent of merged PRs.

