from playwright.sync_api import Page


class HomePage:

    def __init__(self, page: Page):
        self.page = page

        # Navigation
        self.signup_login_link = page.get_by_role(
            "link",
            name="Signup / Login"
        )

        self.products_link = page.get_by_role(
            "link",
            name="Products"
        )

        self.cart_link = page.get_by_role(
            "link",
            name="Cart"
        )

        self.home_link = page.get_by_role(
            "link",
            name="Home"
        )

    def navigate(self, base_url: str):
        self.page.goto(base_url)

    def click_signup_login(self):
        self.signup_login_link.click()

    def click_products(self):
        self.products_link.click()

    def click_cart(self):
        self.cart_link.click()

    def is_home_page_visible(self):
        return self.home_link.is_visible()