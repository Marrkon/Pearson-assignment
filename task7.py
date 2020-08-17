from pandas.util.testing import assert_frame_equal, assert_series_equal, assert_index_equal
from task2 import check_files_correctness 
import pandas as pd
import unittest

class DFTests(unittest.TestCase):

    def setUp(self):
        """ Check set up of the csv """
        
        path = 'datasets/'
        test_file_name =  'test.csv'
        
        try:
            data = pd.read_csv(path + test_file_name,
                sep = ';')
            
        except IOError:
            print ('Cannot open the file')
            
        self.fixture = data

    def check_NaN_filtering(self):
        """ Check if function in task2 clear the dataset in a proper way """


        # Test few cases of data filtering from task2  
        print("Here", self.fixture.iloc[1])

        case1 = check_files_correctness(self.fixture.iloc[1])
        case2 = check_files_correctness(self.fixture.iloc[2])
        case3 = check_files_correctness(self.fixture.iloc[3])
        case4 = check_files_correctness(self.fixture.iloc[4])

        try:
            assert_frame_equal(case1, [])
            assert_frame_equal(case2, [])
            assert_frame_equal(case3, [])
            assert_frame_equal(case4, [])
        except:
            print('Assert error')
        
if __name__ == '__main__':
    DFTests.setUp(unittest)
    DFTests.check_NaN_filtering(unittest)
