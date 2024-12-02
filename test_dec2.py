import unittest
import dec2 as dec2

class Test2December(unittest.TestCase):

    def test_count_safe_records(self):
        input = [[7,6,4,2,1],
        [1,2,7,8,9],
        [9,7,6,2,1],
        [1,3,2,4,5],
        [8,6,4,4,1],
        [1,3,6,7,9]]

        output = dec2.count_number_of_save_reports(input)
        self.assertEqual(output,2)
    
    def test_count_safe_records_with_problem_damper(self):
        input = [[7,6,4,2,1],
        [1,2,7,8,9],
        [9,7,6,2,1],
        [1,3,2,4,5],
        [8,6,4,4,1],
        [1,3,6,7,9]]

        output = dec2.count_number_of_save_reports_problem_damper(input)
        self.assertEqual(output,4)


if __name__ == "__main__":
    unittest.main()