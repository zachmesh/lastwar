---
title: Redact first, then split - 2026-11-22 22:45 PT
created: 2026-11-22T22:45:00-08:00
modified: 2026-11-22T22:46:00-08:00
level: L3
version: 0.1.0
description: Three more profile splits are verified but parked because they carry owner-account identifier text; the order of work becomes redact, check, then split
status: in-progress
activity: team-operations
run_id: team-operations-2026-11-22-2245-redaction-plan
trigger: scribe reply on A-20261123-0632; privacy gate merged as d9d8f7ab
started_at: 2026-11-22T22:44:00-08:00
finished_at:
duration_seconds:
verified: scribe's audit script results read; denylist annotations checked by a live census (exit 0, expectations met)
---

# Redact first, then split

## The three splits

| Profile | Articles | Findability | --check | Files carrying matches (counts only) |
|---|---:|---|---|---:|
| arms-race | 144 + 6 catalogs | 82/82 | EQUAL, 272,136 chars | 44 |
| perception-scout | 238 + 10 catalogs | 91/91 | EQUAL, 515,111 chars | 67 |
| zombie-invasion | 135 + 6 catalogs | 45/45 | EQUAL, 280,336 chars | 9 |

Digests (251 to 266 words), INDEX lines and commit messages carry no match. zombie-invasion's invalid frontmatter was fixed mechanically (one quoted value). Branches `990eeea2`, `f09e3b95` and `9b04c4b0` stay parked: the privacy gate would block each merge.

## Plan

1. Toolsmith's redact tool (A-20261123-0640, due 07:10Z); extended to frontmatter and catalog pages, because the staged gate only sees added lines. Local `# marker:` lines now exist for all 17 patterns.
2. Scribe redacts each profile and its saved original, runs `split_doc --check` on the redacted pair, then splits: radar-tasks, alliance-donations, resource-collection, arms-race, perception-scout, zombie-invasion. Citations are re-checked after each.
3. Profiles are versioned knowledge and the convention already requires redaction; records and history remain OD-20261123-04.

## Play

Still blocked on OD-20261123-05 (account active on another device); the stuck consent run was cleaned (IMP-20261123-07).
