---
title: Notes
created: 2026-11-23T09:06:14Z
modified: 2026-11-23T09:06:14Z
version: 0.1.0
sequence: 4
description: Retro loop-health has a one-day blind spot - if the retro job itself fails, the gap
---
## Notes

- Retro loop-health has a one-day blind spot: if the retro job
  itself fails, the gap is only visible at the next retro (plus
  cron failure notices). Accepted for now; recorded so the
  acceptance is explicit.
- Owner-decision items (skipped-needs-owner units) resurface via
  round summaries and the retro; there is no separate aging digest
  for them. Rule R5 covers owner-named tasks. Accepted for now.
