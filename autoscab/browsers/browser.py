import typing
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Optional, Union, List, Tuple, Type
from random import randint, choice

if typing.TYPE_CHECKING:
    from selenium.webdriver.common.options import ArgOptions
    from webdriver_manager.manager import DriverManager
    from selenium.webdriver.remote.webdriver import WebDriver
    from selenium.webdriver.common.service import Service

from autoscab.logger import init_logger
from autoscab.constants.agents import USER_AGENTS

DEFAULT_OPTIONS = ["--disable-dev-shm-usage"]

class Browser(ABC):
    priority = 999
    extra_options = [] # type: List[str]
    profile_options = [] # type: List[Tuple[str,str]]

    def __init__(self,
                 options:Optional[List[str]]=None,
                 user_agent:Optional[str] = None,
                 headless:bool = True,
                 size:Optional[Tuple[int]]=None,
                 **kwargs):
        """
        Args:
            options (list[str]): A list of strings passed to the `Options` object 
        """
        if options is None:
            options = []
        self._options = [*DEFAULT_OPTIONS, *self.extra_options, *options]

        if size is not None:
            self.size = size
        else:
            self.size = (randint(1800,1920), randint(900,1080))
        self._options.append(f'--window-size={self.size[0]},{self.size[1]}')

        if user_agent is None:
            user_agent = choice(USER_AGENTS)
        self.user_agent = user_agent

        self.headless = headless
        if headless:
            self._options.append('--headless')

        self.logger = init_logger(self.name)

        self.__postinit__(**kwargs)

    def __postinit__(self, **kwargs):
        pass

    @classmethod
    def get(cls, name:Optional[str]=None, all:bool=False, sort:bool=True):
        if name:
            for subclass in cls.__subclasses__():
                if subclass.name == name:
                    return subclass
        elif all:
            subclasses = cls.__subclasses__()
            if sort:
                subclasses.sort(key=lambda x: x.priority)
            return subclasses
        else:
            raise ValueError(f'Can only return by name or return all')


    @classmethod
    def list(cls, sort:bool=True) -> List[str]:
        browser_list = cls.__subclasses__()
        browser_list.sort(key=lambda b: b.priority)
        return [b.name for b in browser_list]

    def init(self) -> 'WebDriver':
        manager = self._init_manager()
        bin_path = manager.install()
        options = self._init_options()
        service = self._init_service(bin_path)
        profile = self._init_profile()

        # open browser
        browser = self._init_driver(service=service, options=options, profile=profile)
        browser.set_window_size(self.size[0], self.size[1])
        return browser

    def _init_manager(self) -> 'DriverManager':
        return self.manager()

    def _init_options(self) -> 'ArgOptions':
        options = self.options()
        for option in self._options:
            options.add_argument(option)
        return options

    def _init_service(self, executable_path:str):
        return self.service(executable_path=executable_path)

    def _init_profile(self):
        if self.profile is None:
            return None
        else:
            profile = self.profile()
            for option in self.profile_options:
                profile.set_preference(option[0], option[1])

            return profile

    def _init_driver(self, options, service, profile=None):
        """
        Default profile is unused, since they are named like 'firefox_profile'.
        override in subclasses
        """
        return self.driver(service=service, options=options)


    @property
    @abstractmethod
    def name(self) -> str:
        pass
    
    @property
    @abstractmethod
    def manager(self) -> Type['DriverManager']:
        """
        Returns:
            :class:`webdriver_manager.manager.DriverManager`
        """
        pass
        
    @property
    @abstractmethod
    def driver(self) -> Type['WebDriver']:
        """
        Returns:
            : 
        """
        pass
    
    @property
    @abstractmethod
    def service(self) -> Type['Service']:
        """
        Returns:
            : 
        """
        pass

    @property
    @abstractmethod
    def options(self) -> Type['ArgOptions']:
        pass

    @property
    def profile(self) -> Optional[typing.Callable]:
        return None
    
    
