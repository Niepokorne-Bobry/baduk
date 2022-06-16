import tkinter as tk
from math import floor

__root = tk.Tk()

FPS = 30  # frames per second

size = 9  # liczba linii 9 pionowo 9 poziomo
SIZE = floor(__root.winfo_screenheight() * 0.7)  # zmienna do rozmiaru boku czyli dlugosci kwadtatów wynaczonych przez linie gdy mamy np 3 linie to dziela one bok na 4 czesci wiec 9 linii to 10 kwadratów

LINE_LENGTH = SIZE / 12
FIELD_OFFSET = (SIZE - (LINE_LENGTH * (size - 1))) / 4
line_color = '#D4AF37'  # kolor linii ciemne złoto
LINE_WIDTH = floor(LINE_LENGTH / 6)  # szerokosc linii
PLAYER_ONE_COLOR = (0, 0, 0)
PLAYER_TWO_COLOR = (255, 255, 255)
CIRCLE_RADIUS = floor(LINE_LENGTH * 0.4)
CIRCLE_WIDTH = 5

CLICKABLE_FIELD_SIZE = floor(LINE_LENGTH / 7)  # ilosc pixeli w kazdym kierunku od wspolrzednych punktu - zasięg przypisania kamienia do pola

HUD_SIZE = floor(SIZE / 12)
PLAYER_BUTTONS_SECTION_SIZE = 100
# Menu size
MENU_WIDTH = 800
MENU_HEIGHT = 600

BUTTON_SECTION_POS_Y = SIZE + HUD_SIZE

GAME_TIME_STRING = 'Czas rozgrywki'

PLAYER_MOVE_TIME = 10  # czas na wykonanie ruchu w sekundach

# colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
RED_HOVERED = (144, 32, 32)

#return vals
myQUIT = 0
myPLAY_AGAIN = 1

