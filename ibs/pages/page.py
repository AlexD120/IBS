from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from ibs.data import locator


class BasicPage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def get_response_code(self, response_code_locator):
        return self.driver.find_element(By.CSS_SELECTOR, response_code_locator).text

    def get_response_body(self, response_body_locator):
        return self.driver.find_element(By.CSS_SELECTOR, response_body_locator).text
