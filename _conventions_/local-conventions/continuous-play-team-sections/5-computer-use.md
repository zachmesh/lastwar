---
title: 5. Computer use
created: 2026-11-23T07:20:36Z
modified: 2026-11-24T12:21:31Z
version: 0.5.0
sequence: 10
description: Play happens through dtadpole/computer-use on this Mac, using its MCP server.
---
## 5. Computer use

Play happens through `dtadpole/computer-use` on this Mac, using its
MCP server. The integration contract is the project's own:
`computer-use-mcp` exposes `computer_use_start`, `_status`,
`_respond` and `_control`; a desktop run names the apps it may use,
and a person approves each app once in the live view.

Local rules:

- The bridge is `_tools_/cu_bridge.py`; it speaks JSON-RPC to the
  MCP server over stdio and stores run ids under
  `_tools_/state/cu_runs.json`. It is the only route the operator
  uses; no seat edits a DSH profile to add a tool.
- The app bundle id for the game is `com.lastwar.ios`. Terminals,
  password managers, AI agents and system security apps are excluded
  by the computer-use policy and are never proposed.
- One desktop run at a time. A live run holds the Mac's desktop-run
  lock; a second start is refused, not queued.
- Owner-idle wait, dated: restored 20:04Z on 2026-11-23 (OD-20261123-23), TEMPORARILY 0 from the
  restart after 21:25Z (OD-20261123-27), and 300 s again from 2026-11-24T08:36:10Z, when the bridge moved to
  the computer-use worktree `~/dtadpole/computer-use-wt/lastwar-bridge` (detached at b52c84ba391e, CU-720's
  carry in it; `_records_/2026-11-22/team-operations/1140-tick.md`). The bridge
  prints `owner_idle_seconds=300 (source: default)`. Owner-idle waits: 0 s since; the cost is the cu gate
  runs holding the lock about 2.4 min. The 2026-11-22 opt-out (fd83c35f) ended with OD-23. A refusal `owner_active` is the wait; quiet windows and the token lease (PR 911) are the
  other two cu-coordination rules.
- Consent is human-only. The bridge prints the control-link command
  for the owner; no seat can approve an app, a purchase, a send or a
  consequential step through the tool.
- A run gets a plain-language task, a step cap and a time cap. The
  operator checks `status`, reads the final screenshot and writes the
  result into the unit record. A run that ends `waiting_for_person`
  is recorded as blocked with the control link, never as done.

