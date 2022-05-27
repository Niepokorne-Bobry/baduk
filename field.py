#klasa Field przechowująca nazwę objektu oraz jego nazwę
from const import *

class Field():
    def __init__(self,name: str, x: int, y: int):
        self.__name=name
        self.__fieldType=NONE
        self.__x=x
        self.__y=y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, newX: int):
        self.__x = newX

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, newY: int):
        self.__y = newY

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
        if (newType != NONE
                and newType != PLAYER_1_STONE
                and newType != PLAYER_2_STONE):
            raise ValueError

        self.__fieldType = newType
