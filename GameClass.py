from field import *
from MoveType import *


class Game:
    def __init__(self, size: int):
        if size != 9 and size != 13 and size != 19:
            raise ValueError("incorrect size of the board")
        self.__logical_board = []
        tempRow = []
        for i in range(size):
            for j in range(size):
                tempRow.append(Field())
            self.__logical_board.append(tempRow)
            tempRow = []

    @property
    def logical_board(self):
        return self.__logical_board

    def validateMove(self, xCoord: int, yCoord: int):
        if self.__logical_board[yCoord][xCoord].fieldType != 0:
            return MoveType.MOVE_ILLEGAL
        else:
            return MoveType.MOVE_OK
