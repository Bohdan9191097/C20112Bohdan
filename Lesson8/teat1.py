from logger import Logger
loggerName = __name__
logger = Logger(loggerName,'fileLog.log', 20)
logger.Log('debug message')
logger.Log('info message')
logger.Log('warning message')
logger.Log('error message')
logger.Log('critical message')