import requests

class Http():

    @staticmethod
    def get(url, params=None, allow_redirects=False, **kwargs):
        return requests.get(url, params, allow_redirects=allow_redirects, **kwargs)

    @staticmethod
    def post(url, params=None, allow_redirects=False, **kwargs):
        return requests.post(url, params, allow_redirects=allow_redirects, **kwargs)