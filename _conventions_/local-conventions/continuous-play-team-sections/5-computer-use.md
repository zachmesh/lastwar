---
title: 5. Computer use
created: 2026-11-23T07:20:36Z
modified: 2026-11-23T21:25:06Z
version: 0.3.0
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
- Owner-idle wait, dated: restored 20:04Z on 2026-11-23 (OD-20261123-23,
  `_records_/retro/owner-decisions-log/od-20261123-23.md`; code in PR 937), then TEMPORARILY 0 from
  the bridge restart after 21:20Z (OD-20261123-27, `_records_/retro/owner-decisions-log/od-20261123-27.md`)
  until CU-720 arrives with the tree move (CU-721). The code default is
  300 s and `_tools_/cu_bridge.py` sets no default: only the environment variable
  `CU_OWNER_IDLE_SECONDS=0` in the bridge daemon says 0. The older opt-out (commit fd83c35f,
  2026-11-22) ended with OD-23. A refusal `owner_active` is the wait; the
  quiet windows and the exclusive token lease (PR 911) are the other two cu-coordination rules.
- Consent is human-only. The bridge prints the control-link command
  for the owner; no seat can approve an app, a purchase, a send or a
  consequential step through the tool.
- A run gets a plain-language task, a step cap and a time cap. The
  operator checks `status`, reads the final screenshot and writes the
  result into the unit record. A run that ends `waiting_for_person`
  is recorded as blocked with the control link, never as done.

