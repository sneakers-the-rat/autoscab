import typing
from dataclasses import dataclass
import random
from datetime import date


from autoscab.postbot import PostBot
from autoscab.locators import Locator

@dataclass
class Deployment:
    name: str
    urls: typing.List[str]
    locators: typing.Union[
        typing.Dict[str, typing.Tuple[str, str]],
        Locator
    ]
    """
    Dictionary of locators using selenium.webdriver.common.By classes like::
    
        {
            'locator_name': (By.<LOCATOR_TYPE>, 'locator')
        }
    """
    postbot: typing.Type[PostBot]
    """
    A subclass of PostBot for this particular deployment that implements an apply method
    """

    active_dates: typing.Tuple[date, typing.Optional[date]]
    """
    Dates that this deployment is active, a tuple of :class:`datetime.date` objects that indicate 
    ``[start_date, end_date]`` used to retire active deployments when the need for them has ended.
    
    Deployments that are active but don't have a known end date can declare `[start_date, None]`.
    
    Start date is included so that groups can plan ahead but not tip their hand ;)
    """

    deployments: typing.ClassVar = []

    def make(self, **kwargs) -> PostBot:
        """
        Instantiate a PostBot with a url chosen at random,
        passing **kwargs onto the PostBot
        """
        url = random.choice(self.urls)
        return self.postbot(url=url, locator_dict=self.locators, **kwargs)

    def __post_init__(self):
        self.deployments.append(self)

    @classmethod
    def get_deployments(cls) -> typing.Dict[str, 'Deployment']:
        """
        Return a dictionary of declared Deployment objects, with their `name`s as keys
        """
        deploys = {deploy.name: deploy for deploy in cls.deployments}
        return deploys


