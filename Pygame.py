import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))

# img = pygame.image.load('Week8Lab.PNG')    Change the Icon of the tab
# pygame.display.set_icon(img)

pygame.display.set_caption('Video Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

text_surface = test_font.render('Video Game', False, 'Black')
score_rect = text_surface.get_rect(center = (400, 50))

sky_surface = pygame.image.load('graphics/Water.JPG')
sky_surface = pygame.transform.scale(sky_surface, (800, 400))
ground_surface = pygame.image.load('graphics/Ground.png')

#bird_enemy = pygame.image.load('graphics/bird.png').convert_alpha()
#bird_rect = bird_enemy.get_rect(topright = (80, 390))

Enemy_surf = pygame.image.load('graphics/Aligator.gif').convert()
Enemy_rect = Enemy_surf.get_rect(bottomright = (80, 390))

Stick_Runner = pygame.image.load('graphics/Run.png').convert_alpha()
player_rect = Stick_Runner.get_rect(midbottom=(80, 380))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos):
                player_gravity = -20
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_gravity = -20

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 0))
    screen.blit(text_surface, score_rect)

    #bird_rect.x -= 4
    #if bird_rect.right <= 0: Enemy_rect.left = 800
    #screen.blit(bird_enemy, bird_rect)


    Enemy_rect.x -= 4
    if Enemy_rect.right <= 0: Enemy_rect.left = 800
    screen.blit(Enemy_surf, Enemy_rect)

    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 380: player_rect.bottom = 380
    screen.blit(Stick_Runner, player_rect)



    pygame.display.update()
    clock.tick(60)
