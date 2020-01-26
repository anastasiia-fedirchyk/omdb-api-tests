import pytest

from src.helpers.csv_helper import get_test_data_from_csv
from src.helpers.search_helpers import find_information_about_movie
from src.scenarious.movie_steps import MovieSteps
from tests.base_test import BaseTest


class TestParametrizationExample(BaseTest):
    search_steps = MovieSteps()
    headers_text_search, values_text_search = get_test_data_from_csv(file_name="search_movie_by_text_data.csv")
    headers_id_search, values_id_search = get_test_data_from_csv(file_name="search_movie_by_id_data.csv")
    headers_title_search, values_title_search = get_test_data_from_csv(file_name="search_movie_by_title_data.csv")

    @pytest.mark.parametrize(headers_text_search, values_text_search)
    def test_search_by_text(self, text_to_search, start_search_page, last_search_page, expected_movie_in_list):
        search_by_text_movies_list = self.search_steps.get_movies_by_search_string(search_string=text_to_search,
                                                                                   first_pagination=start_search_page,
                                                                                   last_pagination=last_search_page)
        assert (find_information_about_movie(movies_list=search_by_text_movies_list,
                                             value=expected_movie_in_list)), f"Movies list does not contain " \
            f"information about {expected_movie_in_list}"

    @pytest.mark.parametrize(headers_id_search, values_id_search)
    def test_search_by_id(self, id_to_search, released_expected, title_expected):
        search_by_id_result = self.search_steps.get_movie_by_id(movie_id=id_to_search)
        assert search_by_id_result.released == released_expected, f"Expected released value - {released_expected}, " \
            f"but was - {search_by_id_result.released}"
        assert search_by_id_result.title == title_expected, f"Expected genre value - {title_expected}, " \
            f"but was - {search_by_id_result.genre}"

    @pytest.mark.parametrize(headers_title_search, values_title_search)
    def test_search_by_title(self, title_to_search, expected_in_plot, expected_runtime):
        search_by_title_result = self.search_steps.get_movie_by_title(movie_title=title_to_search)
        assert expected_in_plot in search_by_title_result.plot, f"Movie's plot does not contain {expected_in_plot}"
        assert search_by_title_result.runtime == expected_runtime, f"Expected runtime value - {expected_runtime}, " \
            f"but was - {search_by_title_result.runtime}"
