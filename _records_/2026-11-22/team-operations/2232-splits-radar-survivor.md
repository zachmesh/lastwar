---
title: radar-tasks and survivor-intake splits merged - 2026-11-22 22:32 PT
created: 2026-11-22T22:32:00-08:00
modified: 2026-11-22T22:34:00-08:00
level: L3
version: 0.1.0
description: Two more profile splits verified and merged locally; the clean one prepared as a second public push, the other held for the privacy decision
status: done
activity: team-operations
run_id: team-operations-2026-11-22-2232-splits-radar-survivor
trigger: scribe reply on A-20261123-0625
started_at: 2026-11-22T22:30:00-08:00
finished_at: 2026-11-22T22:34:00-08:00
duration_seconds: 240
verified: --check run by the coordinator against originals that match main; denylist scan of both branches (counts only); push/clean-2 diff scanned and gated
---

# radar-tasks and survivor-intake splits merged

| Profile | Articles | INDEX | Digest | --check | Added lines matching the denylist |
|---|---:|---:|---:|---|---:|
| radar-tasks | 231 + 9 catalogs | 171 words | 262 words | EQUAL, 464,865 characters | 30 (18 files, moved verbatim) |
| survivor-intake | 127 + 5 catalogs | 150 words | 259 words | EQUAL, 250,918 characters | 0 |

Merged to local main as `83643621` and `f9a97a79`. Both digests were verified by the scribe against the article text (37 of 37 phrases each); the scribe caught and fixed a wrong claim in its first radar-tasks errata draft.

## Publication

- `survivor-intake` is clean: `push/clean-2` at `d6718c00`, one commit on the published `push/clean`, 134 files, 0 matching lines or file names, gate ok. Sent to the Steward for its own scan.
- `radar-tasks`, like `alliance-donations` and `resource-collection`, carries the pre-existing tag and alliance text moved verbatim, so it stays out of the public branch until OD-20261123-04 is answered; local main is never pushed.

## Next

Scribe `A-20261123-0632`: arms-race, perception-scout and zombie-invasion (due 07:20Z), each scanned by me. About 24 profiles remain over 500 words after those.
