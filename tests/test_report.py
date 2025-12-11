import unittest
from report import find_suspicious_orders

class TestReport(unittest.TestCase):

    def test_suspicious_orders(self):
        orders = [
            {"id": "o1", "marketplace": "amazon", "amount_cents": 100},
            {"id": "o2", "marketplace": "", "amount_cents": 50},      
            {"id": "o3", "marketplace": "ebay", "amount_cents": -200}, 
            {"id": "o4", "amount_cents": 300},                         
        ]

        suspects = find_suspicious_orders(orders)

        expected = [
            "- o2: empty marketplace",
            "- o3: negative amount (-200)",
            "- o4: empty marketplace"
        ]
        self.assertEqual(suspects, expected)

if __name__ == "__main__":
    unittest.main()
