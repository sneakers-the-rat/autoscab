from dataclasses import dataclass
import typing
import sys
if sys.version_info.minor >= 8:
    from typing import Literal
else:
    from typing_extensions import Literal

from selenium.webdriver.common.by import By



@dataclass
class Location:
    """
    A single location on an application page.

    Examples:

        Location(By.CLASS_NAME, '#first_name_textbox', 'send_keys', '{identity.first_name}')

    """
    by: Literal[By.CLASS_NAME, By.CSS_SELECTOR, By.ID, By.LINK_TEXT, By.NAME, By.PARTIAL_LINK_TEXT, By.TAG_NAME, By.XPATH]
    """
    The Selenium By selector to use for the :attr:`.location`
    """

    location: str
    """
    The location on the webpage, depends on :attr:`.by`.
    
    Examples:
        By ``CSS_SELECTOR`` : ``'#fbclc_country > option[value=US]'``
        By ``XPATH`` : ``//*[@id="dialogTemplate-dialogForm-userName"]``
    
    """

    action: Literal['send_keys', 'click', 'manual']
    """
    The selenium action to take with the location, if ``send_keys``, need to provide a value.
    
    if 'manual', mark as to be handled manually in the post-bot
    """

    value: typing.Optional[str] = None
    """
    The value to input in the location. 
    
    Specify values from the :class:`~autoscab.identity.identity.Identity` class like::
    
        '{identity.first_name}'
    
    """


@dataclass
class Page:
    """
    Collectioon of :class:`.Location` objects . Not Implemented.
    """
    pass

@dataclass
class Locator:
    """
    A mapping that gives simple names to elements on the form, and tells the
    :class:`autoscab.postbot.PostBot` how do use them.

    .. todo::

        Group Locators into Pages
    """
    locations: typing.Dict[str, Location]
    """
    Locations for a given :class:`.Deployment` . as a dictionary mapping {'shortname': :class:`.Location` }
    """

    @property
    def postbot_dict(self) -> typing.Dict[str, typing.Tuple[str, str]]:
        """
        Make a dictionary compatible with the :class:`.PostBot`, eg. ::

            {
                "shortname": (By.CSS_SELECTOR, '#target_id')
            }

        """
        return { shortname : (loc.by, loc.location) for shortname, loc in self.locations.items() }

