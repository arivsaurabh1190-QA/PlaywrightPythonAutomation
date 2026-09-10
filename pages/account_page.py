from playwright.sync_api import Page


class AccountPage:

    def __init__(self, page: Page):

        self.page = page

        self.logged_in_user = page.locator(
            "li:has-text('Logged in as')"
        )

        self.delete_account = page.get_by_text(
            "Delete Account"
        )

        self.account_deleted_message = page.locator(
            "[data-qa='account-deleted']"
        )

    def is_logged_in(self):
        return self.logged_in_user.is_visible()

    def delete_user_account(self):
        self.delete_account.click()

    def is_account_deleted(self):
        return self.account_deleted_message.is_visible()