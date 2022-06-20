import os
import pygame, sys
from pygame import mixer
import time
import datetime
from enums.field_types import FieldTypes
from game_class import Game
from constants import *

mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Baduk')

screen = pygame.display.set_mode((MENU_WIDTH, MENU_HEIGHT), 0, 32)

icon = pygame.image.load(os.path.join("assets/images", "emperor.png"))
pygame.display.set_icon(icon)


font = pygame.font.SysFont(None, 20)
font2 = pygame.font.SysFont(None, 40)

# play music
mixer.init()
mixer.music.load(
    os.path.join("assets/sounds", "mao-zedong-propaganda-music-red-sun-in-the-sky.mp3"))  # background music
pop_sound = mixer.Sound(os.path.join("assets/sounds", "pop.mp3"))  # put stone sound
mixer.music.set_volume(0.05)
mixer.music.play(-1)  # -1 czyli infinite loop


# przycisk
def button(screen, position, text, size, colors="white on blue"):
    fg, bg = colors.split(" on ")
    font = pygame.font.SysFont("Arial", size)
    text_render = font.render(text, 1, fg)
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w, y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)

    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
    pygame.draw.rect(screen, bg, (x, y, w, h))
    
    return screen.blit(text_render, (x, y))


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    return textrect




# MENU
def main_menu(surface):
    click = False
    isMuted = False
    inputActive = False
    text = ""
    textRect = None
    playerMoveTime = -1
    while True:
        menu_img = pygame.image.load(os.path.join("assets/images","menu2_smoczek.png"))
        menu_img = pygame.transform.scale(menu_img, (800, 600))

        # wyjebanie hud size
        screen.blit(menu_img, (0, 0))
        draw_text('', font, (255, 255, 255), screen, 20, 20)
        mx, my = pygame.mouse.get_pos()
        button_1 = button(screen, (360, 100), "PLAY", 30, "black on yellow")
        button_2 = button(screen, (360, 200), "QUIT", 30, "black on yellow")
        button_3 = button(screen, (349,300),"SOUND",30,"black on yellow");
        draw_text("Write player move time (in seconds)",font,WHITE,screen,290,380)
        input_box = pygame.Rect(349,400, 100, 30)
        pygame.draw.rect(screen,"yellow",input_box)

        # button_1 = pygame.Rect(150, 150, 200, 50)
        # button_2 = pygame.Rect(150, 250, 200, 50)

        if button_1.collidepoint(pygame.mouse.get_pos()):
            if click:
                mixer.Sound.play(pop_sound)
                game(playerMoveTime)
                surface = pygame.display.set_mode((MENU_WIDTH,MENU_HEIGHT), 0, 32)
        if button_2.collidepoint(pygame.mouse.get_pos()):
            if click:
                pygame.quit()
                sys.exit()
        if button_3.collidepoint(pygame.mouse.get_pos()):
            if click:
                if isMuted is False:
                    mixer.music.set_volume(0)
                    isMuted = True
                else:
                    mixer.music.set_volume(0.05)
                    isMuted = False
        if input_box.collidepoint(pygame.mouse.get_pos()):
            if click:
                isActive = True
                print(isActive)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if isActive:
                    if event.key == K_RETURN:
                        active = False
                        try:
                            playerMoveTime = int(text)
                            print(playerMoveTime)
                        except:
                            text = ""
                            pass
                    elif event.key == K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        textRect = draw_text(text, font, BLACK, screen, 349, 400)
        pygame.display.update()
        mainClock.tick(FPS)



def end_menu(game):
    click = False
    surface = pygame.display.set_mode((MENU_WIDTH,MENU_HEIGHT), 0, 32)
    while True:
        end_menu_img = pygame.image.load(os.path.join("assets/images","menu2_smoczek.png"))
        end_menu_img = pygame.transform.scale(end_menu_img, (800, 600))
        screen.blit(end_menu_img, (0, 0))
        draw_text('', font, WHITE, screen, 20, 20)
        score_string = f"White {game.players[1].score} - {game.players[0].score} Black"
        ret_btn_txt = "Return to main menu"
        draw_text(score_string,font2,WHITE,screen,screen.get_width()/2
                                -pygame.font.Font.size(font2,score_string)[0]/2,
                                100)
        button_1 = button(screen, (screen.get_width()/2
                                -pygame.font.Font.size(font,"Return to main menu")[0]+20, 200), ret_btn_txt, 30, "black on yellow")
        if button_1.collidepoint(pygame.mouse.get_pos()):
            if click:
                mixer.Sound.play(pop_sound)
                return myQUIT
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


