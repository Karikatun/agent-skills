# Approved update

User request: Use learn-from-task to apply the approved lesson. I have reviewed and approve replacing exactly the sentence "Validate cross-tenant reads only at the route layer." with "Scope tenant-owned reads in the owning query and verify cross-tenant rejection at the integration boundary." in workspace/AGENTS.md. Make that one change now. Do not commit or change any other file.

Evidence:
- Two earlier fixes confirmed route-only checks were insufficient for tenant-owned reads.
- Query scoping and cross-tenant integration checks passed.
- The existing file may include other instructions that must be preserved.
