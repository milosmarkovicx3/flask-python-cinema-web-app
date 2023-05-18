# https://docs.python.org/3/library/logging.html#logging.Formatter
import logging
import time
from logging.handlers import TimedRotatingFileHandler, SMTPHandler
from config import PROJECT_ROOT

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

log_path = PROJECT_ROOT + "/log/"
current_time = time.strftime("%Y-%m-%d")

handler = TimedRotatingFileHandler(f'{log_path}server.log.{current_time}', when="d", interval=1, backupCount=30, utc=True, encoding='utf-8')
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s %(levelname)-7s [%(filename)s(%(funcName)s:%(lineno)d)] %(message)s")
handler.setFormatter(formatter)
log.addHandler(handler)

mail_handler = SMTPHandler(
    mailhost='smtp.gmail.com',
    fromaddr='office@arhiv.com',
    toaddrs=['milos.dj.markovic@gmail.com'],
    subject='Application Error'
)
mail_handler.setLevel(logging.ERROR)
mail_handler.setFormatter(formatter)
log.addHandler(mail_handler)