def game(playerMoveTime):
    bg_img = pygame.image.load(os.path.join("assets/images", "smoczek_tlo.png"))
    bg_img = pygame.transform.scale(bg_img, (SIZE, SIZE))

    playerTime = 15

    # inicjalizacja pygame i glownego surface
    pygame.init()
    screen = pygame.display.set_mode((SIZE, SIZE + HUD_SIZE + PLAYER_BUTTONS_SECTION_SIZE))

    # inicjalizacja surface gornego i dolnego paska informacji
    hud_surface = screen.subsurface((0, 0), (SIZE, HUD_SIZE))
    buttons_section_surface = screen.subsurface((0, SIZE + HUD_SIZE), (SIZE, PLAYER_BUTTONS_SECTION_SIZE))

    pygame.display.set_caption('Baduk')
    screen.blit(bg_img, (0, HUD_SIZE))

    # inicjalizacja gry
    game = Game(size)
    game.board.draw_lines(screen, HUD_SIZE, SIZE)
    pygame.display.flip()

    # inicjalizacja timera
    start = int(time.time())
    pygame.time.set_timer(pygame.USEREVENT, 1000)  # sekundnik
    if playerMoveTime == -1:
        playerTime = PLAYER_MOVE_TIME
    else:
        playerTime = playerMoveTime

    pass_button = pygame.Rect(SIZE / 2 - SIZE / 4, BUTTON_SECTION_POS_Y + PLAYER_BUTTONS_SECTION_SIZE * 0.25, SIZE / 4,
                              SIZE / 2)
    surr_button = pygame.Rect(pass_button.right + 50, BUTTON_SECTION_POS_Y + PLAYER_BUTTONS_SECTION_SIZE * 0.25,
                              SIZE / 4, SIZE / 2)

    running = True
    while running:
        if game.getActivePlayer().isPassing and game.getInactivePlayer().isPassing and game.gameEnd is False:
            game.gameEnd = True
            game.gameScoreCalculation()
            hud_surface.fill(BLACK)
            buttons_section_surface.fill(BLACK)
            draw_buttons_section(buttons_section_surface, WHITE, RED, RED, playerTime,
                                 pygame.mouse.get_pos())
            draw_hud(game, hud_surface, start)
            pygame.display.flip()
        
        if game.gameEnd == True:
            ret = end_menu(game)
            if ret == 0:
                running = False

        if game.gameEnd is False:
            hud_surface.fill(BLACK)
            buttons_section_surface.fill(BLACK)
            # rysowanie gornego i dolnego paska informacji, przyciskow itp.
            draw_hud(game, hud_surface, start)
            draw_buttons_section(buttons_section_surface, WHITE, RED, RED_HOVERED, playerTime,
                                 pygame.mouse.get_pos())

            # odswiezanie paskow (x, y), (width, height)
            pygame.display.update([(buttons_section_surface.get_abs_offset(), (SIZE, PLAYER_BUTTONS_SECTION_SIZE)),
                                   # buttons_section subsurface coords
                                   (hud_surface.get_abs_offset(), (SIZE, HUD_SIZE))])  # hud subsurface coords

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.USEREVENT:
                playerTime -= 1
                if playerTime <= 0 and game.gameEnd is False:
                    game.getActivePlayer().isPassing = True
                    game.playerToggle()
                    mixer.Sound.play(pop_sound)
                    if playerMoveTime == -1:
                        playerTime = PLAYER_MOVE_TIME
                    else:
                        playerTime = playerMoveTime

            if event.type == pygame.MOUSEBUTTONDOWN and game.gameEnd is False:
                x, y = pygame.mouse.get_pos()
                if event.button == 1:
                    # lewy przycisk
                    if pass_button.collidepoint((x, y)):
                        game.getActivePlayer().isPassing = True
                        mixer.Sound.play(pop_sound)
                        active_player_move_time = playerTime
                        game.playerToggle()
                    elif surr_button.collidepoint((x, y)):
                        game.gameEnd = True
                        game.gameScoreCalculation()
                        hud_surface.fill(BLACK)
                        draw_hud(game, hud_surface, start)
                        draw_buttons_section(buttons_section_surface, WHITE, RED, RED_HOVERED, playerTime,
                                             pygame.mouse.get_pos())
                        pygame.display.flip()
                    else:
                        correctXCoord, correctYCoord, boardX, boardY = game.getActivePlayer().makeMove(x, y)
                        if correctXCoord == -1 and correctYCoord == -1 and boardX == -1 and boardY == -1:
                            continue
                        playerTime = playerMoveTime
                        mixer.Sound.play(pop_sound)
                        game.getActivePlayer().createGroups()
                        game.clearFieldChecks()
                        game.getInactivePlayer().updateGroups()
                        game.playerToggle()
                        draw_board(game, screen, bg_img)
                        pygame.display.flip()


