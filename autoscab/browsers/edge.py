from autoscab.browsers import Browser

from webdriver_manager.microsoft import EdgeChromiumDriverManager as EdgeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options as EdgeOptions

class EdgeBrowser(Browser):
    name = 'edge'
    manager = EdgeDriverManager
    driver = Edge
    service = EdgeService
    options = EdgeOptions

    def __postinit__(self, **kwargs):
        self._options.append(f'user-agent={self.user_agent}')
