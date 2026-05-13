from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    URL = "http://automationpractice.pl/index.php"
    SEARCH_BOX = (By.ID, "search_query_top")
    SEARCH_BUTTON = (By.NAME, "submit_search")

    def open(self):
        self.driver.get(self.URL)

    def search(self, text):
        self.type(self.SEARCH_BOX, text)
        self.click(self.SEARCH_BUTTON)
