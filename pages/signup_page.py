from playwright.sync_api import Page


class SignupPage:

    def __init__(self, page: Page):

        self.page = page

        # Initial Signup
        self.signup_name = page.locator(
            "[data-qa='signup-name']"
        )

        self.signup_email = page.locator(
            "[data-qa='signup-email']"
        )

        self.signup_button = page.locator(
            "[data-qa='signup-button']"
        )

        # Account Information
        self.title_mr = page.get_by_label("Mr.")
        self.title_mrs = page.get_by_label("Mrs.")

        self.password = page.locator(
            "[data-qa='password']"
        )

        self.days = page.locator(
            "[data-qa='days']"
        )

        self.months = page.locator(
            "[data-qa='months']"
        )

        self.years = page.locator(
            "[data-qa='years']"
        )

        # Newsletter / Special Offers
        self.newsletter = page.locator(
            "#newsletter"
        )

        self.special_offers = page.locator(
            "#optin"
        )

        # Address Information
        self.first_name = page.locator(
            "[data-qa='first_name']"
        )

        self.last_name = page.locator(
            "[data-qa='last_name']"
        )

        self.company = page.locator(
            "[data-qa='company']"
        )

        self.address = page.locator(
            "[data-qa='address']"
        )

        self.address2 = page.locator(
            "[data-qa='address2']"
        )

        self.country = page.locator(
            "[data-qa='country']"
        )

        self.state = page.locator(
            "[data-qa='state']"
        )

        self.city = page.locator(
            "[data-qa='city']"
        )

        self.zipcode = page.locator(
            "[data-qa='zipcode']"
        )

        self.mobile_number = page.locator(
            "[data-qa='mobile_number']"
        )

        self.create_account_button = page.locator(
            "[data-qa='create-account']"
        )

        self.account_created_message = page.locator(
            "[data-qa='account-created']"
        )

    # --------------------------------
    # Initial Signup
    # --------------------------------

    def enter_signup_details(
        self,
        name: str,
        email: str
    ):
        self.signup_name.fill(name)
        self.signup_email.fill(email)

    def click_signup(self):
        self.signup_button.click()

    # --------------------------------
    # Account Information
    # --------------------------------

    def select_title(self, title: str):

        if title.lower() == "mr":
            self.title_mr.check()

        elif title.lower() == "mrs":
            self.title_mrs.check()

        else:
            raise ValueError(
                f"Unsupported title: {title}"
            )

    def enter_password(self, password: str):
        self.password.fill(password)

    def select_date_of_birth(
        self,
        day: str,
        month: str,
        year: str
    ):
        self.days.select_option(day)
        self.months.select_option(month)
        self.years.select_option(year)

    def subscribe_newsletter(self):
        self.newsletter.check()

    def accept_special_offers(self):
        self.special_offers.check()

    # --------------------------------
    # Address Information
    # --------------------------------

    def enter_personal_details(
        self,
        first_name: str,
        last_name: str,
        company: str,
        address: str,
        address2: str,
        state: str,
        city: str,
        zipcode: str,
        mobile_number: str
    ):

        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.company.fill(company)
        self.address.fill(address)
        self.address2.fill(address2)
        self.state.fill(state)
        self.city.fill(city)
        self.zipcode.fill(zipcode)
        self.mobile_number.fill(mobile_number)

    def select_country(self, country: str):
        self.country.select_option(label=country)

    # --------------------------------
    # Account Creation
    # --------------------------------

    def click_create_account(self):
        self.create_account_button.click()

    def is_account_created(self):
        return self.account_created_message.is_visible()

    
    