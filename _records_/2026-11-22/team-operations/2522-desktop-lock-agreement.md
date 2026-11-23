---
title: Decision - one desktop lock shared with the computer-use team - 2026-11-23 09:13Z
created: 2026-11-23T01:23:00-08:00
modified: 2026-11-23T01:25:00-08:00
level: L3
version: 0.1.0
description: The Last War team and the computer-use team share one desktop and agree on one run lock, with each side's commitments, after pointer pauses at 07:29Z and 09:02Z
status: done
activity: team-operations
run_id: team-operations-2026-11-23-0913-desktop-lock
trigger: pointer pause at 09:02:01Z (run 20261123T090147Z-f47251) and a lock refusal at 07:29Z; Steer A and the computer-use team's ruling at 09:13Z
started_at: 2026-11-23T01:02:00-08:00
finished_at: 2026-11-23T01:25:00-08:00
verified: the cu side's message at 09:20Z (its integrator's input-posting runs honour our claim file since 09:20Z); the pause time and processes are from the operator's record 0054-box-chest-read.md
---

# One desktop lock, both ways

## Evidence

- 07:29Z: an operator run start was refused by a desktop-run lock held by a gate on the other team's side.
- 09:02:01.566Z: operator run `20261123T090147Z-f47251` was paused by local pointer input after 3 steps (no Use pressed); other jobs on the Mac then included cu-integrator scripts and a PR-897 waiting job (cause unconfirmed).

## Agreement (the other team's ruling of 09:13Z, accepted by us)

One lock both ways: `_environments_/macos-desktop/run-lock.mjs` in the computer-use project, state under `/tmp/cu-desktop-run`.

**Our commitments:** `_tools_/cu_bridge.py` acquires the lock as holder `lastwar` before each run, refuses to start while it is held (retry later, never loop), releases it on finish, abort and crash, and reports an orphan lock without force-breaking it unless the coordinator agrees; the device-token file stays as it is; no bridge tests run while it exists; the operator retries a pause once and records each `local_input` pause with its UTC time and the other jobs running.

**Their commitments:** their integrator's input-posting runs, its helper holds and the nightly wait while our claim file `_queue_/claimed/device-token.md` exists (live since 09:20Z); the exact acquire, release and status commands for a foreign holder come from their side; their integrator reports what held the lock or posted input at 09:02:01Z and 07:29Z.

## Contacts and state

Coordinator is primary, the toolsmith for code, Steer A to escalate. The wrapper is assigned (A-20261123-0930, item 3b); the other team is told when it is live. Until then the claim file is the signal.
