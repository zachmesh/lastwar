---
title: App approval and 5 more
created: 2026-11-23T07:02:07Z
modified: 2026-11-23T07:02:07Z
version: 0.1.0
sequence: 8
description: The owner approves com.lastwar.ios once with Always allow.
---
### App approval

The owner approves `com.lastwar.ios` once with **Always allow**. The
approval is persistent. A run that waits for `new_app` is `blocked`,
with the control link; the seat never approves it.

### Control lock

Three fresh sessions failing at the first input is a control lock. The
operator stops, records `blocker_overlay=control-lock`, and the
coordinator lifts it only after four hours or a new observation.

### Stale tool

`queue.py version` must read `currency: current`. A stale copy refuses
`enqueue`, `sync`, `plan`, `sweep` and `next`; land the tool change by
PR or run decisions from a fresh main worktree. Never set the
stale-tool bypass in production.

### Queue debt

A main-checkout queue can be a stale snapshot. Measure the live pool
from the day index and the records branch. A reset is a genesis reset:
expire old units, keep the current and next windows, never backfill.

### Session death

A seat whose session is gone is replaced by the coordinator through
the DSH client RPC. The seat record and `handover.md` are the
replacement's first read. The old session id is recorded in the
handover, never reused.

### Mac load

One desktop run at a time; two browsers team-wide; the memory floor is
25 percent. If free memory is low, stop the run and report; do not
start a second agent to "help".

