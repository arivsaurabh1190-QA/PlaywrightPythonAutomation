from playwright.sync_api._generated import Page

from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.config import BASE_URL


def test_valid_login(browser_page: Page):

    home_page = HomePage(browser_page)
    login_page = LoginPage(browser_page)

    # Navigate to application
    home_page.navigate(BASE_URL)

    # Verify home page
    assert home_page.is_home_page_visible()

    # Navigate to Login
    home_page.click_signup_login()

    # Verify Login page
    assert login_page.is_login_heading_visible()

    # Login
    login_page.login(
        "ariv.saurabh1190@gmail.com",
        "Starlord@123"
    )

    # Verify successful login
    assert login_page.is_logged_in()