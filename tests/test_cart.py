import pytest

import time  

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage


@pytest.mark.smoke
def test_add_product_to_cart(page):

    login = LoginPage(page)
    login.open()
    login.login(
        "standard_user",
        "secret_sauce"
    )

    home = HomePage(page)
    home.add_product(
        "Sauce Labs Backpack"
    )
    home.open_cart()

    cart = CartPage(page)
    assert cart.get_item_count() == 1
    
    # 💡 स्क्रीन पाहण्यासाठी ३ सेकंद थांबेल
    time.sleep(3)


@pytest.mark.regression
def test_cart_product_name(page):

    login = LoginPage(page)
    login.open()
    login.login(
        "standard_user",
        "secret_sauce"
    )

    home = HomePage(page)
    home.add_product(
        "Sauce Labs Bike Light"
    )
    home.open_cart()

    cart = CartPage(page)
    products = cart.get_product_names()
    assert "Sauce Labs Bike Light" in products
    
    time.sleep(3)


@pytest.mark.regression
def test_multiple_products(page):

    login = LoginPage(page)
    login.open()
    login.login(
        "standard_user",
        "secret_sauce"
    )

    home = HomePage(page)
    home.add_product(
        "Sauce Labs Backpack"
    )
    home.add_product(
        "Sauce Labs Bike Light"
    )
    home.open_cart()

    cart = CartPage(page)
    assert cart.get_item_count() == 2
    
    time.sleep(3)
