---
title: Play Sessions
created: 2026-10-25T17:56:00Z
modified: 2026-10-25T18:58:00Z
version: 1.1.0
description: Play records, one dated file per day, appended in time order
grounded_in:
  - source: human-authored
---

# Play sessions

Instance folder. Each day is one leaf file named by its date. Entries are
appended in time order during the day and are immutable once committed
(C1). A correction is appended as a new entry in a later file or as a
correction section in the same file before its first commit.

## Contents

- [2026-10-25](2026-10-25.md) — Mac install, Game Center login to the
  original character, the first base snapshot, and the first daily round.

Per activity lookup for the same days lives in
[`activity-executions/`](../activity-executions/INDEX.md), one file per
activity type.
