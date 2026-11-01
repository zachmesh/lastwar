---
title: Tool Runtime State
created: 2026-11-01T07:58:31Z
modified: 2026-11-01T07:58:31Z
version: 1.0.0
description: Persistent state shared by repository helper commands
---

# Tool runtime state

Date-named JSON files hold the recurring-activity tracker state.
`resources.jsonl` contains the append-only resource snapshot history.
Both canonical and compatibility tool commands read and write these same files.

State follows the records branch flow in the
[push and PR policy](../../_conventions_/local-conventions/push-and-pr-policy.md).
