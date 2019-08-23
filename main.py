import pygame
from chess_game import *
from chess_functions import *

# Game constants and globals
CHESS_BOARD_FULL_PATH = 'C:\\Users\\Administrator\\Desktop\\Projects\\Ziv_Games\\GamesWithZD\\Chess\\Chess_Sprites\\Sprite_Chess_Board.png'
BORAD_LENGTH = 8
GAME_DONE = False
SCREEN_WIDTH, SCREEN_HEIGHT = get_board_size(CHESS_BOARD_FULL_PATH)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_board = [[Tile(i, j, False, False) for i in range(BORAD_LENGTH)] for j in range(BORAD_LENGTH)]

# Loading Images
chess_board = pygame.image.load(CHESS_BOARD_FULL_PATH)

while not GAME_DONE:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			GAME_DONE = True

	screen.blit(chess_board, (0, 0))

	pygame.display.update()



# TODO
# 1. Make SCREEN_WIDTH && SCREEN_HEIGHT The same width and height of chess_board_image - 'Chess_Sprites/Sprite_Chess_Board.png'