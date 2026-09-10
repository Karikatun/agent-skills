# Review request

Review `api.py` for API performance and resilience. Do not edit files. Use only the supplied artifacts; no network or package installation is needed.

The caller authenticates the user, resolves an allowed tenant, and validates page_size as an integer from 1 to 100 before calling this function. SQLite execute runs one SQL statement immediately; no ORM, loader, memoization, or other middleware intervenes. Tables have composite keys `(tenant, id)`. Customer IDs can repeat across orders. This is the complete read path for this endpoint. No timings or production traffic measurements are supplied. A customer name is required for every returned order.
