import pygame
from win32api import GetSystemMetrics
import os
import math

class Tiles:
	def __init__(self, x_pos, y_pos, width, height, mark):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.width = width
		self.height = height
		self.mark = mark

def draw_tiles():
	for rect in BOARD_RECT_ARRAY:
		if rect.mark == 'X':
			draw_X(rect)
		if rect.mark == 'O':
			draw_O(rect)

def get_map_array_coord():
	start_x_pos = 0
	start_y_pos = 0
	game_arr = [None, None, None, None, None, None, None, None, None]
	
	for i in range(0, 9):
		game_arr[i] = Tiles(start_x_pos, start_y_pos, BOARD_WIDTH / 3, BOARD_HEIGHT / 3, ' ')

		start_x_pos += BOARD_WIDTH / 3

		if ((i + 1) % 3 == 0):
			start_y_pos += BOARD_HEIGHT / 3
			start_x_pos = 0

	return game_arr

WIN_WIDTH = GetSystemMetrics(0)
WIN_HEIGHT = GetSystemMetrics(1)
WIN_BACKGROUND = (0, 0, 0)

SCALE = 1
BOARD_WIDTH = WIN_WIDTH / SCALE
BOARD_HEIGHT = WIN_HEIGHT / SCALE
BOARD_COLOR = (120, 155, 155)
LINE_WIDTH = 5
LINE_NUM = 2 + 1

BOARD_RECT_ARRAY = get_map_array_coord()
IS_FIRST_PLAYER = True

os.environ['SDL_VIDEO_WINDOW_POS'] = "{0}, {1}".format(10, 10)
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# pos -> (x, y)
# rect -> (x, y, width, height)
def is_inside_rect(rect, pos):
	print("is inside rect")
	pos_x = pos[0]
	pos_y = pos[1]
	rect_x = rect.x_pos
	rect_y = rect.y_pos
	rect_width = rect.width
	rect_height = rect.height

	print("Mouse pos = {0}".format(pos))
	print("Rect pos = ({0}, {1})".format(rect_x, rect_y))

	rect_left_side = rect_x
	rect_up_side = rect_y
	rect_right_side = rect_x + rect_width
	rect_bottom_side = rect_y + rect_height

	if (pos_x <= rect_right_side and pos_x >= rect_left_side and
		pos_y <= rect_bottom_side and pos_y >= rect_up_side):
		return True

	return False

def is_valid_rect(rect):
	if (rect.mark != ' '):
		return False

	return True

def place_marker(mouse_pos):
	global IS_FIRST_PLAYER

	for rect in BOARD_RECT_ARRAY:
		if (is_inside_rect(rect, mouse_pos) and is_valid_rect(rect)):
			print("gasjkgklasgnj")
			if (IS_FIRST_PLAYER):
				rect.mark = 'X'
				IS_FIRST_PLAYER = False
			else:
				rect.mark = 'O'
				IS_FIRST_PLAYER = True
			
			break

def draw_X(rect):
	rect_x = rect.x_pos
	rect_y = rect.y_pos
	rect_width = rect.width
	rect_height = rect.height

	fake_x_center = (int(math.ceil(rect_x + rect_width / 2)), int(math.ceil(rect_y + rect_height / 2)))
	fake_x_radius = int(rect_width / 15)
	fake_x_thickness = LINE_WIDTH * 5

	fake_x = pygame.draw.circle(window, BOARD_COLOR, fake_x_center, fake_x_radius, fake_x_thickness)

def draw_O(rect):
	rect_x = rect.x_pos
	rect_y = rect.y_pos
	rect_width = rect.width
	rect_height = rect.height

	circle_center = (int(math.ceil(rect_x + rect_width / 2)), int(math.ceil(rect_y + rect_height / 2)))
	circle_radius = int(rect_width / 4)
	circle_thickness = LINE_WIDTH

	pygame.draw.circle(window, BOARD_COLOR, circle_center, circle_radius, circle_thickness)

def check_win():
	for i in range(0, 3):
		if (BOARD_RECT_ARRAY[i].mark == BOARD_RECT_ARRAY[i + 3].mark and BOARD_RECT_ARRAY[i].mark == BOARD_RECT_ARRAY[i + 6].mark and BOARD_RECT_ARRAY[i].mark != ' '):
			return True
		if (BOARD_RECT_ARRAY[i * 3].mark == BOARD_RECT_ARRAY[i * 3 + 1].mark and BOARD_RECT_ARRAY[i * 3].mark == BOARD_RECT_ARRAY[i * 3 + 2].mark and BOARD_RECT_ARRAY[i * 3].mark != ' '):
			return True
		
	if (BOARD_RECT_ARRAY[0].mark == BOARD_RECT_ARRAY[4].mark and BOARD_RECT_ARRAY[0].mark == BOARD_RECT_ARRAY[8].mark and BOARD_RECT_ARRAY[0].mark != ' '):
		return True
	
	if (BOARD_RECT_ARRAY[2].mark == BOARD_RECT_ARRAY[4].mark and BOARD_RECT_ARRAY[2].mark == BOARD_RECT_ARRAY[6].mark and BOARD_RECT_ARRAY[2].mark != ' '):
		return True

	return False

def end_screen():
	# Code...
	pygame.quit()
	pass

def draw_board():
	# Vertical Lines
	for i in range(1, LINE_NUM):
		pygame.draw.rect(window, BOARD_COLOR, (WIN_WIDTH / 2 - BOARD_WIDTH / 2 + BOARD_WIDTH / (LINE_NUM / i), WIN_HEIGHT / 2 - BOARD_HEIGHT / 2, LINE_WIDTH, BOARD_HEIGHT))

	# Horizontal Lines
	for i in range(1, LINE_NUM):
		pygame.draw.rect(window, BOARD_COLOR, (WIN_WIDTH / 2 - BOARD_WIDTH / 2, WIN_HEIGHT / 2 - BOARD_HEIGHT / 2 + BOARD_HEIGHT / (LINE_NUM / i), BOARD_WIDTH, LINE_WIDTH))

game_done = False
while not game_done:
	window.fill(WIN_BACKGROUND)
	draw_board()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_done = True

		#Press CTRL + W for QUITING the game
		if (pygame.key.get_pressed()[pygame.K_RCTRL] or pygame.key.get_pressed()[pygame.K_LCTRL]) and pygame.key.get_pressed()[pygame.K_w]:
			game_done = True

		if (pygame.key.get_pressed()[pygame.K_ESCAPE]):
			game_done = True

		if (event.type == pygame.MOUSEBUTTONUP):
			mouse_pos = pygame.mouse.get_pos()

			place_marker(mouse_pos)
	
	draw_tiles()

	if (check_win()):
		game_done = True
	
	pygame.display.update()

end_screen()
 
# pygame.draw.rect(window, (213, 165, 100), (int(self.player_x_pos), int(self.player_y_pos), self.player_width, self.player_height))
# When moving window.fill should be inside of the main while loop

