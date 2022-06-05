import pygame
from game_class import Game
from constants import size, SIZE, PLAYER_ONE_COLOR, PLAYER_TWO_COLOR
# Obrazy
bg_img = pygame.image.load("smoczek_tlo.png")
bg_img = pygame.transform.scale(bg_img, (SIZE, SIZE))
BG_COLOR = (50, 170, 156)
pygame.init()
screen = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption('Baduk')
screen.blit(bg_img, (0, 0))
#screen.fill(BG_COLOR)
game = Game(size)
game.board.draw_lines(screen, SIZE)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if event.button == 1:
                #lewy przycisk
                game.player1.makeMove(x,y)
                game.board.drawStone(screen, PLAYER_ONE_COLOR, x, y)
            elif event.button == 3:
                #prawy przycisk
                game.board.rightclickdraw(screen, PLAYER_ONE_COLOR, x, y)
            pygame.display.flip()
            """
            elif event.button == 2:
                #srodkowy przycisk
            elif event.button == 4:
                print("mouse wheel up")
            elif event.button == 5:
                print("mouse wheel down")
            """

