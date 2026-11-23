---
unit: research-age-of-oil-survey-2026-11-23-002
regular: research
activity: research-queue
segment: 1
priority: 1
created_at: 2026-11-23T13:01:16Z
expires_at: 2026-11-23T14:00:00Z
planned_for:
not_before: 2026-11-23T13:10:00Z
window: oil counter and coin output v panel read for the research speed multiplier read only
est_minutes: 8
serves: baseline Age of Oil research tree
chain_id: age-of-oil-survey-2026-11-23
chain_seq: 2
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# research

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: baseline Age of Oil research tree

## Brief (planner, survey item 5: the oil counter and the Coin Output V panel, read-only)

serves: baseline Age of Oil research tree

Follow-up to `research-age-of-oil-survey-2026-11-23-001`, which was claimed before this item was added (Steer A's decisions on the Base Expansion path). Skip anything the survey record already answers (the newest record in `_records_/2026-11-22/research-queue/`).

1. The oil counter: read it on the HUD and in the Oil Well panel (434K at an earlier read, 647.0K at 12:51Z by the operator), with the tag text of each place. Say whether it includes the 180K barrels: look for an oil barrel item in the Backpack (select by one tap, never Use) and say what it shows.
2. Both labs are busy (Food Output V in slot 1, Coin Output V in slot 2, started on the other device), so the flask may open only the Research Queue list: read both rows by tag text (level, Time Left to the second, the UTC time of the read) and the research speed percent if any panel shows it; if a node panel or the tree opens, then the Coin Output V panel (Flask icon, the tree that holds it): read its coin, iron, food and oil cost, its BASE (original) time and its EFFECTIVE time, each exactly as shown with the seconds; write the effective time in seconds. The research speed multiplier is M = 485,100 s divided by the effective seconds. Also read the account's research speed percent if the survey did not.
3. Press NOTHING that starts, speeds up or completes (no Research, Speed Up, Complete, Obtain, Use). Close panels with X; a base menu with an empty-ground tap such as (400,640); never tap WORLD (660,940) with a menu open low. In the Backpack the Resources tab opens with the 5,000 Diamonds x16 tile SELECTED and a live Use: press nothing there. A TIPS dialog about another device: STOP and report, never Confirm.

One or two runs, 10 steps each. Tag text beside every number; none means [G]. Rules and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. No chain successor.
Cost cap, stated: 0.60 USD per run (the harness stops near 0.36 of it).
