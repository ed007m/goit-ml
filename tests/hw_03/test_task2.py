import unittest
from src.hw_03.task2 import get_numbers_ticket

class TestGetNumbersTicket(unittest.TestCase):

    def test_valid_input(self):
        result = get_numbers_ticket(1, 49, 6)
        self.assertEqual(len(result), 6)
        self.assertEqual(result, sorted(result))
        self.assertEqual(len(result), len(set(result)))
        self.assertTrue(all(1 <= n <= 49 for n in result))

    def test_min_greater_than_max(self):
        self.assertEqual(get_numbers_ticket(10, 5, 3), [])

    def test_quantity_too_large(self):
        self.assertEqual(get_numbers_ticket(1, 5, 10), [])

    def test_quantity_zero(self):
        self.assertEqual(get_numbers_ticket(1, 10, 0), [])

    def test_min_less_than_one(self):
        self.assertEqual(get_numbers_ticket(0, 10, 3), [])

    def test_max_greater_than_1000(self):
        self.assertEqual(get_numbers_ticket(1, 1001, 3), [])

    def test_full_range(self):
        result = get_numbers_ticket(1, 5, 5)
        self.assertEqual(result, [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
