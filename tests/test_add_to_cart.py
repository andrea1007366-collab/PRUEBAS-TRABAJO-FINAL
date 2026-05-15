import pytest
from selenium import webdriver
from pages.product_page import ProductPage

def test_add_to_cart():
    driver = webdriver.Chrome()
    driver.get("https://automationpractice.com/index.php?id_product=1&controller=product")

    product = ProductPage(driver)
    product.add_to_cart()

    assert "Product successfully added" in driver.page_source

    driver.quit()
