---
title: Knowledge
created: 2026-10-25T17:56:00Z
modified: 2026-11-01T07:09:43Z
version: 1.2.1
description: Game knowledge for Last War Survival, one instance per topic
grounded_in:
  - source: human-authored
---

# `_knowledge_`

Type folder, registered locally in
[typed-folder adoption](../_conventions_/local-conventions/typed-folder-adoption.md).
Holds versioned claims about the game. Each child is one topic; the topic's
`INDEX.md` is its article.

## Contents

- [`account-and-platforms/`](account-and-platforms/INDEX.md) — the account,
  its binding, and how each platform logs in.
- [`heroes-and-squads/`](heroes-and-squads/INDEX.md) — hero types, the
  counter triangle, formation bonuses, tier consensus and canonical squads.
- [`headquarters-and-resources/`](headquarters-and-resources/INDEX.md) —
  the core resources, headquarters gating and troop tier milestones.
- [`season-two-winter/`](season-two-winter/INDEX.md) — Season 2 Polar
  Storm, covering temperature, furnaces, coal, titanium alloy and Rare Soil.
- [`events-and-cycles/`](events-and-cycles/INDEX.md) — Arms Race phases,
  the Alliance Duel VS week, the double-dip rule and radar discipline.
- [`strategy-playbook/`](strategy-playbook/INDEX.md) — how this account
  is played: duel week timing gates, radar discipline, resource floors
  and the tools that enforce them (`tools/duel.py`,
  `tools/resource_map.py`, `tools/regulars.py`).

Further topics are added as instances when their research lands. Planned
knowledge work is tracked in the [improvements backlog](../_records_/retro/improvements.md),
so this index names only topics that already exist.
