---
title: Team Organization
created: 2026-11-23T04:03:00Z
modified: 2026-11-23T04:03:00Z
level: L2
version: 0.1.0
description: How the eight top-level DSH seats of the Last War team are organized - roles, cadence, communication contract, failure playbooks, migration and acceptance
status: unverified
grounded_in:
  - source: owner request 2026-11-22 to organize the team and establish UI-visible DSH sessions
  - source: TEAM.yaml 0.3.0 with the six top-level seats created at 2026-11-23T04:01Z
  - source: continuous-play-team.md 0.1.0 and the reflection session-team v3 convention
---

# Team organization

This page is the organization plan for the team. `TEAM.yaml` is the
live roster; this page explains how the roster works, how work moves,
what each seat may write, how failures are handled, and how the
current child-session team migrates to top-level DSH sessions.

## 1. Principles

1. **One seat, one session, one owner.** A seat is a stable position;
   its session is the current holder. A title is a label, not an
   authority.
2. **The repository is the single source of truth.** A chat reply is
   not a record. Queue state, records, knowledge and conventions live
   in this repository; the session is the worker.
3. **One device, one operator.** Only the operator seat may hold the
   device token or send input to the game. A second input path is a
   defect.
4. **Disjoint write scopes.** A seat writes only its own scope. A
   cross-scope change is a proposal to the owning seat.
5. **Coordinator routes, does not play.** The coordinator owns the
   clock, the assignment and the owner gateway; it may read and
   measure but does not take a play unit.
6. **Bounded assignments.** Every assignment names a question, the
   expected artifact, a completion condition, a deadline and a cap.
   A seat stops when the condition is met.
7. **Measure the work and the system.** L1 execution, L2 discovery and
   L3 improvement are measured from records, never from impressions.

## 2. Roster

Eight seats; the coordinator plus seven roles. All eight are now
`assigned` in `TEAM.yaml` with a session id.

| Seat | Session | Mission | Primary output | Cadence |
|---|---|---|---|---|
| coordinator | `session-4b4cb08d-fb77-419a-be34-14a72a3b73d1` `[Last War] Coordinator` | clock, routing, roster | tick record, assignment, TEAM.yaml | 15 min |
| operator | child `session-238b9ce7...` until migration | play one bounded unit | unit result + per-unit record | every tick |
| scout | `session-d658da6d-95f9-4762-9648-b4e208b55c08` | perceive the whole surface | observation pass, candidate list | every 2 h |
| researcher | `session-4335084a-3125-486d-9b61-03d23737b5f7` | internet + local reasoning | research note with a falsification test | 2 per day |
| planner | `session-c2652e1a-8fa4-4468-8d44-6d351762ed67` | queue hygiene and staging | planner record, clean queue | hourly |
| coach | `session-953a3676-cf57-4be2-8008-0ee9bc294d2d` | measure, retro, improve | dashboard, retro, backlog | daily |
| toolsmith | `session-339995b4-ebd2-4710-94a1-fcc946be01cf` | tool and automation fixes | tested diff, PR | on assignment |
| scribe | `session-c104e601-b16b-49cf-95a7-888543eb2499` | fold knowledge, integrate PRs | profile/PR | on assignment |

### The Steward and the Coordinator

The owner's root session is the **Steward**, `session-eb024f72-e661-4a77-9303-66af95dbcfd1`,
titled `[lastwar] Steward`. It is the owner gateway, not a seat: it holds
no write scope, takes no assignment, and runs no loop schedule. It
relays owner instructions and approvals to the Coordinator and receives
`needs-owner` escalations.

By the reflection convention every team has exactly one **Coordinator**.
The Coordinator is a separate top-level seat
(`session-4b4cb08d-fb77-419a-be34-14a72a3b73d1`) that owns the 900-second
loop clock, dispatches the other seats and keeps `TEAM.yaml`. The
Coordinator seat was moved from the Steward to its own session on
2026-11-23T04:04Z; the Steward deleted its old 900-second schedule in the
same turn, so there is exactly one clock.

### Seat briefs

**Coordinator.** Reads the newest queue/ticker record and the coach's
dashboard. Picks exactly one next act per tick. Sends one bounded
assignment through `session-relay send`. Verifies the artifact exists.
Appends the tick record. Reviews one seat per day. Reconciles
`TEAM.yaml` with the actual sessions. Escalates owner-only decisions.

**Operator.** Reads the unit and its activity profile. Acquires the
device token and the claim. Starts exactly one computer-use desktop
run. Stops at any consequential surface. Verifies on a fresh
observation. Completes the unit with full stats. Writes the per-unit
record. Never approves an app, a purchase or a send.

**Scout.** Sweeps the base edges, event hub, activity panels and red
dots. Appends one observation section through `observation.py`. Files
candidate profiles for unowned elements. Never claims a reward and
never sends game input.

