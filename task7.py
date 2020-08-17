from pandas.util.testing import assert_frame_equal, assert_series_equal, assert_index_equal
from task2 import check_files_correctness 
import pandas as pd
import unittest

class DFTests(unittest.TestCase):

    def setUp(self, filename):
        """ Check set up of the csv """
        
        path = 'datasets/'
        
        try:
            data = pd.read_csv(path + filename, sep = ';')
            
        except IOError:
            print ('Cannot open the file')
            
        self.fixture = data

    def check_NaN_filtering(self):
        """ Check if function in task2 clear the dataset in a proper way """        
        empty_df = pd.DataFrame([],columns = ['id', 'student_id', 'class_id',  'created_at',  'updated_at', 'last_event_time',  'overall_score', 'test_status',	'institution_id', 'authorized_at', 'confidence_level',  'speaking_score', 'writing_score',  'reading_score',  'listening_score',  'test_level_id',  'licence_id'])

        # Test few cases of data filtering from task2  
        case1 = check_files_correctness(self.fixture.iloc[2:3,])
        case2 = check_files_correctness(self.fixture.iloc[3:4,:])
        case3 = check_files_correctness(self.fixture.iloc[37:38,])
        case4 = check_files_correctness(self.fixture.iloc[41:42,])
    
        # If left != right rise an error
        assert_frame_equal(case3, self.fixture.iloc[37:38,])
   
     
        
if __name__ == '__main__':
    # Filename which opening will be tested
    filename =  'test.csv'

    # Test part 
    DFTests.setUp(unittest, filename)
    DFTests.check_NaN_filtering(unittest)

    print("Test finished!")
