import time

import common.utility
from client.web_client import WebClient
from config import Configurator
#from common.utility import Generator


class TestSignInForm:
    config = Configurator()
    client = WebClient()
    mail = common.utility.email_generator()
    phone = common.utility.phone_number_generator()


    @classmethod
    def setup_class(cls):
        """
        Works only before all tests started
        """
        cls.client.home_page.open_home_page()

    def test_check_messages(self):
        self.client.home_page.click_on_login()


        #self.client.home_page.click_on_casual_dress()

    def test_login_created(self):
        self.client.login_page.fill_create_email_field(self.mail)
        self.client.login_page.click_create_an_account()
        self.client.create_page.click_gender_male_mr()
        self.client.create_page.click_gender_male_mrs()
        self.client.create_page.fill_customer_first_name()
        self.client.create_page.fill_customer_last_name()
        #self.client.create_page.fill_email(self.mail)
        self.client.create_page.fill_password()
        self.client.create_page.select_date_of_birth_day()
        self.client.create_page.fill_date_of_birth_day()
        self.client.create_page.select_date_of_birth_month()
        self.client.create_page.fill_date_of_birth_month()
        self.client.create_page.select_date_of_birth_year()
        self.client.create_page.fill_date_of_birth_year()
        self.client.create_page.fill_address_first_name()
        self.client.create_page.fill_address_last_name()
        self.client.create_page.fill_company()
        self.client.create_page.fill_address()
        self.client.create_page.fill_address_second_line()
        self.client.create_page.fill_city()
        #self.client.hover_over_women_button()
        self.client.create_page.select_state()
        self.client.create_page.fill_state()
        self.client.create_page.fill_postal_code()
        self.client.create_page.select_country()
        self.client.create_page.fill_country()
        self.client.create_page.fill_additional_info()
        self.client.create_page.fill_home_phone(self.phone)
        self.client.create_page.fill_mobile_phone(self.phone)
        self.client.create_page.fill_assign_address()
        self.client.create_page.click_register_button()

        time.sleep(5)


    # def register_user(self):
    #     self.client.create_page.

    @classmethod
    def teardown_class(cls):
        """
        After all tests
        """
        cls.client.quit()
