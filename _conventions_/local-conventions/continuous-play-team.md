---
title: Continuous Play Team
created: 2026-11-22T19:10:00-08:00
modified: 2026-11-22T19:10:00-08:00
level: L2
version: 0.1.0
description: The operating model for a durable DSH team that plays the account continuously and improves its own execution, discovery and learning rate
status: unverified
grounded_in:
  - source: owner request 2026-11-22 to establish team and DSH sessions as UI visible seats for continuous play and three-level improvement
  - source: measured queue and retro state on 2026-11-22 at 19:00 PT, recorded in the same-day team-operations run
  - source: reflection session-team v3, pinned in typed-folder-adoption.md
---

# Continuous play team

Owner request, 2026-11-22 - establish the team and DSH sessions as
visible seats, play the game continuously, and improve on three
levels: how well each task is played, how completely new tasks are
discovered, and how fast the ability to play improves.

This article is the operating model. `TEAM.yaml` is the roster;
the seat records under `_seats_/` are each seat's lasting brief;
`_records_/` remains the single source of truth for what happened.
The repository's queue, records, conventions and constitution
clauses C1 to C5 are unchanged and govern the team.

## 1. The diagnosis at establishment

Measured from this checkout on 2026-11-22 at about 19:00 PT, before
any repair:

| Observation | Reading | Source |
|---|---|---|
| Inbox units | 766, oldest unit window 2026-11-10 (12 units), then 2026-11-11 (3) | `_queue_/inbox` |
| Done units | 2,310 | `_queue_/done` |
| `queue.py next` | returned `scout-midday-2026-11-12-0700`, a unit about ten days past its window | tool output |
| Latest retro | 2026-11-21 | `_records_/retro/2026-11-21.md` |
| Duel days lost | five consecutive, duel day 6 lost whole | same retro, top leak 1 |
| Donations | 0 of 30 on a day the game ran | same retro, top leak 2 |
| Unverified rate | 91.3 percent | same retro, top leak 6 |
| Ledger coverage | 5 of 23 lines | same retro, top leak 5 |
| Unexplained red dots | one (red target badge) | same retro, top leak 7 |
| Recordless passes | ticker, planner, knowledge organiser, catch-all | same retro, top leak 9 |
| Prior executor | the Muse app, stopped on the owner's request this day | owner instruction |

The system did not fail because the game was unavailable. It failed
because the loop lost its clock, its queue hygiene, its verification
discipline and its recovery path at the same time. A new team that
simply resumes the old schedule would replay the same failure. The
first duty is therefore a measured reset, not a backlog burn-down.

### Migration finding, 2026-11-22 19:15 PT

The queue above is a snapshot in this checkout, not the previous host's
live pool. The day index for 2026-11-22 records the live pool at about
14:40 PT as inbox 96 and done 2,884, while this tree held inbox 766 and
done 2,310; the records branch holds yet another count. The live pool
lived in the previous host's `~/workspace/lastwar` checkout and was not
migrated with the clone.

Consequence: the first queue pass on this Mac is a **genesis reset**,
not a recovery of the old live pool. The stale snapshot is historical
evidence and is not executed. The planner expires every unit whose
window closed before the current reset, keeps only the current and
upcoming windows, and records the genesis timestamp. The coach reads
historical metrics from the delivered retro data files, never from this
snapshot. The missing done units are a data gap, not a zero.

## 2. Three loops, three metric families

One team runs three nested loops. Each loop has a measurable
question, an owner seat and a fixed artifact. A loop that cannot
produce its artifact is recorded as a no-op or a failure, never as
silence.

| Loop | Period | Question | Owner | Artifact |
|---|---|---|---|---|
| L1 play | 15 min tick | Did one task get played, verified and recorded? | operator | unit record and `result.stats` |
| L2 discovery | 2 h and daily | What did the game offer that no profile owns, and what did the world know that we did not? | scout and researcher | observation pass, candidate register, research note |
| L3 meta | daily and weekly | Is the ability to play improving faster than the game changes? | coach | evaluation dashboard and improvement backlog |

### L1 - execution effectiveness

Sources are the per-unit `result` fields in `_queue_/done` and the
canonical appendix `_records_/retro/<date>-data.json`. The measures
are the ones [evaluation metrics](evaluation-metrics.md) family A
already specifies - done rate, duration median and p90, attempts,
target attainment, resource yield, points per minute, unverified
rate and blocker category - read per regular and per day.

Additions for continuous play:

- **Tick yield** - the share of 15-minute ticks that closed at least
  one done unit. A tick that only re-read state is not a yield.
- **Token wait** - seconds an operator waits for the one device
  token, per hour. This is the serialisation cost of one account.
