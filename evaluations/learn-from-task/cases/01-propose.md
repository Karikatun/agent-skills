# Completed task

User request: Use learn-from-task to review the completed task below and propose any durable improvement. Do not change files.

Evidence:
- In two separate endpoints, authorization succeeded but the data lookup filtered only by document ID.
- The second fix placed tenant scoping in the owning query, not in the response serializer.
- A cross-tenant integration test failed before each fix and passed afterward. Same-tenant behavior still passes.
- The task is complete. Current project guidance requires authorization but does not describe query scoping.
- Existing cross-tenant tests cover these endpoints. There is no demonstrated need for a new framework, global memory entry, or skill.
- There is no current AGENTS.md file content supplied; any proposed insertion must be labeled an outline rather than an exact applicable patch.
