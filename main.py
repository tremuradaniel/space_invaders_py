"""
Randaom library
"""
import random
"""
Pygame is a set of Python modules designed for writing games.
"""
import pygame


# initialize pygame
pygame.init()

# create the screen
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
BACKGROUND_COLOR = (23, 23, 100) # rgb
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('resources/ufo.png')
pygame.display.set_icon(icon)

"""
    PLAYER
"""
playerImg = pygame.image.load('resources/player.png')
PLAYER_IMG_WIDTH = playerImg.get_rect().size[0]
# setting initial position
X_MIDDLE_OF_SCREEN = int (SCREEN_WIDTH / 2 - PLAYER_IMG_WIDTH / 2)
player_x = X_MIDDLE_OF_SCREEN
Y_BOTTOM_OF_SCREEN = 90 * SCREEN_HEIGHT / 100
player_y = Y_BOTTOM_OF_SCREEN

# unit of motion
STEP = 0.3
player_x_change = 0
player_y_change = 0

"""
    ENEMY
"""
enemyImg = pygame.image.load('resources/enemy.png')
ENEMY_IMG_WIDTH = playerImg.get_rect().size[0]

# setting initial position
enemy_x = random.randint(0, SCREEN_WIDTH - ENEMY_IMG_WIDTH)
Y_ENEMY_TOP_OF_SCREEN = 10 * SCREEN_HEIGHT / 100
enemy_y = Y_ENEMY_TOP_OF_SCREEN
enemy_direction = 1
ENEMY_STEP = 0.3
ENEMY_STEP_DOWN = 40


RIGHT_OUT_OF_BOUNDS = SCREEN_WIDTH - PLAYER_IMG_WIDTH
ENEMY_RIGHT_OUT_OF_BOUNDS = SCREEN_WIDTH - ENEMY_IMG_WIDTH

def player(player_x, player_y):
    """    draw player    """
    screen.blit(playerImg, (player_x, player_y))

def enemy(enemy_x, enemy_y):
    """    draw player    """
    screen.blit(enemyImg, (enemy_x, enemy_y))

RUNNING = True

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

        # if keystroke is presed check if whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -STEP
            if event.key == pygame.K_RIGHT:
                player_x_change = STEP
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
    player_x += player_x_change

    if player_x <= 0:
        player_x = 0
    elif player_x >= RIGHT_OUT_OF_BOUNDS:
        player_x = RIGHT_OUT_OF_BOUNDS

    # Enemy Movement
    enemy_x += ENEMY_STEP * enemy_direction
    if enemy_x <= 0:
        enemy_y += ENEMY_STEP_DOWN
        enemy_direction = 1
    elif enemy_x >= ENEMY_RIGHT_OUT_OF_BOUNDS:
        enemy_direction = -1
        enemy_y += ENEMY_STEP_DOWN

    screen.fill(BACKGROUND_COLOR)


    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    pygame.display.update()
