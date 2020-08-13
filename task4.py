### Task 4 - prepare test_average_scores.csv

from task3 import get_name, adjust_format_to_date

def prepare_avg_score():
    # Take idx of test marked as SCORING_SCORED
    df = test[test['test_status'] == 'SCORING_SCORED']
    df = df[['class_id', 'created_at', 'authorized_at', 'overall_score']]
    df.columns = ['class_id', 'test_created_at', 'test_authorized_at', 'overall_score']

    # Change 'test_created_at' and 'test_authorized_at' date format
    df[['test_created_at', 'test_authorized_at']] = df.apply(adjust_format_to_date, axis=1, result_type="expand")

    # Take the earliest/latest date from particular class (creation date/final authorization date)
    min_date = df.groupby(['class_id']).agg({'test_created_at': [np.min]})
    max_date = df.groupby(['class_id']).agg({'test_authorized_at': [np.max]})

    # Calculate avg_class_test_overall_score
    avg_score = df[['class_id','overall_score']].groupby('class_id').mean().round(2)

    # Join avg_class_test_overall_score with min_date and max_date 
    avg_score = avg_score.join(min_date).join(max_date)
    avg_score = avg_score.reset_index()
    avg_score.columns = ['class_id', 'avg_class_test_overall_score', 'test_created_at', 'test_authorized_at']

    # Take class 'name' and 'teaching hours' from class_csv
    avg_score[['class_name', 'teaching_hours']] = avg_score.apply(get_name, axis=1, result_type="expand")

    # Sort columns to desired order
    avg_score = avg_score[['class_id', 'class_name', 'teaching_hours', 'test_created_at', 'test_authorized_at', 'avg_class_test_overall_score']]

    return avg_score

if __name__ == '__main__':
    prepare_avg_score()