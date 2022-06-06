from field import *
from enums.move_types import *
from board import Board
from player import Player
from constants import PLAYER_ONE_COLOR, PLAYER_TWO_COLOR


class Game:
    def __init__(self, size: int):
        self.__players = [Player(FieldTypes.PLAYER_1_STONE, self, PLAYER_ONE_COLOR), Player(FieldTypes.PLAYER_2_STONE, self, PLAYER_TWO_COLOR)]
        self.__board: Board = Board(size)
        self.__active_player = 0

    @property
    def board(self):
        return self.__board

    def validateMove(self, xCoord: int, yCoord: int):
        if self.__board.fields[xCoord][yCoord].fieldType != FieldTypes.NONE:
            return MoveType.MOVE_ILLEGAL
        else:
            return MoveType.MOVE_OK

    def clearFieldChecks(self):
        for i in range(self.board.size):
            for j in range(self.board.size):
                self.board.fields[i][j].wasChecked = False

    def playerToggle(self):
        self.__active_player = 1 if self.__active_player == 0 else 0

    def getActivePlayer(self):
        return self.__players[self.__active_player]
