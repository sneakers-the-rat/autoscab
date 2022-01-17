import time
import typing
import traceback
import random
from pathlib import Path
from abc import ABC, abstractmethod

import requests

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from autoscab.identity.identity import Identity
from autoscab.logger import init_logger
from autoscab.locators import Locator



class PostBot(ABC):

    identity_args = None
    """
    Subclasses can specify kwargs to pass on to the identity instance
    rather than passing as an argument.
    """

    def __init__(self,
                 url:str,
                 locator_dict: typing.Union[dict, Locator],
                 identity:typing.Optional[Identity] = None,
                 identity_args:typing.Optional[dict] = None,
                 headless:bool=True):

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

        self.options = Options()

        # initialize identity, if none given
        if identity is None:
            self.identity = Identity(**self.identity_args)
        elif isinstance(identity, Identity):
            self.identity = identity
        else:
            raise ValueError('identity must be an Identity object!')

        self.options.add_argument("disable-infobars")
        self.options.add_argument("--disable-dev-shm-usage") #// overcome limited resource problems
        # self.options.add_argument("--no-sandbox") #// Bypass OS security model

        if headless:
            self.options.add_argument("--headless")

        # vary window size slightly to avoid obvious fingerprinting
        width, height = random.randint(1800,1920), random.randint(900, 1080)
        self.options.add_argument(f"--window-size={width},{height}")

        self.url = url
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=self.options)  # export PATH=$PATH:/path/to/chromedriver/folder
        self.timeout = 5

        self.logger.info('Created webdriver, loading first page')
        self.logger.debug(f'First page is {self.url}')

        self.browser.get(self.url)

        self.__postinit__()



    def __postinit__(self):
        """
        override in subclasses to add additional logic
        after the initial page load but before filling the application
        """
        pass

    @abstractmethod
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