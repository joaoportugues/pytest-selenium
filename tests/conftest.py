import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def driver():
    # Setup WebDriver (e.g., Chrome)
    driver = webdriver.Chrome()
    # Maximize window or set other configurations
    driver.maximize_window()
    yield driver
    driver.quit()
