import os
from PIL import Image
from selenium.common.exceptions import WebDriverException

from common.context import Context
from common.logger import get_configured_logger
from config import Configurator
from selenium.webdriver.chrome.webdriver import WebDriver
import time


class PageObject:
    logger = get_configured_logger('page_obj')
    config = Configurator()
    IS_PAGE_OPENED_LOCATORS = []
    driver: WebDriver = None

    def is_opened(self):
        locators_found = [self.driver.find_elements(*locator) for locator in self.IS_PAGE_OPENED_LOCATORS]
        return all(locators_found)

    def wait_for_page_opened(self):
        for _ in range(3):
            if self.is_opened():
                break
            else:
                pass

    def assert_page_opened(self):
        try:
            assert self.is_opened()
        except AssertionError:
            self._save_screenshot()
            raise

    def __getattribute__(self, item):
        """
        getattribute has been overridden to automatically detect if the page we want to interact with is open
        """
        class_name = object.__getattribute__(self, '__class__').__name__
        if class_name == Context.current_page_obj:
            pass
        elif item.endswith('_') and callable(object.__getattribute__(self, item)) \
                and class_name != Context.current_page_obj:
            self.wait_for_page_opened()
            self.assert_page_opened()
            Context.current_page_obj = class_name
        else:
            pass
        object.__getattribute__(self, 'logger').info(
            'Executing %s->\'%s\'. Current auto-waited page: \'%s\'', class_name, item, Context.current_page_obj)
        try:
            return object.__getattribute__(self, item)
        except WebDriverException:
            self._save_screenshot()
            raise

    def _find_element(self, by, wait_sec=15):
        poll_end_time = time.time() + wait_sec
        while poll_end_time >= time.time():
            try:
                found_element = self.driver.find_element(*by)
                if found_element.is_displayed() and found_element.is_enabled():
                    return found_element
                else:
                    raise WebDriverException("Element is not interactable")
            except WebDriverException:
                pass
        try:
            found_element = self.driver.find_element(*by)
            if found_element.is_displayed() and found_element.is_enabled():
                return found_element
            else:
                raise WebDriverException("Element is not interactable")
        except WebDriverException as e:
            self._save_screenshot()
            raise e

    def _find_elements(self, by):
        """
        Method returns only displayed and enabled elements, which were found by WebDriver.find_element() method
        """
        found_elements = self.driver.find_elements(*by)
        filtered_elements = [element for element in found_elements if element.is_displayed() and element.is_enabled()]
        if not filtered_elements:
            self._save_screenshot()
            raise ValueError(f'No active/displayed elements found with using {by}')
        return filtered_elements

    def _click(self, by):
        """
        Method finds element and clicks on it 3 times before raising an error
        """
        error = None
        element = self._find_element(by=by)
        for _ in range(3):
            try:
                return element.click()
            except (WebDriverException, AssertionError) as e:
                error = e
                time.sleep(0.2)
            self._save_screenshot()
        if error:
            raise error

    def _save_screenshot(self):
        try:
            test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        except AttributeError:
            test_name = ''  # In case of debug outside of tests there is no PYTEST_CURRENT_TEST env variable
        screenshot_path = os.path.join(self.config.SCREENSHOT_DIR_PATH, f'{test_name}.png')
        self.driver.save_screenshot(screenshot_path)
        # A lot of screenshots may be saved thru whole run, so it is better to decrease their weight
        # Screenshots are still informative, but this block may be updated/deleted in future in case if screen will
        # contain small elements to check
        image = Image.open(screenshot_path)
        resized_screenshot = image.resize((int(image.size[0] / 2), int(image.size[1] / 2)), Image.ANTIALIAS)
        with open(screenshot_path, 'wb') as f:
            resized_screenshot.save(f, format='PNG')

    def _send_keys(self, by, keys):
        try:
            self.driver.find_element(*by).send_keys(keys)
        except WebDriverException:
            self._save_screenshot()
            raise

