
from selenium.webdriver.common.by import By
from client.page_objects.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

class CreateAccountPage(BasePage):

    GENDER_MALE_MR = (By.XPATH, "//label[@for='id_gender1']")
    GENDER_MALE_MRS = (By.XPATH, "//label[@for='id_gender2']")
    CUSTOMER_FIRST_NAME = (By.XPATH, "//input[@id='customer_firstname']")
    CUSTOMER_LAST_NAME = (By.XPATH, "//input[@id='customer_lastname']")
    EMAIL = (By.XPATH, "//input[@id='email']")
    PASSWORD = (By.XPATH, "//input[@id='passwd']")
    DATE_OF_BIRTH_DAY = (By.XPATH, "//div[@id='uniform-days']")
    DATE_OF_BIRTH_DAY_DAY = (By.XPATH, "//select[@id='days']//option[@value='3']")

    DATE_OF_BIRTH_MONTH = (By.XPATH, "//div[@id='uniform-months']")
    DATE_OF_BIRTH_MONTH_MONTH = (By.XPATH, "//select[@id='months']//option[@value='1']")

    DATE_OF_BIRTH_DAY_YEAR = (By.XPATH, "//div[@id='uniform-years']")
    DATE_OF_BIRTH_DAY_YEAR_YEAR = (By.XPATH, "//select[@id='years']//option[@value='2000']")

    FIRST_NAME = (By.XPATH, "//input[@id='firstname']")
    LAST_NAME = (By.XPATH, "//input[@id='lastname']")
    COMPANY = (By.XPATH, "//input[@id='company']")
    ADDRESS = (By.XPATH, "//input[@id='address1']")
    ADDRESS_SECOND_LINE = (By.XPATH, "//input[@id='address2']")
    CITY = (By.XPATH, "//input[@id='city']")

    STATE = (By.XPATH, "//div[@id='uniform-id_state']")
    STATE_NAME = (By.XPATH, "//div[@id='uniform-id_state']//option[contains(text(),'Alabama')]")
    #STATE_NAME = (By.XPATH, "//body/div[@id='page']/div[2]/div[1]/div[3]/div[1]/form[1]/div[1]/div[6]/div[1]/div[1]/div[1]/select[1]/option[5]")


    POSTAL_CODE = (By.XPATH, "//input[@id='postcode']")
    COUNTRY = (By.XPATH, "//div[@id='uniform-id_country']")
    COUNTRY_NAME = (By.XPATH, "//div[@id='uniform-id_country']//option[contains(text(),'United States')]")
    ADDITIONAL_INFO = (By.XPATH, "//textarea[@id='other']")
    HOME_PHONE = (By.XPATH, "//input[@id='phone']")
    MOBILE_PHONE = (By.XPATH, "//input[@id='phone_mobile']")
    ASSIGN_ADDRESS = (By.XPATH, "//input[@id='alias']")
    REGISTER_BUTTON = (By.XPATH, "//span[normalize-space()='Register']")


    def click_gender_male_mrs(self):
        self._find_element(self.GENDER_MALE_MRS).click()

    def click_gender_male_mr(self):
        self._find_element(self.GENDER_MALE_MR).click()

    def fill_customer_first_name(self):
        self._find_element(self.CUSTOMER_FIRST_NAME).click()
        self._find_element(self.CUSTOMER_FIRST_NAME).send_keys('customer')

    def fill_customer_last_name(self):
        self._find_element(self.CUSTOMER_LAST_NAME).click()
        self._find_element(self.CUSTOMER_LAST_NAME).send_keys('customers')

    def fill_email(self):
        self._find_element(self.EMAIL).click()
        self._find_element(self.EMAIL).send_keys()

    def fill_password(self):
        self._find_element(self.PASSWORD).click()
        self._find_element(self.PASSWORD).send_keys('password')

    def select_date_of_birth_day(self):
        self._find_element(self.DATE_OF_BIRTH_DAY).click()

    def fill_date_of_birth_day(self):
        self._find_element(self.DATE_OF_BIRTH_DAY_DAY).click()

    def select_date_of_birth_month(self):
        self._find_element(self.DATE_OF_BIRTH_MONTH).click()

    def fill_date_of_birth_month(self):
        self._find_element(self.DATE_OF_BIRTH_MONTH_MONTH).click()

    def select_date_of_birth_year(self):
        self._find_element(self.DATE_OF_BIRTH_DAY_YEAR).click()

    def fill_date_of_birth_year(self):
        self._find_element(self.DATE_OF_BIRTH_DAY_YEAR_YEAR).click()

    def fill_address_first_name(self):
        self._find_element(self.FIRST_NAME).click()
        self._find_element(self.FIRST_NAME).send_keys('First')

    def fill_address_last_name(self):
        self._find_element(self.LAST_NAME).click()
        self._find_element(self.LAST_NAME).send_keys('Last')

    def fill_company(self):
        self._find_element(self.COMPANY).click()
        self._find_element(self.COMPANY).send_keys('fill_company')

    def fill_address(self):
        self._find_element(self.ADDRESS).click()
        self._find_element(self.ADDRESS).send_keys('Address1')

    def fill_address_second_line(self):
        self._find_element(self.ADDRESS_SECOND_LINE).click()
        self._find_element(self.ADDRESS_SECOND_LINE).send_keys('Address2')

    def fill_city(self):
        self._find_element(self.CITY).click()
        self._find_element(self.CITY).send_keys('City')

    def select_state(self):
        self._find_element(self.STATE).click()

    def fill_state(self):
        self._find_element(self.STATE_NAME).click()

    def fill_postal_code(self):
        self._find_element(self.POSTAL_CODE).click()
        self._find_element(self.POSTAL_CODE).send_keys('87500')

    def select_country(self):
        self._find_element(self.COUNTRY).click()

    def fill_country(self):
        self._find_element(self.COUNTRY_NAME).click()

    def fill_additional_info(self):
        self._find_element(self.ADDITIONAL_INFO).click()
        self._find_element(self.ADDITIONAL_INFO).send_keys('fill_additional_info')

    def fill_home_phone(self, home_phone):
        self._find_element(self.HOME_PHONE).click()
        self._find_element(self.HOME_PHONE).send_keys(home_phone)

    def fill_mobile_phone(self, mobile_phone):
        self._find_element(self.MOBILE_PHONE).click()
        self._find_element(self.MOBILE_PHONE).send_keys(mobile_phone)

    def fill_assign_address(self):
        self._find_element(self.ASSIGN_ADDRESS).click()
        self._find_element(self.ASSIGN_ADDRESS).send_keys('fill_assign_address')

    def click_register_button(self):
        self._find_element(self.REGISTER_BUTTON).click()
