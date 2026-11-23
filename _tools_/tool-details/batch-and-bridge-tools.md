---
title: Batch and bridge tools
created: 2026-11-23T04:53:59Z
modified: 2026-11-23T04:53:59Z
version: 1.0.0
description: Verbatim index rows for records_batch.py, cu_bridge.py
---

# Batch and bridge tools

Moved verbatim from the former `_tools_/INDEX.md` table; only link destinations are adjusted for this folder. Back to the [tool index](../INDEX.md).

| Tool | Purpose | Data |
|---|---|---|
| [records_batch.py](../records_batch.py) | Mechanical gate and audit for the records batch cadence (policy 2.3.0, merged as PR #116, issue #126, IMP-20261101-09): six daily batch points at 03:00, 07:00, 11:00, 15:00, 19:00 and 23:00 America/Los_Angeles, with the 60-minute half-open window `[point, point + 60 min)` this tool defines for the policy's first-integrator-pass-at-or-after rule; `due` gates the integrator on an exit code (0 due, 1 not due, 2 usage or input error) and is merge-aware under `--merges`, so only the first pass at or after a batch point merges and an already-merged window is not due again (issue #335); `audit` lists merges outside every window and the second and later merge inside one window under the first-pass rule (issue #418), exiting 0 even when it finds violations because a violation is a finding and not a tool failure; `--window-minutes` overrides BATCH_WINDOW_MINUTES and `--at` replays a past moment, an offset timestamp is authoritative and a naive one is read as Los Angeles wall time | a records-merge JSON list recorded from gh |
| [cu_bridge.py](../cu_bridge.py) | The operator's only route to the computer-use MCP server, which exposes four tools over MCP stdio - `computer_use_start`, `computer_use_status`, `computer_use_respond` and `computer_use_control`; a desktop run must stay inside one server process for its whole life, so the bridge keeps one server alive behind a Unix socket and lets short CLI calls start, poll and stop runs; `serve` runs the daemon in the foreground, `ensure` starts it if it is not running, `self-test` initializes MCP and lists the four tools, `start --task TEXT [--app ID]` starts a desktop run (default app com.lastwar.ios), `status [--run-id ID] [--wait N] [--image PATH]` polls the latest or named run and saves the final screenshot (the wait is capped at MAX_WAIT 50), `control --run-id ID --command` one of pause, resume, stop or guide, with `[--text TEXT]`, sends a caller command, `runs` lists the runs the bridge recorded, `stop-daemon` stops the daemon; consent and app approval are human-only, so the bridge never approves an app, a consent request, a purchase or a send, and approval comes only from the owner through the control link printed by `start` and run in a real terminal; exit 0 ok, 1 refused or failed, 2 usage or environment error | `_tools_/state/cu_runs.json` (run state, newest first, last 50) plus the daemon socket, pid and log files and `cu_last.png` beside it under `_tools_/state/` |
