import allure
import pytest

from ibs.utils import utils
from ibs.schema import schemas
from jsonschema import validate


@allure.title("Тест на получение пользователя")
@allure.feature("Управление пользователями")
@allure.story("Получение пользователя через API")
@allure.label('component', 'API')
@allure.tag('API', 'Regression', 'Negative')
@allure.severity('Minor')
@allure.label("owner", "Davydov")
@pytest.mark.parametrize("client_class", [utils.Client])
def test_single_users():
    client = client_class()
    response = client.get(
        "/api/users?pages=2",
        allow_redirects=False,
    )
    body = response.json()
    assert response.status_code == 200
    validate(body, schema=schemas.GET_SINGLE_USER)
    assert body['data'][0]['email'] == 'michael.lawson@reqres.in'
