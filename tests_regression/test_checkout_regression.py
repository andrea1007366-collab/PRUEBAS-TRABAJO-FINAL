def test_checkout_regression(driver):
    from pages.home_page import HomePage
    from pages.search_results_page import SearchResultsPage
    from pages.product_page import ProductPage
    from pages.cart_page import CartPage
    from pages.checkout_page import CheckoutPage

    home = HomePage(driver)
    home.open()
    home.search("dress")
    results = SearchResultsPage(driver)
    assert results.has_results()
    results.select_first_product()
    product = ProductPage(driver)
    product.add_to_cart()
    product.proceed_to_checkout()
    cart = CartPage(driver)
    cart.proceed_to_checkout()
    checkout = CheckoutPage(driver)
    checkout.start_guest_checkout("testuser@example.com")
