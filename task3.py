### Task 3 - prepare test_utilization.csv

import numpy as np
import datetime

# Transform date ie. 06.07.18 11:37 to 2018-07-06 (YY-MM-DD format)
def adjust_format_to_date(row):
    dd_c = datetime.datetime.strptime(row['test_created_at'][:8],'%d.%m.%y')
    dd_a = datetime.datetime.strptime(row['test_authorized_at'][:8],'%d.%m.%y')
    dd_c = str(dd_c.year) + '-' + '%02d' % dd_c.month + '-' + '%02d' % dd_c.day
    dd_a = str(dd_a.year) + '-' + '%02d' % dd_a.month + '-' + '%02d' % dd_a.day
    return dd_c, dd_a

# Get 'name' and 'teaching hours' from class_csv
def get_name(row):
    desired_row = class_csv[class_csv['id'] == row['class_id']]
    return desired_row.values[0][3], desired_row.values[0][6]
    
# Copy from test desired columns in test_utilization.csv and sort by 'class_id'
df = test.sort_values(by = ['class_id'])
df = df[['class_id','created_at','authorized_at','test_level_id']]
df.columns = ['class_id', 'test_created_at','test_authorized_at','test_level']

# Change 'test_created_at' and 'test_authorized_at' date format
df[['test_created_at', 'test_authorized_at']] = df.apply(adjust_format_to_date, axis=1, result_type="expand")

# Take class 'name' and 'teaching hours' from class_csv
df[['class_name', 'teaching_hours']] = df.apply(get_name, axis=1, result_type="expand")

# Enumerate test_id from 1 to the range of data frame
df['test_id'] = np.arange(1, df.shape[0]+1)

# Make class_test_number
df['class_test_number'] = df.groupby('class_id').cumcount()+1

# Sort columns to desired order
test_utilization = df[['class_id', 'class_name', 'teaching_hours', 'test_id', 'test_created_at', 'test_authorized_at', 'test_level', 'class_test_number']]