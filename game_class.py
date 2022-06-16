from field import *
from enums.move_types import *
from board import Board
from player import Player
from constants import PLAYER_ONE_COLOR, PLAYER_TWO_COLOR
from Int_Container import IntContainer
from enums.field_types import FieldTypes


class Game:
    def __init__(self, size: int):
        self.__players = [Player(FieldTypes.PLAYER_1_STONE, self, PLAYER_ONE_COLOR),
                          Player(FieldTypes.PLAYER_2_STONE, self, PLAYER_TWO_COLOR)]
        self.__board: Board = Board(size)
        self.__active_player = 0
        self.__gameEnd = False

    @property
    def gameEnd(self):
        return self.__gameEnd

    @gameEnd.setter
    def gameEnd(self, newVal: bool):
        self.__gameEnd = newVal

    @property
    def board(self):
        return self.__board

    @property
    def players(self):
        return self.__players

    def validateMove(self, xCoord: int, yCoord: int):
        if self.__board.fields[yCoord][xCoord].fieldType != FieldTypes.NONE:
            return MoveType.MOVE_ILLEGAL
        else:
            return MoveType.MOVE_OK

    def clearFieldChecks(self):
        for i in range(self.board.size):
            for j in range(self.board.size):
                self.board.fields[i][j].wasChecked = False

    def playerToggle(self):
        self.__active_player = 1 if self.__active_player == 0 else 0

    def getInactivePlayer(self):
        return self.__players[1 if self.__active_player == 0 else 0]

    def getActivePlayer(self):
        return self.__players[self.__active_player]

    def __gameScoreCalculationAlgorithm(self, field: Field, pointCounter: IntContainer,
                                        playerOneStoneCounter: IntContainer,
                                        playerTwoStoneCounter: IntContainer):
        if field.fieldType == FieldTypes.NONE and field.wasChecked is False:
            pointCounter.intIncrement()
            field.wasChecked = True
            try:
                self.__gameScoreCalculationAlgorithm(field.getUpperNeighbour(), pointCounter, playerOneStoneCounter,
                                                     playerTwoStoneCounter)
            except:
                pass
            try:
                self.__gameScoreCalculationAlgorithm(field.getRightNeighbour(), pointCounter, playerOneStoneCounter,
                                                     playerTwoStoneCounter)
            except:
                pass
            try:
                self.__gameScoreCalculationAlgorithm(field.getLowerNeighbour(), pointCounter, playerOneStoneCounter,
                                                     playerTwoStoneCounter)
            except:
                pass
            try:
                self.__gameScoreCalculationAlgorithm(field.getLeftNeighbour(), pointCounter, playerOneStoneCounter,
                                                     playerTwoStoneCounter)
            except:
                pass
        elif field.fieldType == FieldTypes.PLAYER_1_STONE and field.wasChecked is False:
            playerOneStoneCounter.intIncrement()
            field.wasChecked = True
            return
        elif field.fieldType == FieldTypes.PLAYER_2_STONE and field.wasChecked is False:
            playerTwoStoneCounter.intIncrement()
            field.wasChecked = True
            return
        return

    def gameScoreCalculation(self):
        self.__gameEnd = True
        playerOneSurroundingStones = IntContainer()
        playerTwoSurroundingStones = IntContainer()
        gainedPoints = IntContainer()
        for fieldRow in self.board.fields:
            for field in fieldRow:
                self.__gameScoreCalculationAlgorithm(field, gainedPoints, playerOneSurroundingStones,
                                                     playerTwoSurroundingStones)
                if playerOneSurroundingStones.int > playerTwoSurroundingStones.int:
                    self.__players[0].score += gainedPoints.int
                elif playerTwoSurroundingStones.int > playerOneSurroundingStones.int:
                    self.__players[1].score += gainedPoints.int
                gainedPoints.resetInt()
                playerOneSurroundingStones.resetInt()
                playerTwoSurroundingStones.resetInt()
                for fieldRow2 in self.board.fields:
                    for field2 in fieldRow2:
                        if field2.fieldType != FieldTypes.NONE:
                            field2.wasChecked = False
