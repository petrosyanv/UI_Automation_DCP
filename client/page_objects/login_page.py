import time

from selenium.webdriver.common.by import By

from client.page_objects.base_page import BasePage


class LoginPage(BasePage):

    LOGIN = (By.CSS_SELECTOR, "section[class='login-page has-animation'] input[id='userEmail']")
    PASSWORD = (By.XPATH, "(//input[@id='userPass'])[1]")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "section[class='login-page has-animation'] input[id='userEmail']")

    IS_PAGE_OPENED_LOCATORS = [LOGIN, PASSWORD, LOGIN_BUTTON]

    def fill_login_field(self, username):
        self._find_element(self.LOGIN).click()
        self._find_element(self.LOGIN).send_keys(username)

    def fill_password_field(self, password):
        self._find_element(self.PASSWORD).click()
        self._find_element(self.PASSWORD).send_keys(password)

    def click_login_button(self):
        time.sleep(10)
        self._find_element(self.LOGIN_BUTTON).click()