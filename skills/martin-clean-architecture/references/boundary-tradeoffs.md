# Boundary tradeoffs

## Partial separation

A module or facade can concentrate knowledge without a separate package or deployment. A small consumer-owned port may support a second delivery path without a parallel abstraction hierarchy. State what this seam prevents and what it does not enforce. Inspect direct imports and leaked types that could bypass it. Adopt stronger separation when actual consumers, security boundaries, ownership or release needs justify its cost.

## Cohesion and consumers

Group code that changes together for the same reason. Compare that with what consumers use together and what must be delivered as one compatible release. These pressures can conflict: a reusable package can force consumers to absorb dependencies they do not use, while excessive splitting can turn one policy edit into coordinated releases. Use observed change and consumer evidence rather than maximizing a principle or counting folders.

## Dependency cycles and stability

Trace an actual import cycle and its build, test or change consequences. Breaking it may require moving a decision to its owner, supplying a narrow port, or extracting a genuinely shared concept. Do not move everything into a generic common package just to make the graph acyclic.

A component depended on by many others can be costly to change. A stable contract can contain that cost, but concrete stable code can also be appropriate when its behavior is intentionally settled. Fan-in, fan-out and abstractness ratios are diagnostic clues, not automatic quality gates or reasons to add interfaces.

## Services and runtime boundaries

Moving code behind a network call introduces latency, authorization, delivery failure, compatibility, observability and recovery obligations. It does not automatically separate domain ownership or eliminate shared release coupling. Retain a local boundary unless a concrete independent scaling, deployment, isolation or ownership requirement pays for those costs.

Data storage is an implementation mechanism with real semantics. Isolating SQL types from policy does not make transactions, consistency, query costs or migration order irrelevant. Test the actual invariant at the layer that enforces it.
