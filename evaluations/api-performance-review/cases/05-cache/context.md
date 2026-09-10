# Review request

Review `api.py` for API performance and resilience, including correctness of its cache. Do not edit files. Use only the supplied artifacts; no network or package installation is needed.

Authentication and tenant authorization occur before this function. An actor is allowed to read only records belonging to its tenant. The dictionary is shared across requests in one process; cache contents live for 30 seconds before the dictionary is replaced. Two tenants can have the same item_id with different private data. One process can serve both tenants, and the response directly serializes this function's return value. No intermediary HTTP caching occurs. This is a behavioral model, not a live server.
