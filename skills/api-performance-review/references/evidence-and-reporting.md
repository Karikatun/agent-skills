# Evidence and reporting

Use to choose an experiment or calibrate a finding. A performance review may establish deterministic waste by code without proving that the operation violates a latency objective.

## Baseline and experiment

Record the scenario, revision, environment, operation mix, arrival/concurrency model, input and dataset distribution, cache state, and target if available. Prefer existing measurements to introducing a new benchmark framework. Select only the metrics relevant to the hypothesis: latency distribution, useful completed work, errors/timeouts, resource saturation, query/call count, queue age, bytes, or cost.

Separate successful and failed request latency; fast rejections can make an average look better while service degrades. Tail percentiles need enough samples and a reported window. Do not average percentiles across instances as if the result were the fleet percentile; use mergeable distributions or clearly describe the approximation. Inspect instrumentation boundaries and retry accounting. [Google SRE: monitoring](https://sre.google/sre-book/monitoring-distributed-systems/).

Use route templates and bounded operation labels when possible. Raw user IDs, full URLs, arbitrary SQL, and query text can create excessive series and expose data. Metrics and traces have different tradeoffs; redact sensitive values in both. Inspect the installed telemetry version rather than requiring a specific vendor or every optional metric. [OpenTelemetry HTTP metrics](https://opentelemetry.io/docs/specs/semconv/http/http-metrics/).

Choose the smallest workload that answers the question. A query counter can establish N+1 without a high-RPS test. A saturation or recovery claim needs resource/concurrency evidence, not a sleep-based timing mock. If a load generator slows its own request arrivals while the service stalls, an apparent tail improvement may reflect less offered load; record the arrival model and achieved load. Long tests are justified by long-lived phenomena, not as a default gate.

Compare the same conditions before and after a change. Record warm-up, repetitions/variability where useful, and failures. Explain changed conditions instead of presenting incomparable runs as a speedup. Keep rollback and correctness checks proportional to the proposed remedy.

## Finding calibration

Use the project's severity scale when supplied. Otherwise:

- High: a reachable scenario causes broad availability failure, persistent duplicate effects, data exposure, or similarly serious impact; state prerequisites and scope.
- Medium: a supported common or plausible workload incurs material repeated work, contention, or a contract failure with a bounded impact.
- Low: a demonstrated localized inefficiency with modest impact. Optional improvements belong outside findings.

Do not force a severity when materiality cannot yet be assessed; retain a hypothesis with the required measurement. A broad claim such as "will crash production" needs evidence of the workload and resource limit, not merely an unbounded construct.

## Examples of sufficient and insufficient evidence

**Established by code:** A route loads 80 orders and calls an uncached SQL lookup once for each order. The adapter executes one statement per call and no upstream batch is used. This establishes 81 statements for that input; it does not establish the p99 latency. Propose a bounded batch and verify statement count, result order, and tenant filtering.

**Confirmed by execution:** A deterministic provider fake commits before its first timeout. Repeating the command creates a second effect. This proves the caller's behavior under that fake's explicit semantics. Verify the real provider's idempotency contract before claiming its production effect is duplicated.

**Hypothesis:** A route delegates to an unavailable repository helper. Its name suggests a full scan, but emitted SQL, bounds, and plans are missing. Inspect the implementation or request a sanitized plan; do not report an unbounded query from a name alone.

**Rejected candidate:** A list endpoint permits offsets within a fixed 200-row reference dataset, clamps page size, has a total order, and uses one join. There is no demonstrated reason to require keyset pagination, caching, or microservices.

## Compact output contract

For an actionable finding: consequence and priority; verified location; trigger; evidence level; why current controls do not prevent it; smallest remedy; verification.

Then state reviewed paths/artifacts, meaningful hypotheses, and unverified runtime/deployment aspects. If no finding meets the bar, report no actionable finding in that scope. Do not fill space with generic hardening advice or a list of every skipped technology.
