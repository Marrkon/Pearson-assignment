### Task 2 - check files correctness 
from task1 import import_files

def check_files_correctness():

    _, _, test = import_files()

    # Select only rows with integer id
    test = test[test['student_id'].apply(lambda x: str(x).isdigit())]
    test = test[test['class_id'].apply(lambda x: str(x).isdigit())]
    test = test[test['test_level_id'].apply(lambda x: str(x).isdigit())]
    test = test[test['licence_id'].apply(lambda x: str(x).isdigit())]

    # Clear empty overall_score and authorized_at rows
    test = test[test['test_status'].notna()]
    test = test[test['authorized_at'].notna()]

    return test 

if __name__ == '__main__':
    check_files_correctness()