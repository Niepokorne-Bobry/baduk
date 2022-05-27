import pygame
size=9
SIZE=(size*90)+90
#Obrazy
bg_img = pygame.image.load("smoczek_tlo.png")
bg_img = pygame.transform.scale(bg_img,(SIZE,SIZE))
#BG_COLOR = (50, 170, 156)
pygame.init()
screen = pygame.display.set_mode((SIZE,SIZE))
pygame.display.set_caption('Baduk')
screen.blit(bg_img,(0,0))
pygame.display.flip()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False





