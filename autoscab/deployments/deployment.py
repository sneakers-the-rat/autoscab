import typing
from dataclasses import dataclass
import random
from datetime import date
import sys
if sys.version_info.minor<8:
    from importlib_metadata import version
else:
    from importlib.metadata import version

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

    message: str = ''
    """
    Attach a message to your deployment ;)
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
    def get_deployments(cls, active:typing.Optional[bool]=None) -> typing.Dict[str, 'Deployment']:
        """
        Return a dictionary of declared Deployment objects, with their `name`s as keys.


        Args:
            active (bool): If ``None``, return all. If ``True`` or ``False``, only return
                active or inactive deployments, respectively, depending on ``active_dates``
        """
        if active is None:
            deploys = {deploy.name: deploy for deploy in cls.deployments}
        elif active:
            deploys = {deploy.name: deploy for deploy in cls.deployments if deploy.active}
        else:
            deploys = {deploy.name: deploy for deploy in cls.deployments if not deploy.active}
        return deploys

    @classmethod
    def print_deployments(cls):
        deploys = cls.deployments.copy()
        # sort list
        deploys.sort(key= lambda d: (d.active, d.active_dates[0]), reverse=True)
        print('-'*80)
        print(f'Autoscab Deployments ({version("autoscab")})')
        inactive_line = False
        for d in deploys:
            if not d.active and not inactive_line:
                print('~'*80)
                inactive_line = True
            print(str(d))
        print('-' * 80)

    @property
    def active(self) -> bool:
        # get active status
        today = date.today()
        active = False
        if today > self.active_dates[0]:
            if self.active_dates[1] is None or self.active_dates[1] > today:
                active = True
        return active

    def __str__(self) -> str:
        outstr = ''
        BOLD = '\u001b[1m'
        GREEN = '\u001b[32;1m'
        RESET = '\u001b[0m'

        outstr += self.name + ' - '

        if self.active:
            outstr += BOLD + GREEN + "[ ACTIVE ]" + RESET + "   "
        else:
            outstr += "[ INACTIVE ] "

        outstr += self.active_dates[0].strftime('%y-%m-%d') + ' - '
        if self.active_dates[1] is None:
            outstr += '(indefinite)'
        else:
            outstr += self.active_dates[1].strftime('%y-%m-%d')

        if len(self.message)>0:
            if len(self.message) + len(outstr) > 80:
                # get first section
                stridx = 80 - len(outstr)
                stringpcs = [self.message[0:stridx]]
                substr = self.message[stridx:]
                # then break into length 76 segments
                stringpcs.extend([substr[0+i:76+i] for i in range(0, len(substr), 76)])
                message = '\n    '.join(stringpcs)
            else:
                message = self.message
            outstr += ': ' + message

        return outstr











