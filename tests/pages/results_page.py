from selenium.webdriver.common.by import By
from .base_page import BasePage


class ResultPage(BasePage):
    PAGE_HEADER = (By.ID, "firstHeading")

    def __init__(self, driver):
        super().__init__(driver)

    def header_matches(self, phrase):
        return phrase in self.driver.find_element(*self.PAGE_HEADER).text
