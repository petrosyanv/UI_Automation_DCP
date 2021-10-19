from selenium.webdriver.common.by import By

from client.page_objects.base_page import BasePage


class CreateAccountPage(BasePage):

    GENDER_MALE = (By.XPATH, "")
    CUSTOMER_FIRST_NAME = (By.XPATH, "")
    CUSTOMER_LAST_NAME = (By.XPATH, "")
    EMAIL = (By.XPATH, "")
    PASSWORD = (By.XPATH, "")
    DATE_OF_BIRTH_DAY = (By.XPATH, "")
    DATE_OF_BIRTH_MONTH = (By.XPATH, "")
    DATE_OF_BIRTH_DAY_YEAR = (By.XPATH, "")
    FIRST_NAME = (By.XPATH, "")
    LAST_NAME = (By.XPATH, "")
    COMPANY = (By.XPATH, "")
    ADDRESS = (By.XPATH, "")
    ADDRESS_SECOND_LINE = (By.XPATH, "")
    CITY = (By.XPATH, "")
    STATE = (By.XPATH, "")
    POSTAL_CODE = (By.XPATH, "")
    COUNTRY = (By.XPATH, "")
    ADDITIONAL_INFO = (By.XPATH, "")
    HOME_PHONE = (By.XPATH, "")
    MOBILE_PHONE = (By.XPATH, "")
    ASSIGN_ADDRESS = (By.XPATH, "")
    REGISTER_BUTTON = (By.XPATH, "")