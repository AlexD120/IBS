import pytest

from ibs.pages.page import BasicPage
from ibs.utils.utils import Client, Client2
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def client2():
    return Client2()


# @pytest.fixture()
# def driver():
#     options = Options()
#     options.add_experimental_option(
#         'excludeSwitches', ['enable-logging']
#     )  # опция что бы не было ничего лишнего в терминале
#     driver = webdriver.Chrome(options=options)
#     yield driver
#     driver.quit()
