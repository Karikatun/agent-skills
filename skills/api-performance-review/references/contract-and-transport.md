# Contract and transport

Use for request shape, collection access, aggregation, serialization, and protocol behavior. Record which client scenario the endpoint serves before suggesting contract changes.

## Cost follows the execution path

Check whether field selection reduces storage/computation or merely trims the final response. Count aggregation fan-out, including nested calls and pagination. A single endpoint can hide more backend work than several small calls; reducing client round-trips can still be worthwhile when ownership and bounds are explicit.

Find where request-size, collection-size, filter-cost, and nesting limits are enforced. A response slice after an unbounded fetch does not bound upstream work. A schema maximum helps only if the active path validates it. Consider decompressed bodies, expansion of archive/multipart input, and in-memory serialization only when those paths exist.

## Pagination

- Trace parsing, server-enforced page bounds, filters, sort order, cursor encoding, and the next-page predicate. Check ties, mixed sort directions, missing values, and changes to mutable sort keys.
- Stable pagination requires a total order, often a sort key plus a unique tie-breaker. A cursor should represent the complete ordering boundary and preserve the relevant filter/scope. A cursor is not an authorization mechanism.
- Cursor/keyset pagination can avoid large offsets; it is not a universal replacement for page-number access, nor does it provide snapshot consistency under arbitrary concurrent updates. Inspect the promised consistency contract and relevant database semantics.
- Inspect both the list query and count query. An exact count may dominate latency even when the page itself is cheap. Confirm the product needs that count before changing its semantics.
- Distinguish returned rows from scanned rows and query round-trips. Pagination does not by itself remove N+1.

PostgreSQL's documentation explains unique ordering and the cost of skipped offset rows; use the equivalent plan and semantics for the actual datastore. [LIMIT/OFFSET](https://www.postgresql.org/docs/18/queries-limit.html).

## Conditional protocol checks

For HTTP, check method semantics, conditional requests, response size, connection reuse, and compatible error handling. A retried operation must be semantically safe to repeat; the presence of an HTTP method or idempotency header alone does not prove the application implementation. `202 Accepted` reports acceptance, not successful completion: a status resource is an application contract to inspect. [HTTP semantics](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2).

For GraphQL, inspect resolver calls, loader lifetime/batching, nested lists, aliases, breadth, input variables, operation batches, and enforced cost limits. A depth limit alone does not bound width or expensive arguments. A request-local loader does not establish cross-request caching, and a process-global loader needs a compatible authorization boundary. HTTP success can include field execution errors; inspect the actual result contract. [Demand control](https://graphql.org/learn/security/).

For gRPC or other RPC, inspect channel reuse, streaming buffers, message bounds, and deadline propagation in the installed implementation. For event APIs, inspect payload bounds and consumer/ack semantics in the owning background path.

Compression and binary formats are conditional optimizations. Compare realistic messages and CPU cost before recommending them. Avoid mixing header compression (HPACK/QPACK) with content compression. A protocol upgrade does not establish an improvement in database or application work.

Changes to error formats, collection order, count accuracy, caching, or versioning can break clients. Follow directly coupled consumers and the migration contract. Problem Details is an optional standard format, not a requirement to replace an existing stable error envelope. [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457.html).
