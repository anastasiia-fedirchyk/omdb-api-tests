import pytest

from src.helpers.csv_helper import get_test_data_from_csv
from src.helpers.search_helpers import find_information_about_movie
from src.scenarious.movie_steps import MovieSteps
from tests.base_test import BaseTest


class TestParametrizationExample(BaseTest):
    search_steps = MovieSteps()
    values_text_search = get_test_data_from_csv(file_name="search_movie_by_text_data.csv")
    values_id_search = get_test_data_from_csv(file_name="search_movie_by_id_data.csv")
    values_title_search = get_test_data_from_csv(file_name="search_movie_by_title_data.csv")

    @pytest.mark.parametrize("case", values_text_search)
    def test_search_by_text(self, case):
        search_by_text_movies_list = self.search_steps.get_movies_by_search_string(search_string=case["text_to_search"],
                                                                                   first_page=case["start_search_page"],
                                                                                   last_page=case["last_search_page"])
        assert (find_information_about_movie(movies_list=search_by_text_movies_list,
                                             value=case["expected_movie_in_list"])), f"Movies list does not contain " \
            f"information about case{case['expected_movie_in_list']}"

    @pytest.mark.parametrize("case", values_id_search)
    def test_search_by_id(self, case):
        search_by_id_result = self.search_steps.get_movie_by_id(movie_id=case["id_to_search"])
        assert search_by_id_result.released == case["released_expected"], f"Expected released" \
            f" value - {case['released_expected']}, but was - {search_by_id_result.released}"
        assert search_by_id_result.title == case["title_expected"], f"Expected genre value " \
            f"- {case['title_expected']}, but was - {search_by_id_result.genre}"

    @pytest.mark.parametrize("case", values_title_search)
    def test_search_by_title(self, case):
        search_by_title_result = self.search_steps.get_movie_by_title(movie_title=case['title_to_search'])
        assert case['expected_in_plot'] in search_by_title_result.plot, f"Movie's plot " \
            f"does not contain {case['expected_in_plot']}"
        assert search_by_title_result.runtime == case['expected_runtime'], f"Expected runtime value " \
            f"- {case['expected_runtime']}, but was - {search_by_title_result.runtime}"
