### Task 1 - import files

import pandas as pd

def import_files():
    path = 'datasets/'
    class_csv = pd.read_csv(path + 'class.csv', sep=';')
    test_level = pd.read_csv(path + 'test_level.csv', sep=';')
    test = pd.read_csv(path + 'test.csv', sep=';')

    print('Class_csv, test_level, test are imported!')
    return class_csv, test_level, test

if __name__ == '__main__':
    import_files()