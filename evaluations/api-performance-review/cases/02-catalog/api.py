"""Reference catalog. Schema constrains each tenant to at most 200 entries."""


def list_catalog(connection, tenant, page_size, offset):
    if type(page_size) is not int or type(offset) is not int:
        raise ValueError("integer pagination required")
    if not 1 <= page_size <= 50 or not 0 <= offset <= 200:
        raise ValueError("pagination outside supported range")
    return connection.execute(
        """SELECT o.id, c.name FROM orders o
           LEFT JOIN customers c ON c.tenant = o.tenant AND c.id = o.customer_id
           WHERE o.tenant = ? ORDER BY o.id LIMIT ? OFFSET ?""",
        (tenant, page_size, offset),
    ).fetchall()
