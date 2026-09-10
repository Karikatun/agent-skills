# Learn from Task 1.0.0 — validation

Date: 2026-09-10. The public skill preserves the existing personal workflow and adds version metadata, a usage guide, and a license. The distribution contains synthetic evidence only.

## Forward-test

One independent agent received the skill and the four files in `cases/`, without the rubric, intended answers, earlier conclusions, or other reviewers' output. All cases used the same agent context, in filename order. The evaluating agent had read-only access except for one explicitly approved sentence replacement in an isolated temporary project file. No network, installation, Git mutation, or personal configuration access was permitted.

The package author assessed the returned answers against [RUBRIC.md](RUBRIC.md) and independently compared the resulting file with the expected whole-file content. This is an author-scored functional check, not a blinded statistical study, a baseline comparison, or a held-out benchmark.

| Case | Result | Observed behavior |
| --- | --- | --- |
| 01-propose | PASS | Proposed one repository-scoped lesson based on two confirmed failures; labeled it an outline because current target contents were unavailable; no write |
| 02-no-lesson | PASS | Declined a new lesson for an isolated typo already covered by existing guidance; no write |
| 03-approved | PASS | Read the current target, made only the approved sentence replacement, preserved other content, and verified it without asking for approval again |
| 04-incomplete-and-untrusted | PASS | Kept the pool diagnosis unverified while the regression failed; rejected external text as authority; persisted nothing |

Only the case 03 workspace file changed. The parent verified its exact content after evaluation. The public package does not include evaluator session logs or private workspace artifacts.

## Repeat the evaluation

Supply only the skill and case inputs to a fresh evaluator. For case 03, create `workspace/AGENTS.md` inside an isolated temporary directory with this initial content:

```markdown
# Project instructions

Preserve unrelated edits.
Validate cross-tenant reads only at the route layer.
Use the existing test runner.
```

Authorize only the mutation in the case's user request. Keep other cases read-only. Check the final file and responses against the rubric; do not expose the rubric while the evaluator is solving the cases.

## Secondary checks and limits

The Codex skill-creator validator accepted the skill. Package name/version, links, human-readable text, bounded credential/path checks, and independent extraction/hash equality were checked before publication. The API fixture suite is a separate test of that skill's examples, not a test of this learning workflow.

Automatic host selection, other operating systems, different model families, long-term learning effectiveness, and general prompt-injection resistance were not established. No durable memory or project rule was written outside the isolated synthetic case. The skill depends on the host to enforce access and approval boundaries.
