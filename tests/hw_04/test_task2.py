import unittest
import os
from src.hw_04.task2 import get_cats_info

class TestGetCatsInfo(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_cats.txt"
        with open(self.test_file, "w", encoding="utf-8") as f:
            f.write("1,Tayson,3\n2,Vika,1\n")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_return_type(self):
        result = get_cats_info(self.test_file)
        self.assertIsInstance(result, list)
        if result:
            self.assertIsInstance(result[0], dict)

    def test_correct_data(self):
        result = get_cats_info(self.test_file)
        expected = [
            {"id": "1", "name": "Tayson", "age": "3"},
            {"id": "2", "name": "Vika", "age": "1"}
        ]
        self.assertEqual(result, expected)

    def test_empty_or_missing_file(self):
        self.assertEqual(get_cats_info("missing.txt"), [])