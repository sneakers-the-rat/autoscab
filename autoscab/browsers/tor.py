import requests
from pathlib import Path
import typing
import tarfile
import subprocess
import shutil

from selenium.webdriver.common.proxy import Proxy

from autoscab.browsers.tor.parsers import get_latest_version
from autoscab.utils import get_os, download, extract_tarxz


TOR_BINARIES = {
    'mac': '/Applications/TorBrowser.app/Contents/MacOS/firefox',
    'linux': '/usr/bin/tor-browser/Browser/firefox',
    'windows': r'C:\Program Files (x86)\TorBrowser\Browser\firefox.exe'
}
"""
Default Tor Browser Locations across different operating systems
"""


class TorProvider:
    """
    Provide a version of the Tor Browser by downloading from the release archiv e
    """
    TOR_ARCHIVE = 'https://archive.torproject.org/tor-package-archive/torbrowser/'
    SORT_SUFFIX = '?C=M;O=D'
    REQUEST_STR = TOR_ARCHIVE + SORT_SUFFIX

    def __init__(self):
        self._latest_idx = None
        self.version_links = {}
        self.tmp_dir = Path().home() / 'autoscab'

    @property
    def default_location(self) -> Path:
        return Path(TOR_BINARIES[self.os])

    @property
    def os(self) -> str:
        return get_os()

    def _check_download(self, method='cli') -> bool:

        if method == 'cli':
            if self.os == 'windows':
                res = input(f'Tor was not detected on your computer. Would you like to try to install it now? To install on Windows, we will download the installer, run it, and you will need to complete the install wizard. (Do not change the default path, as we will be looking for the browser executable at {TOR_BINARIES["windows"]}\nTry to install Tor? ([y]/n): ')
            else:
                res = input('Tor was not detected on your computer, try and install it automatically now? ([y]/n): ')

            if res.lower().startswith('n'):
                return False
            else:
                return True

        else:
            raise NotImplementedError('No other method but CLI assent has been implemented!')

    def get_tor(self) -> typing.Union[Path, bool]:
        """
        Return the path to the tor binary, getting it if needed.

        Returns:

        """
        if self.default_location.exists():
            return self.default_location

        try_install = self._check_download()
        if not try_install:
            try:
                version_link = get_latest_version(self.REQUEST_STR)[self.os]
                print(f'Not attempting to install Tor automatically. To install it yourself, the download link for the latest version on your operating system should be {version_link}')
            except:
                print('Not attempting to automatically download Tor. See the download page for manual installation: https://www.torproject.org/download/')

            return False

        print('Attempting to download and install Tor')
        result = self._download()
        if not result:
            raise RuntimeError('Something went wrong downloading the file! Sorry cant be verbose, still testing!')

        tor_file, firefox_file, firefox_profile = self._install(result)



    def _download(self) -> typing.Union[Path,bool]:
        self.tmp_dir.mkdir(exist_ok=True, parents=True)
        version_link = get_latest_version(self.REQUEST_STR)[self.os]
        tmp_file = self.tmp_dir / Path(version_link).name
        print(f'Downloading {version_link} to {str(tmp_file)}')
        result = download(version_link, tmp_file)
        if not result:
            return False
        else:
            return tmp_file

    def _install(self, infile:Path) -> typing.Tuple[Path, Path, Path]:
        """
        Install in airquotes. Do what it takes to get us a path to firefox.exe

        Args:
            infile (:class:`pathlib.Path`): Location of downloaded (os dependent) file

        Returns:
            tuple of paths to (tor, firefox, firefox profile)
        """
        if self.os == 'linux':
            extract_tarxz(infile, infile.parent)
            # name of first member will be the folder
            with tarfile.open(infile, 'r') as tf:
                dirname = tf.getmembers()[0].name
            tor_file = infile.parent / dirname / 'Browser' / 'TorBrowser' / 'Tor' / 'tor'
            ff_file = infile.parent / dirname / 'Browser' / 'firefox'
            ff_profile = infile.parent / dirname / 'Browser' / 'TorBrowser' / 'Data' / 'Browser' / 'profile.default'
        elif self.os == 'mac':
            # mount with hdiutil
            subprocess.run(
                ['/usr/bin/hdiutil', 'attach', str(infile)],
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE
            )
            # mounts to the same place always i think
            mountfile = Path('/Volumes/Tor Browser/Tor Browser.app')
            shutil.copy(mountfile, infile.parent)
            appfile = infile.parent / 'Tor Browser.app'
            tor_file = appfile / 'Contents' / 'Resources' / 'TorBrowser' / 'Tor' / 'tor'
            ff_file = appfile / 'Contents' / 'MacOS' / 'firefox'
            ff_profile = None

        elif self.os == 'windows':
            raise NotImplementedError("Windows not implemented yet! Sorry!")
        else:
            raise ValueError('How did you even get here!?')

        return tor_file, ff_file, ff_profile

    @property
    def latest_idx(self) -> str:
        """
        Returns:
            str: the url to the index of the latest tor releases
        """
        if self._latest_idx is None:
            page = requests.get(self.TOR_ARCHIVE)
        return self._latest_idx







class TorProxy(Proxy):
    """
    JUST DO THIS ONE - https://stackoverflow.com/a/69797422/13113166

    References:
        - https://stackoverflow.com/a/69797422/13113166
        - https://stackoverflow.com/a/21836296/13113166
        - https://boredhacking.com/tor-webscraping-proxy/
        - https://stackoverflow.com/q/28651889/13113166
        - https://stem.torproject.org/api/process.html
        - https://github.com/SeleniumHQ/selenium/blob/64447d4b03f6986337d1ca8d8b6476653570bcc1/py/selenium/webdriver/common/proxy.py
        - https://github.com/SeleniumHQ/selenium/blob/a97b1dd709be551693ab7004e729207cbc73427a/py/test/unit/selenium/webdriver/remote/remote_connection_tests.py
        - https://github.com/SeleniumHQ/selenium/blob/a22d0fd220abf69e7ad32100f6f60a426dfba9c6/py/test/unit/selenium/webdriver/firefox/firefox_options_tests.py
        - https://github.com/SeleniumHQ/selenium/blob/64447d4b03f6986337d1ca8d8b6476653570bcc1/py/test/selenium/webdriver/common/proxy_tests.py
        - https://www.thedurkweb.com/automated-anonymous-interactions-with-websites-using-python-and-tor/
        - https://gitlab.torproject.org/legacy/trac/-/wikis/doc/TorifyHOWTO
        - https://www.py4u.net/discuss/16726
    """
    def __init__(self, **kwargs):
        super(TorProxy, self).__init__(**kwargs)

        # check if tor is launched, otherwise launch it
        # then make an already-configured proxy

        # proxy type = manual
        # socks = local ip
        # socks_port = local port (9050)



def init_tor():
    """
    Initialize the tor process with stem
    """
    pass