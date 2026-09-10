# Review request

Review `api.py` for API performance and resilience. Do not edit files. Use only the supplied artifacts; no network or package installation is needed.

The caller has already authenticated and authorized the order. The provider fake models a documented downstream contract: each deliver invocation creates one durable delivery; it has no deduplication, idempotency key support, or lookup by client request identifier. A timeout may occur after commit. There is no outer retry. The goal is to deliver an order once. There are no production timings in this fixture. State precisely what this model proves and what it cannot establish about an unspecified live provider.
