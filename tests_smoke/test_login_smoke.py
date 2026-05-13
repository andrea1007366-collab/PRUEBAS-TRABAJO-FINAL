def test_login_smoke(driver):
    from pages.login_page import LoginPage
    login = LoginPage(driver)
    driver.get("https://practicetestautomation.com/practice-test-login/")
    login.login("student", "Password123")
    assert "Bienvenido" in driver.page_source
