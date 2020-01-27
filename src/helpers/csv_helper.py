import csv
import os

from constants import TEST_DATA_DIRECTORY


def get_test_data_from_csv(file_name: str):
    """
    gets test data from csv file and returns data structures for use in parametrization
    :param file_name: file_name (file should be located in "test_data" dir)
    :return: headers - list of str, values - list of tuples
    """
    full_file_path = os.path.join(TEST_DATA_DIRECTORY, file_name)
    values = []
    with open(full_file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            values.append(row)
        return values
