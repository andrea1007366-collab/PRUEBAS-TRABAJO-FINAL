import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.pages.home_page import HomePage
from selenium.pages.search_results_page import SearchResultsPage
from selenium.pages.product_page import ProductPage
from selenium.pages.cart_page import CartPage
from selenium.pages.checkout_page import CheckoutPage

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_checkout_guest(driver):
    home = HomePage(driver)
    home.open()
    home.search("dress")
    results = SearchResultsPage(driver)
    assert results.has_results()
    product = ProductPage(driver)
    product.add_to_cart()
    product.proceed_to_checkout()
    cart = CartPage(driver)
    cart.proceed_to_checkout()
    checkout = CheckoutPage(driver)
    checkout.start_guest_checkout("testuser@example.com")
