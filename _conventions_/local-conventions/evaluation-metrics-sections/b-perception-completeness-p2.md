---
title: B. Perception completeness part 2
created: 2026-11-23T09:02:25Z
modified: 2026-11-23T09:02:25Z
version: 0.1.0
sequence: 5
description: Known defects - observed items carry no per-item timestamp; the observation file is appended pass by
---
Known defects - observed items carry no per-item timestamp; the
observation file is appended pass by pass, so latency is
computable at pass granularity only. Where a pass time cannot be
recovered, latency for that day is a data-gap, not a zero. Until
the scout diff auto-invocation lands (loop review open link 1),
conversion measures a hand-run tool and must be read as such.

