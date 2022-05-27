from field import Field
from constants import line_color, LINE_WIDTH, LINE_LENGTH
import pygame


class Board:
    def __init__(self, size: int):
        if size != 9 and size != 13 and size != 19:
            raise ValueError("incorrect size of the board")
        self.__size = size
        zmienna = 1
        self.__fields = []
        tempRow = []
        for i in range(self.__size):
            for j in range(self.__size):
                name = 'object' + str(zmienna)
                tempRow.append(Field(name, LINE_LENGTH + (j * LINE_LENGTH), LINE_LENGTH + (i * LINE_LENGTH)))
                zmienna += 1
            self.__fields.append(tempRow)
            tempRow = []

    # funkcja do rysowania linii
    tempCoordinates = []

    def draw_lines(self, screen, SIZE):
        for i in range(self.__size):
            x = i * LINE_LENGTH
            # poziome linie
            pygame.draw.line(screen, line_color, [0, LINE_LENGTH + x], [SIZE, LINE_LENGTH + x], LINE_WIDTH)
            # pionowe linie
            pygame.draw.line(screen, line_color, [LINE_LENGTH + x, 0], [LINE_LENGTH + x, SIZE], LINE_WIDTH)

    @property
    def size(self):
        return self.__size

    @property
    def fields(self):
        return self.__fields
