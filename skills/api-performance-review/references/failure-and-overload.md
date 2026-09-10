# Failure and overload

Use for external calls, retries, queues, fan-out, and resource pressure. Trace success, slowdown, ambiguous completion, and recovery through the actual owners.

## Time budget and cancellation

Identify the end-to-end deadline, time already spent, each remaining operation, and cleanup margin. Child calls should not each obtain a fresh copy of the entire request budget. A timeout on the caller's wait may leave the underlying operation running. Inspect cancellation propagation and cleanup at the driver/provider boundary, including streams, timers, locks, and connection releases. [gRPC deadlines](https://grpc.io/docs/guides/deadlines/).

Do not equate an async function with parallelism, or `await` with blocking the whole process. Inspect whether CPU work or synchronous I/O blocks the runtime, whether work is buffered without bounds, and how scheduling behaves under concurrency.

## Repeats and durable effects

List retry owners: client, gateway, SDK, app, transaction, queue consumer. Calculate possible attempt multiplication before recommending another retry. Inspect retryable conditions, attempt cap, total budget, increasing delay, jitter, and server hints. A timed-out operation may already have committed. An error does not establish that no side effect occurred. [HTTP retry semantics](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2).

For repeated commands, inspect the actual deduplication boundary: key scope, request-payload agreement, concurrent claims, effect/result persistence, retention, replay response, and crash recovery. A random key regenerated on each retry or a cache write after an external effect does not establish idempotency. Where an external provider owns the effect, verify its contract; do not promise exactly-once behavior from a local transaction alone.

## Work admission and queues

Calculate request concurrency times per-request fan-out times attempt count, then include workers and replica count. Distinguish rate limits, in-flight concurrency limits, pool limits, and queue bounds. Each controls a different resource; an upstream enforced bound can make a local mechanism unnecessary.

For a job path, follow acceptance, durable enqueue, claim/lease, effect, acknowledgement, retries, terminal state, result retention, and cancellation. Inspect stale workers, duplicate delivery, poison messages, queue growth, message age, and recovery throughput. Moving work to a background queue does not establish bounded load or reliable acceptance. `202` without a durable accepted job is only a problem when the promised delivery contract requires durability; inspect that promise.

Quotas may use operation cost or bytes as well as requests. Confirm tenant/principal scope and bypass paths before alleging missing enforcement. When a dependency saturates, consider bounded admission, backpressure, and explicit degraded/failure responses. Circuit breakers and fallback data must preserve correctness; their absence alone is not a defect. [Google SRE: overload](https://sre.google/sre-book/handling-overload/).

Treat `429` quota exhaustion and `503` temporary unavailability according to the API contract. `Retry-After` can communicate a retry delay; do not turn an optional hint into an unconditional compliance finding. After recovery, check backlog and synchronized retries, not just whether a health endpoint responds.

## Focused verification

Use deterministic fake dependencies or a disposable test service to observe active work after cancellation, duplicate effects after ambiguous responses, maximum in-flight calls, and release of permits on failures. State what the fake cannot prove about the real provider. Any production experiment requires an authorized target, traffic/error budget, duration, and stop conditions; lacking that authority, provide the experiment plan and use existing evidence.
