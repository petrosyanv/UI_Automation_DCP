from selenium.webdriver.common.by import By

from client.page_objects.base_page import BasePage


class HomePage(BasePage):

    MY_PROFILE = (By.XPATH, "//strong[contains(text(),'Мой профиль')]")
    MAKE_ADVERTISMENT = (By.XPATH, "//span[contains(text(),'Подать объявление')]")
    COOKIE = (By.XPATH, "//button[contains(text(),'Принять и Закрыть')]")

    IS_PAGE_OPENED_LOCATORS = [MY_PROFILE, MAKE_ADVERTISMENT]

    def open_login_page(self):
        self.driver.get(self.config.WEB_APP_URL)
        self.driver.set_window_size(1920, 1080)

    def click_my_profile(self):
        self._find_element(self.MY_PROFILE).click()

    def click_on_advertisment(self):
        self._find_element(self.MAKE_ADVERTISMENT).click()

    def accept_all_cookie(self):
        self._find_element(self.COOKIE).click()