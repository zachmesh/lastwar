---
unit: scout-midday-growth-snapshot-2026-11-23-021
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-23T08:31:39Z
expires_at: 2026-11-23T09:54:00Z
planned_for:
not_before: 2026-11-23T09:05:00Z
window: growth snapshot ST1b read only nothing bought
est_minutes: 10
serves: snapshot (Story 868)
chain_id: growth-snapshot-2026-11-23
chain_seq: 21
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at:
  finished_at: 2026-11-23T13:45:50Z
  duration_seconds: 
  executor:
  summary: retired by the planner: the stores follow-up read was done by a direct assignment
  claimed: []
  claimed_count: 0
  evidence: 
  follow_up: none
  stats:
  stats_missing: [target, achieved, resources_gained, costs, verified]
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: snapshot (Story 868)

## Brief (planner, growth snapshot ST1b, Story 868, from the scout's unit table)

serves: snapshot (Story 868)

Read-only unit ST1b. Queue placement: right after ST1 (the store reads), ahead of the routine claims.

Question: What do the Season, Cosmetics, VIP and cut-off tabs sell, and where are the Black Market cash, Bond Badges, Guidebooks, Training Certificates and medals shown?

Route: Same entry as ST1 (avatar, VIP badge, cart at the VIP screen top right). Season tab (balance 800 on 2026-11-08), Cosmetics, drag the tab strip to the cut-off tab that starts with Cou, the VIP tab last (priced in red gems, read only). Then the base right-edge Alliance icon: read the Alliance Store entry and, in Alliance Techs, the contribution counter (a context slot). Back arrows in the last step.

Read: Per tab balance and name, every tile with item, currency icon, price, limit, refresh; the full name of the cut-off tab; for Black Market cash, honor, alliance contribution, campaign stars, crystals, medals, Bond Badge, Guidebook and Training Certificate, the screen and place that shows the balance, or not seen.

Budget: at most 8 steps and 10 minutes. Notes: Output _records_/<date>/growth/<HHMM>-st1b-stores.csv, schema m_store. Same stops as ST1; the VIP tab and VIP exclusive offer are read and left alone. Season, Cosmetics and the cut-off tab were never read in full. Known places: Skill Medal 9,521 and Amethyst Crystal sit in the Inventory (0009 read); Black Market cash is the page header, which BM1 reads. The Crystal Shop has never been located and is not in the Mall tab row (Official Event, Weekly Deal, passes, Diamond, Gold Brick Mall, Hot Sale Packs); the Mall is paid, never open it. If the Alliance panel Store icon opens something other than the STORE Alliance tab, read it as in ST1.

Rules: stop rules R1 to R7 in `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md`; red lines and the snap command in `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. Snap takes only K or M numbers: write 1.1G as 1100M. Buy nothing, open nothing, press no Claim. Do not enqueue a chain successor.

Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
