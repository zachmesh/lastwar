---
title: Numbers line format and ranking rule for the playbook cards
created: 2026-11-23T09:25:00Z
modified: 2026-11-23T09:25:00Z
version: 1.0.0
description: The fixed numbers-line format the scribe pastes into the playbook cards, the weekly ranking on done-or-by-design rate, and the unit stat names rule_gap, rules_used and rule_failed, as decided by the coordinator
status: done
activity: coach
run_id: coach-2026-11-23-0125
trigger: coordinator decisions after the playbook baselines
started_at: 2026-11-23T09:20:00Z
finished_at: 2026-11-23T09:25:00Z
duration_seconds: 300
verified: no
grounded_in:
  - source: playbook-stats-method.py in this folder, the script that writes the lines and the ranking
  - source: coordinator decisions on the playbook baselines
---

# Numbers line format

**Format, fixed.** One line, pasted verbatim on the card:

`Numbers, 7 days to <YYYY-MM-DD>: <N> units; done <X>%; done-or-by-design <Y>%; partial <P>, failed <F>; mean steps <S or n/a> (<k> of <N> report it); top blocker <letter> <name> (<b> of <M> non-done).`

With no units: `Numbers, 7 days to <date>: 0 units.` With no non-done unit: `top blocker none (0 of 0 non-done)`. Letters and names follow the miss audit table: a window closure, b crowding out, c tap method, d inference over live read, e repeated blocker, f missing precondition, g red-line miss, h by-design partial, i owner-named without escalation.

**Source.** [playbook-numbers-lines.csv](playbook-numbers-lines.csv) holds the line for each of the 31 activities; [playbook-pilot-numbers.csv](playbook-pilot-numbers.csv) holds the two pilots. The coach regenerates both at each conformance wake and sends the changed lines on request.

**Ranking.** The weekly worst three rank on done-or-by-design rate (done plus by-design partials counted as met), lowest first, with the raw done rate shown beside it; then most rule_failed and oldest unverified rule. Under it the three are daily-missions, vip-rewards and troop-training ([worst three](playbook-worst-three.csv)); recomputed before 2026-11-30.

**Stat names.** The operator's new unit stats are `rules_used`, `rule_failed` and `rule_gap`; the legacy `gap` on 13 old units is a score gap and is ignored. Until units carry `rule_failed` the ranking uses the blocker proxy and says so in the `rule_failed_source` column.

Re-run: `python3 playbook-stats-method.py <cutoff>` beside `queue-parse.py`.
