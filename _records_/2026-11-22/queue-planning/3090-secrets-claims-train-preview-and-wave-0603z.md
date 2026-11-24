---
title: Queue Planning Secrets Claims The Train Preview And The 06:03Z Wave 3090 2026-11-24
created: 2026-11-23T19:55:00-08:00
modified: 2026-11-23T19:55:00-08:00
level: L0
version: 1.0.0
description: Planner pass at 03:40Z on 2026-11-24 - the three secret mission claim units, the read-only train preview for the free Drill Ground room, the replacement of the never retry the collect rule, the 06:03Z wave with the late 02:57Z group, and three more donation passes
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-1955-secrets-train-wave
trigger: coordinator messages 03:36Z and 03:40Z
started_at: 2026-11-23T19:37:00-08:00
finished_at: 2026-11-23T19:55:00-08:00
verified: the secrets digest read for the claim and deploy rules; the inbox diffed before and after plan; the forecast check, the quiet window and a pool simulation to 10:00Z run; word counts read back; validate exit 0
grounded_in:
  - source: _activities_/secret-missions/rule-digest.md
  - source: _records_/2026-11-22/perception-scout/0330-queue-run.md (as relayed)
---

# Secrets claims, the train preview and the 06:03Z wave, 3090

## Secrets

The Oil Depot was deployed at 03:35:16Z; `secrets-oil-depot-claim-2026-11-24-001` (priority 1, 07:35:30Z to 07:52:00Z) reads the card timer, claims only with the in-game Claim, and must end before 07:58Z or wait for 08:25Z. `secrets-refugee-claim-2026-11-24-001` (04:36Z to 06:36Z) and `secrets-rescue-claim-2026-11-24-001` (05:37Z to 07:20Z) claim and re-deploy with Mega Deploy, with no Mega Refresh, no spend and no Plunder Others, as the digest says. The old `secrets-oil-depot-2026-11-24-002` was retired. A re-deploy sets the next claim times (about 08:36Z, 09:37Z and 11:35Z): they are staged from the real timers, not estimates.

## The train preview and the rule

At 03:30:53Z the Lv.27 batch of 726 collected without refusal because the siege's 1,000 wounded left the army: about 274 room is left. `training-train-preview-2026-11-24-001` (priority 2, 04:00Z to 07:50Z) reads the Train panel of an idle barracks (tiers, cost, time, power per troop, slider maximum, then the Total lines at 274) and never presses Train, Confirm, Speed Up, Buy, Use or Collect. The Strategist decides whether to train. The wording 'a finished batch is never retried while the Drill Ground is Full' is replaced in the roster units by 'collects only when the free room covers it'; the dedicated collect unit, when it is staged after a ground level completes (the Lv.26 ground ends 11-26T21:10:37Z), tries one Collect tap and records the toast.

## The wave

`plan --hours 4` minted 24 units and reaped 14 expired ones. It minted the 06:03Z wave, the 06:30Z group, the 06:57Z group, and also the 02:57Z group (events, passes, secrets, treasures, trucks) that my 22:33Z plan missed because its horizon ended at 02:33Z; the late group has about three hours left. The roster donations unit was retired; donation passes `-005`, `-006` and `-007` (10:30Z, 14:00Z, 17:30Z) carry the schedule. All 68 units pass the forecast check, none has an expiry or opening inside 08:00Z to 08:25Z on 11-24 to 11-26, and a simulation to 10:00Z leaves none expiring unrun.
