from playwright.sync_api import Page
from utils.logger import get_logger

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger(__name__)

        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.locator("[data-test='error']")

    def open(self):
        self.logger.info("Opening login page")
        self.page.goto("https://saucedemo.com")

    def login(self, username, password):
        self.logger.info(f"Logging in with user: {username}")
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def get_error_message(self):
        return self.error_message.inner_text()
