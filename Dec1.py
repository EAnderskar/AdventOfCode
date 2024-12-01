import numpy as np
import pandas as pd


class LocationDistanceCalculator():
    def __init__(self, left_list, right_list):
        """
        Initilize Location Distnce calculator by sorting two lists and calculate the total distance beween the lists. 
        """
        self.left_array = np.sort(left_list)
        self.right_array = np.sort(right_list)

    def calculate_total_distance(self):
       distances = np.abs(self.left_array-self.right_array)
       self.total_distance = np.sum(distances)

    def calculate_similarity_score(self):
        unique_values, counts = np.unique(self.left_array, return_counts=True)
        right_occurrences = np.array([np.sum(self.right_array == value)*count for value,count in zip(unique_values,counts)])
        self.similarity_score = np.sum(unique_values * right_occurrences)


if __name__ == '__main__':
    df = pd.read_csv('input_dec1.csv', sep=';')
    left_list = df['left_list'].to_list()
    right_list = df['right_list'].to_list()
    
    location_distance_calculator = LocationDistanceCalculator(left_list=left_list, right_list=right_list)
    location_distance_calculator.calculate_total_distance()
    location_distance_calculator.calculate_similarity_score()

    print(f"the Total Distance Between Locations is {location_distance_calculator.total_distance}")
    print(f"the similarity score between the lists is {location_distance_calculator.similarity_score}")



