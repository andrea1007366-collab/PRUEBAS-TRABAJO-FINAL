import pytest
from selenium import webdriver
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout_guest():
    driver = webdriver.Chrome()
    driver.get("https://automationpractice.com/index.php?controller=order")

    cart = CartPage(driver)
    cart.proceed_to_checkout()

    checkout = CheckoutPage(driver)
    assert checkout.is_guest_checkout_available()

    driver.quit()
