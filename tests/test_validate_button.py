import time

from client.web_client import WebClient
from config import Configurator


class TestValidateButton:
    config = Configurator()
    client = WebClient()

    @classmethod
    def setup_class(cls):
        """
        Works only before all tests started
        """
        cls.client.home_page.open_home_page()

    def test_valid_button(self):
        assert 'Women' == self.client.home_page.get_value_button_woman()

        assert 'Dresses' == self.client.home_page.get_value_button_dresses()

        assert 'T-shirts' == self.client.home_page.get_value_button_t_shirts()

        self.client.home_page.hover_over_women_button()
        assert self.client.home_page.get_value_button_woman_tops_t_shirts() == 'T-shirts'
        assert self.client.home_page.get_value_button_woman_tops_blouses() == 'Blouses'

        assert self.client.home_page.get_value_button_woman_dresses_casual_dresses() == 'Casual Dresses'
        assert self.client.home_page.get_value_button_woman_dresses_evening_dresses() == 'Evening Dresses'
        assert self.client.home_page.get_value_button_woman_dresses_summer_dresses() == 'Summer Dresses'

        self.client.home_page.hover_over_dresses_button()
        assert self.client.home_page.get_value_button_dresses_casual_dresses() == 'Casual Dresses'

        self.client.home_page.hover_over_women_button()
        self.client.home_page.hover_over_dresses_button()
        assert self.client.home_page.get_value_button_dresses_evening_dresses() == 'Evening Dresses'

        self.client.home_page.hover_over_women_button()
        self.client.home_page.hover_over_dresses_button()
        assert self.client.home_page.get_value_button_dresses_summer_dresses() == 'Summer Dresses'

        assert 'Women' == self.client.home_page.get_value_categories_women()
        assert 'Specials' == self.client.home_page.get_value_information_button_specials()
        assert 'New products' == self.client.home_page.get_value_information_button_new_products()
        assert 'Best sellers' == self.client.home_page.get_value_information_button_best_sellers()
        assert 'Our stores' == self.client.home_page.get_value_information_button_our_stores()
        assert 'Contact us' == self.client.home_page.get_value_information_button_contact_us()
        assert 'Terms and conditions of use' == self.client.home_page.get_value_information_button_terms_and_conditions()
        assert 'About us' == self.client.home_page.get_value_information_button_about_us()
        assert 'Sitemap' == self.client.home_page.get_value_information_button_site_map()
        assert 'My orders' == self.client.home_page.get_value_my_account_button_my_orders()
        assert 'My credit slips' == self.client.home_page.get_value_my_account_button_my_credit_slips()
        assert 'My addresses' == self.client.home_page.get_value_my_account_button_my_addresses()
        assert 'Manage my personal information' == self.client.home_page.get_value_my_account_button_my_personal_info()

        #assert 'Sign out' == self.client.home_page.get_value_my_account_button_sign_out()


    @classmethod
    def teardown_class(cls):
        """
        After all tests
        """
        cls.client.quit()