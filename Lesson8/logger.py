from logging import *

class Logger:
    def __init__(self, loggerName: str, fileName: str):
        self.LoggerName = loggerName
        self.FileName = fileName
        self.__ConfigureLogger()

    def __ConfigureLogger(self):
        self.__Logger = getLogger(self.LoggerName)
        formatter = Formatter('%(asctime)s : %(levelname)s - %(name)s - %(message)s')
        file_handler = FileHandler(filename=self.FileName, mode='a')
        file_handler.setFormatter(formatter)
        self.__Logger.addHandler(file_handler)

    def __LogDecorator(self, *exc_types):
        def Decorator(function):
            def Wrapper(*args, **kwargs):
                try:
                    return function(*args, **kwargs)
                except (exc_types) as ex:
                    raise ex
            return  Wrapper
        return Decorator

    def __Log(self, message: str):
        if self.Level == DEBUG:
            self.__Logger.debug(message)
        elif self.Level == INFO:
            self.__Logger.info(message)
        elif self.Level == WARNING:
            self.__Logger.warning(message)
        elif self.Level == ERROR:
            self.__Logger.error(message)
        elif self.Level == CRITICAL:
            self.__Logger.critical(message)

    @__LogDecorator(Exception)
    def Log(self, message: str, level: int):
        try:
            self.Level = level
            self.__Logger.setLevel(self.Level)
            self.__Log(message)
        except:
            raise