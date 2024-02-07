from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePage(BasePage):
    WIKIPEDIA_URL = "https://www.wikipedia.org"
    SEARCH_FIELD = (By.ID, "searchInput")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_wikipedia(self):
        self.driver.get(self.WIKIPEDIA_URL)

    def title_matches(self):
        return "Wikipedia" in self.driver.title

    def search_for(self, phrase):
        search_field = self.driver.find_element(*self.SEARCH_FIELD)
        search_field.clear()
        search_field.send_keys(phrase)
        search_field.submit()

    def url_matches(self, phrase):
        return phrase in self.driver.current_url
