from datetime import datetime

class Clock:
    def __init__(self):
        self.__dt = datetime

    def dateNow(self):
        return self.__dt.now().date()

    def timeNow(self):
        return self.__dt.now().time()
