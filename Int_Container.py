class IntContainer:

    def __init__(self):
        self.__int = 0

    @property
    def int(self):
        return self.__int

    def intIncrement(self):
        self.__int += 1

    def resetInt(self):
        self.__int = 0
