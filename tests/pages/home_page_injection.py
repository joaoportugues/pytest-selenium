from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePageInjection(BasePage):
    SEARCH_FIELD = (By.ID, "searchInput")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_wikipedia(self, url):
        self.driver.get(url)

    def search_for(self, locator, phrase):
        search_field = self.driver.find_element(By.ID, locator)
        search_field.clear()
        search_field.send_keys(phrase)
        search_field.submit()

    def url_matches(self, url):
        return url in self.driver.current_url
