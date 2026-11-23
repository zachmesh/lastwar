---
title: Queue Planning The Builder Start Order Batching And The Trade Icon 3050 2026-11-23
created: 2026-11-23T13:00:00-08:00
modified: 2026-11-23T13:00:00-08:00
level: L0
version: 1.0.0
description: Planner pass applying the coordinator's answers to note 3040 - the start order of the builders, the two read-only units that may share a run, and the absent trade icon in the trucks and plunder briefs
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-1300-order-batching-icon
trigger: coordinator message 20:30Z
started_at: 2026-11-23T12:30:00-08:00
finished_at: 2026-11-23T13:00:00-08:00
verified: the pool ranking read with the tool's own pick_key at 23:20:20Z; the inbox searched for the read-only slot units, any survey unit and the trucks units; word counts under 450; validate exit 0
grounded_in:
  - source: coordinator message 20:30Z
---

# Start order, batching and the trade icon, 3050

## Order of the builder starts

Ground unit `building-queues-growth-convert-2026-11-24-001` (two starts in one run) now expires 23:45Z, the Oil Well unit `building-queues-oil-well-2026-11-24-001` 23:50Z and ground unit `-002` 00:20Z, so the pool ranks them in that order at the 23:20:20Z dispatch (checked with the tool's pick_key). The Oil Well unit says that the ground unit runs first and does the Completes; ground `-002` and the five fills name the new order. Each of the three opens at 23:20:15Z. The final order is confirmed with the Strategist's pick, which also sets the pre-conversion total T.

## Batching

Only one pair is clean: `building-queues-slot-read-2026-11-24-001` and `research-slot-read-labs-2026-11-24-001` (02:10Z to 04:30Z, both read-only and in the same family) carry the line that they may share a run, together at most 14 steps or 12 minutes, and that a first read over 8 steps means running the other separately. The barracks read stays alone, because two is the limit. I staged no pairing for the secrets units: there is no survey unit in the inbox, and the secrets units can claim. The units that complete, start, convert, collect or fight carry no sharing line.

## The trade icon

The trade icon (107,580) has been absent since 16:39Z. The three trucks units (22:57Z wave, 00:30Z, and the old 18:57Z unit) and the eight plunder scans of 2026-11-24 now say to look for it first, since the 02:00Z reset may return it, and to close 'blocked by route: trade icon absent' with the frame if it is missing, searching no other route. If the first scan at 02:30Z finds it absent, the later scans would each be a blocked run behind the 300 second gate: the coordinator can hold them until the icon is seen.
