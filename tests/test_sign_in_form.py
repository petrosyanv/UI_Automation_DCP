from client.web_client import WebClient
from config import Configurator


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
        self.client.home_page.click_on_casual_dress()

    @classmethod
    def teardown_class(cls):
        """
        After all tests
        """
        cls.client.quit()
