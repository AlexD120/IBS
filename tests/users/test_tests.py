import json
import allure
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from ibs.utils import utils
from ibs.schema import schemas
from jsonschema import validate
from ibs.pages.page import BasicPage
from ibs.data import locator


@allure.title("Тест получения списка пользователей")
@allure.feature("Управление пользователями")
@allure.story("Получение списка пользователей")
@allure.label('type', 'regression')
@allure.tag('API')
@allure.severity('normal')
@allure.label("owner", "Davydov")
def test_list_users():
    client_v1 = utils.Client()
    response = client_v1.get(
        "/api/users?pages=2",
        allow_redirects=False,
    )
    body = response.json()
    assert response.status_code == 200
    validate(body, schema=schemas.GET_LIST_USERS)
    assert body['data'][0]['id'] == 7


def test_web_list_users_positive(driver):

    url = locator.base_url

    page = BasicPage(driver, url)
    page.open()
    button = page.find_element(locator.LIST_USERS)
    button.click()

    # button = driver.find_element(By.CSS_SELECTOR, '[data-id="users"]')
    # button.click()
    #
    # response_status = driver.find_element(
    #     By.CSS_SELECTOR, '[data-key="response-code"]'
    # ).text
    # response_body = driver.find_element(
    #     By.CSS_SELECTOR, '[data-key="output-response"]'
    # ).text
    #
    # api_response = requests.get('https://reqres.in/api/users?page=2')
    # assert api_response.status_code == int(response_status)
    # assert api_response.json() == json.loads(response_body)

    driver.quit()
