# based on http://help.papertrailapp.com/kb/configuration/configuring-centralized-logging-from-python-apps
# IMPORTANT NOTE: remeember to set PAPERTRAIL_PORT enviroment variable
import logging, os

from logging.handlers import SysLogHandler
logger = logging.getLogger()
logger.setLevel(logging.INFO)
syslog = SysLogHandler(address=('logs.papertrailapp.com', int(os.environ['PAPERTRAIL_PORT'])))
formatter = logging.Formatter('%(name)s: %(levelname)s %(message)s')
syslog.setFormatter(formatter)
logger.addHandler(syslog)

logger.info("I'm alive!")
