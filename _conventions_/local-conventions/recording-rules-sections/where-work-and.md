---
title: Where work and evidence live
created: 2026-11-23T08:37:03Z
modified: 2026-11-23T08:37:03Z
version: 0.1.0
sequence: 3
description: Knowledge (_knowledge_) versioned claims about the game.
---
## Where work and evidence live

- **Knowledge** (`_knowledge_`) — versioned claims about the game. Edit in
  place, bump `version` and `modified`, keep the grounding current.
- **Execution units** (`_queue_`) — concrete work that moves through
  inbox, claimed and done, with a result linked to its dated record.
- **One-off improvements** — the existing
  [improvements backlog](../../_records_/retro/improvements.md), with
  evidence, ownership and a verification condition. Proposals that
  still need an owner decision go to its companion
  [owner decisions register](../../_records_/retro/owner-decisions.md).
  Do not maintain a separate current/completed task list.
- **Activities** (`_activities_`) — one instance folder per kind of
  activity, named in kebab-case like the activity it covers. Each folder
  is the accumulating source of knowledge for that kind - how it works,
  its costs, caps, refresh times and lessons - and follows the knowledge
  rule of editing in place with a version bump. The `daily-activities`
  instance is the umbrella checklist and holds no knowledge of its own
  beyond the order of a round. Participation results are never checklist
  edits - they are execution records.
- **Play records** (`_records_`) — what actually happened, organised by
  date first. One instance folder per date, named by its date. Its
  `INDEX.md` is the day record - the narrative of the day, its
  snapshots and disclosures. Inside the date, one subfolder per activity
  type, named as in `_activities_`, holding one file per execution,
  added one at a time. Each execution file states performed, performed
  in part, checked only, or not performed, with its session window and
  outcome. Whether and when an activity was performed is looked back on
  by opening that date, then that activity. Records are append-only
  under C1. A correction is appended as a new record and never rewrites
  the original entry.

