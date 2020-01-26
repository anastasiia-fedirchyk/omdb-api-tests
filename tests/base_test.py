import os


# TODO: Is used for logging. Add implementation in future
from logger_configuration import logger


class BaseTest:

    def setup_method(self):
        logger.info(f"{os.environ.get('PYTEST_CURRENT_TEST')} test started")

    def teardown_method(self):
        logger.info(f"{os.environ.get('PYTEST_CURRENT_TEST')} test finished")
