---
title: Recording Rules
created: 2026-10-25T17:56:00Z
modified: 2026-10-25T17:56:00Z
level: L2
version: 1.0.0
description: Evidence, language and append-only rules for knowledge, tasks, activities and play records
status: unverified
grounded_in:
  - source: human-authored, owner requests 2026-10-25 on recording scope
builds_on:
  - _conventions_/local-conventions/typed-folder-adoption.md@1.0.0
---

# Recording rules

## Evidence

- Every figure comes from the game screen, checked at the time of writing,
  or from the owner, marked as owner-reported. Anything else is marked
  unverified. External guides are named with links in `grounded_in` and in
  the body, and a claim needs two independent sources or one official source
  before it is stated without a hedge.
- Screenshots are evidence, not records. The record is the text written from
  them the same day.

## The four record kinds

- **Knowledge** (`_knowledge_`) — versioned claims about the game. Edit in
  place, bump `version` and `modified`, keep the grounding current.
- **Tasks** (`_tasks_`) — the live list in the `task-list` instance. A
  finished task moves to its completed section with its date.
- **Activities** (`_activities_`) — checklists are knowledge and follow its
  rule. Participation results are play records, not checklist edits.
- **Play records** (`_records_`) — what actually happened, one file per day
  under `play-sessions`. Append-only under C1. A correction is appended as
  a correction entry and never rewrites the original entry.

## Language and scope

- Tracked content and logs are English. Replies to the owner are Chinese.
- No credential values, verification codes, payment details, or other
  players' private chat text, anywhere in this repository.
- In-game purchases, spending, alliance diplomacy, war declarations and
  city moves require the owner's approval before they happen, and the
  approval is recorded in the day's play record.
