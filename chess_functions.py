from PIL import Image

# chess_board.size return a tuple of width and height -> (width, height)
def get_board_size(chess_board_image_path):
	chess_board = Image.open(chess_board_image_path)

	return chess_board.size