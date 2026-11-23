---
title: Repository first rule
created: 2026-11-23T08:39:25Z
modified: 2026-11-23T08:39:25Z
version: 0.1.0
sequence: 1
description: The owner rule that everything which helps play the account lives in this repository, with the tools path and staging notes
---
## Everything lives in this repository

Owner rule, 2026-10-25 - everything that helps play this account
lives here: schedules, strategy, tools, resource maps and records.
Nothing load-bearing is kept only in chat or in the agent's memory.
If a fact, rule, list or tool would matter next week, it is written
into this repository in the same session that produced it - the
duel schedule in `_knowledge_` and `_tools_/duel_schedule.json`, the
strategy in `_knowledge_/strategy-playbook`, the resource map in
`_tools_/resources.json` and its snapshots, and the working tools in
`_tools_/`.

Use `_tools_/` in every new tool command and Git stage pathspec. The root
`tools` compatibility symlink supports old Python commands, but Git cannot
stage a path through a symlink. Records writers must stage `_tools_/state/`
explicitly alongside their other records paths, even when an older job
prompt still names the previous path.
