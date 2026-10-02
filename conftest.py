import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page

load_dotenv()


@pytest.fixture
def logged_in_page(page: Page):

    page.goto("https://saucedemo.com")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    page.wait_for_url("**/inventory.html")

    return page
