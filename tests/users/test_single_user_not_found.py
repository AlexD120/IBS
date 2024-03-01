import allure
import pytest

from ibs.utils import utils
from ibs.schema import schemas
from jsonschema import validate


@allure.title("")
@allure.feature("")
@allure.story("Получение пользователя через API")
@allure.label('component', 'API')
@allure.tag('API', 'Regression', 'Negative')
@allure.severity('Minor')
@allure.label("owner", "Davydov")
def test_single_users():
    client_v1 = utils.APIClient()
    response = client_v1.get(
        "/api/users?pages=2",
        allow_redirects=False,
    )
    body = response.json()
    assert response.status_code == 200
    validate(body, schema=schemas.GET_SINGLE_USER)
    assert body['data'][0]['email'] == 'michael.lawson@reqres.in'
