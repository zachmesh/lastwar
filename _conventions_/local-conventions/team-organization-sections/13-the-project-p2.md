---
title: 13. The project board part 2
created: 2026-11-23T09:04:37Z
modified: 2026-11-23T09:04:37Z
version: 0.1.0
sequence: 17
description: The Feedback loop view groups by Status, not by Feedback state - the API has no
---
- The `Feedback loop` view groups by Status, not by Feedback state: the API
  has no input for a board's column field, so changing it is a web-UI step.
  It stays empty until feedback items exist.
- The built-in project workflows (item closed -> Done and the like) are
  disabled; the API can delete workflows but not enable them.
- Open issues are not yet parented to an Epic or given an Agent; the
  Coordinator's triage pass does that, `Maintenance` first.


