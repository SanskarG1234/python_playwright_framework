import pytest
import time

from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.regression
def test_product_count(page):

    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")   
    page.wait_for_load_state("networkidle")



    home = HomePage(page)
    page.wait_for_load_state("networkidle")
    assert home.product_count() > 0
    

@pytest.mark.regression
def test_search_product(page):

    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    page.wait_for_load_state("networkidle")

    home = HomePage(page)
    product = home.search_product("Sauce Labs Backpack")
    page.wait_for_load_state("networkidle")
    assert product == 1
    
    


@pytest.mark.regression
def test_sort_product(page):

    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    page.wait_for_load_state("networkidle")

    home = HomePage(page)
    home.sort_products("lohi")
    page.wait_for_load_state("networkidle")

    assert page.url.endswith("inventory.html")