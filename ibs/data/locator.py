import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# ENDPOINT:
list_users = os.getenv('LIST_USERS')
single_user = os.getenv('SINGLE_USER')
single_user_not_found = os.getenv('USER_NOT_FOUND')
list_resource = os.getenv('LIST_RESOURCES')
single_resource = os.getenv('SINGLE_RESOURCE')
single_resource_not_found = os.getenv('SINGLE_RESOURCE_NOT_FOUND')
creat_user = os.getenv('CREATE_USER')
user = os.getenv('USER')
register_user = os.getenv('REGISTER_USER')
login_user = os.getenv('LOGIN_USER')
delayed_response = os.getenv('DELAYED_RESPONSE')


# STATUS CODE:
OK = 200
CREATE = 201
NO_CONTENT = 204
BAD_REQUEST = 400
NOT_FOUND = 404

# LOCATOR
driver = webdriver.Chrome()
base_url = "https://reqres.in/"
LIST_USERS = (By.XPATH, '//li[@data-id="users"]')
SINGLE_USER = (By.CSS_SELECTOR, '[data-id="users"]')
SINGLE_USER_NOT_FOUND = (By.CSS_SELECTOR, '[data-id="users"]')
LIST_RESOURCE = (By.CSS_SELECTOR, '[data-id="users"]')
SINGLE_RESOURCE = (By.CSS_SELECTOR, '[data-id="users"]')
SINGLE_RESOURCE_NOT_FOUND = (By.CSS_SELECTOR, '[data-id="users"]')
CREATE = (By.CSS_SELECTOR, '[data-id="users"]')
UPDATE_PUT = (By.CSS_SELECTOR, '[data-id="users"]')
UPDATE_PATCH = (By.CSS_SELECTOR, '[data-id="users"]')
DELETE = (By.CSS_SELECTOR, '[data-id="users"]')
REGISTER_SUCCESSFUL = (By.CSS_SELECTOR, '[data-id="users"]')
REGISTER_UNSUCCESSFUL = (By.CSS_SELECTOR, '[data-id="users"]')
LOGIN_SUCCESSFUL = (By.CSS_SELECTOR, '[data-id="users"]')
LOGIN_UNSUCCESSFUL = (By.CSS_SELECTOR, '[data-id="users"]')
DELAY = (By.CSS_SELECTOR, '[data-id="users"]')
FIELD_REQUEST = (By.CSS_SELECTOR, '[data-id="users"]')
FIELD_RESPONSE_CODE = (By.CSS_SELECTOR, '[data-key="response-code"]')
