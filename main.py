import pygame, sys
from pygame import mixer
from game_class import Game
from constants import size, SIZE, PLAYER_ONE_COLOR, PLAYER_TWO_COLOR

mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Baduk')
screen = pygame.display.set_mode((500, 500), 0, 32)

font = pygame.font.SysFont(None, 20)

#play music
mixer.init()
mixer.music.load("mao-zedong-propaganda-music-red-sun-in-the-sky.mp3") #background music
pop_sound = mixer.Sound("pop.mp3") #put stone sound
mixer.music.set_volume(0.5)
mixer.music.play(-1) # -1 czyli infinite loop

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False
#MENU
def main_menu():
    while True:
        screen.fill((0, 0, 0))
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                mixer.Sound.play(pop_sound)
                game()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)
def game():
    bg_img = pygame.image.load("smoczek_tlo.png")
    bg_img = pygame.transform.scale(bg_img, (SIZE, SIZE))
    BG_COLOR = (50, 170, 156)
    pygame.init()
    screen = pygame.display.set_mode((SIZE, SIZE))
    pygame.display.set_caption('Baduk')
    screen.blit(bg_img, (0, 0))
    # screen.fill(BG_COLOR)
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
                    # lewy przycisk
                    correctXCoord, correctYCoord, boardX, boardY = game.getActivePlayer().makeMove(x, y)
                    if correctXCoord == -1 and correctYCoord == -1 and boardX == -1 and boardY == -1:
                        continue
                    mixer.Sound.play(pop_sound)
                    game.board.drawStone(screen, game.getActivePlayer().playerColor, correctXCoord, correctYCoord)
                    game.playerToggle()
                pygame.display.flip()
main_menu()