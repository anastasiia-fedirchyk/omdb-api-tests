import logging
import os
import sys

# LOGGER CONFIGURATION FILE
from constants import PROJECT_DIRECTORY

logging.getLogger().setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s %(levelname)s: %(funcName)s: %(message)s", "%Y-%m-%d %H:%M:%S")
log_location = os.path.join(PROJECT_DIRECTORY, "omdb_api_log.txt")

# console log
console = logging.StreamHandler(sys.stdout)
console.setLevel(logging.DEBUG)
console.setFormatter(formatter)
logging.getLogger().addHandler(console)
logging.getLogger("urllib3").setLevel("ERROR")

# file log
file = logging.FileHandler(filename=log_location, mode="w")
file.setLevel(logging.DEBUG)
file.setFormatter(formatter)
logging.getLogger().addHandler(file)

logger = logging.getLogger("LOG")
