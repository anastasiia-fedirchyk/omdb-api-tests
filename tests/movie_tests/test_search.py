import pytest

from src.helpers.search_helpers import find_information_about_movie
from src.scenarios.movie_steps import MovieSteps
from tests.base_test import BaseTest


class TestSearch(BaseTest):
    search_steps = MovieSteps()

    @pytest.mark.end_to_end
    def test_search(self):
        text_to_search = "hacker"
        start_search_page = 1
        last_search_page = 50
        expected_list_len = 35
        title_to_find_1 = "Happy Birthday Hacker John"
        title_to_find_2 = "Untitled Hacker Story"
        title_to_find_3 = "Hacker: Hunter"
        released_expected = "21 Aug 2019"
        genre_expected = "Documentary, Crime"
        title_to_get_by_title = "The STEM Journals"
        expected_in_plot = "Science, Technology, Engineering and Math"
        expected_runtime = "22 min"

        # step 1
        search_by_text_movies_list = self.search_steps.get_movies_by_search_string(search_string=text_to_search,
                                                                                   first_page=start_search_page,
                                                                                   last_page=last_search_page)
        assert len(
            search_by_text_movies_list) >= expected_list_len, f"Expected list length - {expected_list_len}, " \
            f"but was - {len(search_by_text_movies_list)}"
        assert (find_information_about_movie(movies_list=search_by_text_movies_list,
                                             value=title_to_find_1)), f"Movies list does not contain " \
            f"information about {title_to_find_1}"

        assert (find_information_about_movie(movies_list=search_by_text_movies_list,
                                             value=title_to_find_2)), "Movies list does not contain " \
            f"information about {title_to_find_2}"

        # step 2
        movie_id = find_information_about_movie(movies_list=search_by_text_movies_list, value=title_to_find_3).imdb_id

        search_by_id_result = self.search_steps.get_movie_by_id(movie_id=movie_id)
        assert search_by_id_result.released == released_expected, f"Expected released value - {released_expected}, " \
            f"but was - {search_by_id_result.released}"
        assert search_by_id_result.genre == genre_expected, f"Expected genre value - {genre_expected}, " \
            f"but was - {search_by_id_result.genre}"

        # step 3
        search_by_title_result = self.search_steps.get_movie_by_title(movie_title=title_to_get_by_title)
        assert expected_in_plot in search_by_title_result.plot, f"Movie's plot does not contain {expected_in_plot}"
        assert search_by_title_result.runtime == expected_runtime, f"Expected runtime value - {expected_runtime}, " \
            f"but was - {search_by_title_result.runtime}"
