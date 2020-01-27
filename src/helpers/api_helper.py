from requests import Session

from constants import API_KEY, BASE_URL

"""
Api helper to work with Requests library
"""


class ApiHelper:
    def get_request(self, params, route=""):
        """
        sends "GET" api request as authorized user
        :param params: params according to documentation
        :param route: request route (without base url)
        :return: response
        """
        # TODO: Api key is hardcoded. Add authentication logic in future
        params["apikey"] = API_KEY
        response = Session().request(url=BASE_URL + route, method="GET", params=params)
        return response
