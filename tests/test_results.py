import pytest
from .pages.home_page import HomePage
from .pages.results_page import ResultPage

def test_wikipedia_result(driver):
    home_page = HomePage(driver)
    result_page = ResultPage(driver)

    home_page.navigate_to_wikipedia()
    assert home_page.is_title_matches(), "The title doesn't match."
    home_page.search_for("Selenium")
    assert result_page.get_page_header("Mercury"), "The header doesn't match."