**Researcher.** Takes two questions per day from the scout's
unexplained items and the coach's top leaks. At least two independent
dated sources. States one local observation that could falsify the
claim. Writes a note with a verdict; only a supported verdict may
propose a rule.

**Planner.** Snapshots the pool, reaps and expires stale units, stages
the next window, proves the pass with `validate`, `slot_coverage` and
`sweep-status`. Never executes a game task. A stale unit is never
played because it is old.

**Coach.** Builds the day's data appendix, computes L1/L2/L3, runs the
retro, maintains the improvement backlog and the dashboard. A closure
needs a moved metric or a passed verification; an edit alone never
closes.

**Toolsmith.** Implements the smallest tool change that moves a named
metric. Checks the held-patches register first. Tests on an isolated
fixture. Opens a PR with the improvement id, target metric and
validation.

**Scribe.** Folds verified records into activities and knowledge with
a version bump and a changelog line. Never rewrites a play record.
Lands load-bearing changes by PR.

## 3. The clock

| Time | Owner | Act |
|---|---|---|
| every 15 min | coordinator | one tick: read, assign, verify, record |
| every 2 h | scout | one perception pass |
| 16:00 and 17:00 | scout/planner | pre-reset sweep pair (roster `[120, 60]`) |
| hourly | planner | pool hygiene and staging |
| 18:20 | coach | daily retro and dashboard |
| Sunday 18:30 | coach/coordinator | weekly improvement review |
| on assignment | operator/toolsmith/scribe | the bounded unit |

The coordinator's schedule is the only recurring schedule. Delegated
sessions cannot create their own schedules, so the coordinator wakes
them with `session-relay send` and collects the reply. A seat that is
idle is not a stopped loop.

## 4. Assignment and reply contract

Coordinator to seat:

```
ASSIGNMENT <id>
Question: <one sentence>
Evidence expected: <artifact path or measurement>
Completion condition: <what makes it done>
Deadline: <local time or tick>
Write scope: <paths>
Cap: <minutes, steps, cost>
```

Seat to coordinator:

```
STATUS: done | partial | blocked | no-op
ARTIFACT: <repository path or none>
MEASUREMENT: <the number the assignment asked for>
NEXT: <one bounded next action or none>
```

A reply without an artifact or a measurement is `partial`, not
`done`. Chat text alone never closes an assignment.

## 5. Work priority

1. **Incident** - the game is down, the control lock stands, the queue
   is corrupt, or a session is gone. The coordinator handles it before
   any play.
2. **Owner request** - an explicit owner instruction.
3. **P1 window** - a pre-reset sweep or a unit whose deadline is
   close.
4. **L1 play** - the next queued unit.
5. **L2 discovery** - perception and research.
6. **L3 improvement** - tools, knowledge and meta-work.

The queue is the only task list. Do not create a second list in chat
or in a seat folder.

## 6. Measurement and review

The coach owns the daily dashboard and the retro. The three families
are fixed in [evaluation metrics](evaluation-metrics.md) and extended
by [continuous play](continuous-play-team.md) section 2.

- **Daily** - L1 done rate, unverified, duration, attempts; L2 ledger
  coverage and red dots; L3 open/closed and recurrence.
- **Weekly** - compare the week with the previous one; name one
  meta-change; review one seat per day in rotation.
- **A metric without a source** is a data gap, never zero.
- **Association is not causation.** A tool landing is reported with
  the before/after windows and the game-change confounders named.

## 7. Failure playbooks

### The game is not frontmost

A notification or another app in front makes a click land on the wrong
app. The computer-use policy refuses it (`excluded:terminal`) or the
run is handed over. Before a play run: activate Last War, dismiss
NotificationCenter, verify `lsappinfo front` names LastWar. If it does
not, do not claim or start; report `blocked: foreground`.

Measured 2026-11-22 20:03 PT: `com.apple.UserNotificationCenter`
(`/System/Library/CoreServices/UserNotificationCenter.app`) can hold
the global front slot for days and flip back within a minute, while the
screen shows no dialog. A click whose hit-test target is Last War is
still refused with `excluded_front:os_security`. The working fix is to
run `killall UserNotificationCenter NotificationCenter` in the same
shell immediately before the run start, then verify `lsappinfo front`
names LastWar. A read-only observation is the cheap probe: if its
`last_step` says `looked at app:lastwar.ios`, the front slot is clear.
The longer-term fix - judging `excluded_front` on the click's hit-test
target rather than the global front app - is a computer-use policy
change and needs the owner's call.

### App approval

The owner approves `com.lastwar.ios` once with **Always allow**. The
approval is persistent. A run that waits for `new_app` is `blocked`,
with the control link; the seat never approves it.

### Control lock

