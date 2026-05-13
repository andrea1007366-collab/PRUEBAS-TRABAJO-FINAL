from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.ID, "email_create")
        self.create_account_button = (By.ID, "SubmitCreate")

    def start_guest_checkout(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.create_account_button).click()