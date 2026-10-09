from playwright.sync_api import Page


class AccountPage:

    def __init__(self, page: Page):

        self.page = page

        # Account Created Page
        self.account_created_message = page.locator(
            "[data-qa='account-created']"
        )

        self.continue_button = page.locator(
            "[data-qa='continue-button']"
        )

        # Logged-in User
        self.logged_in_user = page.get_by_text(
            "Logged in as",
            exact=False
        )

        # Delete Account
        self.delete_account = page.get_by_text(
            "Delete Account",
            exact=True
        )

        # Account Deleted Page
        self.account_deleted_message = page.locator(
            "[data-qa='account-deleted']"
        )

    def is_account_created(self):
        return self.account_created_message.is_visible()

    def click_continue(self):
        self.continue_button.click()

    def is_logged_in(self):
        return self.logged_in_user.is_visible()

    def delete_user_account(self):
        self.delete_account.click()

    def is_account_deleted(self):
        return self.account_deleted_message.is_visible()