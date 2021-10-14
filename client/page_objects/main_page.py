from selenium.webdriver.common.by import By

from client.page_objects.base_page import BasePage


class MainPage(BasePage):

    ALERT = (By.XPATH, "//button[contains(text(),'Понятно')]")
    MESSAGES = (By.XPATH, "//a[@class='tdnone inlblk']//span[contains(text(),'Сообщения')]")
    MY_PROFILE = (By.XPATH, "//strong[contains(text(),'Мой профиль')]")
    LOGOUT = (By.XPATH, "//span[contains(text(),'Выйти')]")

    IS_PAGE_OPENED_LOCATORS = []

    def click_to_messages(self):
        self._find_element(self.MESSAGES).click()

    def hover_over_my_profile(self):
        profile = self._find_element(self.MY_PROFILE)
        self.action.move_to_element(profile)

    def click_logout(self):
        self._find_element(self.LOGOUT).click()