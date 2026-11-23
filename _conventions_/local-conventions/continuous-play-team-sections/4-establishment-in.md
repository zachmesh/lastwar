---
title: 4. Establishment in DSH
created: 2026-11-23T07:20:36Z
modified: 2026-11-23T07:20:36Z
version: 0.1.0
sequence: 9
description: The team runs on the local DSH host in the lastwar workspace.
---
## 4. Establishment in DSH

The team runs on the local DSH host in the `lastwar` workspace. The
coordinator is this session; the other seats are DSH sessions created
through a supported DSH operation, never by editing a DSH store.

- **Visibility** - every seat is a real DSH session the UI can list
  and open. The team roster projection or the workspace session list
  is the proof; a seat with no session id in `TEAM.yaml` is planned,
  not established.
- **Continuation** - the coordinator holds the only recurring
  schedule (`15 min`). The schedule is the loop clock. A delegated
  child cannot create its own schedule, so the coordinator wakes each
  seat with a bounded assignment; an idle seat is not a stopped loop.
- **Communication** - bounded assignments carry a question, the
  expected evidence and a completion condition. A seat replies with
  the artifact path and the measurement; chat text alone is not a
  result.
- **Lease** - `TEAM.yaml` records each seat's session id and start
  time. A session that dies is replaced; a seat is never silently
  abandoned.
- **One device** - only the operator may hold the device token and
  send input to the game. A second input path is a defect, not a
  parallel speed-up.

The first establishment is honestly partial. A seat created as a
delegated child session is UI-visible and durable, but it is not a
top-level workspace session with its own schedule. The coordinator
therefore records `session_id` and `session_started` for every
established seat, and the first weekly review judges whether the
child-session form is sufficient or a top-level session per seat is
required. The decision is recorded in the owner decisions register,
not assumed.

