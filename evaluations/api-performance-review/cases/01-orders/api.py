"""Isolated review fixture. Caller validates tenant and page_size in 1..100."""


def list_orders(connection, tenant, page_size):
    rows = connection.execute(
        "SELECT id, customer_id FROM orders WHERE tenant = ? ORDER BY id LIMIT ?",
        (tenant, page_size),
    ).fetchall()
    result = []
    for order_id, customer_id in rows:
        customer = connection.execute(
            "SELECT name FROM customers WHERE tenant = ? AND id = ?",
            (tenant, customer_id),
        ).fetchone()
        result.append({"id": order_id, "customer": customer[0] if customer else None})
    return result
