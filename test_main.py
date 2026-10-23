from main import calculate_avg, find_highest, find_lowest
import unittest
from csv_practice import load_grades , save_grades

class TestGradeAnalyzer(unittest.TestCase):
    def setUp(self):
        self.grades = {
            "math": 90,
            "python": 80,
             "statistics": 100
        }


    def test_avg(self):
        self.assertEqual(calculate_avg(self.grades), 90)


    def test_highest(self):
        self.assertEqual(find_highest(self.grades), ("statistics", 100))


    def test_lowest(self):
        self.assertEqual(find_lowest(self.grades), ("python", 80))
    
    def test_empty_avg(self):
        grades = {
                }
        self.assertEqual(calculate_avg(grades), 0)


    def test_zero_highest(self):
        grades ={
            "math" : 0,
            "python" : 0
        }
        self.assertEqual(find_highest(grades), ("math", 0))
    def test_single_lowest(self):
        grades = {
            "stats" : 75
        }
        self.assertEqual(find_lowest(grades), ("stats", 75))

    def test_save_grade(self):
       save_grades(self.grades, "test_grades")
       self.assertEqual(load_grades("test_grades"), self.grades)
if __name__ == "__main__":
    unittest.main()