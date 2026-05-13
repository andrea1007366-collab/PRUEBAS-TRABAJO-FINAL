import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Configura el servicio de Chrome correctamente
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_search_product(driver):
    driver.get("http://automationpractice.pl/index.php")
    search_box = driver.find_element(By.ID, "search_query_top")
    search_box.send_keys("dress")
    driver.find_element(By.NAME, "submit_search").click()
    assert "dress" in driver.page_source.lower()