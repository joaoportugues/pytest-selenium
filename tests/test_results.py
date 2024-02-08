from selenium.webdriver.common.by import By
from .pages.home_page import HomePage
from .pages.home_page_chain import HomePageChain
from .pages.home_page_injection import HomePageInjection
from .pages.results_page import ResultPage


def test_wikipedia_result(driver):
    # page object model
    home_page = HomePage(driver)
    result_page = ResultPage(driver)

    home_page.navigate_to_wikipedia()
    assert home_page.title_matches("Wikipedia"), "The title doesn't match."
    home_page.search_for("Selenium")
    assert result_page.header_matches("Mercury"), "The header doesn't match."


def test_wikipedia_result_chain(driver):
    # chaining
    HomePageChain(driver) \
        .navigate_to_wikipedia() \
        .search_for("Selenium") \
        .url_matches("https://en.wikipedia.org/wiki/Selenium")


def test_wikipedia_result_injection(driver):
    # dependency injection
    home_page = HomePageInjection(driver)

    home_page.navigate_to_wikipedia("https://en.wikipedia.org/")
    home_page.search_for("searchInput", "Selenium")
    home_page.url_matches("https://en.wikipedia.org/wiki/Selenium")

