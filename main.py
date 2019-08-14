import pygame
from win32api import GetSystemMetrics
import os
import math

WIN_WIDTH = GetSystemMetrics(0)
WIN_HEIGHT = GetSystemMetrics(1)
WIN_BACKGROUND = (0, 0, 0)

os.environ['SDL_VIDEO_WINDOW_POS'] = "{0}, {1}".format(0, 0)
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

def draw_board():
	SCALE = 1.01
	BOARD_WIDTH = WIN_WIDTH / SCALE
	BOARD_HEIGHT = WIN_HEIGHT / SCALE
	BOARD_COLOR = (255, 255, 255)
	LINE_WIDTH = 5
	LINE_NUM = 2 + 1

	# Vertical Lines
	for i in range(1, LINE_NUM):
		pygame.draw.rect(window, BOARD_COLOR, (WIN_WIDTH / 2 - BOARD_WIDTH / 2 + BOARD_WIDTH / (LINE_NUM / i), WIN_HEIGHT / 2 - BOARD_HEIGHT / 2, LINE_WIDTH, BOARD_HEIGHT))

	# Horizontal Lines
	for i in range(1, LINE_NUM):
		pygame.draw.rect(window, BOARD_COLOR, (WIN_WIDTH / 2 - BOARD_WIDTH / 2, WIN_HEIGHT / 2 - BOARD_HEIGHT / 2 + BOARD_HEIGHT / (LINE_NUM / i), BOARD_WIDTH, LINE_WIDTH))

		
game_done = False
while not game_done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_done = True

		#Press CTRL + W for QUITING the game
		if (pygame.key.get_pressed()[pygame.K_RCTRL] or pygame.key.get_pressed()[pygame.K_LCTRL]) and pygame.key.get_pressed()[pygame.K_w]:
			game_done = True

		if (pygame.key.get_pressed()[pygame.K_ESCAPE]):
			game_done = True
	
	
	window.fill(WIN_BACKGROUND)

	draw_board()
	
	pygame.display.update()

pygame.quit()
 
# pygame.draw.rect(window, (213, 165, 100), (int(self.player_x_pos), int(self.player_y_pos), self.player_width, self.player_height))
# When moving window.fill should be inside of the main while loop