from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_button = (By.ID, "add_to_cart")
        self.proceed_to_checkout_button = (By.XPATH, "//a[@title='Proceed to checkout']")

    def add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    def proceed_to_checkout(self):
        self.driver.find_element(*self.proceed_to_checkout_button).click()
