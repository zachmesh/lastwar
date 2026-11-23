---
title: What this activity is and 1 more
created: 2026-11-23T06:46:48Z
modified: 2026-11-23T06:46:48Z
version: 0.1.0
sequence: 2
description: Checking the four build queues, recording long running upgrades and noting idle slots.
---
## What this activity is

Checking the four build queues, recording long running upgrades and
noting idle slots. This folder accumulates building knowledge - queue
count, upgrade times and panel safety lessons. Starting an upgrade
spends resources and locks a queue for a long time, so it needs the
owner choice unless it was already queued. Executions are recorded in
`_records_/<date>/building-queues/`, one file per execution.

## How it is done

- Open the build queue list from the base screen queue icons. The hammer icon opens the panel - tap [44,195] measured 2026-11-09.
- Record each running upgrade, its level and its time left.
- Close building panels from their panel base area with care - see the
  safety lesson below.

