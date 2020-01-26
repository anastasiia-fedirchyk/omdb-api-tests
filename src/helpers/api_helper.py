from requests import Session

from constants import API_KEY, BASE_URL


class ApiHelper:
    def request(self, method, params, route=""):
        """
        sends api request as authorized user
        :param method: method which is supported by web service
        :param params: params according to documentation
        :param route: request route (without base url)
        :return: response
        """
        # TODO: Api key is hardcoded. Add authentication logic in future
        params["apikey"] = API_KEY
        response = Session().request(url=BASE_URL + route, method=method, params=params)
        return response
