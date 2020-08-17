### Task 2 - check files correctness 

from task1 import import_files

# Filter rows of datasets in order to eliminate noise 
def check_files_correctness(test):

    # Select only rows with integer id
    test = test[test['student_id'].apply(lambda x: str(x).isdigit())]
    test = test[test['class_id'].apply(lambda x: str(x).isdigit())]
    test = test[test['test_level_id'].apply(lambda x: str(x).isdigit())]
    test = test[test['licence_id'].apply(lambda x: str(x).isdigit())]

    # Clear empty overall_score and authorized_at rows
    test = test[test['test_status'].notna()]
    test = test[test['authorized_at'].notna()]

    print('File correctness inspection finished!')
    return test 

if __name__ == '__main__':
    path = 'datasets/'
    _, _, test = import_files(path)
    check_files_correctness(test)