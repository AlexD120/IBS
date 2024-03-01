from ibs.data import locator as loc
from ibs.data import requests_body as rb


class ApiTestScenario:
    def __init__(self, url_endpoint: str, body_request: str, status_code: int):
        self.url_endpoint = url_endpoint
        self.body_request = body_request
        self.status_code = status_code


list_user = ApiTestScenario(
    url_endpoint=loc.list_users, body_request=None, status_code=loc.OK
)
create_user = ApiTestScenario(
    url_endpoint=loc.creat_user, body_request=rb.USER_CREATE, status_code=loc.CREATE
)
