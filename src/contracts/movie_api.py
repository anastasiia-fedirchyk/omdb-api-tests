from logger_configuration import logger
from src.helpers.api_helper import ApiHelper

"""
class to describe logic to work with Movie controller, 
for example: in future will be added: def api_post_movie(), def api_delete_movie() etc.
"""


class MovieApi:
    api = ApiHelper()

    @classmethod
    def api_get_movies(cls, **kwargs):
        """
        sends request with params
        :param kwargs: params
        :return: response
        """
        response = cls.api.get_request(**kwargs)
        return response
