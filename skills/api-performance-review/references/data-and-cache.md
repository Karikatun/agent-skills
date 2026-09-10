# Data and cache

Use when storage or cache work is on the selected path. An ORM name or method call is not enough to infer the generated query.

## Storage cost

Find the emitted query, execution boundary, parameters, filters, ordering, projection, and bound. Count calls at the real storage boundary; consider request-local memoization, batches, joins, and duplicate IDs. Eager loading can overfetch; lazy loading can introduce N+1. Neither is universally wrong.

Read plans for a representative dataset and parameter distribution. Distinguish estimates from actual rows/timing, check loops, scans, sorts/spills, row-width, and lock waits where available. A sequential scan on a small table or broad query may be optimal. Do not add an index solely because a column appears in a filter; account for selectivity, order, write cost, and existing indexes. [PostgreSQL EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html).

`EXPLAIN ANALYZE` executes the statement. A transaction rollback does not make arbitrary statements safe: locks, external side effects, sequences, and resource consumption can still matter. Prefer an existing plan or an authorized isolated dataset when safety is uncertain.

Inspect pool limits across all app replicas, workers, and reserved consumers. Increasing pool size can move a queue into the database. Trace acquisition timeout, release on errors/cancellation, transaction duration, external calls inside transactions, and retry multiplication across layers. Recommend changes against the actual resource budget.

## Application cache

Trace lookup, fill, mutation/invalidation, expiry, eviction, and failure behavior. Identify whether the cache is per request, per process, shared, or client-side.

Questions to resolve:

- Does the key include every result-affecting dimension, such as tenant, permission scope, locale, filters, and representation version? Does authorization happen on hits as well as misses? Test principals whose results must differ.
- What age is acceptable for this data? TTL does not guarantee immediate consistency, and delayed fills or stale sources can exceed a naive freshness assumption. Trace invalidation races and whether a version can reject obsolete fills.
- What happens when a popular key expires? Verify coalescing/single-flight ownership and scope. A process-local lock does not coalesce requests across replicas; that can still be sufficient for a small bounded deployment.
- Are miss-path work, refreshes, and fallback concurrency bounded? Fail-open behavior must not bypass authorization or overload the source. Fail-closed behavior may be correct for sensitive data.
- Can errors, missing values, or incomplete results be cached? Are their expiry and invalidation appropriate? Do not apply a blanket ban to intentional short negative caching.

A high hit ratio is not enough: compare saved cost, miss latency, refresh/eviction cost, and behavior during cache loss. Adding a distributed cache is a tradeoff, not an automatic remedy.

## HTTP caches

Inspect the application, reverse proxy/CDN, and client policy that actually serve the response. Standard directives have different meanings: unqualified `private` prohibits shared-cache storage; `no-store` prohibits storage by compliant caches; `no-cache` allows storage but requires validation before reuse. None is a replacement for authorization.

Check freshness/validation (`ETag`, `Last-Modified`, conditional requests), `Vary` for representation selection, and authenticated response handling. `Vary` alone is not a complete tenant or access-control scheme. Test the real intermediary configuration when claiming a cache leak or reuse bug. [RFC 9111](https://www.rfc-editor.org/rfc/rfc9111.html).
