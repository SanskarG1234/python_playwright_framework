import pytest
import time  

from pages.login_page import LoginPage
from utils.test_data_reader import read_json

login_data = read_json("test_data/login.json")


@pytest.mark.smoke
def test_valid_login(page):

    login_page = LoginPage(page)
    login_page.open()

    user = login_data["valid_user"]
    login_page.login(user["username"], user["password"])

    assert "inventory.html" in page.url
    
    # 💡 स्क्रीन पाहण्यासाठी ३ सेकंद थांबेल
    time.sleep(3)


@pytest.mark.regression
def test_invalid_login(page):

    login_page = LoginPage(page)
    login_page.open()

    user = login_data["invalid_user"]
    login_page.login(user["username"], user["password"])

    error = login_page.get_error_message()
    assert "Username and password do not match" in error
    
    time.sleep(3)


@pytest.mark.smoke
@pytest.mark.parametrize(
    "username,password",
    [
        ("standard_user", "secret_sauce"),
        ("standard_user", "secret_sauce")
    ]
)
def test_login_parameterization(page, username, password):

    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username, password)

    assert "inventory.html" in page.url
    
    time.sleep(3)
