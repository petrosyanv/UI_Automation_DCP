from client.page_objects.home_page import HomePage
from client.page_objects.login_page import LoginPage
from client.page_objects.main_page import MainPage


class WebClient:

    def __init__(self):
        self.home_page = HomePage()
        self.login_page = LoginPage()
        self.main_page = MainPage()

    def quit(self):
        self.home_page.driver.quit()