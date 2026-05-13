from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USER = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "submit")

    def login(self, user, password):
        self.type(self.USER, user)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
