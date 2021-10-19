from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from client.page_objects.base_page import BasePage


class HomePage(BasePage):

    LOGIN_BUTTON = (By.XPATH, "//a[contains(text(),'Sign in')]")
    CONTACT_US_BUTTON = (By.XPATH, "//a[@title='Contact Us']")
    WOMEN_BUTTON = (By.XPATH, "//a[@title='Women']")
    DRESSES_BUTTON = (By.XPATH, "(//a[@title='Dresses'][normalize-space()='Dresses'])[2]")
    T_SHORTS_BUTTON = (By.XPATH, "(//a[@title='T-shirts'][normalize-space()='T-shirts'])[2]")
    SEARCH_BUTTON = (By.XPATH, "//button[@name='submit_search']")
    SEARCH_FIELD = (By.XPATH, "//input[@id='search_query_top']")
    CASUAL_DRESSES_BUTTON = (By.LINK_TEXT, "Casual Dresses")

    IS_PAGE_OPENED_LOCATORS = [LOGIN_BUTTON]

    def open_home_page(self):
        self.driver.get(self.config.WEB_APP_URL)
        self.driver.set_window_size(1920, 1080)

    def click_on_login(self):
        self._find_element(self.MY_PROFILE).click()

    def hover_over_women_button(self):
        woman = self._find_element(self.WOMEN_BUTTON)
        ActionChains(self.driver).move_to_element(woman).perform()

    def click_on_casual_dress(self):
        self._find_element(self.CASUAL_DRESSES_BUTTON).click()