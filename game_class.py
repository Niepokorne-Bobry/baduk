from field import *
from enums.move_types import *
from board import Board


class Game:
    def __init__(self, size: int):
        self.__board: Board = Board(size)

    @property
    def board(self):
        return self.__board

    def validateMove(self, xCoord: int, yCoord: int):
        if self.__board.fields[yCoord][xCoord].fieldType != FieldTypes.NONE:
            return MoveType.MOVE_ILLEGAL
        else:
            return MoveType.MOVE_OK

    def clearFieldChecks(self):
        for i in range(self.board.size):
            for j in range(self.board.size):
                self.board.fields[i][j].wasChecked = False
