# klasa Field przechowująca nazwę objektu oraz jego nazwę
from enums.field_types import *


class Field:
    def __init__(self, name: str, coordX: int, coordY: int, boardX: int, boardY: int, board):
        self.__name = name
        self.__fieldType = FieldTypes.NONE
        self.__coordX = coordX
        self.__coordY = coordY
        self.__boardX = boardX
        self.__boardY = boardY
        self.__liberties = 0
        self.__wasChecked = False
        self.__board = board

    @property
    def wasChecked(self):
        return self.__wasChecked

    @wasChecked.setter
    def wasChecked(self, newVal: bool):
        self.__wasChecked = newVal

    def getLeftNeighbour(self):
        try:
            return self.__board.fields[self.__boardY][self.__boardX - 1]
        except:
            raise MemoryError("Can't get left neighbour")

    def getRightNeighbour(self):
        try:
            return self.__board.fields[self.__boardY][self.__boardX + 1]
        except:
            raise MemoryError("Can't get right neighbour")

    def getUpperNeighbour(self):
        try:
            return self.__board.fields[self.__boardY - 1][self.__boardX]
        except:
            raise MemoryError("Can't get upper neighbour")

    def getLowerNeighbour(self):
        try:
            return self.__board.fields[self.__boardY + 1][self.__boardX]
        except:
            raise MemoryError("Can't get lower neighbour")

    def calculateFieldLiberties(self):
        libs = 0
        try:
            if self.getLowerNeighbour().fieldType == FieldTypes.NONE:
                libs += 1
        except:
            pass
        try:
            if self.getLeftNeighbour().fieldType == FieldTypes.NONE:
                libs += 1
        except:
            pass
        try:
            if self.getUpperNeighbour().fieldType == FieldTypes.NONE:
                libs += 1
        except:
            pass
        try:
            if self.getRightNeighbour().fieldType == FieldTypes.NONE:
                libs += 1
        except:
            pass
        return libs

    @property
    def boardX(self):
        return self.__boardX

    @boardX.setter
    def boardX(self, newBoardX):
        self.__boardX = newBoardX

    @property
    def boardY(self):
        return self.__boardY

    @boardY.setter
    def boardY(self, newBoardY):
        self.__boardY = newBoardY

    @property
    def coordX(self):
        return self.__coordX

    @coordX.setter
    def coordX(self, newCoordX: int):
        self.__coordX = newCoordX

    @property
    def coordY(self):
        return self.__coordY

    @coordY.setter
    def coordY(self, newCoordY: int):
        self.__coordY = newCoordY

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newName: str):
        self.__name = newName

    @property
    def fieldType(self):
        return self.__fieldType

    @fieldType.setter
    def fieldType(self, newType):
        if (newType != FieldTypes.NONE
                and newType != FieldTypes.PLAYER_1_STONE
                and newType != FieldTypes.PLAYER_2_STONE):
            raise ValueError

        self.__fieldType = newType
