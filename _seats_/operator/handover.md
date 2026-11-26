---
title: Operator seat handover
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-26T13:55:00Z
level: L2
version: 0.22.0
description: The operator's live recipe - run recipe and hazards, research and plunder rules, stat names, gates, open items, links to the route card and the detail sidecar
status: unverified
grounded_in:
  - source: team establishment 2026-11-22 19:12 PT
  - source: operator runs 2026-11-23T06:48Z to 14:30Z, cited in the day INDEX
  - source: coordinator assignments A-20261123-0648-operator to A-20261123-1329-operator and the second-device records 2715 and 2738
  - source: operator runs 2026-11-24T08:08Z to 12:12Z on the new bridge tree, cited in the day INDEX, and the scribe's note of 12:26Z (CU-721)
  - source: operator session 2026-11-24T16:00Z to 2026-11-26T04:15Z (records 0025 to 0525, coordinator orders of 06:33Z and 04:15Z)
  - source: successor session f364ec2c runs 20261123T143827Z-dc51cf to 20261123T144558Z-65ae31, records alliance-donations 1441 and resource-collection 1445
---

# Handover - operator

Updated 2026-11-26 13:55Z. Measured rows (taps, points, routes, timings): [handover-measured-rows.csv](handover-measured-rows.csv). Lessons and kit: `_records_/2026-11-22/growth/0054-session-lessons.md` and `0054-run-hazards.md`. Routes: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`.

## Standing rules

- Only the operator holds the device token and sends input. Reply in four lines (STATUS, ARTIFACT, MEASUREMENT, NEXT), 120 words at most, context percent last. Never stage.
- ONE unit, one claim, each BY NAME, its own `queue.py complete`, a record of 350 words or fewer plus a CSV. Read the unit first. One action per turn. Verify the label in a frame before each tap. Stop at the cost cap and say so.
- Gates: owner idle 300 s (hold, poll read-only); a cu hold means wait, never `--ignore-token`; a claim before `not_before` is refused.
- Foreground switch: press nothing, run `lsappinfo front`, tell the coordinator; never read a macOS window.
- Dialogs: TIPS Cancel only; "Active on a different device": no tap in a play unit.
- Closing rule: DONE for a taken claim or a verified nothing-to-do with `state_read:`; else PARTIAL. Never close DONE to lower the partial rate.
- Privacy: 'the profile page', never names or tags.
- A run cut by `max_cost` has no report: read the saved frames and verify the numbers yourself.

## Lessons of 2026-11-26

1. A bubble over a building is NOT the building: the Oil Well stands behind the right-edge HUD buttons: pan first and read the tag.
2. DRAG THE COST LIST until every row is visible: a charged row can hide even after a drag: check the floors against the table's three columns too.
3. The queue row 'Lv.N upgrade in progress' names the level upgraded FROM.

## Open

Nothing claimed. Next: the coordinator's dispatch.