- **Freshness** - the age of the oldest inbox unit the operator could
  have picked. Anything over one window is queue debt, not work.

### L2 - discovery comprehensiveness

The existing [perception-driven queue](perception-driven-queue.md)
already defines the ledger walk, the scout diff and the candidate
state machine. Continuous play adds a second discovery channel:

- **Local interaction reasoning** - every unexpected screen, changed
  label, new badge or missing button becomes an observation line
  with its coordinates, time and the pass that saw it. The scout
  files it; the researcher explains it.
- **Internet research** - a bounded question, at least two
  independent sources, a dated citation, and one in-game check that
  could falsify the claim. A research note with no local check is
  labelled `unverified` and cannot change a play rule.
- **Discovery yield** - new task profiles activated per week, split
  from owner-named intake; candidate conversion and dwell; unmatched
  label trend; false-discovery rate. All are evaluation metrics
  family C.

### L3 - improvement of improvement

The meta-question is not "did a tool land" but "did the landing move
the metric it named, and did the movement survive". The measures:

- **Learning rate** - closed improvements with verified metric
  movement per week, and the change in L1 and L2 headline metrics
  over the same weeks, reported with game-change confounders named.
- **Recurrence rate** - the share of closed improvements whose root
  cause class reappears within seven days. Target zero.
- **Time to detect and time to fix** - from the first record that
  shows a defect to the improvement filing, and from filing to a
  verified closure.
- **Experiment count and calibration** - play-rule experiments run,
  their predicted effect, and the measured effect. A team that never
  predicts cannot learn.
- **Research-to-rule conversion** - research notes that became a
  verified play rule or activity profile change, over notes filed.

A weekly L3 review compares the week against the previous one and
names one thing the team will change about how it improves. That
change is itself an improvement entry with a target metric.

## 3. The seats

Eight seats, one coordinator and seven roles. DSH Team capacity is
eight members; the coordinator is the current session and seven
teammates is the largest roster the platform admits without a size
exception. Roles may combine temporarily, but write scopes stay
disjoint.

| Seat | Responsibility | Write scope | Cadence |
|---|---|---|---|
| coordinator | dispatch, queue health, owner gateway, team review | `TEAM.yaml`, `_seats_/`, `_records_/retro/improvements.md` proposals | 15 min tick |
| operator | play units, hold the device token, close records | `_queue_/claimed`, `_queue_/done`, `_records_/<date>/<activity>` | every tick |
| scout | perceive surfaces, ledger walk, file candidates | `_records_/<date>/perception-scout`, `_activities_` candidates by proposal | every 2 h |
| researcher | internet and local-interaction research | `_records_/<date>/research`, `_knowledge_` by proposal | 2 questions per day |
| planner | queue hygiene, staging, slot coverage | `_queue_/inbox`, `_tools_/state` | hourly |
| coach | metrics, retro, improvement backlog | `_records_/retro`, `_records_/<date>/retro-review` | daily and weekly |
| toolsmith | tool and automation improvements | `_tools_/` code and tests | on assignment |
| scribe | knowledge and activity folding, PR integration | `_knowledge_`, `_activities_`, `_conventions_` by PR | on assignment |

Every seat reads its own `bootstrap.md`, `duties.md` and
`handover.md` before acting. A seat that is not loaded receives its
messages when it wakes; the coordinator is the clock and the router.

## 4. Establishment in DSH

The team runs on the local DSH host in the `lastwar` workspace. The
coordinator is this session; the other seats are DSH sessions created
through a supported DSH operation, never by editing a DSH store.

- **Visibility** - every seat is a real DSH session the UI can list
  and open. The team roster projection or the workspace session list
  is the proof; a seat with no session id in `TEAM.yaml` is planned,
  not established.
- **Continuation** - the coordinator holds the only recurring
  schedule (`15 min`). The schedule is the loop clock. A delegated
  child cannot create its own schedule, so the coordinator wakes each
  seat with a bounded assignment; an idle seat is not a stopped loop.
- **Communication** - bounded assignments carry a question, the
  expected evidence and a completion condition. A seat replies with
  the artifact path and the measurement; chat text alone is not a
  result.
- **Lease** - `TEAM.yaml` records each seat's session id and start
  time. A session that dies is replaced; a seat is never silently
  abandoned.
- **One device** - only the operator may hold the device token and
  send input to the game. A second input path is a defect, not a
  parallel speed-up.

The first establishment is honestly partial. A seat created as a
delegated child session is UI-visible and durable, but it is not a
top-level workspace session with its own schedule. The coordinator
therefore records `session_id` and `session_started` for every
established seat, and the first weekly review judges whether the
child-session form is sufficient or a top-level session per seat is
required. The decision is recorded in the owner decisions register,
not assumed.

