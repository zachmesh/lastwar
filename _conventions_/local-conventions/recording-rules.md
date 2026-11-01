---
title: Recording Rules
created: 2026-10-25T17:56:00Z
modified: 2026-11-01T07:26:52Z
level: L2
version: 1.9.1
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

## Task intake

How a task the owner names is handled — check whether its task type
metadata exists, create it first if it does not, execute and log new
types, and only check and update existing types without executing —
is stated in [task intake workflow](task-intake-workflow.md). Task type
metadata always keeps its own top level folder, `_activities_`, and is
never nested inside `_records_`.

## Commit discipline - execution commits stay on records branches

Pushes run under the PR-only policy of
[push and PR policy](push-and-pr-policy.md) (owner decision,
2026-10-31 - main advances only by pull request merge, and
the tier-1 direct tier of the earlier two-tier policy is
abolished). An execution commit - the ticker's per-pass
record commits and any other commit an executor makes while
doing the work - is made on the date branch
`records/<YYYY-MM-DD>` for the local date of the records,
never on main, and stages only the records paths, by
explicit pathspec, never a blanket add:

- `_records_`, `_queue_`, `_logs_`, `tools/state/`

A change under `tools/`, `_conventions_` or `_activities_` is
load-bearing and must never be swept into a record commit,
however small it looks - the scout production seeds in
`tools/queue.py` landed exactly that way once, inside a
ticker records commit (d1fa5b9, 2026-10-31). When an executor
finds load-bearing changes sitting in the working tree, it
leaves them exactly as they are, notes them in the run
record, and leaves them for the pull request flow. The
executor does not wait for its records to reach main: the
records branch is pushed through the standard route and
reaches main through the integrator's records PR on the
policy's cadence.

Pull request branches follow the mirror rule for the logs: a
work branch never stages `_logs_` at all. The append-only
input and action logs are written on records branches, and
for pull request work the integrator adds the log lines at
merge time (or they ride the next records branch), per the
push and PR policy - during the PR's life its body and
commit messages are the record. Log appends on a PR branch
race main's records commits and conflict by construction
(PR #2, 2026-10-31).

## Owner-only actions

- **Assembling is the owner's alone** (owner rule, 2026-10-25). The
  agent never teleports the base to the Alliance Assembly Point and
  never uses a teleport item for assembly. The Assemble panel may be
  opened to inspect - where the point is, how far the base sits -
  but any move is left to the owner, even when an approval for other
  work is already in hand.

## Device access

- **Retry the device-access error at least 3 times** (owner rule,
  2026-10-26). The error reporting that a run lacks owner-authorized
  device access is unreliable - runs have held access for minutes
  and then hit it mid-run (2026-10-26, the 0435, 0448 and 0456
  runs). When it appears, do not abandon the run at once - reopen
  the computer session and try again, at least 3 attempts, before
  recording the run as access-failed. The owner has confirmed the
  authorization stands and is not to be asked about again.

- **Kick the other device out** (owner rule, 2026-10-27). When the
  game shows the "active on a different device" dialog, the agent
  is authorized to click Confirm and take the session over on the
  Mac, kicking the other device - every time the dialog appears.
  The app exits; reopen it and continue. The dialog alone never
  ends a run. Only after two takeovers in the same run, if the
  dialog still returns, record the run as contested - the owner
  is likely playing on his phone at that moment - and stop.

## Language and scope

- Tracked content and logs are English. Replies to the owner are Chinese.
- No private account data, verification codes, payment details, or other
  players' private chat text, anywhere in this repository.
- In-game purchases, spending, alliance diplomacy, war declarations and
  city moves require the owner's approval before they happen, and the
  approval is recorded in the day's play record.
