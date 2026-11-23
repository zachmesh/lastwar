---
title: 1. Principles
created: 2026-11-23T09:04:37Z
modified: 2026-11-23T09:04:37Z
version: 0.1.0
sequence: 2
description: One seat, one session, one owner.
---
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

