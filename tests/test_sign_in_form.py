import time


from client.web_client import WebClient
from config import Configurator
from common.utility import phone_number_generator, email_generator


class TestSignInForm:
    config = Configurator()
    client = WebClient()

    @classmethod
    def setup_class(cls):
        """
        Works only before all tests started
        """
        cls.client.home_page.open_home_page()

    def test_check_messages(self):
        self.client.home_page.click_on_login()

    def test_login_created(self):
        self.client.login_page.fill_create_email_field(email_generator())
        self.client.login_page.click_create_an_account()
        self.client.create_page.click_gender_male_mr()
        self.client.create_page.click_gender_male_mrs()
        self.client.create_page.fill_customer_first_name(customer_first_name='Firstame')
        self.client.create_page.fill_customer_last_name('LastName')
        self.client.create_page.fill_password('password')
        self.client.create_page.select_date_of_birth_day()
        self.client.create_page.fill_date_of_birth_day()
        self.client.create_page.select_date_of_birth_month()
        self.client.create_page.fill_date_of_birth_month()
        self.client.create_page.select_date_of_birth_year()
        self.client.create_page.fill_date_of_birth_year()
        self.client.create_page.fill_address_first_name('AddressFirstName')
        self.client.create_page.fill_address_last_name('AddressLastName')
        self.client.create_page.fill_company('company')
        self.client.create_page.fill_address('address')
        self.client.create_page.fill_address_second_line('AddressSecondLine')
        self.client.create_page.fill_city('city')
        self.client.create_page.select_state()
        self.client.create_page.fill_state()
        self.client.create_page.fill_postal_code('87500')
        self.client.create_page.select_country()
        self.client.create_page.fill_country()
        self.client.create_page.fill_additional_info()
        self.client.create_page.fill_home_phone(phone_number_generator())
        self.client.create_page.fill_mobile_phone(phone_number_generator())
        self.client.create_page.fill_assign_address('AssignAddress')
        self.client.create_page.click_register_button()

        time.sleep(5)
        #time.sleep(5)
        #TODO test comment

    @classmethod
    def teardown_class(cls):
        """
        After all tests
        """
        cls.client.quit()
