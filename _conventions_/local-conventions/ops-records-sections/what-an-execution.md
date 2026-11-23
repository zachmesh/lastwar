---
title: What an execution record is
created: 2026-11-23T08:38:24Z
modified: 2026-11-23T08:38:24Z
version: 0.1.0
sequence: 3
description: An execution record is the structured account of one run of one standing activity - when
---
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

