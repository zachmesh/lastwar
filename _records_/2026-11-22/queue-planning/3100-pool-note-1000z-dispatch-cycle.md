---
title: Queue Planning Pool Note 10:00Z And The Dispatch Cycle 3100 2026-11-24
created: 2026-11-24T02:10:00-08:00
modified: 2026-11-24T02:10:00-08:00
level: L0
version: 1.0.0
description: Planner pass at 10:00Z on 2026-11-24 - the plan for the 10:57Z group and the 14:03Z wave, the retirement of the roster donations and trucks units, the dispatch cycle staged from estimates, and the pool state
status: done
activity: queue-planning
run_id: queue-planning-2026-11-24-0210-plan-dispatch-cycle
trigger: coordinator ping 10:00Z and message 10:03Z
started_at: 2026-11-24T02:01:00-08:00
finished_at: 2026-11-24T02:10:00-08:00
verified: the inbox diffed before and after plan; the forecast check, the quiet window, the on-the-hour scan and a pool simulation to 14:00Z run; word counts read back; validate exit 0
grounded_in:
  - source: _records_/2026-11-22/queue-planning/3090-secrets-claims-train-preview-and-wave-0603z.md
---

# Pool note 10:00Z and the dispatch cycle, 3100

## The plan

`plan --hours 4` minted only the 10:57Z group (a 4 hour horizon from 10:02Z ends before the 14:03Z wave), so a 5 hour pass minted the 14:03Z wave, the 14:30Z group, the 14:57Z group and the daily `scout-midday` unit (20 units; the 8 hour setting stays unused). The roster donations unit and the two roster trucks units were retired (the passes carry donations; own dispatch is the owner's daily quota and has its own units). Specifics went into 22 units: the radar dialog ruling, the three-class barracks read, the clipped Claim for passes, the Cancel-only TIPS rule, and the badge state of the vehicle-front icon at every left-column read.

## The dispatch cycle

`trucks-dispatch-2026-11-24-002` (14:15Z), `-003` (18:15Z) and `-004` (11-25 02:15Z) settle returned trucks and dispatch up to 5 of 5 by the verified route (tram icon, yard bubble, the Intercity Trade dialog). Their times are ESTIMATES from a 4 hour return: they are re-timed from the real arrival the operator writes. The count is 5 a day and resets at 02:00Z, so after the fifth dispatch the 18:15Z cycle only settles. The plunder list is still unlocated: the first dispatch run reads the screen that follows its Let's Go.

## Checks

53 units, all pass the forecast check; none opens or expires inside 08:00Z to 08:25Z on 11-24 to 11-26; a simulation to 14:00Z at 5 minutes a unit leaves none expiring unrun. Two units opened exactly on the hour (donation pass 14:00Z and the 15:00Z scout) and moved three minutes, because an owner-side job took the front at 10:00:05Z.
