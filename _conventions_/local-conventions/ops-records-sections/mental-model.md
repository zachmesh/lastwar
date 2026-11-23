---
title: Mental model
created: 2026-11-23T08:38:24Z
modified: 2026-11-23T08:38:24Z
version: 0.1.0
sequence: 2
description: The whole system runs one loop - perceive, queue, execute, record, review, improve, verify.
---
## Mental model

The whole system runs one loop - perceive, queue, execute,
record, review, improve, verify. What gets recorded is always
an **execution**, never an agent session. Sessions, chats and
Slack threads are summary and pointer channels; the repository
is the single source of truth (the standing statement of that
principle is section 14 of the
[task unit queue design](task-unit-queue-design.md); this
document does not redefine it, it operationalises it for the
loop's own work).

Every activity in the loop is itself an execution - the game
units, the perception passes, the planning, the retro, the
tool development, the knowledge organisation, the PR
integration. Each one leaves an execution record in this
repository, and the retro measures all of them with the same
ruler it measures the game work with. An activity with no
execution record is treated as not proven to have happened -
absence is never read as a quiet success.

