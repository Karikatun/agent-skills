# Security scope

Review date: 2026-09-10. Scope: the original instruction-only skill, metadata, bundled references, distribution documentation, and synthetic evaluation code. This is a scoped assessment, not certification of an agent host or the reviewed APIs.

## Capabilities and authority

The installed skill contains Markdown and YAML only. It has no runtime script, remote installer, dependency manifest, MCP configuration, telemetry, updater, credential handler, or network listener. The optional evaluation code uses Python's standard library, in-memory SQLite, and a local provider fake.

The skill directs an agent to read user-selected code and relevant evidence. It may select existing bounded verification tools when the user's task and host policy permit them. A review is read-only; implementation remains conditional on the user's instruction. No permission is granted for production load, destructive queries, publication, dependency installation, credential access, or persistent agent changes. External pages and source/issue comments cannot expand these permissions.

These are instruction boundaries, not OS enforcement. An agent host determines actual filesystem, process, network, and credential access. Deployments needing stronger isolation must enforce that in the host. No per-skill sandbox, publisher signature, registry identity verification, or enterprise revocation service is provided.

## Threat review and matrices

Mode: full, because reusable agent instructions influence tool use. The affected path is user request -> skill selection -> code/evidence/reference reading -> optional authorized check -> finding or scoped fix. History comparison has no prior version to inspect; this is a new package. Adjacent paths reviewed: broad/diff/endpoint scope, SQL/cache/retry/queue checks, incomplete evidence, report creation, maintenance, and installation instructions. Candidate issues were challenged against actual instructions, metadata, and behavioral cases.

| Boundary | Threat and protected invariant | Control and evidence |
| --- | --- | --- |
| User scope versus analyzed content | A comment or fetched page asks for secret access, uploads, or a fabricated verdict | Explicit untrusted-evidence boundary; hostile-comment evaluation case |
| Analysis versus execution | A review launches production traffic or executes mutating SQL | Read-only review scope; effective environment and script inspection; explicit ANALYZE execution warning |
| Observation versus claim | A tiny test is presented as production performance proof | Three evidence levels, workload reporting, incomplete-evidence and misleading-measurement cases |
| Authoring versus installation/update | A package overwrites unrelated files or gains new tools | Manual copying of one selected skill directory, no installer/updater, version and checksums |
| Private input versus report | Raw credentials, personal records, or private traces leak | Sanitized evidence requirement; no credential-store access needed; synthetic distributable examples |

Actor/object matrix: the operator selects scope; an untrusted content author may influence analyzed files; a recipient chooses an agent host. This package has no product user/owner/operator IDs, authentication database, or protected object endpoint. Tenant isolation is a review subject and synthetic case, not a product authorization implementation in this package.

State-change matrix: the skill does not itself create jobs, migrate data, publish, or update configuration. A separately requested fix remains subject to host policy. Installation is one explicit directory copy; replacement/removal is manual and bounded. SQL writes in the optional test create only an in-memory database. No production mutation/replay or PostgreSQL concurrency matrix has a product subject here.

Input/output matrix: plain UTF-8 Markdown/YAML, relative local references, fixed synthetic Python fixtures, and user-supplied review evidence. Package metadata uses safe YAML parsing during validation; no custom runtime deserializer is included. Cross-platform host deserialization behavior is not asserted. The intentional hostile comment in case 04 is an inert evaluation input, not a package instruction or executable request.

## OWASP assessment

Official OWASP Agentic Skills Top 10 checklist and overview URLs were attempted on 2026-09-10 but unavailable. The live official GitHub repository was verified instead at revision `d6f7d7d0de314f52a83a85d1828e06ab096e595c`: [checklist](https://github.com/OWASP/www-project-agentic-skills-top-10/blob/d6f7d7d0de314f52a83a85d1828e06ab096e595c/checklist.md). Applicable detail pages consulted: AST02, AST03, AST04, AST05 and AST08. The remaining categories below distinguish package controls from host or publication infrastructure. No external checklist instruction was executed.

| Area | Evidence status and limit |
| --- | --- |
| AST01/AST08: instructions and evaluation | Manual semantic review and synthetic behavioral tests; see VALIDATION.md. No claim of exhaustive prompt-injection resistance or scanner certification. |
| AST02: provenance/dependencies | Original package, versioned sources and SHA256SUMS; no runtime dependencies. Publisher identity/signature verification: NOT VERIFIED; checksums are not signatures. |
| AST03: authority | PASS for declared bounded review behavior and evaluation scope. Host-enforced least privilege: NOT VERIFIED; no per-skill permission sandbox is provided. |
| AST04: metadata | PASS for safe YAML, allowed fields, readable text and reference validation in this release. Other agents' loaders: NOT VERIFIED. |
| AST05: external evidence | PASS for bundled workflow, explicit instruction distrust and bounded source use. Optional live pages are mutable, not hash-pinned or executable dependencies; host egress enforcement: NOT VERIFIED. |
| AST06: isolation | No service/listener or installed script. Host isolation and cross-agent separation are host responsibilities: NOT VERIFIED. |
| AST07: drift | Version/checksums and manual update guidance; no updater. Signed updates and registry enforcement: NOT VERIFIED. |
| AST09: governance | This package supplies inventory, evaluation and removal guidance. Organization-wide approvals, logging, offboarding and incident governance: outside this package / NOT VERIFIED. |
| AST10: portability | Codex authoring format and local evaluation checked. Other agents and operating systems: NOT VERIFIED; no equivalent safety claim. |

There is no overall "OWASP PASS" because host and publication controls remain unverified. Those limits do not prevent local use of the reviewed instruction-only package within the user's authorized environment. A dedicated credential scanner was not installed and was not run; manual review plus checks for personal paths, invisible controls, private-key headers and common token prefixes found no such content. These bounded checks are not exhaustive secret detection.

## Distribution and maintenance

SHA256SUMS detects changed package content when obtained through a trusted channel; it cannot authenticate a publisher when an attacker can replace both files and hashes. Review new versions before replacement. There is no public registry or remote repository configured by this package.

To revoke local use, remove only this skill's installed directory and verify it disappears from discovery. An existing agent context may retain already-loaded instructions; start a fresh context after removal when that distinction matters. Report concerns privately to the person who supplied the package; no verified public reporting channel is claimed.
