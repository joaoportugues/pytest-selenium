import pytest
from selenium import webdriver

#@pytest.fixture(scope="class")
@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def pytest_exception_interact(node, call, report):
    if report.failed:
        driver = node.funcargs['driver']
        driver.save_screenshot("screenshot.png")
