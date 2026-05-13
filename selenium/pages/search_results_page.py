from selenium.webdriver.common.by import By

class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        # Cada producto en los resultados tiene esta clase
        self.product = (By.CLASS_NAME, "product-container")

    def has_results(self):
        """Verifica si hay al menos un producto en los resultados"""
        return len(self.driver.find_elements(*self.product)) > 0

    def select_first_product(self):
        """Haz clic en el primer producto encontrado"""
        products = self.driver.find_elements(*self.product)
        if products:
            products[0].click()
