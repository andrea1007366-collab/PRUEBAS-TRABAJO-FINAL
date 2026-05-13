import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.pages.home_page import HomePage
from selenium.pages.search_results_page import SearchResultsPage
from selenium.pages.product_page import ProductPage

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_add_to_cart(driver):
    home = HomePage(driver)
    home.open()
    home.search("dress")
    results = SearchResultsPage(driver)
    assert results.has_results()
    product = ProductPage(driver)
    product.add_to_cart()
    product.proceed_to_checkout()
