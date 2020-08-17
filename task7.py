### Task 7 - unit testing

from pandas.util.testing import assert_frame_equal, assert_series_equal, assert_index_equal
from task2 import check_files_correctness 
import pandas as pd
import unittest

class DFTests(unittest.TestCase):

    def setUp(self, filename, path):
        """ Check set up of the csv """
        try:
            data = pd.read_csv(path + filename, sep = ';')
            
        except IOError:
            print ('Cannot open the file')
            
        self.fixture = data


    # Task2 tests - filtering of NaN and int(id)
    def check_NaN_filtering(self):
        """ 
             Test columns which are processed in task 2:
            'student_id', 'class_id', 'test_status', 'authorized_at', 'test_level_id', 'licence_id'
             If left != right, assert_frame_equal(left,right) will rise an error
        """        

        # Nothing to change 
        testing_set = self.fixture[['student_id', 'class_id', 'test_status',	'authorized_at', 'test_level_id',  'licence_id']]
        case1 = check_files_correctness(testing_set.iloc[37:39,])
        assert_frame_equal(case1, testing_set.iloc[37:39,])

        # Values as numbers 
        testing_set_2 = pd.DataFrame({'student_id':3, 'class_id':3, 'test_status':3, 'authorized_at':3, 'test_level_id':3, 'licence_id':3}, index=['student_id'])
        case2 = check_files_correctness(testing_set_2)
        assert_frame_equal(case2, testing_set_2)

        # student_id values as string number
        testing_set_3 = pd.DataFrame({'student_id':'3', 'class_id':3, 'test_status':3, 'authorized_at':3, 'test_level_id':3, 'licence_id':3}, index=['student_id'])
        case3 = check_files_correctness(testing_set_3)
        assert_frame_equal(case3, testing_set_3)

        # All column values as string numbers
        testing_set_4 = pd.DataFrame({'student_id':'4', 'class_id':'4', 'test_status':'4', 'authorized_at':'4', 'test_level_id':'4', 'licence_id':'4'}, index=['student_id'])
        case4 = check_files_correctness(testing_set_4)
        assert_frame_equal(case4, testing_set_4)

    # Task3 tests - utils 
    # Task4 tests - avg 
   
if __name__ == '__main__':
    # Filename which opening will be tested
    filename, path =  'test.csv', 'datasets/'

    # Test part 
    DFTests.setUp(unittest, filename, path)
    DFTests.check_NaN_filtering(unittest)

    print("Test finished!")
