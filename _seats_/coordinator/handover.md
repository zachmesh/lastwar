---
title: Coordinator seat handover
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-23T04:55:00Z
level: L2
version: 0.4.1
description: The live state a replacement coordinator starts from - holder, clock, operating rules, in-flight work and open owner decisions
status: unverified
grounded_in:
  - source: coordinator ticks _records_/2026-11-22/team-operations/2011-tick.md to 2043-tick.md
  - source: lint audit _records_/2026-11-22/team-operations/2036-lint-audit.md
---

# Handover - coordinator

Updated 2026-11-23 04:48Z. Earlier versions are in git history.

## Holder

- Session `session-4b4cb08d-fb77-419a-be34-14a72a3b73d1`, since 2026-11-23T04:04Z.
- Only clock: `schedule-53b1277f-4e75-4e35-ae7b-ce379f0b53b0`, every 900 s.
- Owner gateway: the Steward `session-eb024f72-e661-4a77-9303-66af95dbcfd1`, outside the roster. It held this seat before and no longer dispatches.
- All eight seats are top-level sessions. The operator is `session-b718c7de-6aab-4159-b87e-41aa424237e9`; the old child `238b9ce7-...` is stood down. The relay cannot address child sessions.

## How a tick runs (owner speed rules, duties.md 0.2.0)

`queue.py next`, eligibility check and dispatch in one turn, under 60 s. One unit, one run, one reply. Chain: each operator reply is verified, then the next `next` unit is sent at once. The 900 s clock is only the backstop; if the operator is busy, record a no-op. Routine runs use `claude-gateway/claude-sonnet-5-5` and `--max-steps 8`. Every unit starts with `killall -9 UserNotificationCenter NotificationCenter` and `lsappinfo front` naming LastWar. The owner's Screen Sharing must be View Only; a run paused by local input is closed partial within 2 minutes. At most two seats run model turns at once.

## In flight

- Toolsmith `A-20261123-0437`: `_tools_/lint-gate/` (check, install, watch, record-check), due 05:20Z. After review, run `install`.
- Operator: a one-pass trim of its over-limit records (measured rows to sidecars, narrative untouched), then back to play. Next unit: `secrets-2026-11-22-1857`.
- Not yet assigned: planner stages a duel-score read before the 02:00Z rollover on 11-24; scribe pilot split of alliance-donations; planner and scribe on IMP-20261123-04.

- One-shot claim reminders for the Secret Missions deploy of about 04:50Z: 05:21Z, 05:51Z, 06:51Z and 08:51Z (ids in `2049-tick.md`). Each sends the operator a claim-only assignment; unclaimed finished tasks get plundered.

## Open owner decisions

OD-20261109-02 (what the 4 idle builders build, Issue 517); OD-20261123-01 (the mid-base trophy bubble, possibly the Arena, never tapped); OD-20261122-01 (live pool recovery); INDEX.md for 450 records folders; hourly day-index files.

## State

Queue inbox 22, claimed 0, done 2,627. Open improvements IMP-20261123-01 to 04. My commits are local and unpushed; the Steward owns the push route.

## Lessons

Never dispatch by an id the relay cannot reach; verify with `session-relay list`. Take `next`'s unit without re-reading history. Play records are immutable; only measured rows may move to sidecars.