Three fresh sessions failing at the first input is a control lock. The
operator stops, records `blocker_overlay=control-lock`, and the
coordinator lifts it only after four hours or a new observation.

### Stale tool

`queue.py version` must read `currency: current`. A stale copy refuses
`enqueue`, `sync`, `plan`, `sweep` and `next`; land the tool change by
PR or run decisions from a fresh main worktree. Never set the
stale-tool bypass in production.

### Queue debt

A main-checkout queue can be a stale snapshot. Measure the live pool
from the day index and the records branch. A reset is a genesis reset:
expire old units, keep the current and next windows, never backfill.

### Session death

A seat whose session is gone is replaced by the coordinator through
the DSH client RPC. The seat record and `handover.md` are the
replacement's first read. The old session id is recorded in the
handover, never reused.

### Mac load

One desktop run at a time; two browsers team-wide; the memory floor is
25 percent. If free memory is low, stop the run and report; do not
start a second agent to "help".

## 8. Migration from child sessions

The first team used delegated child sessions. The organization now
moves to top-level DSH sessions, created through the DSH client RPC
with the local gate:

| Phase | Act | State |
|---|---|---|
| M0 | spawn six top-level seats (scout, researcher, planner, coach, toolsmith, scribe) | done 2026-11-23T04:01Z |
| M0b | spawn the top-level Coordinator; move the seat from the Steward; delete the Steward schedule | done 2026-11-23T04:04Z |
| M1 | verify each seat reads its brief and replies | in progress |
| M2 | after the operator's current unit closes, spawn `[Last War] Operator`; update its session id | pending |
| M3 | record the child sessions as predecessors in each handover; stop using them | pending |
| M4 | first full-team tick through `session-relay`; 24 h pilot | pending |
| M5 | weekly review: keep top-level or roll back | pending |

Rollback: if a top-level seat fails, revert its `TEAM.yaml` id to the
child session and record why. The child sessions remain until the
pilot passes.

The top-level sessions are created with:

```bash
DSH_WEB_URL=http://localhost:8080 SESSION_RELAY_JAR=/tmp/dsh-gate.cj \
  python3 ~/dtadpole/reflection/_tools_/session-relay/session-relay.py spawn \
  --workspace /Users/zhenchen/zachmesh/lastwar --title '[Last War] <Role>' \
  --prompt-file /tmp/lw-<role>-bootstrap.md
```

The gate supplies the cookie; no seat reads the DSH launch token.

## 9. Capacity and resource budget

- **Sessions** - maximum 8 top-level seats; no nested team.
- **Desktop runs** - one at a time, team-wide; the lock is the
  serialization point.
- **Browser runs** - two team-wide (computer-use D-014).
- **Model turns** - at most two seats in a model-heavy turn at once;
  the coordinator staggers the rest.
- **Run caps** - a play unit 15 minutes, 20 steps, 1 USD unless the
  assignment says otherwise.
- **Memory** - free memory below 25 percent stops a browser launch;
  the coordinator reports it rather than adding a run.

## 10. Governance and safety

- C1 to C5 of dtadpole/reflection govern; this page does not amend
  them.
- Purchases, alliance diplomacy, PvP attacks and premium-currency
  spends need the owner's approval first.
- The account is `owner account` in public content; screenshots with
  other players' names stay local and are not committed.
- The LAN control proxy exposes a control token to the local network;
  it is temporary, trusted-network only, and stopped after use.
- A seat never stores a credential, a token or a launch URL in the
  repository.

## 11. Acceptance

The organization is accepted when all of these hold:

- [ ] Eight top-level seats exist (Coordinator plus seven roles), titled
      `[Last War] <Role>`, and `TEAM.yaml` ids match them; the Steward is
      outside the roster and holds no schedule.
- [ ] Exactly one loop schedule exists, owned by the Coordinator, fires
      every 15 minutes and leaves a record.
- [ ] The operator closes one unit `done` with complete stats.
- [ ] The scout appends one perception pass with a red-dot accounting.
- [ ] The planner leaves no inbox unit older than one window.
- [ ] The coach's dashboard has L1, L2 and L3 with sources.
- [ ] The toolsmith's #859 fix is merged and `queue.py version` is
      current.
- [ ] The scribe lands one knowledge or activity PR.
- [ ] The 24-hour pilot review names one change to the organization.

## 12. Open owner decisions

- Whether to recover the previous host's live queue pool or accept the
  genesis reset (`OD-20261122-01`).
- The model and cost budget for computer-use runs.
- Whether the LAN proxy may stay available, or only the SSH tunnel.

## Read next

- [Continuous play team](continuous-play-team.md) - the loops and the
  metric hierarchy.
- [`TEAM.yaml`](../../TEAM.yaml) - the live roster.
- [`_seats_/SEAT-PROTOCOL.md`](../../_seats_/SEAT-PROTOCOL.md) - the
  shared seat rules.
