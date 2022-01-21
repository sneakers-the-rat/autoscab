from html.parser import HTMLParser

import requests

TOR_ARCHIVE = 'https://archive.torproject.org/tor-package-archive/torbrowser/'
SORT_STR = '?C=M;O=D'

class VersionParser(HTMLParser):
    """
    nodep, lightweight html parsing instead of booting up selenium for this

    - Parse until we encounter the first folder icon, mark encountered_folder True
    - If encountered_folder is true and encountered_version is false,
          parse until we encounter a version, mark encountered_version true
    """
    def __init__(self, url:str=TOR_ARCHIVE, lang='en-US'):
        super(VersionParser, self).__init__()
        self.url = url
        self.lang = lang
        self.encountered_folder = False
        self.encountered_version = False
        self.version = None

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            if any([attr[0] == 'src' and attr[1] == '/icons/folder.gif' for attr in attrs]):
                self.encountered_folder = True

        if self.encountered_folder and not self.encountered_version:
            if tag == 'a':
                for attr in attrs:
                    if attr[0] == 'href':
                        self.version = attr[1].rstrip('/')
                        self.encountered_version = True

    @property
    def windows_str(self) -> str:
        return f'{self.url}/{self.version}/torbrowser-install-win64-{self.version}_{self.lang}.exe'

    @property
    def mac_str(self) -> str:
        return f'{self.url}/{self.version}/TorBrowser-{self.version}-osx64_{self.lang}.dmg'

    @property
    def linux_str(self) -> str:
        return f'{self.url}/{self.version}/tor-browser-linux64-{self.version}_{self.lang}.tar.xz'

def get_latest_version(archive_url:str = 'https://archive.torproject.org/tor-package-archive/torbrowser/', suffix:str = '?C=M;O=D') -> dict:
    """
    Get the latest version number of tor, given the url to the version archive
    ( https://archive.torproject.org/tor-package-archive/torbrowser/?C=M;O=D )

    Args:
        archive_url (str): Theoretically it could be any of those weird
            source archive pages, but it'll probably be https://archive.torproject.org/tor-package-archive/torbrowser/?C=M;O=D

    Returns:
        dict: like::

            {
                'version': '11.0.4',
                'linux': 'https://dist.torproject.org/torbrowser/11.0.4/tor-browser-linux64-11.0.4_en-US.tar.xz'
                'mac': 'https://dist.torproject.org/torbrowser/11.0.4/TorBrowser-11.0.4-osx64_en-US.dmg',
                'windows': 'https://dist.torproject.org/torbrowser/11.0.4/torbrowser-install-11.0.4_en-US.exe'
            }
    """
    result = requests.get(archive_url + suffix)
    parser = VersionParser(archive_url)
    parser.feed(result.text)
    return {
        'version': parser.version,
        'linux': parser.linux_str,
        'mac': parser.mac_str,
        'windows': parser.windows_str
    }
