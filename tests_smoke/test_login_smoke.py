def test_login_smoke(driver):
    from pages.login_page import LoginPage
    login = LoginPage(driver)
    driver.get("http://automationpractice.pl/index.php?controller=authentication")
    login.login("usuario_test", "pass123")
    assert "Bienvenido" in driver.page_source
