import os
import allure
import pytest
from dotenv import load_dotenv
from requests import Request, Session
from allure_commons.types import AttachmentType
from logging import info
from curlify import to_curl


class APIClientBase:
    load_dotenv()
    base_url = os.getenv('BASE_URL')

    def __init__(self, base_url: str = None):
        self.BASE_URL = base_url or self.base_url
        self.session = Session()

    def _make_request(self, method: str, url: str, **kwargs):
        full_url = self.BASE_URL + url
        with allure.step(f"{method} {url}"):
            response = self.session.request(method, full_url, **kwargs)
            curl = to_curl(response.request)
            info(curl)
            allure.attach(
                body=curl,
                name="curl",
                attachment_type=AttachmentType.TEXT,
                extension="txt",
            )
            return response

    def get(self, url: str, **kwargs):
        return self._make_request("GET", url, **kwargs)

    def post(self, url: str, **kwargs):
        return self._make_request("POST", url, **kwargs)

    def put(self, url: str, **kwargs):
        return self._make_request("PUT", url, **kwargs)

    def delete(self, url: str, **kwargs):
        return self._make_request("DELETE", url, **kwargs)

    def patch(self, url: str, **kwargs):
        return self._make_request("PATCH", url, **kwargs)


class Client(APIClientBase):
    def __init__(self):
        super().__init__()

    def get_list_users(self, url, **kwargs):
        return self._make_request("GET", url, **kwargs)

    def post(self, url: str, **kwargs):
        return self._make_request("POST", url, **kwargs)

    def put(self, url: str, **kwargs):
        return self._make_request("PUT", url, **kwargs)

    def delete(self, url: str, **kwargs):
        return self._make_request("DELETE", url, **kwargs)

    def patch(self, url: str, **kwargs):
        return self._make_request("PATCH", url, **kwargs)


class Client2(APIClientBase):
    def __init__(self):
        base_url = os.getenv('BASE_URL_2') or APIClientBase.base_url
        super().__init__(base_url)
