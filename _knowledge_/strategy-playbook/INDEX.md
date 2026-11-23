---
title: Strategy Playbook
created: 2026-10-26T04:45:00Z
modified: 2026-11-23T09:06:47Z
level: L1
version: 1.6.0
description: How this account is played day to day - the objective, duel week timing gates, radar discipline, resource floors and the tools that enforce them
status: unverified
grounded_in:
  - source: owner direction on duel schedule discipline and resource mapping, 2026-10-25
  - source: owner statement of the ultimate goal, 2026-10-25
  - source: in-game Alliance Duel schedule and theme page, observed 2026-10-25
  - source: in-game profile and Individual Power ranking, observed 2026-10-25
  - source: events-and-cycles knowledge in this repository
---

# Strategy Playbook

How this account is played day to day - the objective, duel week timing gates, radar discipline, resource floors and the tools that enforce them. This document was split verbatim into 10 articles in reading order; nothing was rewritten, and `split_doc.py --check` rebuilds the original body from them. Find a section by its key (an entry id, a unit key such as run-20261107-1824, or a day) or heading; each line gives the title, the keys the article holds and its first sentence.

- [Strategy playbook](strategy-playbook.md)
- [Objective](objective-section.md) - objective-section - Owner, 2026-10-25 - the ultimate goal is to increase Hero Power and Total Power,...
- [The planning unit is the duel week part](the-planning-unit-p1.md) - the-planning-unit - The Alliance Duel week (full table in _knowledge_/events-and-cycles) sets when things are spent.
- [The planning unit is the duel week part](the-planning-unit-p2.md) - the-planning-unit - Day 7, off day - settlement and setup.
- [Radar discipline](radar-discipline.md) - radar-discipline - The researched rule (Handbook and the Kimikas guide agree) is finer than "save for...
- [The double dip](the-double-dip.md) - the-double-dip - Arms Race phases bookend each duel day on theme (events-and-cycles), so a completion landing...
- [Resource map and floors](resource-map-and.md) - resource-map-and - Every run that reads the HUD records a snapshot with _tools_/resource_map.py snap, and every...
- [Enforcement](enforcement-section.md) - enforcement-section - _tools_/duel.py prints today's duel day, theme, gate and radar posture.
- [Standing boundaries](standing-boundaries.md) - standing-boundaries - The recording rules red lines are unchanged and override this playbook wherever they touch...
- [What the 2026-11-19 retro ruled - dead-window reset](day-20261119.md) - day-20261119 - Sources: daily retro 2026-11-19 (flag (l) RULED - the reset boundary is 02:00Z, evidenced...

## Changelog

- 1.4.0, 2026-11-23 - Split verbatim by `split_doc.py` from a 178-line, 1,354-word body into 7 key-named articles; `--check` EQUAL, sha256 aeb7d727aea0; the unsplit 1.3.0 file is commit 1f0610cb.
- 1.5.0, 2026-11-23 - Dated note added under Standing boundaries (resource-only starts, decision record 2350); the old text is not rewritten.
- 1.6.0, 2026-11-23 - Re-split verbatim into articles of 300 words or fewer (split_doc.py with a 300-word limit); --check EQUAL, sha256 d9e18fcdbbfc; the 1.5.0 split is in git history.
