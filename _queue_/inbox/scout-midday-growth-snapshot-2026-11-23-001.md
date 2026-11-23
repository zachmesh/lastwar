---
unit: scout-midday-growth-snapshot-2026-11-23-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-23T07:48:54Z
expires_at: 2026-11-23T10:58:00Z
planned_for:
not_before: 2026-11-23T09:05:00Z
window: growth snapshot P1 read only never press Upgrade
est_minutes: 6
chain_id: growth-snapshot-2026-11-23
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (planner, growth snapshot P1, Story 868, from the scout protocol)

serves: snapshot (Story 868)

Read-only unit P1, order 1. Question: What do Total Power and every category read, and what are the builders doing?

Route: Base HUD power figure (top bar), one tap, Power Details panel; swipe the panel up for lower rows; panel X; hammer icon (about 108,200 in the 1920x1080 frame), BUILDING QUEUE panel; panel X (about 612,237).

Read: Total power; every category and sub-row, chevrons expanded; four builder slots with target and time left; hammer count.

Budget: at most 8 steps and 6 minutes. Notes: Never batch-tap near the HUD power figure; do not press Power Up. Screenshot after each scroll. If the panel does not scroll write single screen. Run daily as well as weekly. Record Total Power with the UTC time of the capture, in a fixed state (no troops marching), as the control for the power baseline.

Stop rules from `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md`: S1 never press Upgrade, Finish Now, Speed Up, Construct, Research, Train, Hire, Complete, Claim, Quick Dispatch, Promote or Equip. S2 read a diamond or price figure, never tap it. S3 stop at any march, attack, rally, Arena or PvP surface. S4 close any Confirm dialog with Cancel or X. S5 close a preview only by X or left-edge swipe-back, never a low tap (one once hit Upgrade, +14,800 power). S6 two failed taps on one target end the unit as partial. S7 no owner name or ID; skip profile and ranking screens.

If this unit reads the HUD, run `python3 _tools_/resource_map.py snap food=<n> iron=<n> coin=<n> --note <this unit id>`. The tool reads only plain numbers with a K or M suffix: write 1.1G as 1100M and 732.3M as 732.3M, because a G suffix crashes it with a ValueError. Do not enqueue a chain successor; the planner owns this chain.

Red lines: no purchase or diamond spend, no PvP, attack, rally, march, Arena fight or General's Trial fight, no alliance diplomacy, no ally-exchange trade, no speedup or Finish Now, no owner name or identifier values in any record. Any such surface stops the unit as needs-owner.
