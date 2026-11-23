---
title: Enforcement and 2 more
created: 2026-11-23T07:46:59Z
modified: 2026-11-23T07:47:35Z
version: 0.2.0
sequence: 7
description: tools_/duel.py prints today's duel day, theme, gate and radar posture.
---
## Enforcement

- `_tools_/duel.py` prints today's duel day, theme, gate and radar
  posture. Every scheduled run reads it first and follows the gate:
  on preserve days the radar regular is marked skip with the duel
  reason instead of being emptied; on Day 1 it is worked first.
- `_tools_/regulars.py` remains the per-day ledger of what was done;
  the gates change how a regular is worked, never whether it is
  accounted for.
- `_tools_/resource_map.py check` output rides along in run reports
  whenever a flag is raised.

## Standing boundaries

The recording rules red lines are unchanged and override this
playbook wherever they touch - no purchases, no diamond spending,
no speedup or stamina item burning to score, no research or
building starts on the agent's own initiative, no coal decisions.
The playbook times what is already allowed; it never widens it.

Dated note 2026-11-23T07:45Z (owner-delegated; decision record `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`): the boundary "no research or building starts on the agent's own initiative" no longer applies to RESOURCE-ONLY starts: idle builders, labs and training queues are filled from surplus when the cost is at most a third of each stock and above the reserves (food 100M, iron 150M, coin 10M, diamonds untouched). Unchanged: no purchase, diamond spend, speed-up, stamina-item burning, coal decision, PvP, diplomacy or ally exchange.

## What the 2026-11-19 retro ruled - dead-window reset label corrected to 02:00Z (B-2026-11-19-02)

- Sources: daily retro 2026-11-19 (flag (l) RULED - the reset boundary is 02:00Z, evidenced by the sweep pair expiring 18:00 local, the VIP unit expires_at 2026-11-21T02:00:00Z, and the ticker-1926 time note).
- Correction: the dead-window rule still timed the roll at 19:00. Corrected to the daily reset (02:00Z, about 18:00 PST in winter, 19:00 PDT in summer). No other claim in this profile changes.
- The B-2026-11-19-02 issue is filed at VPS recovery; the PR carrying this fold names its issue number then. Owner: lastwar-knowledge-organizer.
