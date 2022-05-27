from field import *
from move_type import *
from board import Board


class Game:
    def __init__(self, size: int):
        self.__board = Board(size)

    @property
    def board(self):
        return self.__board

    def validateMove(self, xCoord: int, yCoord: int):
        if self.__board.fields[yCoord][xCoord].fieldType != FieldTypes.NONE:
            return MoveType.MOVE_ILLEGAL
        else:
            return MoveType.MOVE_OK
