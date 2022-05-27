#klasa Field przechowująca nazwę objektu oraz jego nazwę
class Field():
    def __init__(self,name,x,y):
        self.name=name
        self.__fieldType=NONE
        self.x=x
        self.y=y

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

class coordinates():
    def __init__(self,x,y):
        self.x=x
        self.y=y