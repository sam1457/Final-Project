import pygame
from sys import exit
from random import randint
def display_score():
    current_time = int(pygame.time.get_ticks() /1000) - start_time
    score_surf = test_font.render(f'score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf, score_rect)

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300: screen.blit(Enemy_surf,obstacle_rect)
            else: screen.blit(bird_surf,obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else: return []

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Video Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
game_active = False
start_time = 0


sky_surface = pygame.image.load('graphics/Water.JPG')
sky_surface = pygame.transform.scale(sky_surface, (800, 400))
ground_surface = pygame.image.load('graphics/Ground.png')

Enemy_surf = pygame.image.load('graphics/Aligator.gif')

bird_surf = pygame.image.load('graphics/bird.png')

obstacle_rect_list = []

Stick_Runner = pygame.image.load('graphics/Run.png').convert_alpha()
player_rect = Stick_Runner.get_rect(midbottom=(80, 380))
player_gravity = 0

player_stand = pygame.image.load('graphics/Water.jpg')
player_stand = pygame.transform.scale(player_stand, (800, 400))
player_stand_rect = player_stand.get_rect(center = (400,200))
text_surface = test_font.render('Video Game', False, 'Black')
score_rect = text_surface.get_rect(center=(380, 50))

space_surface = test_font.render('Press Space to Start', False, 'Black')
space_rect = text_surface.get_rect(center=(340, 350))

person_Runner = pygame.image.load('graphics/Run.png').convert_alpha()
person_rect = Stick_Runner.get_rect(midbottom=(400, 300))

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if game_active == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

        if event.type == obstacle_timer and game_active:
            if randint(0,2):
                obstacle_rect_list.append(Enemy_surf.get_rect(bottomright=(randint(900,1100), 100)))
            else:
                obstacle_rect_list.append(bird_surf.get_rect(bottomright=(randint(900, 1000), 300)))


    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 0))
        display_score()

        player_gravity += 2
        player_rect.y += player_gravity
        if player_rect.bottom >= 380: player_rect.bottom = 380
        screen.blit(Stick_Runner, player_rect)

        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        game_active = collisions(player_rect, obstacle_rect_list)

    else:
        screen.fill('grey')
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        screen.blit(text_surface, score_rect)
        screen.blit(space_surface, space_rect)
        screen.blit(person_Runner, person_rect)


    pygame.display.update()
    clock.tick(60)
