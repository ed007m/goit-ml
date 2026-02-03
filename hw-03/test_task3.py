import unittest
from task3 import normalize_phone

class TestNormalizePhone(unittest.TestCase):

    def test_examples(self):
        raw_numbers = [
            "067\t123 4567",
            "(095) 234-5678\n",
            "+380 44 123 4567",
            "380501234567",
            "    +38(050)123-32-34",
            "     0503451234",
            "(050)8889900",
            "38050-111-22-22",
            "38050 111 22 11   ",
        ]

        expected = [
            "+380671234567",
            "+380952345678",
            "+380441234567",
            "+380501234567",
            "+380501233234",
            "+380503451234",
            "+380508889900",
            "+380501112222",
            "+380501112211",
        ]

        results = [normalize_phone(num) for num in raw_numbers]
        self.assertEqual(results, expected)

    def test_with_only_digits(self):
        self.assertEqual(normalize_phone("0501234567"), "+380501234567")
        self.assertEqual(normalize_phone("380501234567"), "+380501234567")

    def test_with_plus_code(self):
        self.assertEqual(normalize_phone("+380501234567"), "+380501234567")
        self.assertEqual(normalize_phone("+380 50 123 45 67"), "+380501234567")

    def test_edge_cases(self):
        self.assertEqual(normalize_phone(""), "+38")
        self.assertEqual(normalize_phone("abc-def"), "+38")

if __name__ == "__main__":
    unittest.main()
