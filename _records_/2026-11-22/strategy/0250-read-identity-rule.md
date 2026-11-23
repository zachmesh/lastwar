---
title: Read identity rule
created: 2026-11-23T10:49:00Z
modified: 2026-11-23T15:26:00Z
version: 1.0.0
level: L3
description: Every building read records the tag text it came from, and a panel's numbers are checked against a level signature so a mis-tapped or misread building is caught
status: unverified
grounded_in:
  - source: Steer A red team round 9 of 2026-11-23 10:47Z and the base map _records_/2026-11-22/growth/1030-base-map.md
  - source: _records_/2026-11-22/strategy/0030-dg-level-table.csv, guide times 0.85 with five exact panel matches
---

# Read identity rule

Three tap-identity errors on one day: the Hospital read as Barracks Lv.20, a Farmland read as a Drill Ground, and a Tavern read as one. A tag can be wrong; a panel's own numbers are harder to fake.

## Rule

1. Every building read records the tag text (name and level) it was read from and the panel header text.
2. For a Drill Ground upgrade panel, check the numbers against the signature below. A mismatch between tag and signature flags the read and the level stays [G] until a re-read.
3. The coach checks the signature; the strategist does not use a flagged number in a ranking.
4. A negative ("there is no X") names its enumeration: a list, or a systematic pan of all four edges. One drag is not enumeration (H73).
5. The tap target for a Drill Ground is a soldier in the middle of its red parade field, not the building inside (the orange roof is a Tavern Lv.20) (H74).

## Drill Ground signatures (the next-level panel)

| Panel | Unit Count | Power | Coin | Iron | Time |
|---|---|---|---|---|---|
| Lv.26 to 27 | +7,200 to +7,400 | 118,600 to 140,200 | 59.5M | 74.8M | 10.1 days |
| Lv.27 to 28 | +7,400 to +7,600 | 140,200 to 165,800 | 83.3M | 102.0M | 14.2 days |
| Lv.28 to 29 | +7,600 to +7,800 | 165,800 to 196,200 | 119.0M | 144.5M | 18d 09h |
| Lv.29 to 30 | +7,800 to +8,000 | 196,200 to 232,000 | 161.5M | 204.0M | 23.9 days |

Lv.28 to 29 is measured (F1 0035); the Lv.26 to 28 rows rest on the 11-10 panels and the guide.

## Use now

F1b settled it: the F1 panel was a real Lv.28 ground (field 2, signature matched). The base map's two grounds were Lv.30 and Lv.27, and its orange building was a Tavern. That is the third tap-identity error of the day; the grounds are parade fields, tapped on a soldier, not on the building inside.

## Exit surfaces (Steer A rule, 2026-11-23 15:25Z)

A test or action whose possible effect includes opening another app, a browser, a store or a payment surface needs Steer A's approval in advance, with an exit plan: what is pressed if it happens and what is never pressed. The check-in banner Go opens a web store in Chrome (test T3): never press it. An unexpected foreground switch stops the run, nothing is answered, and the coordinator tells Steer A within minutes. No seat but the operator and the bridge touches the desktop; others use `lsappinfo front` at most, never osascript or System Events. My plan rows carry no such test.

