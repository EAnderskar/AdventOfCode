import unittest
import Dec1 as Dec1

class TestDec1Pussel1(unittest.TestCase):
    def setUp(self):
        left_list = [3,4,2,1,3,3]
        right_list = [4,3,5,3,9,3]
        self.location_distance_calculator = Dec1.LocationDistanceCalculator(left_list=left_list, right_list=right_list)

    def test_example_on_website(self):      
        self.location_distance_calculator.calculate_total_distance()
        self.assertEqual(self.location_distance_calculator.total_distance, 11)

    def test_similarity_score(self):
        self.location_distance_calculator.calculate_similarity_score()
        self.assertEqual(self.location_distance_calculator.similarity_score,31)
    

if __name__ == '__main__':
    unittest.main()
