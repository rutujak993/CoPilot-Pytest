import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from AutoInfraAmazon import *


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    web_driver = None
    web_driver = webdriver.Chrome(ChromeDriverManager().install())
    web_driver.implicitly_wait(2)
    request.cls.driver = web_driver

    TestLogin.test_login(request.cls, username="8999634754", password="Shriram@1693")
    yield
    web_driver.close()