## 5. Computer use

Play happens through `dtadpole/computer-use` on this Mac, using its
MCP server. The integration contract is the project's own:
`computer-use-mcp` exposes `computer_use_start`, `_status`,
`_respond` and `_control`; a desktop run names the apps it may use,
and a person approves each app once in the live view.

Local rules:

- The bridge is `_tools_/cu_bridge.py`; it speaks JSON-RPC to the
  MCP server over stdio and stores run ids under
  `_tools_/state/cu_runs.json`. It is the only route the operator
  uses; no seat edits a DSH profile to add a tool.
- The app bundle id for the game is `com.lastwar.ios`. Terminals,
  password managers, AI agents and system security apps are excluded
  by the computer-use policy and are never proposed.
- One desktop run at a time. A live run holds the Mac's desktop-run
  lock; a second start is refused, not queued.
- This Mac opts out of the 300-second owner-idle wait for bridge runs:
  `_tools_/cu_bridge.py` sets `CU_OWNER_IDLE_SECONDS=0` in the MCP child
  environment. The computer-use default stays 300 for every other caller,
  and the override is a local, reversible decision, not a change to the
  shared rule.
- Consent is human-only. The bridge prints the control-link command
  for the owner; no seat can approve an app, a purchase, a send or a
  consequential step through the tool.
- A run gets a plain-language task, a step cap and a time cap. The
  operator checks `status`, reads the final screenshot and writes the
  result into the unit record. A run that ends `waiting_for_person`
  is recorded as blocked with the control link, never as done.

## 6. Queue genesis on this Mac

The 766-unit snapshot is queue debt, not a work plan, and it is not the
old live pool. The first planner passes apply this genesis protocol, in
order:

1. **Freeze** - stop staging new units except the current and next
   window. Record the inbox, claimed and done counts before any move.
   On 2026-11-22 the measured state was inbox 766, claimed 0, done 2,310.
2. **Retire** - every inbox unit whose window ended before the
   current reset is closed `expired`, with the count and the oldest
   date in the planner record. A unit is not executed merely because
   it is old. Units whose window is current or future are kept.
3. **Reset** - the regular schedule restarts at the next slot after
   the current time. Missed cycles are not backfilled; the ledger
   records them as missed with the reason. The genesis timestamp is
   the current reset, not the snapshot date.
4. **Reconcile** - the live tree and the delivered records branch
   are compared for the same day before any new close. A split is
   recorded and repaired on the branch side, never by force.
5. **Prove** - `queue.py validate`, `sync`, `slot_coverage.py` and
   `sweep-status` run at the end of the pass, and their outputs are
   in the planner record.

## 7. Safety and governance

- Purchases, alliance diplomacy, PvP attacks and any action that
  spends premium currency need the owner's approval first. The
  operator stops at the confirmation surface and records
  `needs-owner`.
- The account stays `owner account` in public content; the account
  privacy convention is unchanged.
- C1 to C5 are untouched. Play records are append-only. Knowledge is
  versioned. Every claim carries evidence or `unverified`.
- A seat never writes outside its scope. A cross-scope change is a
  proposal to the owning seat, not an edit.
- The team never declares the account's play complete; only the
  owner does.

## 8. Rollout and acceptance

| Phase | Duration | Output | Acceptance |
|---|---|---|---|
| P0 reset | first 3 planner passes | clean queue, baseline dashboard | no inbox unit older than one window; `validate` exits 0 |
| P1 play | first 24 h | at least one done unit per hour of game availability | tick yield at or above 0.75; every done unit has stats |
| P2 discover | first 3 days | full ledger walk, two research notes per day | coverage at or above 20 of 23; unexplained red dots zero on two days |
| P3 learn | first 7 days | three improvements closed with verified movement | recurrence zero; weekly review names one meta-change |

The pilot is reviewed at 24 hours and 7 days. A phase that misses
its acceptance is not declared done; it is re-planned with the
measured gap and one named change.

## 9. What this article does not decide

The exact model and cost budget for the computer-use inside each
run, the owner's approval of the game app, and whether the team
migrates from delegated child sessions to top-level DSH sessions
remain owner decisions. They are recorded in the owner decisions
register when the owner answers, not inferred here.

## Read next

- [`TEAM.yaml`](../../TEAM.yaml) - the roster and policy.
- [`_seats_/INDEX.md`](../../_seats_/INDEX.md) - the seat records.
- [Evaluation metrics](evaluation-metrics.md) - the existing metric
  definitions this article extends.
- [Perception-driven queue](perception-driven-queue.md) - the scout
  layer and discovery state machine.
