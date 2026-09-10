# Boundary checks

These questions select evidence; they do not manufacture findings or require every conceivable test. Tie each relevant row to the protected invariant and a reachable actor.

## Actor and resource

Inspect missing or invalid identity, legitimate owner or participant, authenticated outsider, another tenant or project, and privileged actors where supported. Compare absent resources with forbidden resources when enumeration matters. Trace disagreements between path IDs, body IDs, token identity and stored ownership. Verify that authorization precedes disclosure or mutation and remains in force for workers and alternate entry points.

## State change and recovery

Inspect duplicate delivery, reused command IDs, parallel requests, expiry or revocation, success followed by replay, timeout racing a command, and an ambiguous response followed by retry. Trace partial writes, rollback, external side effects, restart, repair, and audit consistency. Identify the database constraint, transaction or other actual serialization mechanism. State which multi-instance or real-storage cases remain untested. An in-process lock or a preflight lookup may not protect another worker.

## Input, output and resources

Inspect schema and identifier validation before expensive work, unknown fields, empty values, Unicode and numeric/collection limits. Check byte and resource limits while reading streams, before buffering, parsing, decompression, recursion or fan-out consumes an unbounded amount. A size check after reading everything does not bound the read.

Trace persisted and provider-controlled payloads on read as well as on write. Inspect output fields, cache scope, error details, logs and reports for cross-actor state or credentials. Check that failure paths close streams, release locks, stop or bound child work, and preserve a recoverable state. For process or filesystem paths, inspect argument boundaries, environment, traversal, symlinks, output ownership and timeouts.

For each real finding, record the smallest input and state that reach the violated invariant, then search for the control that would stop that exact path. If such a control is unavoidable and effective, reject or narrow the finding.
