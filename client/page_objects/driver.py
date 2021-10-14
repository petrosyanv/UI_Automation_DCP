import selenium
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.webdriver import WebDriver

from config import Configurator


class Driver:

    __instance = None
    _config = Configurator()

    def __init__(self):
        raise PermissionError('Initialization not allowed')

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            options = selenium.webdriver.ChromeOptions()
            #options.add_argument("--headless")
            options.add_argument("--start-maximized")
            cls.__instance = WebDriver(
                executable_path=cls._config.CHROME_DRIVER_PATH,
                desired_capabilities=DesiredCapabilities.CHROME,
                options=options
            )
            cls.__instance.implicitly_wait(cls._config.IMPLICIT_WAIT)
        return cls.__instance
