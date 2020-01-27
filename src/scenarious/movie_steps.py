from logger_configuration import logger
from src.contracts.movie import Movie
from src.models.movie import Movies, UniqueMovie, mapping_factory


class MovieSteps:
    movie_contract = Movie()

    def get_movies_by_search_string(self, search_string, first_page: int = 1, last_page: int = 1) -> list:
        """
        gets all movies that match search query on defined pages
        :param search_string: search query
        :param first_page: start search from page, default: 1
        :param last_page: stop search (including page), default: 1
        :return: list of UniqueMovie objects
        """
        movies_data = Movies()
        payload = {"s": search_string}

        for page in range(int(first_page), int(last_page) + 1):
            payload["page"] = page
            response = self.movie_contract.api_get_movies(params=payload).json()
            if "totalResults" in response.keys():
                logger.info(f"Page {page} contains information for search query '{search_string}'")
                for item in response["Search"]:
                    unique_movie = mapping_factory.load(item, UniqueMovie)
                    movies_data.movies_list.append(unique_movie)
            else:
                logger.info(f"Page {page} does not contain information for search query '{search_string}'")

        return movies_data.movies_list

    def get_movie_by_id(self, movie_id: str) -> UniqueMovie:
        """
        gets movie by id ("imdbID")
        :param movie_id: imdbID to search
        :return: UniqueMovie object
        """
        payload = {"i": movie_id}
        response = self.movie_contract.api_get_movies(params=payload)
        logger.info(f"Movie by id '{movie_id}' found") if movie_id in response.text else logger.info(
            f"Movie by id '{movie_id}' not found")
        return mapping_factory.load(response.json(), UniqueMovie)

    def get_movie_by_title(self, movie_title: str) -> UniqueMovie:
        """
        gets movie by movie title ("Title")
        :param movie_title: title to search
        :return: UniqueMovie object
        """
        payload = {"t": movie_title}
        response = self.movie_contract.api_get_movies(params=payload)
        logger.info(f"Movie by title '{movie_title}' found") if movie_title in response.text else logger.info(
            f"Movie by title '{movie_title}' not found")
        return mapping_factory.load(response.json(), UniqueMovie)
