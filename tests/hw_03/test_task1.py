import unittest
from datetime import datetime, timedelta
from src.hw_03.task1 import get_days_from_today

class TestGetDaysFromToday(unittest.TestCase):

    def test_past_date(self):
        past_date = (datetime.today() - timedelta(days=10)).strftime("%Y-%m-%d")
        self.assertEqual(get_days_from_today(past_date), 10)

    def test_future_date(self):
        future_date = (datetime.today() + timedelta(days=5)).strftime("%Y-%m-%d")
        self.assertEqual(get_days_from_today(future_date), -5)

    def test_today_date(self):
        today_date = datetime.today().strftime("%Y-%m-%d")
        self.assertEqual(get_days_from_today(today_date), 0)

    def test_invalid_format(self):
        self.assertIsNone(get_days_from_today("03-02-2026"))
        self.assertIsNone(get_days_from_today("2026/02/03"))

if __name__ == "__main__":
    unittest.main()