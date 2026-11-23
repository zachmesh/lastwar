---
title: Promotion and scheduling
created: 2026-11-23T09:03:33Z
modified: 2026-11-23T09:03:33Z
version: 0.1.0
sequence: 21
description: When the mechanism is clear and the task sits inside the free and safe envelope -
---
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

