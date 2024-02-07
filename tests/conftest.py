import pytest
import base64
from selenium import webdriver

#@pytest.fixture(scope="class")
@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

