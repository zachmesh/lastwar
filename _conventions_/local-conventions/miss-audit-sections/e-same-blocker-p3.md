---
title: E. Same blocker repeated with no escalation - 42 units part 3
created: 2026-11-23T09:03:19Z
modified: 2026-11-23T09:03:19Z
version: 0.1.0
sequence: 12
description: Prevention rule E - three strikes stops the loop for that regular.
---
Prevention rule E - three strikes stops the loop for that regular.
The third consecutive partial with the same blocker writes the
blocker into the activity metadata, changes the entry route or
method before any further unit of that type runs, and surfaces the
blocker in that day round summary. A fourth identical partial is a
process failure, not a result.

