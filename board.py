from field import Field
from constants import HUD_SIZE, line_color, LINE_WIDTH, LINE_LENGTH, FIELD_OFFSET, CIRCLE_RADIUS
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
                tempRow.append(
                    Field(name, LINE_LENGTH + (j * LINE_LENGTH) + FIELD_OFFSET, LINE_LENGTH + (i * LINE_LENGTH) + HUD_SIZE + FIELD_OFFSET, j, i, self))
                zmienna += 1
            self.__fields.append(tempRow)
            tempRow = []

    # funkcja do rysowania linii
    tempCoordinates = []

    def draw_lines(self, screen, HUD_SIZE, SIZE):
        for i in range(self.__size):
            x = i * LINE_LENGTH
            # poziome linie
            pygame.draw.line(screen, line_color, [0, LINE_LENGTH + x + HUD_SIZE + FIELD_OFFSET], [SIZE, LINE_LENGTH + x + HUD_SIZE + FIELD_OFFSET], LINE_WIDTH)
            # pionowe linie
            pygame.draw.line(screen, line_color, [LINE_LENGTH + x + FIELD_OFFSET, HUD_SIZE], [LINE_LENGTH + x + FIELD_OFFSET, SIZE+HUD_SIZE], LINE_WIDTH)

    @property
    def size(self):
        return self.__size

    @property
    def fields(self):
        return self.__fields

    # rysowanie kamienia o okreslonym kolorze (color) na wspolrzednych xi y
    def drawStone(self, field, color, cords = []):
        pygame.draw.circle(field, color, cords, CIRCLE_RADIUS)
