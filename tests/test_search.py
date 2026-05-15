import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage

def test_search():
    driver = webdriver.Chrome()
    driver.get("https://automationpractice.com/index.php")

    home = HomePage(driver)
    home.search("dress")

    results = SearchResultsPage(driver)
    assert results.has_results()

    driver.quit()
