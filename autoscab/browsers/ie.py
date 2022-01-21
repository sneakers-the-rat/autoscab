from autoscab.browsers import Browser

from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.ie.service import Service as IEService
from selenium.webdriver import Ie
from selenium.webdriver.ie.options import Options as IEOptions

class IEBrowser(Browser):
    name = 'edge'
    manager = IEDriverManager
    driver = Ie
    service = IEService
    options = IEOptions

    def __postinit__(self, **kwargs):
        self._options.append(f'user-agent={self.user_agent}')