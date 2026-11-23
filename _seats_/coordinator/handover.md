---
title: Coordinator seat handover
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-23T07:27:00Z
level: L2
version: 0.6.0
description: The live state a replacement coordinator starts from - holder, clock, operating rules, in-flight work, the privacy finding and open owner decisions
status: unverified
grounded_in:
  - source: coordinator ticks _records_/2026-11-22/team-operations/2011-tick.md to 2228-clean-branch.md
  - source: privacy finding _records_/2026-11-22/team-operations/2222-privacy-finding.md
---

# Handover - coordinator

Updated 2026-11-23 06:31Z. Earlier versions are in git history.

## Holder and clock

- Session `session-4b4cb08d-fb77-419a-be34-14a72a3b73d1`, since 2026-11-23T04:04Z. Only loop clock `schedule-53b1277f-4e75-4e35-ae7b-ce379f0b53b0` (900 s). One-shot Secret Missions claim reminders remain at 06:51Z (`schedule-2227f411-6d4c-4eb9-b260-3df69eca2e79`) and 08:51Z (`schedule-7565d79f-3d26-4c36-a3f9-54375f517d85`).
- Owner gateway: Steer A (formerly the Steward) `session-eb024f72-e661-4a77-9303-66af95dbcfd1`, outside the roster (owner-gateway, steer, watchdog); it feeds the board and relays owner decisions and is NOT the integrator. Landing on the protected main: hand a LOCAL BRANCH NAME to the integrator seat `session-bc838015-7852-464e-8cab-cf2fcc70a335` (9 roster rows). Operator `session-7f6dd658-ebba-4854-9a29-e2f173975825` (respawned 07:03Z at 90 percent context; respawn when an operator passes 88 percent). The relay cannot reach child sessions. Check the target id against the draft before every send.

## How a tick runs

`queue.py next`, check, dispatch in one turn; one unit, one run, one reply; chain on each verified reply; no-op while the operator plays. Sonnet, 8-step cap (7 execute: budget must-execute actions by step 7), never zoom, one action per turn. Pre-start: `killall -9 UserNotificationCenter NotificationCenter`, `lsappinfo front` names LastWar. First-frame rule: a "Boarding closes in" banner with 70 s or more left means board first (standing owner order). OWNER RULES (2026-11-23): never stop the game, no play holds (06:42Z); decide operational choices yourselves and tell the Steward in one line afterwards, never ask the owner (06:47Z). Account-elsewhere dialog: Confirm is approved as a standing rule (OD-20261123-05, answered), but if it returns within 30 minutes of a Confirm do NOT Confirm again, pause desktop play 30 minutes, retry without asking. Still fixed: no purchase or diamond spend, no PvP/attack/rally/march/Arena/General's Trial, no diplomacy, no ally-exchange trade, no identifier values.

## Size and gate

The commit gate is installed (`core.hooksPath`; rollback `git config --unset core.hooksPath`) and blocks any real edit to a document of 500 body words or more. Registers are split (`owner-decisions-log`, `improvements-log`; the coach writes dated notes to the daily retro). The scribe redacts then splits each profile with a rule digest; 20 remain (blocks of three).

## Privacy (OD-20261123-04)

The public repo holds the owner account name and alliance tag from before the team. Never write them, nor alliance or allies' names; counts and paths only in messages. The local denylist is `.git/privacy-denylist.txt` (17 regexes, untracked). Owner decided 2026-11-23: only the owner's own name is redacted, tree-wide, by exception to C1; history is not rewritten; the repo stays public. Never push local `main` (it is a different, shallow-clone line): the integrator lands snapshot branches built on the tip of `origin/main`.

## In flight

Toolsmith privacy check (06:55Z); scribe radar-tasks and survivor-intake (07:35Z); sweep pair for 11-24 staged; Zombie Siege watch for 01:10Z to 02:00Z on 11-24 (server time is UTC-2, so the siege is 01:15Z); Alliance Exercise watch 22:55Z on 11-23; Winter Battlefield held for OD-20261123-03.

## Open owner decisions

None: all were decided by the owner on 2026-11-23 (see the articles' decision lines). Fixed lines remain: no PvP, ally exchange, diplomacy, purchase or diamond spend.

## Lessons

Take `next` without re-reading history. Play records are immutable. A scan covers every identifier class, with regex semantics.
