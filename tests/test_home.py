from pages.home_page import HomePage
from utils.config import BASE_URL


def test_home_page(browser_page):

    home_page = HomePage(browser_page)

    home_page.navigate(BASE_URL)

    assert home_page.is_home_page_visible()