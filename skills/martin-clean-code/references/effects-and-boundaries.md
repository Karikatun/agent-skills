# Effects and boundaries

## External APIs

List what the caller actually needs from an SDK, storage client or framework. A narrow adapter is useful when it concentrates translation, volatile types, errors or policy knowledge. A wrapper that repeats every external method without reducing knowledge adds a second API to maintain. Place translation with its actual owner; do not spread a provider's vocabulary through otherwise stable domain contracts.

When external behavior is uncertain, use installed types, primary documentation or a bounded contract test. Do not mock an assumed response and call it provider verification. Preserve timeout, cancellation, partial success and retry behavior when moving code across a boundary.

## Concurrency

Separate the decision about what work means from coordination of when it runs when that separation makes ownership clearer. Identify shared mutable state, the protected invariant, ordering and the real synchronization mechanism. A smaller critical section is beneficial only while the invariant remains protected; moving a read or write outside it can create a race.

Trace completion, cancellation, draining, error propagation and cleanup. Concurrency is not automatically a performance improvement. Tests should control the relevant ordering or use the real storage/coordination boundary, rather than relying on arbitrary sleeps. A sequential test is not evidence of parallel safety.

## Refactoring verification

Choose evidence for what could accidentally change: public shape, error outcome, effect count and order, transaction boundary, returned data, cancellation or cleanup. Prefer an existing observable boundary over tests that duplicate a proposed helper's implementation. If a seam is hard to test, state what can be established by a bounded trace and what remains unknown; do not fake certainty or perform a broad redesign without need.

Names and formatting may need only narrow static checks. Behavioral changes require the project's appropriate tests and gates. A review request does not authorize either kind of edit.
