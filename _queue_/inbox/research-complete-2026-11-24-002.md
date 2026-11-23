---
unit: research-complete-2026-11-24-002
regular: research
activity: research-queue
segment: 1
priority: 1
created_at: 2026-11-23T13:01:55Z
expires_at: 2026-11-24T19:30:00Z
planned_for:
not_before: 2026-11-24T17:30:10Z
window: lab 1 food output v completion about 1730z then iron output v
est_minutes: 10
serves: PL-04
chain_id: complete-2026-11-24
chain_seq: 2
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# research

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: capacity source: lab 1 Food Output V completion and Oil Output I level 1

## Brief (planner, 17:30Z research chain: Complete Food Output V, the second tech spend on Iron Output V, Oil Output I level 1)

serves: PL-04

Facts [M]: Food Output V (lab 1) ends about 2026-11-24T17:29:58Z; Iron Output V (lab 2), started 14:00:54Z for 131,879 s, ends about 2026-11-25T02:38:53Z, 549 minutes later. The research divisor is 3.678. Read the FINISH NOW clock, not the blue Research button, as an Age of Oil node's effective time. A TIPS dialog about another device: STOP, report. Routes and stop reasons, with the Age of Oil tree route (the running node's icon at (456,925), never (603,925)): `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`.

1. Read both labs (tag text, timers to the second). Press COMPLETE on Food Output V; Total Power before and after.
2. Second tech spend, approved if the preview shows the finish time before confirming: on Iron Output V in lab 2, TECH items only (blue-disc), about 550 minutes (8h x1, 1h x1, 5m x2) so both labs finish together. Read item name and quantity before each press (reduce a default) and the new finish time in the preview before confirming; log inventory before and after (tech 9,895 minutes before). Skip it, saying why, if the preview shows no finish time or the spend exceeds 600 minutes. If Iron Output V then finishes, COMPLETE it.
3. Oil Output I level 1 (needs Food, Iron and Coin Output V at level 1; base 679,140 s, about 51 hours): read oil (at least 60,000 needed) and the preview (iron 3.7M, food 3.7M, coin 11.2M). Coin: N = ceil((node coin + 10M floor - coin now) / 2.4364M) UR chests, STOP above 40; the Resources tab opens with the 5,000 Diamonds x16 tile SELECTED: confirm the tile name, read the number field AND the Total line before Use. Press Research once in the free lab; read the timer and oil. If Iron Output V is not done, start nothing here; the fallback for an idle lab is a Special Forces +15K node, no speed-up.
4. Never Finish Now.
Up to three runs.
Quiet-window margin: 9 h 05 min (17:30:30Z trigger) after the daily 08:25Z end; see `_records_/2026-11-22/queue-planning/2830-quiet-window-margins.md`.
Cost cap, stated: 0.90 USD per run (the harness stops near 0.36 of it).
