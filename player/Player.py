class Player:

  # unit of motion
  STEP = 2
  player_x_change = 0
  player_y_change = 0

  def __init__(self, pygame):
    self.pygame = pygame
    self.playerImg = self.pygame.image.load('resources/player.png')
    self.PLAYER_IMG_WIDTH = self.playerImg.get_rect().size[0]
    self.PLAYER_IMG_HEIGHT = self.playerImg.get_rect().size[1]

  def setInitialPosition(self, screenWidth, screenHeight):
    X_MIDDLE_OF_SCREEN = int (screenWidth / 2 - self.PLAYER_IMG_WIDTH / 2)
    self.player_x = X_MIDDLE_OF_SCREEN
    Y_BOTTOM_OF_SCREEN = 90 * screenHeight / 100
    self.player_y = Y_BOTTOM_OF_SCREEN
