class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def is_guest_checkout_available(self):
        # Busca si existe la opción de checkout como invitado
        try:
            element = self.driver.find_element("xpath", "//button[@name='guest_checkout']")
            return element.is_displayed()
        except:
            return False
