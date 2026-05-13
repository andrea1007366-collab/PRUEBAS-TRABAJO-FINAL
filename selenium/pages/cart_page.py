from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.XPATH, "//a[@class='button btn btn-default standard-checkout button-medium']")

    def proceed_to_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
