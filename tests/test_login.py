import pytest
from .pages.home_page import HomePage
from .pages.login_page import LoginPage

@pytest.mark.parametrize("username, password", [("user1", "password1"), ("user2", "password2")])
def test_login(driver, username, password):
    # Initialize page objects
    home_page = HomePage(driver)
    login_page = LoginPage(driver)

    # Navigate to login page
    home_page.navigate_to_login()

    # Perform login
    login_page.login(username, password)

    # Assert login success
    assert home_page.is_logged_in()

