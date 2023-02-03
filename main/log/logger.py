# https://docs.python.org/3/library/logging.html#logging.Formatter
import os, sys
import logging
import time
from logging.handlers import TimedRotatingFileHandler

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

project_path = os.path.dirname(os.path.abspath(sys.argv[0]))
current_time = time.strftime("%Y.%m.%d")

handler = TimedRotatingFileHandler(f'{project_path}\\server-{current_time}.log', when="d", interval=1, backupCount=30, utc=True)

handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s %(levelname)-7s [%(filename)s(%(funcName)s:%(lineno)d)] %(message)s")
handler.setFormatter(formatter)

log.addHandler(handler)