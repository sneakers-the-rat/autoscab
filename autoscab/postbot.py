import time
import typing
import traceback
import random
from pathlib import Path
from abc import ABC, abstractmethod

import requests

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.utils import ChromeType


from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.ie.options import Options as IEOptions
from selenium.webdriver.opera.options import Options as OperaOptions

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager as FirefoxDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager as EdgeDriverManager
from webdriver_manager.opera import OperaDriverManager

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.service import Service as IEService

from autoscab.identity.identity import Identity
from autoscab.logger import init_logger
from autoscab.locators import Locator

BROWSER_DRIVERS = ('chrome', 'firefox', 'ie', 'edge', 'chromium')


class PostBot(ABC):

    identity_args = None
    """
    Subclasses can specify kwargs to pass on to the identity instance
    rather than passing as an argument.
    """

    def __init__(self,
                 url:typing.Optional[str] = None,
                 locator_dict: typing.Union[dict, Locator]=None,
                 identity:typing.Optional[Identity] = None,
                 identity_args:typing.Optional[dict] = None,
                 headless:bool=True,
                 driver:str='chrome'):
        """

        Args:
            url ():
            locator_dict ():
            identity ():
            identity_args ():
            headless ():
            driver (str): one of 'chrome' (default), 'chromium', 'firefox', 'ie', 'edge', or 'opera'
                Each needs to have the relevant browser installed.
                If we fail to get the requested driver, we'll try all the others
                until we find one that works. see :meth:`.get_browser`
        """
        self._driver = driver
        self.headless = headless
        self.url = url
        self.timeout = 5

        self._tracebacks = True

        if self.identity_args is None:
            self.identity_args = {}

        if identity_args is not None:
            self.identity_args.update(identity_args)

        self.logger = init_logger('postbot')
        if isinstance(locator_dict, dict):
            self.locator_dictionary = dict(locator_dict)
            self.locator = None
        elif isinstance(locator_dict, Locator):
            self.locator = locator_dict
            self.locator_dictionary = locator_dict.postbot_dict
        else:
            raise ValueError(f'Cant handle locator dict {locator_dict}, needs to be a dictionary or Locator object')

        # initialize identity, if none given
        if identity is None:
            self.identity = Identity(**self.identity_args)
        elif isinstance(identity, Identity):
            self.identity = identity
        else:
            raise ValueError('identity must be an Identity object!')

        self.browser = self.get_browser(self._driver)

        self.logger.info('Created webdriver, loading first page')
        self.logger.debug(f'First page is {self.url}')

        if self.url is not None:
            self.browser.get(self.url)

        self.__postinit__()



    def __postinit__(self):
        """
        override in subclasses to add additional logic
        after the initial page load but before filling the application
        """
        pass

    def get_browser(self, driver:str) -> RemoteWebDriver:
        """
        Wrapper around :meth:`._get_browser` that tried to get the requested browser,
        and failing that gets the one that works.

        Args:
            driver ():

        Returns:

        """
        browser = None
        # first try and get the requested driver
        try:
            browser = self._get_browser(driver)
        except (WebDriverException, TypeError):
            self.logger.exception(f'Could not find browser for {driver}, trying other browsers')
            to_try = [d for d in BROWSER_DRIVERS if d != driver]
            for new_driver in to_try:
                self.logger.info(f'Trying driver type {new_driver}')
                try:
                    browser = self._get_browser(new_driver)
                    self._driver = new_driver
                    self.logger.info(f"Success, using {new_driver}")
                    break
                except (WebDriverException, TypeError):
                    self.logger.exception(f'Couldnt find browser {new_driver}')

        if browser is None:
            raise WebDriverException(f"Could not find any browsers on your system! Try firefox!")

        return browser

    def _get_browser(self, driver:str) -> RemoteWebDriver:
        """
        Individual function that tries to get a particular browser, and failing that returns the exception.

        Args:
            driver ():

        Returns:

        """

        if driver == 'chrome':
            options = ChromeOptions()
            manager = ChromeDriverManager().install()
            # why did i do it this getattr way again...
            driver = webdriver.Chrome
            service = ChromeService
        elif driver == 'chromium':
            options = ChromeOptions()
            manager = ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
            driver = webdriver.Chrome
            service = ChromeService
        elif driver == 'firefox':
            options = FirefoxOptions()
            manager = FirefoxDriverManager().install()
            driver = webdriver.Firefox
            service = FirefoxService
        elif driver == 'ie':
            options = IEOptions()
            manager = IEDriverManager().install()
            driver  = webdriver.Ie
            service = IEService
        elif driver == 'edge':
            options = EdgeOptions()
            manager = EdgeDriverManager().install()
            driver = webdriver.Edge
            service = EdgeService
        else:
            raise ValueError(f'Dont know how to handle driver type {driver}, need one of {BROWSER_DRIVERS}')

        # add common options!
        options.add_argument("--disable-dev-shm-usage") #// overcome limited resource problems
        # self.options.add_argument("--no-sandbox") #// Bypass OS security model

        if self.headless:
            options.add_argument("--headless")

        # vary window size slightly to avoid obvious fingerprinting
        width, height = random.randint(1800,1920), random.randint(900, 1080)
        options.add_argument(f"--window-size={width},{height}")

        _service = service(executable_path=manager)
        browser = driver(service=_service, options=options)

        # sometimes window size isn't accepted by options, set it here
        browser.set_window_size(width, height)
        return browser

    def apply(self) -> bool:
        """
        All deployments need to have an 'apply' method that, when called, does the application!
        """

    def random_sleep(self, min=0.05, max=0.25):
        time.sleep(random.random()*(max-min)+min)

    def sleep_until_clickable(self, element:str, timeout:int=10):
        """Note, use the string name of the slement rather than the located self.element"""
        WebDriverWait(
            self.browser, timeout
        ).until(
            EC.element_to_be_clickable(
                self.locator_dictionary[element]
            )
        )

    def quit(self, leaveopen=False):
        if not leaveopen:
            self.browser.close()
        try:
            resume = self.identity.resume
            resume.unlink()
            self.logger.success(f'Deleted resume file: {str(resume)}')
        except Exception as e:
            self.logger.failure(f'Couldnt delete resume file, got error {e}')
        self.browser.quit()

    def execute(self, actions:typing.List[str]):
        """
        Execute a series of actions specified by Locators.

        Args:
            actions (list): A list of strings that correspond to locators with actions associated with them!
        """
        for action in actions:
            # get the action from the locator
            loc = self.locator.locations[action]

            element = getattr(self, action)
            if loc.action == 'click':
                element.click()
            elif loc.action == "send_keys":
                if loc.value.startswith('{') and loc.value.endswith('}'):
                    # get value from identity
                    value = getattr(self.identity, loc.value.lstrip('{').rstrip('}'))
                else:
                    value = loc.value

                element.send_keys(value)

            else:
                raise ValueError(f"Dont know how to execute action type {loc.action}")

            self.random_sleep()

    def print_feedback(self, success:bool):
        """Preformatted string to indicate success or failure"""
        if success:
            self.logger.info("Application submitted and confirmation was successful")
        else:
            self.logger.exception("Was not able to confirm app success! Run again with --noheadless to debug")


    def _find_element(self, *loc):
        return self.browser.find_element(*loc)

    def __getattr__(self, what):
        try:
            locator = self.locator_dictionary.get(what, False)
            if locator:
                try:
                    element = WebDriverWait(self.browser, self.timeout).until(
                        EC.presence_of_element_located(locator)
                    )
                except(TimeoutException, StaleElementReferenceException):
                    if self._tracebacks:
                        traceback.print_exc()

                try:
                    element = WebDriverWait(self.browser, self.timeout).until(
                        EC.visibility_of_element_located(locator)
                    )
                except(TimeoutException, StaleElementReferenceException):
                    if self._tracebacks:
                        traceback.print_exc()
                # I could have returned element, however because of lazy loading, I am seeking the element before return
                return self._find_element(*locator)

        except AttributeError:
            super(PostBot, self).__getattribute__("method_missing")(what)