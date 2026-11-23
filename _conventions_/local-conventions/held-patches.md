---
title: Held Patches Register
created: 2026-11-22T10:32:17Z
modified: 2026-11-23T09:06:22Z
version: 1.2.0
description: The in-repo record of tool patches held outside the repository, so the tool-developer step-2 in-flight check can see them
grounded_in:
  - source: "issue #809 - held patches in hidden_files are invisible to the tool-developer in-flight check"
  - source: hidden_files/tool-development/held-patches/RECONCILED-2026-11-22.md - the reconciled held-patch inventory this register mirrors
  - source: "merged PR #792 (squash d2b0512b8) implements issue #709 on main"
  - source: "merged PR #715 (squash 8b9a83bc0) implements issue #712 on main"
---

# Held Patches Register

The in-repo record of tool patches held outside the repository, so the tool-developer step-2 in-flight check can see them. This register stays at this path as an entry page; its text was split verbatim into 2 articles in [held-patches-sections](held-patches-sections/INDEX.md), unchanged and in reading order.

## Adding an entry

Add one small article file `held-patches-sections/<entry-id>.md`, named by an entry id that starts with letters (for example `entry-20261123-01.md`), with the frontmatter fields title, created, modified, version and description, then add one line for it at the end of this page: `- [Title](held-patches-sections/entry-20261123-01.md) one sentence`. Never edit an existing article.

## Changelog

- 1.2.0, 2026-11-23 - Split verbatim into articles of 300 words or fewer (split_doc.py with a 300-word limit); --check EQUAL, sha256 0d33466f1b33; the 1.1.0 single file is in git history.

## Articles

- [Held patches register](held-patches-sections/held-patches-register.md) - A held patch is tool work that exists as a patch file outside this...
- [Held patches and 1 more](held-patches-sections/held-patches.md) - held-patches, rules-section - Machine-readable table: _tools_/held_patches.py parses these rows (the Issue, Status, Canonical patch and Superseding PR...
