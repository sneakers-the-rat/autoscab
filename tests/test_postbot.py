import pytest
from autoscab.postbot import PostBot
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver


@pytest.mark.parametrize('driver', ['chrome', 'firefox'])
def test_drivers(driver):
    """
    Test that we can instantiate with different drivers
    """
    pbot = PostBot(driver=driver, locator_dict={})
    assert isinstance(pbot.browser, RemoteWebDriver)
    assert pbot._driver == driver
