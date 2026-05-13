from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchResultsPage(BasePage):
    PRODUCT_LINK = (By.CSS_SELECTOR, ".product_list .product-name")

    def select_first_product(self):
        self.click(self.PRODUCT_LINK)
