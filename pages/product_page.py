from playwright.sync_api import Page

class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.product_items = page.locator(".inventory_item")

    def get_product_count(self):
        return self.product_items.count()

    def add_product(self, product_name):
        product = self.product_items.filter(has_text=product_name)
        product.get_by_role("button", name="Add to cart").click()

    def get_product_names(self):
        names = []
        count = self.product_items.count()
        for index in range(count):
            name = self.product_items.nth(index).locator(".inventory_item_name").inner_text()
            names.append(name)
        return names
