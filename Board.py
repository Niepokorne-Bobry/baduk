"""
size=9  liczba linii 9 pionowo 9 poziomo
SIZE=(size*90)+90  zmienna do rozmiaru boku czyli dlugosci kwadtatów wynaczonych przez linie gdy mamy np 3 linie to dziela one bok na 4 czesci wiec 9 linii to 10 kwadratów
line_color='#D4AF37'  kolor linii ciemne złoto
LINE_WIDTH=16      szerokosc linii
"""
class Board():
    def __init__(self,size):
        self.size=size
# wpisywanie do listy pól (objektów) na których można klasc kamienie
    def set_fields(self,x,y):
            zmienna = 1
            self.__logical_board = []
            tempRow = []
            for i in range(self.size):
                for j in range(self.size):
                    name = 'object' + str(zmienna)
                    tempRow.append(Field(name,90+(j*90),90+(i*90)))
                    zmienna += 1
                self.__logical_board.append(tempRow)
                tempRow = []
#funkcja do rysowania linii
    tempCoordinates=[]
    def draw_lines(self):
        for i in range(size):
            x = i * 90
            #poziome linie
            pygame.draw.line(screen, line_color, [0, 90 + x], [SIZE, 90 + x], LINE_WIDTH)
            #pionowe linie
            pygame.draw.line(screen, line_color, [90 + x, 0], [90 + x, SIZE], LINE_WIDTH)