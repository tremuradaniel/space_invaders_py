import pygame

# initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((500, 500))

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('resources/ufo.png')
pygame.display.set_icon(icon)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((23, 23, 100))
    pygame.display.update()