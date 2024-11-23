from logger import Logger
loggerName = __name__
logger = Logger(loggerName, 'fileLog.log')
logger.Log('debug message', 10)
logger.Log('info message', 20)
logger.Log('warning message', 30)
logger.Log('error message', 40)
logger.Log('critical message', 50)