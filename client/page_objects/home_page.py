from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from client.page_objects.base_page import BasePage


class HomePage(BasePage):

    LOGIN_BUTTON = (By.XPATH, "//a[contains(text(),'Sign in')]")
    CONTACT_US_BUTTON = (By.XPATH, "//a[@title='Contact Us']")

    SEARCH_BUTTON = (By.XPATH, "//button[@name='submit_search']")
    SEARCH_FIELD = (By.XPATH, "//input[@id='search_query_top']")

    WOMEN_BUTTON = (By.XPATH, "//a[contains(@title,'Women')]")
    DRESSES_BUTTON = (By.XPATH, "(//a[@title='Dresses'][normalize-space()='Dresses'])[2]")
    T_SHIRTS_BUTTON = (By.XPATH, "(//a[@title='T-shirts'][normalize-space()='T-shirts'])[2]")

    CASUAL_DRESSES_BUTTON = (By.LINK_TEXT, "Casual Dresses")
    EVENING_DRESSES_BUTTON = (By.LINK_TEXT, "Evening Dresses")
    SUMMER_DRESSES_BUTTON = (By.LINK_TEXT, "Summer Dresses")

    TOPS_T_SHIRTS = (By.LINK_TEXT, 'T-shirts')
    TOPS_BLOUSES = (By.LINK_TEXT, 'Blouses')

    DRESSES_CASUAL_DRESSES = (By.LINK_TEXT, 'Casual Dresses')
    DRESSES_EVENING_DRESSES = (By.LINK_TEXT, 'Evening Dresses')
    DRESSES_SUMMER_DRESSES = (By.LINK_TEXT, 'Summer Dresses')

    CATEGORIES_WOMEN_BUTTON = (By.XPATH, "//a[contains(@title,'Women')]")

    INFORMATION_SPECIALS_BUTTON = (By.XPATH, "// a[contains( @ title, 'Specials')]")
    INFORMATION_NEW_PRODUCTS_BUTTON = (By.XPATH, "//a[@title='New products']")
    INFORMATION_BEST_SELLERS_BUTTON = (By.XPATH, "//a[@title='Best sellers']")
    INFORMATION_OUR_STORES_BUTTON = (By.XPATH, "//a[@title='Our stores']")
    INFORMATION_CONTACT_US_BUTTON = (By.XPATH, "//a[contains(@title,'Contact us')]")
    INFORMATION_TERMS_AND_CONDITIONS_OF_USE_BUTTON = (By.XPATH, "//a[@title='Terms and conditions of use']")
    INFORMATION_ABOUT_US_BUTTON = (By.XPATH, "//a[@title='About us']")
    INFORMATION_SITEMAP_BUTTON = (By.XPATH, "//a[@title='Sitemap']")

    MY_ACCOUNT_BUTTON = (By.XPATH, "//a[@title='Manage my customer account']")
    MY_ACCOUNT_MY_ORDERS_BUTTON = (By.XPATH, "//a[@title='My orders']")
    MY_ACCOUNT_MY_CREDIT_SLIPS_BUTTON = (By.XPATH, "//a[@title='My credit slips']")
    MY_ACCOUNT_MY_ADDRESSES_BUTTON = (By.XPATH, "//a[@title='My addresses']")
    MY_ACCOUNT_MY_PERSONAL_INFO_BUTTON = (By.XPATH, "//a[@title='Manage my personal information']")
    MY_ACCOUNT_MY_PERSONAL_SIGN_OUT = (By.XPATH, "//a[@title='Manage my personal information']")

    IS_PAGE_OPENED_LOCATORS = [LOGIN_BUTTON]

    def open_home_page(self):
        self.driver.get(self.config.WEB_APP_URL)
        self.driver.set_window_size(1920, 1080)

    def click_on_login(self):
        self._find_element(self.LOGIN_BUTTON).click()

    def hover_over_women_button(self):
        woman = self._find_element(self.WOMEN_BUTTON)
        ActionChains(self.driver).move_to_element(woman).perform()

    def hover_over_dresses_button(self):
        dresses = self._find_element(self.DRESSES_BUTTON)
        ActionChains(self.driver).move_to_element(dresses).perform()

    def get_value_button_woman(self):
        return self._find_element(self.WOMEN_BUTTON).get_attribute('value')

    def get_value_button_woman_tops_t_shirts(self):
        return self._find_element(self.TOPS_T_SHIRTS).get_attribute('value')

    def get_value_button_woman_tops_blouses(self):
        return self._find_element(self.TOPS_BLOUSES).get_attribute('value')

    def get_value_button_woman_dresses_casual_dresses(self):
        return self._find_element(self.DRESSES_CASUAL_DRESSES).get_attribute('value')

    def get_value_button_woman_dresses_evening_dresses(self):
        return self._find_element(self.DRESSES_EVENING_DRESSES).get_attribute('value')

    def get_value_button_woman_dresses_summer_dresses(self):
        return self._find_element(self.DRESSES_SUMMER_DRESSES).get_attribute('value')

    def get_value_button_dresses(self):
        return self._find_element(self.DRESSES_BUTTON).get_attribute('value')

    def get_value_button_dresses_casual_dresses(self):
        return self._find_element(self.DRESSES_BUTTON).get_attribute('value')

    def get_value_button_dresses_evening_dresses(self):
        return self._find_element(self.DRESSES_BUTTON).get_attribute('value')

    def get_value_button_dresses_summer_dresses(self):
        return self._find_element(self.DRESSES_BUTTON).get_attribute('value')

    def get_value_button_t_shirts(self):
        return self._find_element(self.T_SHIRTS_BUTTON).get_attribute('value')

    def get_value_categories_women(self):
        return self._find_element(self.CATEGORIES_WOMEN_BUTTON).get_attribute('value')

    def get_value_information_button_specials(self):
        return self._find_element(self.INFORMATION_SPECIALS_BUTTON).get_attribute('value')

    def get_value_information_button_new_products(self):
        return self._find_element(self.INFORMATION_NEW_PRODUCTS_BUTTON).get_attribute('value')

    def get_value_information_button_best_sellers(self):
        return self._find_element(self.INFORMATION_BEST_SELLERS_BUTTON).get_attribute('value')

    def get_value_information_button_our_stores(self):
        return self._find_element(self.INFORMATION_OUR_STORES_BUTTON).get_attribute('value')

    def get_value_information_button_contact_us(self):
        return self._find_element(self.INFORMATION_CONTACT_US_BUTTON).get_attribute('value')

    def get_value_information_button_terms_and_conditions(self):
        return self._find_element(self.INFORMATION_TERMS_AND_CONDITIONS_OF_USE_BUTTON).get_attribute('value')

    def get_value_information_button_about_us(self):
        return self._find_element(self.INFORMATION_ABOUT_US_BUTTON).get_attribute('value')

    def get_value_information_button_site_map(self):
        return self._find_element(self.INFORMATION_SITEMAP_BUTTON).get_attribute('value')

    def get_value_button_my_account(self):
        return self._find_element(self.MY_ACCOUNT_BUTTON).get_attribute('value')

    def get_value_my_account_button_my_orders(self):
        return self._find_element(self.MY_ACCOUNT_MY_ORDERS_BUTTON).get_attribute('value')

    def get_value_my_account_button_my_credit_slips(self):
        return self._find_element(self.MY_ACCOUNT_MY_CREDIT_SLIPS_BUTTON).get_attribute('value')

    def get_value_my_account_button_my_addresses(self):
        return self._find_element(self.MY_ACCOUNT_MY_ADDRESSES_BUTTON).get_attribute('value')

    def get_value_my_account_button_my_personal_info(self):
        return self._find_element(self.MY_ACCOUNT_MY_PERSONAL_INFO_BUTTON).get_attribute('value')

    def get_value_my_account_button_sign_out(self):
        return self._find_element(self.MY_ACCOUNT_MY_PERSONAL_SIGN_OUT).get_attribute('value')