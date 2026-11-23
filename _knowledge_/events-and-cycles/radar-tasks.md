---
title: Radar tasks
created: 2026-11-23T06:18:59Z
modified: 2026-11-23T06:18:59Z
version: 0.1.0
sequence: 5
description: New secret tasks generate every six hours, in batches by radar level, with a storage cap
---
## Radar tasks

- New secret tasks generate every six hours, in batches by radar level,
  with a storage cap on completed unclaimed tasks (LDShop).
- Completed tasks can be left unclaimed and cashed on a matching VS day
  for points. The trap is the cap — if storage fills, the refresh timer
  stops and a whole batch of tasks is lost overnight. Keep headroom
  before sleep (LDShop, single source for the timer-stop behaviour).
- Refined by the 2026-10-25 research brief (Handbook VS guide and the
  Kimikas guide agree): claims score on the **odd duel days (1, 3, 5)**
  at **claim time** — so the week runs stack days (complete, do not
  claim) and release days (claim early). The Handbook lists 10,000
  points per claim against the 30,000 the in-game Day 1 page displays;
  the in-game page governs and a watched one-task claim is the pending
  test. The operational rules live in the strategy playbook.

