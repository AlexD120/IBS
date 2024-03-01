import json
import allure
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from ibs.parameters import param
from ibs.schema import schemas
from jsonschema import validate
import pytest


@allure.title("Тест получения списка пользователей")
@allure.feature("Управление пользователями")
@allure.story("Получение списка пользователей")
@allure.label('type', 'regression')
@allure.tag('API')
@allure.severity('normal')
@allure.label("owner", "Davydov")
@pytest.mark.parametrize(
    "creat_users",
    [
        param.ApiTestScenario(
            url_endpoint=param.create_user,
            body_request=param.create_user,
            status_code=param.create_user,
        )
    ],
)
def test_list_users(client, creat_users):
    response = client.post(
        param.create_user.url_endpoint,
        allow_redirects=False,
    )
    body = response.json()
    assert response.status_code == param.create_user.status_code
    validate(body, schema=schemas.GET_LIST_USERS)
    assert body['data'][0]['id'] == 7
