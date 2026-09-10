from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):

        self.page = page

        self.login_heading = page.get_by_text(
            "Login to your account"
        )

        self.name_input = page.locator(
            "[data-qa='signup-name']"
        )

        self.email_input = page.locator(
            "[data-qa='login-email']"
        )

        self.password_input = page.locator(
            "[data-qa='login-password']"
        )

        self.login_button = page.locator(
            "[data-qa='login-button']"
        )

        self.login_error = page.get_by_text(
            "Your email or password is incorrect!"
        )

        self.logged_in_user = page.locator(
            "li:has-text('Logged in as')"
        )

        self.delete_account = page.get_by_text(
            "Delete Account"
        )

    def enter_email(self, email: str):
        self.email_input.fill(email)

    def enter_password(self, password: str):
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()

    def login(self, email: str, password: str):

        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def is_login_heading_visible(self):
        return self.login_heading.is_visible()

    def is_login_error_visible(self):
        return self.login_error.is_visible()

    def is_logged_in(self):
        return self.logged_in_user.is_visible()

    def click_delete_account(self):
        self.delete_account.click()