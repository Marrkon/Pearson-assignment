### Task 5 - Save dataframes to the csv

from task3 import prepare_test_utilization
from task4 import prepare_avg_score

def prepare_csv_from_results(path):
    print("\n\n*Start preparing test_utilization*")
    test_utilization = prepare_test_utilization()

    print("\n\n*Start preparing avg score*")
    avg_score = prepare_avg_score()

    test_utilization.to_csv(path + 'test_utilization.csv')
    avg_score.to_csv(path + 'test_average_scores.csv')

if __name__ == '__main__':
    path = 'datasets/'
    prepare_csv_from_results(path)