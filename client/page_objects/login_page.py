import time

from selenium.webdriver.common.by import By

from client.page_objects.base_page import BasePage


class LoginPage(BasePage):

    EMAIL_FIELD = (By.XPATH, "//input[@id='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='passwd']")
    SIGN_IN_BUTTON = (By.XPATH, "//button[@id='SubmitLogin']")
    FORGOT_YOUR_PASSWORD_BUTTON = (By.XPATH, "//a[contains(text(),'Forgot your password?')]")
    EMAIL_CREATE_FIELD = (By.XPATH, "//input[@id='email_create']")
    CREATE_BUTTON = (By.XPATH, "//button[@id='SubmitCreate']")

    IS_PAGE_OPENED_LOCATORS = []

    def fill_login_field(self, username):
        self._find_element(self.LOGIN).click()
        self._find_element(self.LOGIN).send_keys(username)

    def fill_password_field(self, password):
        self._find_element(self.PASSWORD).click()
        self._find_element(self.PASSWORD).send_keys(password)

    def click_login_button(self):
        self._find_element(self.LOGIN_BUTTON).click()

    def fill_create_email_field(self, email):
        self._find_element(self.EMAIL_CREATE_FIELD).click()
        self._find_element(self.EMAIL_CREATE_FIELD).send_keys(email)

    def click_create_an_account(self):  ##############
        self._find_element(self.CREATE_BUTTON).click()
