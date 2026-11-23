---
title: Ops Execution Records
created: 2026-11-01T05:38:00Z
modified: 2026-11-23T08:38:24Z
version: 1.1.0
status: active
description: The standing rule that every run of the loop itself - retro, tool development, knowledge organisation, PR integration, planning - leaves a structured execution record in this repository, in the same shape the game executions use
grounded_in:
  - source: owner direction of 2026-10-31 - the records are execution records, not agent sessions, and the loop activities must be recorded as executions so the retro can measure them and the loop is closed
  - source: evaluation metrics families D to G, which measure the loop from the records the loop leaves
---

# Ops Execution Records

The standing rule that every run of the loop itself - retro, tool development, knowledge organisation, PR integration, planning - leaves a structured execution record... This register stays at this path as an entry page; its text was split verbatim into 8 articles in [ops-records-sections](ops-records-sections/INDEX.md), unchanged and in reading order.

## Adding an entry

Add one small article file `ops-records-sections/<entry-id>.md`, named by an entry id that starts with letters (for example `entry-20261123-01.md`), with the frontmatter fields title, created, modified, version and description, then add one line for it at the end of this page: `- [Title](ops-records-sections/entry-20261123-01.md) one sentence`. Never edit an existing article.

## Articles

- [Ops execution records](ops-records-sections/ops-execution-records.md)
- [Mental model](ops-records-sections/mental-model.md) - mental-model - The whole system runs one loop - perceive, queue, execute, record, review, improve, verify.
- [What an execution record is](ops-records-sections/what-an-execution.md) - what-an-execution - An execution record is the structured account of one run of one standing activity:...
- [Where records live](ops-records-sections/where-records-live.md) - where-records-live - One file per run, at _records_/<YYYY-MM-DD/<ops-activity/<HHMM-run.md, where the date and time are the run's...
- [The record shape](ops-records-sections/the-record-shape.md) - the-record-shape - Frontmatter carries the identifying fields of every authored file in this repository, plus the...
- [The no-op rule](ops-records-sections/the-no-op.md) - the-no-op - A scheduled run that finds nothing to do still leaves a record, with status...
- [Alignment of the existing activities](ops-records-sections/alignment-of-the.md) - alignment-of-the - Ticker - already aligned: its executions are the task units and their per-unit record...
- [Changelog](ops-records-sections/changelog-section.md) - changelog-section - 1.0.0, 2026-11-01 - first version, under the owner direction of 2026-10-31: records are executions,...

## Changelog

- 1.1.0, 2026-11-23 - Split verbatim by split_doc.py into 8 articles; --check EQUAL, sha256 9adeea92804f; the unsplit 1.0.0 file is commit 6d019ade
