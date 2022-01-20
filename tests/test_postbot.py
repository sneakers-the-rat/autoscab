import pytest
from autoscab.postbot import PostBot
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from platform import system
import os

@pytest.mark.parametrize('driver', ['chrome', 'firefox'])
def test_drivers(driver):
    """
    Test that we can instantiate with different drivers
    """
    if os.getenv('CI') and (system() == 'Windows' or system() == 'Darwin') and driver == 'firefox':
        assert True
        return
    pbot = PostBot(driver=driver, locator_dict={})
    assert isinstance(pbot.browser, RemoteWebDriver)
    assert pbot._driver == driver
