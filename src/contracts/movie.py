from logger_configuration import logger
from src.helpers.api_helper import ApiHelper


class Movie:
    api = ApiHelper()

    def api_get_movies(self, **kwargs):
        """
        sends request with params
        :param kwargs: params
        :return: response
        """
        response = self.api.request(method="GET", **kwargs)
        logger.debug(f"Method: 'GET', Url: {response.url}, Status code: {response.status_code}")
        return response
