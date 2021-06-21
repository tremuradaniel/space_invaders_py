from game import Game
gameSession = Game()
# initialize pygame
gameSession.startGame()

# # Game Over text
# over_font = pygame.font.Font('freesansbold.ttf', 64)
# game_over = False

# def game_over_text():
#     over_text = font.render("GAME OVER!", True, (255, 255, 255))
#     screen.blit(over_text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

# def show_score(x, y):
#     score = font.render("Score : " + str(score_value), True, (255, 255, 255))
#     screen.blit(score, (x, y))

# def player(player_x, player_y):
#     """    draw player    """
#     screen.blit(playerImg, (player_x, player_y))

# def enemy(enemy_x, enemy_y, i):
#     """    draw enemy    """
#     screen.blit(enemiesImg[i], (enemy_x, enemy_y))

# def fire_bullet(bullet_coord_x, bullet_coord_y):
#     global bullet_state
#     bullet_state = 'fire'
#     bullet_above_player_x = bullet_coord_y + 10
#     bullet_above_player_y = bullet_coord_x + 16
#     screen.blit(bulletImg, (bullet_above_player_y, bullet_above_player_x))

# def isHit(enemy_x, enemy_y, bullet_x, bullet_y):
#     power_diff_xs = math.pow(enemy_x - bullet_x, 2)
#     power_diff_ys = math.pow(enemy_y - bullet_y, 2)
#     distance = math.sqrt(power_diff_xs + power_diff_ys)
#     return distance < 1

# def areCollided (objectAx, objectAy, objectBx, objectBy, objectASize, objectBSize):
#     aObjWidth = objectASize[0]
#     aObjHeight = objectASize[1]
#     bObjWidth = objectBSize[0]
#     bObjHeight = objectBSize[1]
#     xAxisSuperposition = objectAx < objectBx + bObjWidth and objectAx + aObjWidth > objectBx
#     yAxisSuperposition = objectAy < objectBy + bObjHeight and objectAy + aObjHeight > objectBy
#     if (xAxisSuperposition and yAxisSuperposition):
#         return True

# def generateEnemyMovement():
#     enemies_x[i] += ENEMY_STEP * enemies_direction[i]
#     if enemies_x[i] <= 0:
#         enemies_y[i] += ENEMY_STEP_DOWN
#         enemies_direction[i] = 1
#     elif enemies_x[i] >= ENEMY_RIGHT_OUT_OF_BOUNDS:
#         enemies_direction[i] = -1
#         enemies_y[i] += ENEMY_STEP_DOWN

# def determinePlayerIsHit():
#     global game_over
#     # ENEMY_STARTS = enemies_x[i]
#     # ENEMY_ENDS = enemies_x[i] + ENEMY_IMG_WIDTH
#     # PLAYER_STARTS =  player_x
#     # PLAYER_ENDS = player_x + PLAYER_IMG_WIDTH
#     # playerIsHit = isHit(enemies_x[i], enemies_y[i], player_x, player_y)
#     playerIsHit = areCollided(enemies_x[i], enemies_y[i], player_x, player_y, [ENEMY_IMG_WIDTH, ENEMY_IMG_HEIGHT], [PLAYER_IMG_WIDTH, PLAYER_IMG_HEIGHT])
#     # print('playerIsHit')
#     if playerIsHit and not game_over:
#         print('here')
#         game_over = True
#         EXPLOSION_SOUND.play(3)
#         for j in range(NUM_OF_ENEMIES):
#             enemies_y[j] = 2000
#         game_over_text()
#         return



