***Api tests for OMDb API web service***

**Technology used:** Python/Pytest/Requests

**Content:**

contracts package - contains classes to execute requests;

helpers package - helpers to work with files and data;

models package  - DTOs;

scenarios  package - contains code to describe steps for tests;

tests package - contains tests and data for tests

**Installation:**

`cd omdb-api-tests`

`pip install -r requirements.txt`

**Tests running:**

`cd omdb-api-tests`

To run all tests: `pytest -s`

To run full flow test: `pytest -m end_to_end -s`

To run parametrized tests: `pytest -m parametrize -s`

The Log file will be generated in the omdb-api-tests directory after tests executions
