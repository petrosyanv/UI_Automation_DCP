import os
from configparser import ConfigParser


class Configurator:

    def __init__(self):
        config = ConfigParser()
        config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

        # Global config
        self.WEB_APP_URL = config.get('global', 'web_app_url')
        self.MAIN_USER = config.get('global', 'main_user')
        self.MAIN_USER_PASS = config.get('global', 'main_user_pass')

        self.SCREENSHOT_DIR_PATH = os.path.join(os.path.dirname(__file__), 'screenshots')

        # Web part
        self.CHROME_DRIVER_PATH = os.path.join(os.path.dirname(__file__), 'drivers', 'chromedriver')
        self.IMPLICIT_WAIT = 10
