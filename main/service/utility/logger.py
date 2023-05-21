# https://docs.python.org/3/library/logging.html#logging.Formatter
import logging
import time
from logging.handlers import TimedRotatingFileHandler, SMTPHandler
from config import PROJECT_ROOT
from main.service.utility.mail import mail

class EmailHandler(logging.Handler):
    def emit(self, record):
        if record.levelno >= logging.ERROR:
            mail.send_message(
                subject='Application Error',
                recipients=['milos.dj.markovic@gmail.com'],
                body=self.format(record)
            )

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

log_path = PROJECT_ROOT + "/log/"
current_time = time.strftime("%Y-%m-%d")

handler = TimedRotatingFileHandler(f'{log_path}server.log.{current_time}', when="d", interval=1, backupCount=30, utc=True, encoding='utf-8')
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s %(levelname)-7s [%(filename)s(%(funcName)s:%(lineno)d)] %(message)s")
handler.setFormatter(formatter)
log.addHandler(handler)
log.addHandler(EmailHandler())