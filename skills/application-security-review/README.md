# Application Security Review

Version 1.0.0. A stack-independent review workflow for reachable security defects, actual enforcement, and explicit evidence gaps. It covers application boundaries and conditionally agent tooling.

```text
Use $application-security-review to review this diff and its coupled authorization, storage, projection and recovery paths. Keep the review read-only.
```

The workflow scales from semantic copy checks to full trust-boundary review. It traces existing controls before reporting a finding, checks history and neighboring variants for material changes, and challenges candidate findings. It uses project-owned checks and does not assume a database, framework, scanner, or deployment process.

For agent-tooling reviews, optional official OWASP references require permitted network access. If unavailable, the skill reports that evidence gap and continues useful local inspection. It does not install scanners, authorize active attacks, transmit private code, or confer host permissions. No companion skill is required. Responses follow the user's language.

This is an independently generalized workflow from private project review procedures. Product-specific matrices, command names, release gates and private findings are excluded. The package contains only instructions and references; it does not certify an application or replace an appropriate security assessment.

Copy this complete folder into a supported skills directory. Preserve the reference files and license; compare an existing copy before replacement.

## Install with Codex

```text
Use $skill-installer to install only application-security-review from https://github.com/Karikatun/agent-skills/tree/application-security-review-v1.0.0/skills/application-security-review into my personal skills directory. Preserve any existing copy; do not install other skills.
```

See the [validation record](https://github.com/Karikatun/agent-skills/blob/application-security-review-v1.0.0/evaluations/application-security-review/VALIDATION.md) for bounded synthetic cases and limitations. Original material uses the adjacent [MIT license](LICENSE).
