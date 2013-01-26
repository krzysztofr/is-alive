# based on http://help.papertrailapp.com/kb/configuration/configuring-centralized-logging-from-python-apps
import logging

from logging.handlers import SysLogHandler
logger = logging.getLogger()
logger.setLevel(logging.INFO)
syslog = SysLogHandler(address=('logs.papertrailapp.com', 57814))
formatter = logging.Formatter('%(name)s: %(levelname)s %(message)s')
syslog.setFormatter(formatter)
logger.addHandler(syslog)

logger.info("I'm alive!")
