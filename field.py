from const import *


class Field:

    def __init__(self):
        self.__fieldType = NONE

    @property
    def fieldType(self):
        return self.__fieldType
    
    @fieldType.setter
    def fieldType(self,newType):
        if (newType != NONE 
        and newType != PLAYER_1_STONE 
        and newType != PLAYER_2_STONE):
            raise ValueError
        
        self.__fieldType = newType



