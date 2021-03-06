from asyncio.windows_events import NULL
from constants import CLICKABLE_FIELD_SIZE
from enums.field_types import FieldTypes
from enums.move_types import MoveType
from group import Group


class Player:
    def __init__(self, fieldType: FieldTypes, game, playerColor):
        self.__game = game
        self.__score = 0
        self.__fieldType = fieldType
        self.__groups: list[Group] = []
        self.__playerColor = playerColor
        self.__isPassing = False

    @property
    def isPassing(self):
        return self.__isPassing

    @isPassing.setter
    def isPassing(self, newVal: bool):
        self.__isPassing = newVal

    @property
    def playerColor(self):
        return self.__playerColor

    @property
    def groups(self):
        return self.__groups

    def createGroups(self):
        self.__groups.clear()
        newGroup: Group
        for i in range(self.__game.board.size):
            for j in range(self.__game.board.size):
                if self.__game.board.fields[i][j].wasChecked:
                    continue
                newGroup = Group(self.fieldType)
                newGroup.addFieldsToGroup(self.__game.board.fields[i][j])
                if newGroup.size() > 0:
                    self.groups.append(newGroup)

    def updateGroups(self):
        newGroups: list[Group] = []
        lostPoints = 0
        for group in self.groups:
            lostPoints = 0
            group.calculateGroupLiberties()
            if group.groupLiberties > 0:
                newGroups.append(group)
            elif group.groupLiberties == 0:
                for field in group.fields:
                    field.fieldType = FieldTypes.NONE
                    lostPoints += 1
                if self.__fieldType == FieldTypes.PLAYER_1_STONE:
                    self.__game.players[1].score += lostPoints
                elif self.__fieldType == FieldTypes.PLAYER_2_STONE:
                    self.__game.players[0].score += lostPoints
        self.__groups = newGroups

    @property
    def fieldType(self):
        return self.__fieldType

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, newScore):
        self.__score = newScore

    def makeMove(self, x, y):
        for i in range(self.__game.board.size):
            for j in range(self.__game.board.size):
                if ((abs(self.__game.board.fields[i][j].coordX - x) <= CLICKABLE_FIELD_SIZE) and
                        abs(self.__game.board.fields[i][j].coordY - y) <= CLICKABLE_FIELD_SIZE):
                    if self.__game.validateMove(self.__game.board.fields[i][j].boardX, self.__game.board.fields[i][j].boardY) == MoveType.MOVE_OK:
                        self.__game.board.fields[i][j].fieldType = self.__fieldType
                        return self.__game.board.fields[i][j].coordX, self.__game.board.fields[i][j].coordY, self.__game.board.fields[i][j].boardX, self.__game.board.fields[i][j].boardY
                    else:
                        return -1, -1, -1, -1
        return -1, -1, -1, -1
