import pytest
from .pages.home_page import HomePage
from .pages.login_page import LoginPage

@pytest.mark.parametrize(
        "search, expected_url", 
        [
            ("Selenium", "https://en.wikipedia.org/wiki/Selenium"), 
            ("Mercury", "https://en.wikipedia.org/wiki/Mercury")
        ]
    )
def test_wikipedia_search(driver, search, expected_url):
    home_page = HomePage(driver)

    home_page.navigate_to_wikipedia()
    assert home_page.is_title_matches(), "The title doesn't match."
    home_page.search_for(search)
    assert home_page.check_url_matches(expected_url), "The url doesn't match."

