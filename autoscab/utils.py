import random
import typing
import requests
from pathlib import Path
from tqdm import tqdm
import tarfile

import requests
import sys

from autoscab.constants.email import MAIL_GENERATION_WEIGHTS


def get_os() -> str:
    if sys.platform in ('linux', 'linux2'):
        return  'linux'
    elif sys.platform == 'darwin':
        return 'mac'
    elif sys.platform == 'win32':
        return 'windows'
    else:
        raise RuntimeError(f'Cant determine OS from {sys.platform}')

def download(url:str, file_name:typing.Union[Path,str]) -> bool:
    """
    Download a file with a progress bar

    Returns:
        bool: ``True`` if nothing happened and its probs good, ``False`` otherwise

    References:
        https://gist.github.com/yanqd0/c13ed29e29432e3cf3e7c38467f42f51
    """
    try:
        response = requests.get(url, stream=True)
        size = int(response.headers.get('content-length', 0))
        with open(file_name, 'wb') as ofile, tqdm(
                    desc=file_name,
                    total=size,
                    unit='iB',
                    unit_scale=True,
                    unit_divisor=1024,
                ) as pbar:
            for data in response.iter_content(chunk_size=1024):
                size = ofile.write(data)
                pbar.update(size)
        return True
    except:
        return False

def extract_tarxz(
    infile:Path,
    outfile:typing.Optional[Path] = Path('.').resolve()
	):
    with tarfile.open(infile, 'r') as tf:
        tf.extractall(outfile)

def random_email(name):

    mailGens = [lambda fn, ln, *names: fn + ln,
                lambda fn, ln, *names: fn + "_" + ln,
                lambda fn, ln, *names: fn[0] + "_" + ln,
                lambda fn, ln, *names: fn + ln + str(int(1 / random.random() ** 3)),
                lambda fn, ln, *names: fn + "_" + ln + str(int(1 / random.random() ** 3)),
                lambda fn, ln, *names: fn[0] + "_" + ln + str(int(1 / random.random() ** 3)), ]

    return random.choices(mailGens, MAIL_GENERATION_WEIGHTS)[0](*name.split(" ")).lower() + "@" + \
           requests.get('https://api.mail.tm/domains').json().get('hydra:member')[0].get('domain')