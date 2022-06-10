import pygame, sys
from pygame import mixer
import time
import datetime
from game_class import Game
from constants import GAME_TIME_STRING, HUD_SIZE, PLAYER_MOVE_TIME, size, SIZE, PLAYER_ONE_COLOR, PLAYER_TWO_COLOR

mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Baduk')
screen = pygame.display.set_mode((500, 500), 0, 32)

font = pygame.font.SysFont(None, 20)
font2 = pygame.font.SysFont(None, 40)

# play music
mixer.init()
mixer.music.load("mao-zedong-propaganda-music-red-sun-in-the-sky.mp3")  # background music
pop_sound = mixer.Sound("pop.mp3")  # put stone sound
mixer.music.set_volume(0.05)
mixer.music.play(-1)  # -1 czyli infinite loop


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    return textrect


click = False


# MENU
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
    pygame.init()
    screen = pygame.display.set_mode((SIZE, SIZE + HUD_SIZE))
    hud_size = (screen.get_width(), HUD_SIZE)
    hud_surface = pygame.Surface(hud_size)
    game_time_rect = draw_text(GAME_TIME_STRING, font, (255, 255, 255), hud_surface,
                               screen.get_width() / 2 - pygame.font.Font.size(font, GAME_TIME_STRING)[0] / 2, 0)
    pygame.display.set_caption('Baduk')
    screen.blit(bg_img, (0, HUD_SIZE))
    screen.blit(hud_surface, (0, 0))
    game = Game(size)

    white_player_score_literal = f'Biały   {game.players[1].score}'
    black_player_score_literal = f'{game.players[0].score}   Czarny'

    draw_text(white_player_score_literal, font2, (255, 255, 255), hud_surface, 0, 10)
    draw_text(black_player_score_literal, font2, (255, 255, 255), hud_surface,
              screen.get_width() - pygame.font.Font.size(font2, black_player_score_literal)[0], 10)
    pygame.draw.polygon(hud_surface, (255, 255, 255),
                        points=[(game_time_rect.right + 30, 30 - 15 / 2), (game_time_rect.right + 15, 15),
                                (game_time_rect.right + 15, 30)])
    screen.blit(hud_surface, (0, 0))
    game.board.draw_lines(screen, HUD_SIZE, SIZE)
    pygame.display.flip()
    start = int(time.time())
    pygame.time.set_timer(pygame.USEREVENT, 1000)  # sekundnik
    active_player_move_time = PLAYER_MOVE_TIME
    running = True
    while running:
        if game.getActivePlayer().isPassing and game.getInactivePlayer().isPassing and game.gameEnd is False:
            game.gameEnd = True
            game.gameScoreCalculation()
        white_player_score_literal = f'Biały   {game.players[1].score}'
        black_player_score_literal = f'{game.players[0].score}   Czarny'
        draw_text(GAME_TIME_STRING, font, (255, 255, 255), hud_surface,
                  screen.get_width() / 2 - pygame.font.Font.size(font, GAME_TIME_STRING)[0] / 2, 0)
        draw_text(white_player_score_literal, font2, (255, 255, 255), hud_surface, 0, 10)
        draw_text(black_player_score_literal, font2, (255, 255, 255), hud_surface,
                  screen.get_width() - pygame.font.Font.size(font2, black_player_score_literal)[0], 10)
        clock_string = str(datetime.timedelta(seconds=int(time.time()) - start)) if game.gameEnd is False else ""
        clock_rect = draw_text(clock_string, font2, (255, 255, 255), hud_surface,
                               screen.get_width() / 2 - pygame.font.Font.size(font2, clock_string)[0] / 2, 20)
        pygame.display.update(clock_rect)
        if game.getActivePlayer().playerColor == PLAYER_TWO_COLOR:
            poly = pygame.draw.polygon(hud_surface, (255, 255, 255),
                                       points=[(game_time_rect.left - 30, 30 - 15 / 2), (game_time_rect.left - 15, 15),
                                               (game_time_rect.left - 15, 30)]) if game.gameEnd is False else None
            timer_string = str(datetime.timedelta(seconds=active_player_move_time)) if game.gameEnd is False else ""
            timer_rect = draw_text(timer_string, font2, (255, 255, 255), hud_surface,
                                   poly.left - pygame.font.Font.size(font2, timer_string)[0] - 20, 10) if game.gameEnd is False else None
        else:
            poly = pygame.draw.polygon(hud_surface, (255, 255, 255), points=[(game_time_rect.right + 30, 30 - 15 / 2),
                                                                             (game_time_rect.right + 15, 15),
                                                                             (game_time_rect.right + 15, 30)]) if game.gameEnd is False else None
            timer_string = str(datetime.timedelta(seconds=active_player_move_time)) if game.gameEnd is False else ""
            timer_rect = draw_text(timer_string, font2, (255, 255, 255), hud_surface, poly.right + 20, 10) if game.gameEnd is False else None
        screen.blit(hud_surface, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.USEREVENT:
                active_player_move_time -= 1
                if active_player_move_time <= 0 and game.gameEnd is False:
                    game.getActivePlayer().isPassing = True
                    game.playerToggle()
                    pygame.display.flip()
                    mixer.Sound.play(pop_sound)
                    active_player_move_time = PLAYER_MOVE_TIME
                pygame.display.update(timer_rect) if game.gameEnd is False else None
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN and game.gameEnd is False:
                x, y = pygame.mouse.get_pos()
                if event.button == 1:
                    # lewy przycisk
                    correctXCoord, correctYCoord, boardX, boardY = game.getActivePlayer().makeMove(x, y)
                    if correctXCoord == -1 and correctYCoord == -1 and boardX == -1 and boardY == -1:
                        continue
                    active_player_move_time = PLAYER_MOVE_TIME
                    mixer.Sound.play(pop_sound)
                    game.board.drawStone(screen, game.getActivePlayer().playerColor, correctXCoord, correctYCoord)
                    game.getActivePlayer().createGroups()
                    game.clearFieldChecks()
                    game.getInactivePlayer().updateGroups()
                    game.playerToggle()
                    pygame.display.flip()
        hud_surface.fill((0, 0, 0))


main_menu()
