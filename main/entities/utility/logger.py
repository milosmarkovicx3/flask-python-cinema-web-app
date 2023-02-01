import logging

# https://docs.python.org/3/library/logging.html#logging.Formatter
LOG_FORMAT = "%(asctime)s %(levelname)-7s [%(pathname)s(%(funcName)s:%(lineno)d)] %(message)s"

logging.basicConfig(format=LOG_FORMAT)

log = logging.getLogger()