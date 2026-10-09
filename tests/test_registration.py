from copy import deepcopy

from pages.home_page import HomePage
from pages.signup_page import SignupPage
from pages.account_page import AccountPage
from utils.config import BASE_URL, load_test_data
from utils.test_data_generator import generate_unique_email


def test_register_user(browser_page):

    # Load registration test data
    test_data = deepcopy(
        load_test_data()["registration_user"]
    )

    # Generate unique email for this execution
    test_data["email"] = generate_unique_email()

    # Initialize Page Objects
    home_page = HomePage(browser_page)
    signup_page = SignupPage(browser_page)
    account_page = AccountPage(browser_page)

    # Navigate to application
    home_page.navigate(BASE_URL)
    assert home_page.is_home_page_visible()

    # Navigate to Signup / Login
    home_page.click_signup_login()

    # Initial Signup Details
    signup_page.enter_signup_details(
        test_data["name"],
        test_data["email"]
    )

    signup_page.click_signup()

    # Account Information
    signup_page.select_title(test_data["title"])
    signup_page.enter_password(test_data["password"])

    signup_page.select_date_of_birth(
        test_data["date_of_birth"]["day"],
        test_data["date_of_birth"]["month"],
        test_data["date_of_birth"]["year"]
    )

    if test_data["newsletter"]:
        signup_page.subscribe_newsletter()

    if test_data["special_offers"]:
        signup_page.accept_special_offers()

    # Address Information
    address = test_data["address"]

    signup_page.enter_personal_details(
        address["first_name"],
        address["last_name"],
        address["company"],
        address["address"],
        address["address2"],
        address["state"],
        address["city"],
        address["zipcode"],
        address["mobile_number"]
    )

    signup_page.select_country(address["country"])

    # Create Account
    signup_page.click_create_account()

    # Verify Account Creation
    assert signup_page.is_account_created(), (
        "Account creation confirmation was not displayed."
    )

    # Continue to logged-in state
    account_page.click_continue()

    # Verify logged-in user
    assert account_page.is_logged_in(), (
        "User is not logged in after account creation."
    )

    # Delete test account
    account_page.delete_user_account()

    # Verify account deletion
    assert account_page.is_account_deleted(), (
        "Account deletion confirmation was not displayed."
    )