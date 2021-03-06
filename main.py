"""
Randaom library
"""
import random
"""
Pygame is a set of Python modules designed for writing games.
"""
import pygame
import math

from pygame import mixer

# initialize pygame
pygame.init()

# create the screen
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
BACKGROUND_COLOR = (23, 23, 100) # rgb
BACKGROUND_IMAGE = pygame.image.load('resources/background.png')
BACKGRROUND_IMAGE_RESIZED = pygame.transform.scale(BACKGROUND_IMAGE, (SCREEN_WIDTH, SCREEN_HEIGHT))
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# background sound
mixer.music.load('resources/background.wav')
PLAY_MUSIC_ON_LOOP = -1
mixer.music.play(PLAY_MUSIC_ON_LOOP)

# other sound effects
EXPLOSION_SOUND = mixer.Sound('resources/explosion.wav')
BULLET_SOUND = mixer.Sound('resources/laser.wav')

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
STEP = 2
player_x_change = 0
player_y_change = 0

"""
    ENEMY
"""
enemiesImg = []
enemies_x = []
enemies_y = []
enemies_direction = []
NUM_OF_ENEMIES = 6
Y_ENEMY_TOP_OF_SCREEN = 10 * SCREEN_HEIGHT / 100
ENEMY_IMG_WIDTH = 0

for i in range(NUM_OF_ENEMIES):
    enemiesImg.append(pygame.image.load('resources/enemy.png'))
    # setting initial position
    ENEMY_IMG_WIDTH = enemiesImg[i].get_rect().size[0]
    enemies_x.append(random.randint(0, SCREEN_WIDTH - ENEMY_IMG_WIDTH))
    enemies_y.append(Y_ENEMY_TOP_OF_SCREEN)
    enemies_direction.append(1)

ENEMY_STEP = 4
ENEMY_STEP_DOWN = 90


"""
    BULLET
"""
bulletImg = pygame.image.load('resources/bullet.png')
bullet_x = 0
bullet_y = player_y
BULLET_X_STEP = 4
BULLET_Y_STEP = 10
bullet_state = 'ready'

RIGHT_OUT_OF_BOUNDS = SCREEN_WIDTH - PLAYER_IMG_WIDTH
ENEMY_RIGHT_OUT_OF_BOUNDS = SCREEN_WIDTH - ENEMY_IMG_WIDTH

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

text_x = 10
text_y = 10

# Game Over text
over_font = pygame.font.Font('freesansbold.ttf', 64)
game_over = False

def game_over_text():
    over_text = font.render("GAME OVER!", True, (255, 255, 255))
    screen.blit(over_text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def player(player_x, player_y):
    """    draw player    """
    screen.blit(playerImg, (player_x, player_y))

def enemy(enemy_x, enemy_y, i):
    """    draw enemy    """
    screen.blit(enemiesImg[i], (enemy_x, enemy_y))

def fire_bullet(bullet_coord_x, bullet_coord_y):
    global bullet_state
    bullet_state = 'fire'
    bullet_above_player_x = bullet_coord_y + 10
    bullet_above_player_y = bullet_coord_x + 16
    screen.blit(bulletImg, (bullet_above_player_y, bullet_above_player_x))

def isCollision(enemy_x, enemy_y, bullet_x, bullet_y):
    power_diff_xs = math.pow(enemy_x - bullet_x, 2)
    power_diff_ys = math.pow(enemy_y - bullet_y, 2)
    distance = math.sqrt(power_diff_xs + power_diff_ys)
    return distance < 27

RUNNING = True

while RUNNING:
    # screen.fill(BACKGROUND_COLOR)
    screen.blit(BACKGRROUND_IMAGE_RESIZED, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

        # if keystroke is presed check if whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -STEP
            if event.key == pygame.K_RIGHT:
                player_x_change = STEP
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)
                    BULLET_SOUND.play()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
    player_x += player_x_change

    if player_x <= 0:
        player_x = 0
    elif player_x >= RIGHT_OUT_OF_BOUNDS:
        player_x = RIGHT_OUT_OF_BOUNDS
        
    for i in range(NUM_OF_ENEMIES):
        # Game Over
        # print('player_y', player_y)
        print('enemies_y[0]', enemies_y[i])
        print('Y_BOTTOM_OF_SCREEN * 100 / 10[0]', Y_BOTTOM_OF_SCREEN - 10)
        if enemies_y[i] >= player_y and (int (enemies_x[i] + ENEMY_IMG_WIDTH) >= player_x) and not game_over:
            game_over = True
            EXPLOSION_SOUND.play(3)
            for j in range(NUM_OF_ENEMIES):
                enemies_y[j] = 2000
            break
        # Enemy Movement
        enemies_x[i] += ENEMY_STEP * enemies_direction[i]
        if enemies_x[i] <= 0:
            enemies_y[i] += ENEMY_STEP_DOWN
            enemies_direction[i] = 1
        elif enemies_x[i] >= ENEMY_RIGHT_OUT_OF_BOUNDS:
            enemies_direction[i] = -1
            enemies_y[i] += ENEMY_STEP_DOWN

        # collision
        collision = isCollision(enemies_x[i], enemies_y[i], bullet_x, bullet_y)
        if collision and not game_over:
            EXPLOSION_SOUND.play()
            bullet_y = player_y
            bullet_state = 'ready'
            score_value += 1
            enemies_x[i] = random.randint(0, SCREEN_WIDTH - ENEMY_IMG_WIDTH)
            enemies_y[i] = Y_ENEMY_TOP_OF_SCREEN

        enemy(enemies_x[i], enemies_y[i], 1)
        enemy(enemies_x[0], enemies_y[0], 0)

    if game_over:
        game_over_text()

    # bullet movement
    if bullet_y <= 0:
        bullet_y = player_y
        bullet_state = 'ready'
    if bullet_state is 'fire':
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= BULLET_Y_STEP

    player(player_x, player_y)
    
    show_score(text_x, text_y)
    pygame.display.update()
