import pytest
import time

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.smoke
def test_complete_checkout(page):

    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")

    home = HomePage(page)
    home.add_product("Sauce Labs Backpack")
    home.open_cart()

    cart = CartPage(page)
    assert cart.get_item_count() == 1
    cart.checkout()

    checkout = CheckoutPage(page)
    checkout.enter_customer_details("Sanskar", "Gaikwad", "413307")
    checkout.continue_checkout()
    checkout.finish_order()

    message = checkout.get_success_message()
    assert message == "Thank you for your order!"
    
    time.sleep(3)


@pytest.mark.regression
def test_checkout_flow(page):

    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")

    home = HomePage(page)
    home.add_product("Sauce Labs Bike Light")
    home.open_cart()

    cart = CartPage(page)
    cart.checkout()

    checkout = CheckoutPage(page)
    checkout.enter_customer_details("Test", "User", "12345")
    checkout.continue_checkout()

    assert "checkout-step-two.html" in page.url
    
    time.sleep(3)
