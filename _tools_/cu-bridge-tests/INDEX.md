---
title: Bridge Tests
created: 2026-11-23T07:10:00Z
modified: 2026-11-23T09:41:30Z
version: 1.3.0
description: Tests for the computer-use bridge daemon lifecycle, run against a fake MCP server in a temporary copy
---

# Bridge tests

Tests for IMP-20261123-07 (a restart left an orphan daemon and a stuck run). Each test copies `cu_bridge.py` into a
temporary tree under /tmp and points it at a fake MCP server, so no real server, device or run is touched.

They cover: a restart during a run ends the old daemon and its MCP child; a second `serve` refuses; `ensure` never starts
a second daemon while one is busy; `status` lists every daemon and run; `control stop` reaches the owning daemon or ends
an unreachable one; SIGTERM cleans up the child.

Waits are on conditions (a marker file, a process gone, a reachable daemon) with generous ceilings, never a guessed
sleep or a wall-clock bound, so load slows a test without failing it. The fake server runs under a seat name of its own.
Every test is skipped while `_queue_/claimed/` of this checkout or the main one holds a file (a live run and its device
token); `CU_TESTS_IGNORE_LIVE_RUN=1` runs them anyway.

`test_desktop_lock.py` covers the computer-use desktop-run lock the bridge now reads before `start` (read-only, through `run-lock.mjs status`): a
free desktop starts; a live run or hold, ours or another seat's, or a waiter refuses before the server is asked, once, with a retry-later
report and no wait, retry or break; an orphan entry (its process dead) is reported and refused unless the coordinator's
`--accept-orphan`, and the bridge never touches it; the server's own refusal is reported once without a phantom run; the default seat is
`cu-lastwar` (CU_SEAT overrides it) and a `CU_SEAT` the lock would refuse (`lastwar`) stops `start`. A fake `run-lock.mjs` and a lock folder of their own stand in for the real ones.

Run: `python3 -m unittest discover -s _tools_/cu-bridge-tests`.
