class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        # Localiza el botón "Add to cart" por su selector
        button = self.driver.find_element("xpath", "//button[@name='Submit']")
        button.click()
