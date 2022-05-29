class Player:
    def __init__(self):
        self.__score = 0;

    @property
    def score(self):
        return self.__score

    def makeMove(self):
        return