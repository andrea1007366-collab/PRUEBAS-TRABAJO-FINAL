class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def proceed_to_checkout(self):
        # Localiza el botón "Proceed to checkout"
        button = self.driver.find_element("xpath", "//a[@title='Proceed to checkout']")
        button.click()