def draw_board(game, surface, background):
    surface.blit(background, (0, HUD_SIZE))
    game.board.draw_lines(screen, HUD_SIZE, SIZE)

    for row in game.board.fields:
        for field in row:
            if field.fieldType == FieldTypes.PLAYER_1_STONE:
                game.board.drawStone(surface, BLACK, field.getCoords())
            elif field.fieldType == FieldTypes.PLAYER_2_STONE:
                game.board.drawStone(surface, WHITE, field.getCoords())


def draw_score(game, surface):
    white_player_score_literal = f'Biały   {game.players[1].score}'
    black_player_score_literal = f'{game.players[0].score}   Czarny'
    draw_text(GAME_TIME_STRING, font, WHITE, surface,
              screen.get_width() / 2 - pygame.font.Font.size(font, GAME_TIME_STRING)[0] / 2, 0)
    draw_text(white_player_score_literal, font2, WHITE, surface, 0, 10)
    draw_text(black_player_score_literal, font2, WHITE, surface,
              screen.get_width() - pygame.font.Font.size(font2, black_player_score_literal)[0], 10)


def draw_clock(surface, beginning_time):
    clock_string = str(datetime.timedelta(seconds=int(time.time()) - beginning_time))
    return draw_text(clock_string, font2, WHITE, surface,
                     screen.get_width() / 2 - pygame.font.Font.size(font2, clock_string)[0] / 2, 20)


def draw_turn_pointer(game, surface, relative_item):
    if game.getActivePlayer().playerColor == PLAYER_TWO_COLOR:
        poly = pygame.draw.polygon(surface, WHITE,
                                   points=[(relative_item.left - 30, 30 - 15 / 2), (relative_item.left - 15, 15),
                                           (relative_item.left - 15, 30)])
    else:
        poly = pygame.draw.polygon(surface, WHITE,
                                   points=[(relative_item.right + 30, 30 - 15 / 2),
                                           (relative_item.right + 15, 15),
                                           (relative_item.right + 15, 30)])
    return poly


def draw_buttons_section(surface, text_color, button_color, button_color_clicked, active_player_move_time, mouse_pos):
    pass_text = font2.render("Pasuj", 1, text_color)
    surr_text = font2.render("Poddanie", 1, text_color)
    surface_width = surface.get_width()
    surface_height = surface.get_height()
    buttons_width = surface_width / 4
    buttons_height = surface_height / 2
    pass_button = pygame.draw.rect(surface, button_color,
                                   [surface_width / 2 - buttons_width / 2, surface_height * 0.25, buttons_width,
                                    buttons_height], 0, 15)
    surrender_button = pygame.draw.rect(surface, button_color,
                                        [pass_button.right + 50, surface_height * 0.25, buttons_width, buttons_height],
                                        0, 15)
    # koordynaty myszki z uwzglednionym offsetem macierzystej powierzchni
    x = mouse_pos[0]
    y = mouse_pos[1] - BUTTON_SECTION_POS_Y

    if pass_button.collidepoint((x, y)):
        pass_button = pygame.draw.rect(surface, button_color_clicked,
                                       [surface_width / 2 - buttons_width / 2, surface_height * 0.25, buttons_width,
                                        buttons_height], 0, 15)
    if surrender_button.collidepoint((x, y)):
        surrender_button = pygame.draw.rect(surface, button_color_clicked,
                                            [pass_button.right + 50, surface_height * 0.25, buttons_width,
                                             buttons_height], 0, 15)
    surface.blit(pass_text, (pass_button.center[0] - pygame.font.Font.size(font2, "Pasuj")[0] / 2,
                             pass_button.center[1] - pygame.font.Font.size(font2, "Pasuj")[1] / 2))
    surface.blit(surr_text, (surrender_button.center[0] - pygame.font.Font.size(font2, "Poddanie")[0] / 2,
                             surrender_button.center[1] - pygame.font.Font.size(font2, "Poddanie")[1] / 2))

    title_rect = draw_text("Czas na wykonanie ruchu", font, text_color, surface, 50, surface_height * 0.25)

    timer_string = str(datetime.timedelta(seconds=active_player_move_time))
    draw_text(timer_string, font2, WHITE, surface, title_rect.left, title_rect.bottom)


def draw_hud(game, surface, beginning_time):
    game_time_rect = draw_text(GAME_TIME_STRING, font, WHITE, surface,
                               screen.get_width() / 2 - pygame.font.Font.size(font, GAME_TIME_STRING)[0] / 2, 0)
    draw_score(game, surface)
    draw_clock(surface, beginning_time)
    draw_turn_pointer(game, surface, game_time_rect)



main_menu(screen)

