import pytest
import pytest_html
import base64
from selenium import webdriver

#@pytest.fixture(scope="class")
@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # Add screenshot on failure
            driver = item.funcargs.get('driver')
            if driver:
                screenshot = driver.get_screenshot_as_base64()
                extras.append(pytest_html.extras.image(screenshot, "Screenshot"))
    
    report.extras = extras
