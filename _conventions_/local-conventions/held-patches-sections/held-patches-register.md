---
title: Held patches register
created: 2026-11-23T09:06:22Z
modified: 2026-11-23T09:06:22Z
version: 0.1.0
sequence: 1
description: A held patch is tool work that exists as a patch file outside this repository, in
---

# Held patches register

A held patch is tool work that exists as a patch file outside this
repository, in the goal `hidden_files/` workspace, because it could
not be delivered as a pull request when it was written. A held patch
counts as in-flight work (job step 2). Before re-implementing an
issue, a tool-developer run MUST consult this register with
`_tools_/held_patches.py check <issue>`; a HELD entry means the
issue already has a live patch and must not be re-taken, and a
SUPERSEDED entry means the issue is implemented on main by the named
merged PR and no patch may be applied.

This register is the step-2 source. The reconciled inventory in the
goal `hidden_files/` (`tool-development/held-patches/
RECONCILED-2026-11-22.md`) is the evidence for it: patch copies,
duplicate designations and the verification behind each row below.
The two are mirrors: when a held patch's status changes, update
both in the same run. Patch paths below are relative to the goal
`hidden_files/` directory.

