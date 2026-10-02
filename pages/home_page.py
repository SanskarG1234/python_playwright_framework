from playwright.sync_api import Page
from utils.logger import get_logger

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger(__name__)

        self.products = page.locator(".inventory_item")
        self.cart_icon = page.locator(".shopping_cart_link")
        self.menu_button = page.get_by_role("button", name="Open Menu")
        self.logout_link = page.get_by_role("link", name="Logout")
        self.sort_dropdown = page.locator(".product_sort_container")

    def product_count(self):
        return self.products.count()

    def search_product(self, product_name):
        return self.products.filter(has_text=product_name).count() 

    def add_product(self, product_name):
        self.logger.info(f"Adding product: {product_name}")
        product = self.products.filter(has_text=product_name)
        product.get_by_role("button", name="Add to cart").click()

    def open_cart(self):
        self.cart_icon.click()

    def sort_products(self, option):
        self.sort_dropdown.select_option(option)

    def logout(self):
        self.menu_button.click()
        self.logout_link.click()
