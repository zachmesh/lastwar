---
title: Queue Planning Quick Dispatch Probe And Owner Decisions Triage 2258 2026-11-22
created: 2026-11-22T22:59:00-08:00
modified: 2026-11-22T22:59:00-08:00
level: L0
version: 1.0.0
description: Planner pass for assignment A-20261123-0655 - a read-only Quick Dispatch probe unit minted, and the 15 open owner decisions classified into 8 operational and 7 fixed with a recommendation and checkable next step for each operational item
status: done
activity: queue-planning
run_id: queue-planning-2026-11-22-2258-owner-decisions-triage
trigger: coordinator assignment A-20261123-0655-planner after OD-20261123-05
started_at: 2026-11-22T22:54:20-08:00
finished_at: 2026-11-22T22:59:00-08:00
verified: probe unit read back and validate exit 0; every OD article read in full; drift check run read-only; record counts searched for the Halloween item
grounded_in:
  - source: _records_/2026-11-22/queue-planning/2258-owner-decisions-triage.csv, 15 rows
  - source: _records_/retro/owner-decisions.md and the 13 article files in owner-decisions-log, read in full
  - source: _activities_/survivor-intake/run-20261109-2358-p2.md and run-20261122-0932-p1.md, the two recorded Quick Dispatch presses
---

# Quick Dispatch probe and owner decisions triage, 2258

Rows are in [the CSV](2258-owner-decisions-triage.csv).

## 1. Probe minted

`scout-midday-2026-11-23-0656`, priority 2, 15 minutes, `not_before` 2026-11-23T07:05:00Z, `expires_at` 2026-11-23T12:30:00Z. It has the earliest expiry of any unit actionable then, so it ranks 1 of 2 at 07:05Z, ahead of the survivors and training units. `validate`: exit 0.

The records changed the brief:
- In the Iron Mine panel it was pressed twice with no dialog: a toast "no survivors available for dispatch" (11-09), then no change (11-22).
- The troop-side button sits in a barracks panel beside an instructor list, like the miner list. "May march troops out" (11-10 record) is a worry, never an observation.

So a Confirm dialog may not exist, and a press may act at once. The brief allows one press per part, cancels any dialog, and stops as needs-owner if nearby text names march, attack, rally or gather, or any troop leaves. **One exposure:** if no dialog exists, the first press in the barracks panel is the action. Drop Part B if you will not accept that.

## 2. Triage: 8 operational, 7 fixed

The register counts 15 open items, not 14; the three 11-23 items share one article.

- **Fixed (7):** OD-20261031-01, 20261101-03, 20261108-01, and 20261123-01, -02, -03, -04. OD-20261108-01 is borderline: split it, so the tool half merges and the mandatory-gate policy waits.
- **Operational (8):** each has a recommendation, reason and checkable next step in the CSV. In short:
  - **Halloween Day 07:** decide by expiry; no record in 19 days mentions it.
  - **Survivor method:** keep the intake, keep Quick Dispatch frozen until the probe is read.
  - **Event calendar:** build it from the To-do List.
  - **End-of-event results:** record them for watched events only.
  - **Batch checker:** choose merge-aware; `--merges` already exists in the tool.
  - **Drift check:** IN SYNC now, exit 0; the stale-copy refusal covers the single checkout.
  - **Old live pool:** accept the genesis reset as a data gap.

## 3. OD-20261109-02, weighed

Builders are 0 of 4 busy. The Hut costs iron 170.0M and food 56.9M against 1.1G and 732M in stock. It takes one slot for 7d 07h effective with power +17,500; three stay free. Research is a separate queue and does not compete for slots; its only coupling is that the Oil Well build is probably gated by Unlock Oil Well research, finishing about 11:43Z (inference). Recommended order: the Oil Well, then the Hut, with resources only and no speed-up or diamond.

**A blocker the operator would hit:** the building-queues rule digest items 2 and 3 still say starting an upgrade is the owner's choice and never tap Upgrade. The scribe must amend them first.
