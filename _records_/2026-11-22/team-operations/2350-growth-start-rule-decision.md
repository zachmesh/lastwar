---
title: Decision - resource-only growth starts are allowed - 2026-11-23 07:45Z
created: 2026-11-22T23:45:00-08:00
modified: 2026-11-22T23:52:00-08:00
level: L3
version: 0.1.0
description: The owner delegated a rule change after four flat weeks - idle builders, labs and training queues are filled from surplus under the 3x rule, and measurement restarts
status: done
activity: team-operations
run_id: team-operations-2026-11-22-2350-growth-start-rule
trigger: owner statement relayed by Steer A at 07:45Z
started_at: 2026-11-22T23:43:00-08:00
finished_at: 2026-11-22T23:52:00-08:00
verified: finding 1 read at _knowledge_/strategy-playbook/INDEX.md line 171; finding 2 read in _tools_/state/resources.jsonl (14 rows, 2026-10-25T21:39 to 2026-10-28T02:40); finding 3 partly (see below)
---

# Decision: resource-only growth starts are allowed

## Owner's words (2026-11-23, relayed)

"The progress over the last 4 weeks reflects clearly poor growth. Research the internet and anything you can find to accelerate growth. It is not working properly." Earlier the same day the owner said the seats decide operational choices.

## Root cause found

1. The playbook's standing boundaries say no research or building starts on the agent's own initiative. The team could claim and collect but not start growth; builders sat idle. Verified at the playbook line cited above.
2. The measuring instrument stopped: `resources.jsonl` has 14 snapshots ending 2026-10-28. Verified.
3. Stock moved apart from power: food and iron piled up. Partly verified: food 638.0M and iron 1.0G in today's builder read; **coin is 9.6M in today's HUD read, not the roughly 35M reported**, probably because the four Training Base upgrades started on the other device spent it. If coin is the scarce resource, the 3x rule will block coin-heavy starts.

## Decision (replaces that line for resource-only starts)

- **Build:** an idle builder starts the best resource-only upgrade costing at most one third of the stock of each resource it needs (coin included) with prerequisites met; by the in-game preview, most power per builder-day; the HQ path first when open.
- **Research:** same for idle labs and the same rule; order until the plan replaces it: Development, Economy, Garage 1, Alliance Duel tree, then the Special Forces gate nodes (Tech Center 30 and Special Forces open the Age of Oil, which lifts the HQ cap); Valor Badges only on those and key Alliance Duel nodes.
- **Train:** keep every training queue full at the highest tier from surplus stock, never speed-ups.
- **Read first:** builders, labs, queues; fill only idle slots; never cancel, replace or reorder a running item (the owner plays by hand too). An idle slot at a read is a recorded miss.
- **Measure:** every HUD read runs `resource_map.py snap`; Total Power and its breakdown at least daily.
- **Serves:** every start says "serves: <plan item>", until then "serves: fill idle slot".
- **Unchanged:** no purchase, diamond spend, speed-up, stamina-item burning, coal decision, PvP, diplomacy or ally exchange.

## Actions

First read-then-fill assignment to the operator at 07:43:47Z (three runs: builders, labs, training); recurring units every 30 minutes from the planner; the scribe adds a dated note under the playbook's standing boundaries (the old text is not rewritten) and Errata to three digests; the coach restarts the daily snapshots and counts misses.
