import json

import allure
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from ibs.data import locator
from ibs.utils import utils
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
@pytest.mark.parametrize("client_class", [utils.Client])
def test_list_users(client_class):
    client = client_class()
    response = client.get_list_users(url=locator.list_users)
    body = response.json()
    assert response.status_code == 200
    validate(body, schema=schemas.GET_LIST_USERS)
    assert body['data'][0]['id'] == 7


def test_web_list_users_positive():
    driver = webdriver.Chrome()
    driver.get('https://reqres.in/')
    button = driver.find_element(By.XPATH, '//li[@data-id="users"]')
    button.click()
    response_status = driver.find_element(
        By.CSS_SELECTOR, '[data-key="response-code"]'
    ).text
    response_body = driver.find_element(
        By.CSS_SELECTOR, '[data-key="output-response"]'
    ).text

    api_response = requests.get('https://reqres.in/api/users?page=2')
    assert api_response.status_code == int(response_status)
    assert api_response.json() == json.loads(response_body)

    driver.quit()
