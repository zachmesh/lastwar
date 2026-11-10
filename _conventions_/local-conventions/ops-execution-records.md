---
title: Ops Execution Records
created: 2026-11-01T05:38:00Z
modified: 2026-11-01T05:38:00Z
version: 1.0.0
status: active
description: The standing rule that every run of the loop itself - retro, tool development, knowledge organisation, PR integration, planning - leaves a structured execution record in this repository, in the same shape the game executions use
grounded_in:
  - source: owner direction of 2026-10-31 - the records are execution records, not agent sessions, and the loop activities must be recorded as executions so the retro can measure them and the loop is closed
  - source: evaluation metrics families D to G, which measure the loop from the records the loop leaves
---

# Ops execution records

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

## What an execution record is

An execution record is the structured account of one run of
one standing activity: when it ran, what triggered it, what it
read, what it produced, how long it took, how its output was
verified, and what it left open. It is not a transcript. The
conversation that drove the run, the tool calls inside it and
the chat summaries around it are not the record and are never
cited as one; where a run's only trace today is a commit or a
merged pull request, that trace is cross-check evidence, not
the record itself.

This standard covers the loop's own activities. Game
executions already have their shape - the task unit result of
the queue design (its section 5) and the per-unit record file
under `_records_/<date>/<activity>/` - and keep it unchanged.
The ops record below deliberately mirrors that shape, so one
aggregation habit reads both.

## Where records live

One file per run, at
`_records_/<YYYY-MM-DD>/<ops-activity>/<HHMM>-run.md`, where
the date and time are the run's local finish time, and the run
is appended to that day's `_records_/<date>/INDEX.md` - the
same layout the game executions use. The ops activities with
standing profiles are registered under `_activities_`:

- `retro-review` - the daily retro pass.
- `tool-development` - the tool developer's runs.
- `knowledge-organization` - the knowledge organiser's runs.
- `pr-integration` - the PR integrator's runs.

Derived retro artifacts keep their standing home at
`_records_/retro/` (the retro file, its data appendix, the
rolling file, the improvements backlog); the retro's execution
record is the per-run file above and points at them.

## The record shape

Frontmatter carries the identifying fields of every authored
file in this repository, plus the ops fields. Values carry no
colon except timestamps, as everywhere here.

| Field | Meaning |
|---|---|
| `activity` | the ops activity slug - retro-review, tool-development, knowledge-organization, pr-integration |
| `run_id` | `<activity>-<YYYY-MM-DD>-<HHMM>` of the local finish time |
| `trigger` | what started the run - schedule, manual, owner, or feedback |
| `started_at` | ISO timestamp, or `unknown` where no evidence survives |
| `finished_at` | ISO timestamp, or `unknown` |
| `duration_seconds` | integer seconds, or `unknown` - never estimated |
| `status` | done, partial, failed, or no-op |
| `verified` | how the outputs were checked - ls-remote, a merged PR state, a fixture run - or `reconstructed` for a retrospective record, or `no` |

The body carries four short sections:

- **Inputs** - what the run read: the backlog state, the open
  PR list, the records window, the observation it consumed.
- **Outputs** - what it wrote: files changed, PRs opened or
  merged, the commit hashes.
- **Stats** - the run's own key counts, in the vocabulary of
  its activity profile: items processed, fixes or filings
  made, errors hit. The counts the evaluation metrics read.
- **Follow-up** - what the run left open, by name, or `none`.

## The no-op rule

A scheduled run that finds nothing to do still leaves a
record, with status `no-op` and the inputs it checked. It may
be a few lines long. Loop health (evaluation metrics family G)
proves a job ran from its records; a missing record is a
missing run, and the retro names it as such. Silence is a
delivery choice in chat - it is never a substitute for the
record.

## Alignment of the existing activities

- **Ticker** - already aligned: its executions are the task
  units and their per-unit record files.
- **Planner** - not yet aligned: its run log lives outside the
  repository, in the goal workspace, so its run rate is
  proxied by the units it produces (evaluation metrics family
  G states this defect). Mirroring the planner log into
  `_records_/<date>/planner/` in this shape is the migration
  item; it is deliberately not forced in the change that
  introduces this standard, because the planner job's own
  instructions must change with it and that change is
  scheduled work, not a document edit.
- **Knowledge organiser** - partially aligned: its dated note
  under `_records_/knowledge-organizer/` carries most of the
  counts but not the field shape. New runs record under
  `_records_/<date>/knowledge-organization/` in this shape;
  the note series stays as history.
- **Retro, tool developer, PR integrator** - aligned from this
  standard forward; their earlier runs are reconstructed where
  evidence survives, marked `verified: reconstructed`, with
  unrecoverable fields written `unknown` - never invented.

## Changelog

- 1.0.0, 2026-11-01 - first version, under the owner direction
  of 2026-10-31: records are executions, not sessions, and the
  loop's own activities record themselves in the repository in
  the game executions' shape, so the retro can measure them
  and the loop is closed. The mental model stated at the head;
  the record shape, the no-op rule, and the alignment state of
  the ticker, planner, organiser, retro, tool developer and
  integrator fixed; baseline records for 2026-10-31
  reconstructed in the same change.
