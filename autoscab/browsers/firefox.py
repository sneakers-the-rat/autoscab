from autoscab.browsers import Browser

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver import Firefox, FirefoxOptions, FirefoxProfile

class FirefoxBrowser(Browser):
    name = 'firefox'
    manager = GeckoDriverManager
    driver = Firefox
    service = FirefoxService
    options = FirefoxOptions
    profile = FirefoxProfile
    priority = 1

    extra_options = ['disable-extensions']

    def __postinit__(self, **kwargs):
        self.profile_options = self.profile_options.copy()
        self.profile_options.append(("general.useragent.override", self.user_agent))

    def _init_driver(self, options, service, profile=None):
        """
        Default profile is unused, since they are named like 'firefox_profile'.
        override in subclasses
        """
        return self.driver(service=service, options=options, firefox_profile=profile)