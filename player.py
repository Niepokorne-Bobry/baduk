from enums.field_types import FieldTypes
from group import Group
from main import game

class Player:
    def __init__(self, fieldType: FieldTypes):
        self.__score = 0
        self.__fieldType = fieldType
        self.__groups: list[Group] = []

    @property
    def groups(self):
        return self.__groups

    def createGroups(self):
        newGroup: Group
        for i in range(game.board.size):
            for j in range(game.board.size):
                if game.board.fields[i][j].wasChecked:
                    continue
                newGroup = Group(self.fieldType)
                newGroup.addFieldsToGroup(game.board.fields[i][j])
                self.groups.append(newGroup)

    def updateGroups(self):
        newGroups: list[Group] = []
        for group in self.groups:
            group.calculateGroupLiberties()
            if group.groupLiberties is not 0:
                newGroups.append(group)
            else:
                for field in group.fields:
                    field.fieldType = FieldTypes.NONE
        self.__groups = newGroups


    @property
    def fieldType(self):
        return self.__fieldType

    @property
    def score(self):
        return self.__score

    def makeMove(self):
        return