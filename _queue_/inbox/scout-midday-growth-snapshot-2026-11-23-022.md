---
unit: scout-midday-growth-snapshot-2026-11-23-022
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-23T09:39:54Z
expires_at: 2026-11-23T10:30:00Z
planned_for:
not_before: 2026-11-23T09:40:00Z
window: age of oil stage 3 cards read and claim free rewards only
est_minutes: 10
serves: baseline Age of Oil
chain_id: growth-snapshot-2026-11-23
chain_seq: 22
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: baseline Age of Oil

## Brief (planner, Age of Oil stage claims read, coordinator instruction after the SC1 season-clock read)

serves: baseline Age of Oil

Source: `_records_/2026-11-22/perception-scout/0935-sc1-season-clock.md`. The Age of Oil page (stage 3 of 4) showed two cards far above target, ending 2026-11-30T02:00Z: Unlock Lv. 31-35 Zombies on World Map (3348/2000) and Rapid Rescue (674067/25000). Nobody has checked whether their rewards are claimable.

1. Open Events from the right-edge column, then The Age of Oil page. For each stage card read the task, its progress, its reward, and whether a green Claim button shows.
2. Press Claim ONLY for a FREE reward that needs no choice with a cost; a claim is not a purchase. This is the one exception to stop rule R1. If any prompt shows a price, a diamond, a choice or a confirmation about a cost, press Cancel or X, STOP and record the prompt text.
3. Record each card and what each claim paid (item and quantity). Read Total Power and the HUD before and after, and run the snap command.
4. On the Events list record only the names and timers of Desert Battlefield (New), Winter Battlefield and Wanted Boss. Do not enter them; Winter Battlefield is PvP.
5. Open question to answer if visible: the stage 4 timer or any main Age of Oil timer. Write what the page shows, or that none shows.

At most 8 steps and 10 minutes. Nothing bought, no speed-up, no Finish Now.

Rules: stop rules R1 to R7 in `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md`; red lines and the snap command in `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. Snap takes only K or M numbers: write 1.1G as 1100M. Do not enqueue a chain successor.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
