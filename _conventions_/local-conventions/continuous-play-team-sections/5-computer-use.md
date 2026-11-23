---
title: 5. Computer use
created: 2026-11-23T07:20:36Z
modified: 2026-11-23T20:05:56Z
version: 0.2.0
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
- Owner-idle wait RESTORED by the owner's decision of 2026-11-23T19:48Z (OD-20261123-23,
  `_records_/retro/owner-decisions-log/od-20261123-23.md`; code in PR 937). The opt-out
  `CU_OWNER_IDLE_SECONDS=0`, which `_tools_/cu_bridge.py` set under commit fd83c35f on an owner
  request of 2026-11-22, is gone: the bridge no longer defaults the variable, the lock's
  constant is 300 s, and a refusal `owner_active` is the wait. The quiet windows and the
  exclusive token lease (PR 911) are the other two cu-coordination rules.
- Consent is human-only. The bridge prints the control-link command
  for the owner; no seat can approve an app, a purchase, a send or a
  consequential step through the tool.
- A run gets a plain-language task, a step cap and a time cap. The
  operator checks `status`, reads the final screenshot and writes the
  result into the unit record. A run that ends `waiting_for_person`
  is recorded as blocked with the control link, never as done.

