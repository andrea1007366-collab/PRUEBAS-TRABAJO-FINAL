import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def pytest_exception_interact(node, call, report):
    driver = node.funcargs.get("driver", None)
    if driver:
        driver.save_screenshot(f"reports/{node.name}.png")
