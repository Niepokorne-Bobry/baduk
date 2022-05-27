size = 9  # liczba linii 9 pionowo 9 poziomo
SIZE = (
                   size * 90) + 90  # zmienna do rozmiaru boku czyli dlugosci kwadtatów wynaczonych przez linie gdy mamy np 3 linie to dziela one bok na 4 czesci wiec 9 linii to 10 kwadratów
line_color = '#D4AF37'  # kolor linii ciemne złoto
LINE_WIDTH = 16  # szerokosc linii

from field import Field
import pygame
from main import screen


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
                tempRow.append(Field(name, 90 + (j * 90), 90 + (i * 90)))
                zmienna += 1
            self.__fields.append(tempRow)
            tempRow = []

    # funkcja do rysowania linii
    tempCoordinates = []

    def draw_lines(self):
        for i in range(self.__size):
            x = i * 90
            # poziome linie
            pygame.draw.line(screen, line_color, [0, 90 + x], [SIZE, 90 + x], LINE_WIDTH)
            # pionowe linie
            pygame.draw.line(screen, line_color, [90 + x, 0], [90 + x, SIZE], LINE_WIDTH)

    @property
    def size(self):
        return self.__size

    @property
    def fields(self):
        return self.__fields
