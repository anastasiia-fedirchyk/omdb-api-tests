from logger_configuration import logger
from src.helpers.api_helper import ApiHelper

"""
class to specify logic to work with Movie controller, 
for example: in future will be added: def api_post_movie(), def api_delete_movie() etc.
"""


class Movie:
    api = ApiHelper()

    def api_get_movies(self, **kwargs):
        """
        sends request with params
        :param kwargs: params
        :return: response
        """
        response = self.api.get_request(**kwargs)
        logger.debug(f"Method: 'GET', Url: {response.url}, Status code: {response.status_code}")
        return response
