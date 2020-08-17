### Task 5 - Save dataframes to the csv

from task1 import import_files
from task2 import check_files_correctness
from task3 import prepare_test_utilization
from task4 import prepare_avg_score

# Convert pandas dataframes to csv files
def prepare_csv_from_results(path, class_csv, test):
    print("\n*Start preparing test_utilization*")
    test_utilization = prepare_test_utilization(class_csv, test)

    print("\n*Start preparing avg score*")
    avg_score = prepare_avg_score(class_csv, test)

    test_utilization.to_csv(path + 'test_utilization.csv')
    avg_score.to_csv(path + 'test_average_scores.csv')

if __name__ == '__main__':
    # Import files
    path = 'datasets/'
    class_csv, _, test = import_files(path)

     # Clear dataset - task2
    test = check_files_correctness(test)

    # Prepare csv files for both datasets
    prepare_csv_from_results(path, class_csv, test)