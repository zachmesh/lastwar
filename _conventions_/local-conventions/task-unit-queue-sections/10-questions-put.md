---
title: 10. Questions put to the owner
created: 2026-11-23T08:37:05Z
modified: 2026-11-23T08:37:05Z
version: 0.1.0
sequence: 15
description: Lease length - 20 minutes proposed.
---
## 10. Questions put to the owner

- Lease length - 20 minutes proposed. Longer is safer against slow
  screens, shorter recovers crashed work faster. **Still open.**
- Ad hoc sessions as units or token-only - **resolved by the owner
  2026-10-28** - they join the pool as continuation chains (section
  2), Zombie Invasion first.
- Batch size - **resolved by the owner 2026-10-28** - there is no
  batch. The cap is per unit (15 minutes) and the executor loop
  re-picks after every unit, which is what lets other tasks ingest
  when their time arrives.

