from selenium.webdriver import ActionChains

from common.page_object import PageObject
from client.page_objects.driver import Driver


class BasePage(PageObject):

    driver = Driver.get_instance()

    action_chain = ActionChains(driver)