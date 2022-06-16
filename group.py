from field import Field
from enums.field_types import FieldTypes

class Group:
    def __init__(self, groupType: FieldTypes):
        self.__fields: list[Field] = []
        self.__groupType = groupType
        self.__groupLiberties = 0

    @property
    def groupLiberties(self):
        return self.__groupLiberties

    def calculateGroupLiberties(self):
        libs = 0
        for field in self.fields:
            field.calculateFieldLiberties()
            libs += field.liberties
        self.__groupLiberties = libs

    @property
    def fields(self):
        return self.__fields

    @property
    def groupType(self):
        return self.__groupType


    def addFieldsToGroup(self, field: Field):
        if field.fieldType == self.__groupType and field.wasChecked is False:
            self.fields.append(field)
            field.wasChecked = True
            try:
                self.addFieldsToGroup(field.getUpperNeighbour())
            except:
                pass
            try:
                self.addFieldsToGroup(field.getRightNeighbour())
            except:
                pass
            try:
                self.addFieldsToGroup(field.getLowerNeighbour())
            except:
                pass
            try:
                self.addFieldsToGroup(field.getLeftNeighbour())
            except:
                pass
        else:
            return


    def size(self):
        size = 0
        for field in self.fields:
            size += 1
        return size


    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False