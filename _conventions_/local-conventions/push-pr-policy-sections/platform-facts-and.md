---
title: Platform facts and enforcement
created: 2026-11-23T09:02:35Z
modified: 2026-11-23T09:02:35Z
version: 0.1.0
sequence: 15
description: This policy is enforced by pipeline discipline, a push-route guard and the retro audit - not
---
## Platform facts and enforcement

This policy is enforced by pipeline discipline, a push-route
guard and the retro audit - not by the platform. Measured on
2026-10-31, while this repository was still private: the
GitHub account is on the Free plan, and for this repository
both branch protection and rulesets returned 403; on a
private repository they require a paid plan. The repository
was transferred to zachmesh/lastwar and made public later on
2026-10-31, so that measurement no longer describes the
repository's platform limits and is to be re-measured for the
public repository. Pull requests work, and the VPS route
carries a `gh` login with the scope to open and merge them.

The push-route guard is a step in the standard route: the
`~/lastwar-push` clone refuses any direct push of the main ref
(a pre-push hook rejecting updates to `refs/heads/main`), so
the route every writer uses cannot push main even by mistake.
Branch pushes are unaffected, and `gh pr merge` operates on
GitHub's side, so merges are unaffected. A hard server-side
lock - branch protection requiring pull requests on main -
needed GitHub Pro while the repository was private; for a
public repository it is available on the Free plan. Enabling
it is an owner decision; if it is enabled, keep this policy
as the operating procedure on top of it, and record the
change in the changelog below.

