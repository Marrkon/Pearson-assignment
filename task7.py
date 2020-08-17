from pandas.util.testing import assert_frame_equal, assert_series_equal, assert_index_equal
from task2 import check_files_correctness 
import pandas as pd
import unittest

class DFTests(unittest.TestCase):

    def setUp(self):
        """ Check set up of the csv """
        
        path = 'datasets/'
        test_file_name =  'test_average_scores.csv'
        
        try:
            data = pd.read_csv(path + test_file_name,
                sep = ',')
            
        except IOError:
            print ('Cannot open the file')
            
        self.fixture = data

    def check_NaN_filtering(self):
        """ Check if function in task2 clear the dataset in a proper way """
        check_files_correctness(self.fixture.iloc[1])

        try:
            assert_frame_equal(self.fixture.loc[8].tolist(), [8, 23, 'Class 1A', '15+', '2018-08-19', '2018-12-20', 18.4])
        except:
            print('Assert error', str([8, 23, 'Class 1A', '15+', '2018-08-19', '2018-12-20', 18.4]))
        
if __name__ == '__main__':
    DFTests.setUp(unittest)
    DFTests.check_NaN_filtering(unittest)
