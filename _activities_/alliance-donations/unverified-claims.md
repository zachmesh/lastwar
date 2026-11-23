---
title: Alliance donations unverified claims
created: 2026-11-23T10:24:41Z
modified: 2026-11-23T10:24:41Z
version: 0.1.0
description: The claims of alliance-donations that no record settles yet, moved verbatim out of the rule digest to keep it under 300 words
---

# Alliance donations unverified claims

Claims no record settles yet, moved verbatim from the last line of the [rule digest](rule-digest.md); the tap from a live 1/30 is settled and left out ([rule 5](rule-digest.md)).

- a refill of one count per 20 minutes (records give 10 to 55).
- a closing standard for a transient 0/30.
- long-press donating.
- R3 checkpoint times.
- Alliance entry in the windowed 788x1083 state.
- coin cost per tap is 100 x (node level + 1), 900 at 8/10 (`_records_/2026-11-07/alliance-donations/2018-queue-run.md`) and 1000 at 9/10 (`_records_/2026-11-22/alliance-donations/0114-queue-run.md`), test: read the cost at the next node level-up.
- the grey timer after a tap: a per-tap cooldown, a daily lock or the countdown to the next refill, and the refill interval (the profile's one count per 20 minutes is a guess), test: log the timer at the last tap and the next entry count with times.
