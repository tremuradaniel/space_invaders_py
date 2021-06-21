"""
Randaom library
"""
import random
"""
Pygame is a set of Python modules designed for writing games.
"""
import pygame
import math

from player.Player import Player

from pygame import mixer

class Game:

  gameIsRunning = True

  def startGame(self):
    # initialize pygame
    pygame.init()
    self.setUpGame()

  def setUpGame(self):
    self.createScreen()
    self.setGameBarContent()
    self.initializeSound()
    self.initializeScore()
    self.initializePlayer(Player(pygame))
    self.runGame()

  def displayPlayer(self):
    self.screen.blit(
        self.player.playerImg, 
        (self.player.player_x, self.player.player_y)
      )

  def initializePlayer(self, player):
    self.setPlayer(player)
    self.player.setInitialPosition(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

  def setPlayer(self, player):
    self.player = player

  def initializeScore(self):
    self.score_value = 0
    self.text_x = 10
    self.text_y = 10
    self.font = pygame.font.Font('freesansbold.ttf', 32)

  def showScore(self, x, y):
    self.score = self.font.render("Score : " + str(self.score_value), True, (255, 255, 255))
    self.screen.blit(self.score, (x, y))

  def createScreen(self):
    # create the screen
    self.SCREEN_WIDTH = 900
    self.SCREEN_HEIGHT = 900
    self.BACKGROUND_COLOR = (23, 23, 100) # rgb
    self.BACKGROUND_IMAGE = pygame.image.load('resources/background.png')
    self.BACKGRROUND_IMAGE_RESIZED = pygame.transform.scale(self.BACKGROUND_IMAGE, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
    self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
  
  def initializeSound(self):
     # other sound effects
    self.EXPLOSION_SOUND = mixer.Sound('resources/explosion.wav')
    self.BULLET_SOUND = mixer.Sound('resources/laser.wav')
    # background sound
    mixer.music.load('resources/background.wav')
    self.PLAY_MUSIC_ON_LOOP = -1
    mixer.music.play(self.PLAY_MUSIC_ON_LOOP)
  
  def setGameBarContent(self):
    # Title and icon
    pygame.display.set_caption("Space Invaders")
    self.icon = pygame.image.load('resources/ufo.png')
    pygame.display.set_icon(self.icon)

  def closeGameWindowUponXClick(self, event):
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()

  def runGame(self):
    print('in runGame')
    while self.gameIsRunning:
      # screen.fill(BACKGROUND_COLOR)
      self.screen.blit(self.BACKGRROUND_IMAGE_RESIZED, (0, 0))
      
      for event in pygame.event.get():
        self.closeGameWindowUponXClick(event)
      #     if event.type == pygame.QUIT:
      #         RUNNING = False

      #     # if keystroke is presed check if whether its right or left
      #     if event.type == pygame.KEYDOWN:
      #         if event.key == pygame.K_LEFT:
      #             self.player_x_change = -STEP
      #         if event.key == pygame.K_RIGHT:
      #             self.player_x_change = STEP
      #         if event.key == pygame.K_SPACE:
      #             if bullet_state is 'ready':
      #                 bullet_x = player_x
      #                 fire_bullet(bullet_x, bullet_y)
      #                 BULLET_SOUND.play()
      #     if event.type == pygame.KEYUP:
      #         if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
      #             self.player_x_change = 0
      # self.player_x += self.player_x_change

      # if self.player_x <= 0:
      #     self.player_x = 0
      # elif self.player_x >= RIGHT_OUT_OF_BOUNDS:
      #     self.player_x = RIGHT_OUT_OF_BOUNDS
          
      # for i in range(self.NUM_OF_ENEMIES):
      #     # print('player_y', player_y)
      #     # if DEBUGGING: print('enemies_y[0]', enemies_y[i])
      #     # if DEBUGGING: print('Y_BOTTOM_OF_SCREEN * 100 / 10[0]', Y_BOTTOM_OF_SCREEN - 10)
      #     # print ('enemies_y[i]', enemies_y[0])
      #     # (end2 >= start1) && (start2 <= end1)
      #     self.determinePlayerIsHit()
      #     # Enemy Movement
      #     self.generateEnemyMovement()
      #     # collision
      #     # enemyIsHit = isHit(enemies_x[i], enemies_y[i], bullet_x, bullet_y)
      #     enemyIsHit = self.areCollided(self.enemies_x[i], self.enemies_y[i], self.bullet_x,self.bullet_y, [self.ENEMY_IMG_WIDTH, self.ENEMY_IMG_HEIGHT], [PLAYER_IMG_WIDTH, PLAYER_IMG_HEIGHT])
      #     if self.enemyIsHit and not self.game_over:
      #         print('enemy hit')
      #         self.EXPLOSION_SOUND.play()
      #         self.bullet_y = self.player_y
      #         self.bullet_state = 'ready'
      #         self.score_value += 1
      #         self.enemies_x[i] = random.randint(0, self.SCREEN_WIDTH - self.ENEMY_IMG_WIDTH)
      #         self.enemies_y[i] = self.Y_ENEMY_TOP_OF_SCREEN

      #     self.enemy(self.enemies_x[i], self.enemies_y[i], 1)
      #     self.enemy(self.enemies_x[0], self.enemies_y[0], 0)

      # if self.game_over:
      #     self.game_over_text()

      # # bullet movement
      # if self.bullet_y <= 0:
      #     self.bullet_y = self.player_y
      #     self.bullet_state = 'ready'
      # if self.bullet_state is 'fire':
      #     self.fire_bullet(self.bullet_x, self.bullet_y)
      #     self.bullet_y -= self.BULLET_Y_STEP

      self.displayPlayer()
      self.showScore(self.text_x, self.text_y)
      pygame.display.update()