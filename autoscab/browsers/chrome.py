from autoscab.browsers import Browser

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver import Chrome, ChromeOptions

from webdriver_manager.utils import ChromeType

class ChromeBrowser(Browser):
    name = 'chrome'
    manager = ChromeDriverManager
    driver = Chrome
    service = ChromeService
    options = ChromeOptions
    priority = 0

    extra_options = ['disable-extensions']

    def __postinit__(self, **kwargs):
        self._options.append(f'user-agent={self.user_agent}')


class ChromiumBrowser(ChromeBrowser):
    name = 'chromium'
    priority = 999

    def _init_manager(self) -> ChromeDriverManager:
        return self.manager(chrome_type=ChromeType.CHROMIUM)


