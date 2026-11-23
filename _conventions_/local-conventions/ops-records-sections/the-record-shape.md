---
title: The record shape
created: 2026-11-23T08:38:24Z
modified: 2026-11-23T08:38:24Z
version: 0.1.0
sequence: 5
description: Frontmatter carries the identifying fields of every authored file in this repository, plus the ops fields.
---
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

