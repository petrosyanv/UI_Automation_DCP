from client.web_client import WebClient
from config import Configurator


class TestSample:
    config = Configurator()
    client = WebClient()

    @classmethod
    def setup_class(cls):
        """
        Works only before all tests started
        """
        cls.client.home_page.open_login_page()
        cls.client.home_page.accept_all_cookie()
        cls.client.home_page.click_my_profile()

    def setup_method(self):
        """
        Before every single test
        """
        self.client.login_page.fill_login_field(username=self.config.MAIN_USER)
        self.client.login_page.fill_password_field(password=self.config.MAIN_USER_PASS)
        self.client.login_page.click_login_button()

    def test_check_messages(self):
        self.client.main_page.click_to_messages()

    def teardown_method(self):
        """
        After every single test
        """
        self.client.main_page.hover_over_my_profile()
        self.client.main_page.click_logout()

    @classmethod
    def teardown_class(cls):
        """
        After all tests
        """
        cls.client.quit()
