---
title: Filing - the provisional profile
created: 2026-11-23T09:03:33Z
modified: 2026-11-23T09:03:33Z
version: 0.1.0
sequence: 19
description: A candidate is filed automatically, in the same session that discovers it -
---
### Filing - the provisional profile

A candidate is filed automatically, in the same session that
discovers it -

- A provisional metadata file under `_activities_`, in the
  candidate register the activities index keeps, carrying only
  what is known - discovery time, the surface it was seen on,
  the on-screen text transcribed, and every clue already in hand
  (the announcing mail, the residue mail, a ledger near-match).
- Its state, one of the state machine below, starting at
  `candidate`.

The state machine -

```text
candidate -> exploring -> active
                       -> rejected (reason recorded)
```

