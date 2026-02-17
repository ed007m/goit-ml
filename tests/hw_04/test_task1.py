import unittest
import os
from src.hw_04.task1 import total_salary


class TestTotalSalary(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_salaries.txt"
        with open(self.test_file, "w", encoding="utf-8") as f:
            f.write("Valera,3000\nAminadav Uasj,2000\nJon Jonson,1000\n")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_correct_calculation(self):
        total, average = total_salary(self.test_file)
        self.assertEqual(total, 6000.0)
        self.assertEqual(average, 2000.0)

    def test_file_not_found(self):
        total, average = total_salary("non_existent_file.txt")
        self.assertEqual(total, 0.0)
        self.assertEqual(average, 0.0)

    def test_empty_file(self):
        empty_file = "empty.txt"
        open(empty_file, 'w').close()
        total, average = total_salary(empty_file)
        os.remove(empty_file)
        self.assertEqual(total, 0.0)
        self.assertEqual(average, 0.0)

    def test_broken_format(self):
        with open(self.test_file, "a", encoding="utf-8") as f:
            f.write("\nInvalid Line\nWorker,wrong_salary\n")

        total, average = total_salary(self.test_file)
        self.assertEqual(total, 6000.0)
        self.assertEqual(average, 2000.0)


if __name__ == "__main__":
    unittest.main()