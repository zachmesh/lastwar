---
title: Push and PR Policy
created: 2026-11-01T05:31:00Z
modified: 2026-11-23T08:37:00Z
version: 2.4.0
status: draft
description: PR-only main policy - main advances only by pull request merge, records ride date branches, every pull request carries a named owning scheduled job, and every executor run checks its own pull requests first and ends by opening one
grounded_in:
  - source: owner decision 2026-10-31 - disallow direct commits to main and require a pull request for all pushes
  - source: owner decision 2026-10-31 - records PR merge cadence option A, the integrator merges every 15 minutes when new commits exist
  - source: owner decision 2026-11-01 - records PR merge cadence superseded by four-hour batches, approved by the owner in chat
  - source: owner instruction 2026-10-31 23:00 PDT - every pull request must name an owning scheduled job, with a catch-all owner job when no class matches
  - source: owner instruction 2026-10-31 23:02 PDT - every executor checks its own previous pull requests before doing anything else, and opens a pull request at the end of every run that produces output
  - source: platform check 2026-10-31 - the GitHub account is on the Free plan and branch protection and rulesets returned 403 on this then-private repository
---

# Push and PR Policy

PR-only main policy - main advances only by pull request merge, records ride date branches, every pull request carries a named owning scheduled job, and... This register stays at this path as an entry page; its text was split verbatim into 15 articles in [push-pr-policy-sections](push-pr-policy-sections/INDEX.md), unchanged and in reading order.

## Adding an entry

Add one small article file `push-pr-policy-sections/<entry-id>.md`, named by an entry id that starts with letters (for example `entry-20261123-01.md`), with the frontmatter fields title, created, modified, version and description, then add one line for it at the end of this page: `- [Title](push-pr-policy-sections/entry-20261123-01.md) one sentence`. Never edit an existing article.

## Changelog

- 2.4.0, 2026-11-23 - Split verbatim by split_doc.py into 15 key-named articles; --check EQUAL, sha256 94f082f50a16; the unsplit 2.3.0 file is commit 6d019ade

## Articles

- [Push and PR policy](push-pr-policy-sections/push-and-pr.md)
- [The rule](push-pr-policy-sections/the-rule.md) - the-rule
- [Records flow - date branches](push-pr-policy-sections/records-flow-date.md) - records-flow-date
- [Records pull requests - batch cadence](push-pr-policy-sections/records-pull-requests.md) - records-pull-requests
- [Knowledge and code pull requests](push-pr-policy-sections/knowledge-and-code.md) - knowledge-and-code
- [Pull request ownership](push-pr-policy-sections/pull-request-ownership.md) - pull-request-ownership
- [Executor PR discipline](push-pr-policy-sections/executor-pr-discipline.md) - executor-pr-discipline
- [PR branches carry no log appends](push-pr-policy-sections/pr-branches-carry.md) - pr-branches-carry
- [The integrator](push-pr-policy-sections/the-integrator.md) - the-integrator
- [Break-glass](push-pr-policy-sections/break-glass.md) - break-glass
- [Audit](push-pr-policy-sections/audit-section.md) - audit-section
- [Platform facts and enforcement](push-pr-policy-sections/platform-facts-and.md) - platform-facts-and
- [Changelog part 1](push-pr-policy-sections/changelog-section-p1.md) - changelog-section
- [Changelog part 2](push-pr-policy-sections/changelog-section-p2.md) - changelog-section
- [Changelog part 3](push-pr-policy-sections/changelog-section-p3.md) - changelog-section
