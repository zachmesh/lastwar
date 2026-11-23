---
title: Coordinator seat handover
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-23T15:29:00Z
level: L2
version: 0.15.0
description: The live state a replacement coordinator starts from - holder, roster, operating rules, the growth Epic, in-flight landings and open decisions
status: unverified
grounded_in:
  - source: coordinator ticks _records_/2026-11-22/team-operations/2011-tick.md to 2228-clean-branch.md
  - source: privacy finding _records_/2026-11-22/team-operations/2222-privacy-finding.md
---

# Handover - coordinator

Updated 2026-11-23 14:35Z (Mac UTC; quote `date -u`). Earlier versions are in git history.

## Holder, clock, roster

- Session `session-4b4cb08d-fb77-419a-be34-14a72a3b73d1`. Loop clock `schedule-53b1277f-4e75-4e35-ae7b-ce379f0b53b0` (900 s, runs `tool_sync.py`, `model_guard.py --apply`, then `queue.py next`); daily `schedule-e1887d97` 12:00Z (word-budget watch; wakes the Coach and Planner); weekly `schedule-fee71877`.
- TEAM.yaml 0.7.2, 10 seats; operator `session-c08193d1-e6c0-489e-aa09-f812877c65ec`. Steer A (`session-eb024f72-e661-4a77-9303-66af95dbcfd1`) and Steer B (`session-e127662e-07ba-4385-b905-3d0e90fd1eeb`) relay the owner; they settle collisions between themselves.

## One-shot triggers (each dispatches the operator BY NAME; check the desktop lock first)

Builders 2026-11-24T09:21Z `schedule-f3804b22` (B1 Oil Well L1 to L30; three slots by the Strategist's pick, due 08:00Z); Food Output V Complete 17:30:30Z `schedule-de14b612`; forecast-refusal flip 2026-11-24T00:05Z `schedule-41383442` (preconditions in its prompt). A TIPS 'active on a different device' dialog means STOP: never Confirm without the owner.

## Respawn checklist

Past 85 percent context, with the seat's handover under 500 words: `python3 _tools_/spawn-seat/spawn_seat.py --title '[Last War] <Seat>' --prompt-file <bootstrap>` (model fixed from TEAM.yaml, read back, fails loudly; never a bare spawn). Then record the new id in TEAM.yaml, the seat's handover and /tmp/lw-new-operator-id.txt, tell Steer A, stand the old session down. The bootstrap points to the handover and the route card.

## Landings (Integrator; branch names, never push local main)

Local main is origin plus my unlanded commits. Deliver: stage explicit paths, commit, `git branch land/records-<UTC> HEAD`, verify in a CLEAN worktree (`check --base origin/main`) and with the whole-tree scan (`/tmp/lw-scan-branch.py`, git archive, wrap-aware), hand the branch name over; after each merge `git fetch && git rebase --autostash origin/main`. Nobody runs checkout, switch, reset or stash in the live tree (incident 2612).

## Facts to carry

- Research speed MEASURED: divisor 3.678 (plus 268 percent); read the Finish Now clock, not the Research button. Speed-up stock exceeds the natural path, so oil limits the date if the stock is spent.
- Standing rule (Steer A, 2026-11-23): any test or action that could open another app, browser, store or payment surface needs Steer A's approval in advance with an exit plan; an unexpected foreground switch stops the run; consent requests are human-only; only the operator seat and the bridge touch the desktop (every other seat, `lsappinfo front` read-only at most: no osascript, no System Events).
- Owner orders: Base Expansion first (OD-18, -19, -22); trade truck plunder re-enabled with a casualty guard (OD-20).

## Open owner decisions

OD-20261123-21: was the second device the owner (likely yes)? D-066: the owner-idle opt-out versus the cu team's request (`work/owner-idle-restore` held at the Integrator).
