"""Verify fixture ground truth, not the quality of an agent's review. Python 3.9+."""
import asyncio
import importlib.util
from pathlib import Path
import sqlite3
import unittest

ROOT = Path(__file__).resolve().parent / "cases"


def module(case):
    spec = importlib.util.spec_from_file_location(case.replace("-", "_"), ROOT / case / "api.py")
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def database():
    connection = sqlite3.connect(":memory:")
    connection.executescript("""
        CREATE TABLE customers (tenant TEXT, id INTEGER, name TEXT, PRIMARY KEY(tenant,id));
        CREATE TABLE orders (tenant TEXT, id INTEGER CHECK(id BETWEEN 1 AND 200), customer_id INTEGER,
                             PRIMARY KEY(tenant,id));
    """)
    connection.executemany("INSERT INTO customers VALUES (?, ?, ?)", [("alpha", 1, "A"), ("beta", 1, "B")])
    connection.executemany("INSERT INTO orders VALUES (?, ?, ?)", [("alpha", n, 1) for n in range(1, 101)])
    connection.execute("INSERT INTO orders VALUES ('beta', 1, 1)")
    connection.commit()
    return connection


class GroundTruth(unittest.TestCase):
    def test_orders_statement_growth(self):
        api = module("01-orders")
        with database() as db:
            statements = []
            db.set_trace_callback(statements.append)
            result = api.list_orders(db, "alpha", 80)
            self.assertEqual(len(result), 80)
            self.assertEqual(len(statements), 81)
            self.assertEqual({row["customer"] for row in result}, {"A"})

    def test_catalog_single_statement_and_tenant_scope(self):
        api = module("02-catalog")
        with database() as db:
            statements = []
            db.set_trace_callback(statements.append)
            result = api.list_catalog(db, "alpha", 50, 0)
            self.assertEqual(len(result), 50)
            self.assertEqual(len(statements), 1)
            self.assertEqual({row[1] for row in result}, {"A"})

    def test_catalog_bounds_precede_query(self):
        api = module("02-catalog")
        with database() as db:
            statements = []
            db.set_trace_callback(statements.append)
            for size, offset in [(51, 0), (1, 201), (True, 0), (1, -1)]:
                with self.assertRaises(ValueError):
                    api.list_catalog(db, "alpha", size, offset)
            self.assertEqual(statements, [])

    def test_catalog_schema_bounds_dataset(self):
        with database() as db:
            with self.assertRaises(sqlite3.IntegrityError):
                db.execute("INSERT INTO orders VALUES ('alpha', 201, 1)")

    def test_retry_repeats_effect_after_ambiguous_completion(self):
        api = module("03-delivery")
        provider = api.Provider()
        self.assertEqual(asyncio.run(api.deliver_order(provider, "order-7")), "delivered")
        self.assertEqual(provider.effects, ["order-7", "order-7"])

    def test_cache_crosses_tenant_boundary(self):
        api = module("05-cache")
        cache = {}
        records = {("alpha", 1): "alpha-only", ("beta", 1): "beta-only"}
        self.assertEqual(api.card(cache, records, "alpha", 1), "alpha-only")
        self.assertEqual(api.card(cache, records, "beta", 1), "alpha-only")

    def test_measurements_success_and_error_rates(self):
        self.assertEqual(5940 / 60, 99)
        self.assertEqual(3000 / 60, 50)
        self.assertEqual(60 / 6000, 0.01)
        self.assertEqual(3000 / 6000, 0.5)


if __name__ == "__main__":
    unittest.main()
