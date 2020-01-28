import csv
import os

from constants import TEST_DATA_DIRECTORY


def get_test_data_from_csv(file_name: str):
    """
    gets test data from csv file and returns data structures for use in parametrization
    :param file_name: file_name (file should be located in "test_data" dir)
    :return: list of dicts
    """
    full_file_path = os.path.join(TEST_DATA_DIRECTORY, file_name)
    with open(full_file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]
