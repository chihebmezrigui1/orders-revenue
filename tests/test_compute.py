import unittest
from compute import compute_total_revenue_eur, revenue_by_marketplace

class TestCompute(unittest.TestCase):

    def test_total_revenue(self):
        orders = [{"amount_cents": 100}, {"amount_cents": 250}, {}]
        self.assertEqual(compute_total_revenue_eur(orders), 3.50)

    def test_revenue_by_marketplace(self):
        orders = [
            {"marketplace":"amazon", "amount_cents":100},
            {"marketplace":"amazon", "amount_cents":200},
            {"marketplace":"ebay", "amount_cents":50},
            {"marketplace":"", "amount_cents":100},
        ]
        res = revenue_by_marketplace(orders)
        self.assertEqual(res["amazon"], 3.00)
        self.assertEqual(res["ebay"], 0.50)
        self.assertNotIn("", res)

if __name__ == "__main__":
    unittest.main()
