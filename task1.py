### Task 1 - import files

import pandas as pd

path = 'datasets/'

class_csv = pd.read_csv(path + 'class.csv', sep=';')
test_level = pd.read_csv(path + 'test_level.csv', sep=';')
test = pd.read_csv(path + 'test.csv', sep=';')