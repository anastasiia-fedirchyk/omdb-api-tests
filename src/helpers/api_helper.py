from requests import Session

from constants import API_KEY, BASE_URL

"""
Api helper to work with Requests library
"""


class ApiHelper:
    def __init__(self, base_url=BASE_URL, api_key=API_KEY):
        self.base_url = base_url
        self.api_key = api_key

    def get_request(self, params, route=""):
        """
        sends "GET" api request as authorized user
        :param params: params according to documentation
        :param route: request route (without base url)
        :return: response
        """
        # TODO: Api key is hardcoded. Add authentication logic in future
        params["apikey"] = self.api_key
        response = Session().request(url=f"{self.base_url}{route}", method="GET", params=params)
        return response
