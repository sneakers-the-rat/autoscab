import typing
from logging import Logger, FileHandler, StreamHandler, INFO, DEBUG, WARNING, ERROR
import logging
from datetime import datetime
from pathlib import Path

import sys
if sys.version_info.minor >= 8:
    from typing import Literal
else:
    from typing_extensions import Literal

from autoscab.constants.colors import GREEN, RESET, RED


class ValenceLogger(Logger):

    def success(self, message:str):
        logstr = GREEN + "[ SUCCESS ] " + message + RESET
        self.info(logstr)

    def failure(self, message:str):
        logstr = RED + "[ SUCCESS ] " + message + RESET
        self.info(logstr)

LOGLEVELS = Literal[DEBUG, INFO, WARNING, ERROR]

def init_logger(name:str="autoscab", loglevel:LOGLEVELS = INFO) -> ValenceLogger:
    logdir = Path().home() / 'autoscab'
    logfile = logdir / f"{datetime.now().strftime('%Y-%m-%d')}_{name}.log"

    log_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s : %(message)s")

    logger = ValenceLogger(name=name)
    logger.setLevel(loglevel)

    sh = StreamHandler()
    sh.setLevel(loglevel)
    sh.setFormatter(log_formatter)
    logger.addHandler(sh)

    try:
        logdir.mkdir(exist_ok=True)
        fh = FileHandler(
            str(logfile),
            mode='a'
        )
        fh.setLevel(loglevel)
        fh.setFormatter(log_formatter)
        logger.addHandler(fh)
    except Exception as e:
        logger.exception(f'couldnt make logging directory or logging file, will not be saving logs to disk, got exception {e}')

    return logger

