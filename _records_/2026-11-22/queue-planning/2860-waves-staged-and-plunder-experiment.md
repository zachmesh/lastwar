---
title: Queue Planning Waves Staged The 11-25 Complete And The Plunder Experiment 2860 2026-11-23
created: 2026-11-23T07:25:00-08:00
modified: 2026-11-23T07:25:00-08:00
level: L0
version: 1.0.0
description: Planner pass after the live tool sync - the 11-25 Iron Output V Complete unit minted, the 18:03Z, 18:30Z and 18:57Z waves staged with briefs, the nine units plan expired, and the left-half plunder experiment amendment to scan 002
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0725-waves-and-experiment
trigger: coordinator messages at 15:12Z and 15:10Z
started_at: 2026-11-23T07:09:00-08:00
finished_at: 2026-11-23T07:25:00-08:00
verified: the inbox diffed before and after each plan; done files read for the expired units; word counts under 450; validate exit 0
grounded_in:
  - source: _tools_/queue.py cmd_plan
  - source: _records_/2026-11-22/queue-planning/2850-plunder-left-half-experiment.md
---

# Waves staged, the 11-25 Complete and the plunder experiment, 2860

## 1. Minted and staged

`research-complete-2026-11-25-001` (02:39:30Z to 04:30Z on 2026-11-25) is minted: it completes Iron Output V if the 17:30Z speed-up did not, then starts Oil Output I level 1 in an idle lab 1, else a Special Forces +15K node with no speed-up. `plan --hours 3` staged the 18:03Z wave (arms race, building queues, donations, harvest, radar, research, survivors, training; 18:03Z to 22:03Z); `plan --hours 4` then staged the 18:30Z group (duel-score, gifts, help, mail, star-ceremony, train; to 22:30Z) and the 18:57Z group (events, passes, secrets, treasures, trucks; to 22:57Z). The roster donations unit for 18:03Z was retired: the donation schedule is passes 001 and 002 and the 00:30Z unit. The roster does not yet write the definition block, so each unit got one, with the corrected shop facts for passes. No new unit has a window or expiry inside a quiet window; the 18:57Z group opens after QW3 ends.

## 2. Expired unrun

`plan` expired nine units: the 10:30Z claims duel-score, gifts, help, star-ceremony and train, the events, secrets and treasures units of 14:57Z, and the fixed-state power read for slot B (13:00Z to 15:00Z), whose status is expired in the done folder. More than two in an hour; the operator's time went to plunder, donations, harvest, the shop and the research chain. The next fixed-state read is slot A (02:00Z to 04:00Z on 2026-11-24, staged).

## 3. The plunder experiment

Scan `-002` carries the one-fight exception from [2850](2850-plunder-left-half-experiment.md): the UR Lv.30 truck (guard 18.9M, two 500-badge x3 stacks in the left half, arriving about 16:00Z) qualifies if still listed and over 30 minutes out, fight by 15:30Z, per-slot cargo before and loot after recorded. `-001` finished at 15:08:45Z, only 11 minutes before `-002` opens, so my own 'too soon' rule would have made `-002` skip itself; it is disapplied in `-002` only. `-003` to `-009` are unchanged. The dated open question for digest rule 9 ('shards preferably on the right') is in 2850 for the scribe.
