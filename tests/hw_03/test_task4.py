import unittest
from datetime import datetime, date
from unittest.mock import patch
from src.hw_03.task4 import get_upcoming_birthdays

class TestGetUpcomingBirthdays(unittest.TestCase):

    def setUp(self):
        self.users = [
            {"name": "John Doe", "birthday": "1985.01.23"},
            {"name": "Jane Smith", "birthday": "1990.01.27"},
            {"name": "Weekend Star", "birthday": "2000.01.27"},
            {"name": "Old Timer", "birthday": "1980.01.20"},
        ]
        self.expected = [
            {'name': 'John Doe', 'congratulation_date': '2024.01.23'},
            {'name': 'Jane Smith', 'congratulation_date': '2024.01.29'},
            {'name': 'Weekend Star', 'congratulation_date': '2024.01.29'},
        ]
        self.today = date(2024, 1, 22)

    @patch("task4.datetime")
    def test_upcoming_birthdays(self, mock_datetime):
        mock_datetime.today.return_value = datetime(2024, 1, 22)
        mock_datetime.strptime = datetime.strptime

        result = get_upcoming_birthdays(self.users)
        self.assertEqual(result, self.expected)

    @patch("task4.datetime")
    def test_no_upcoming_birthdays(self, mock_datetime):
        mock_datetime.today.return_value = datetime(2024, 1, 22)
        mock_datetime.strptime = datetime.strptime

        far_users = [{"name": "Future Star", "birthday": "1995.12.31"}]
        result = get_upcoming_birthdays(far_users)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()
