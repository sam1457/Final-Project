import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
#img = pygame.image.load('Week8Lab.PNG')    Change the Icon of the tab
#pygame.display.set_icon(img)
pygame.display.set_caption('RUN Preacher RUN')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()

