"""
Pygame is a set of Python modules designed for writing games.
"""
import pygame

# initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((500, 500))

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('resources/ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('resources/player.png')
playerImgWidth = playerImg.get_rect().size[0]
PLAYER_X = int (250 - playerImgWidth / 2)
PLAYER_Y = 370

def player():
    """    draw player    """
    screen.blit(playerImg, (PLAYER_X, PLAYER_Y))

RUNNING = True

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    screen.fill((23, 23, 100))
    player()
    pygame.display.update()
