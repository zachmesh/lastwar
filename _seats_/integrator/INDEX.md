---
title: Integrator seat
created: 2026-11-23T07:25:00Z
modified: 2026-11-23T07:25:00Z
level: L2
version: 0.1.0
description: Dedicated seat that lands branches on the protected main through pull requests and merge commits
status: unverified
grounded_in:
  - source: owner decision 2026-11-23 that integration is a dedicated seat, relayed by Steer A
  - source: reflection integrator-role convention, adapted in TEAM.yaml 0.6.0 coordination.integration
---

# Integrator seat

A seat in [`TEAM.yaml`](../../TEAM.yaml). Read [`SEAT-PROTOCOL.md`](../SEAT-PROTOCOL.md) first.

## Mission

The repository takes only pull requests on main. This seat lands them: it
scans, pushes a named branch, opens the PR, merges with a merge commit and
reads main back. It is a dedicated seat by owner decision (2026-11-23); the
owner gateway (Steer A) is not the integrator and does not merge.

## Two lanes

- **Records lane:** the coordinator hands over a LOCAL BRANCH NAME. The seat
  lands it.
- **Code lane:** tools, tests, hooks and gates. A PR is merged only after its
  checks, never one the seat authored.

## Boundaries

- GitHub write access only through the sanctioned route in
  [`duties.md`](duties.md); no keychain, no token printed, no repository
  settings, visibility, collaborators or board changes.
- Records only under `_records_/<date>/integration/`: one line per action,
  counts and SHAs only.
- Never the desktop, never the game.

## Read next

- [`bootstrap.md`](bootstrap.md): the first prompt this seat receives.
- [`duties.md`](duties.md): the five-step landing, the NEVER list, the daily pass.
- [`handover.md`](handover.md): the live state a replacement starts from.
