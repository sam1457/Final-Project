import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
#img = pygame.image.load('Week8Lab.PNG')    Change the Icon of the tab
#pygame.display.set_icon(img)
pygame.display.set_caption('RUN Preacher RUN')
clock = pygame.time.Clock()

sky_surface = pygame.image.load('graphics/Water.JPG')
ground_surface = pygame.image.load('graphics/Ground.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 0))

    pygame.display.update()
    clock.tick(60)

