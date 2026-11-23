---
title: Queue Planning Build Unit And Trophy Brief 2322 2026-11-22
created: 2026-11-22T23:22:00-08:00
modified: 2026-11-22T23:22:00-08:00
level: L0
version: 1.0.0
description: Planner pass after the coordinator's three releases - the build unit minted once the builders digest was amended, the trophy unit given the researcher's operator paragraph and the Likes decision, and the 09:00Z plan approved without running plan
status: done
activity: queue-planning
run_id: queue-planning-2026-11-22-2322-build-and-trophy-units
trigger: coordinator message after A-20261123-0706, three releases
started_at: 2026-11-22T23:19:00-08:00
finished_at: 2026-11-22T23:22:00-08:00
verified: both units read back; validate exit 0; run order simulated with the tool's pick_key and units, none expiring unrun
grounded_in:
  - source: _activities_/building-queues/rule-digest.md rules 2 to 4, read before minting
  - source: _records_/2026-11-22/research/mid-base-trophy-bubble.md, unverified, read in full
  - source: coordinator releases for OD-20261109-02 and OD-20261123-01
---

# Build unit and trophy brief, 2322

## 1. Build unit minted

`building-queues-2026-11-23-0720`, priority 2, 10 minutes, `not_before` 2026-11-23T07:30:00Z, `expires_at` 2026-11-23T10:03:00Z. The digest I read before minting carries the Builders Hut Lv.25 to 26 decision (rule 2), the idle-builder standing rule (rule 3) and the bans on Finish Now, diamonds and speed-ups (rule 4). The brief tells the operator to re-read the builders first. The builders were 4 of 4 busy at 06:51Z, so if none is idle the unit starts nothing and records every timer and the earliest finish. That finish time is what the next build unit is scheduled from.

The commit shown for the digest in this checkout is 8aa62206; the coordinator named d5844298. I checked the text, not the hash.

## 2. Trophy unit

`scout-midday-2026-11-23-0712` now carries the researcher's operator paragraph verbatim and the coordinator's additions: the Likes on podium players are allowed as claims, never Challenge, Battle, a rank or fight entry, report whether Like buttons are present and the diamonds before and after. The identification is the researcher's best fit, the Arena, and is unverified. The earlier "Not yet landed" slot is gone.

## 3. Run order

At 3.0 minutes per unit the build unit starts about 07:30Z, Season Photo about 07:45Z and the trophy unit about 08:00Z. All 14 units run before 10:03Z with none expiring unrun, and at each unit's estimate the starts move by up to 3 minutes.

## 4. Approved

The 10:48Z to 14:03Z catch-up set at my next pass, cap 12, without `plan --hours 8`.
