"""Cache keys are process-global; authorization on the caller is tenant-scoped."""


def card(cache, records, tenant, item_id):
    # records is keyed by (tenant, item_id); two tenants may use the same item_id.
    key = str(item_id)
    if key not in cache:
        cache[key] = records[(tenant, item_id)]
    return cache[key]
