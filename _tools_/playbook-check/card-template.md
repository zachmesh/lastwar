---
title: Card Template
created: 2026-11-23T10:00:00Z
modified: 2026-11-23T10:00:00Z
version: 1.0.0
description: The playbook card shape that playbook_check.py enforces, to copy into an activity INDEX.md
---

# Card template

Copy this into `_activities_/<activity>/INDEX.md` and fill it in. Total 300 words or fewer.

```
# <Activity>

## Goal
One sentence.

## Route
1. A step (at most 8, numbered).

## Rules
- R1 [verified 2026-11-21] The rule. (evidence: _records_/2026-11-21/<activity>/0145-queue-run.md)
- R2 [unverified 2026-11-20] Another. (evidence: _records_/<date>/<activity>/<file>.md)

## Failures
- What fails - the fix. (at most 3)

## Open questions
- The question? test: how it is settled. (at most 3)

## Numbers
One line from the records, with a digit and a record path (_records_/<date>/<activity>/<file>.md).

## Links
- [text](path) (at most 5)
```

Rules: at most 5; status verified or unverified, never superseded (rewrite the rule in place, history stays in git); cite
`_records_/` only, never a run note or a run article. No Errata section.
