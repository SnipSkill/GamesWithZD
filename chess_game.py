class Tile:
	def __init__(self,X_Pos,Y_Pos,Is_Taken_By_White,Is_Taken_By_Black):
		self.X_Pos=X_Pos
		self.Y_Pos=Y_Pos
		self.Is_Taken_By_White=Is_Taken_By_White
		self.Is_Taken_By_Black=Is_Taken_By_Black

class Chess_Piece:
	def __init__(self,Is_White,Start_X_Pos,Start_Y_Pos):
		self.Is_White=Is_White
		self.Start_X_Pos=Start_X_Pos
		self.Start_Y_Pos=Start_Y_Pos

class Pawn(Chess_Piece):
	def __init__(self,Is_White,Start_X_Pos,Start_Y_Pos):
		Chess_Piece.__init__(self,Is_White,Start_X_Pos,Start_Y_Pos)
	
class Knight(Chess_Piece):
	def __init__(self,Is_White,Start_X_Pos,Start_Y_Pos):
		Chess_Piece.__init__(self,Is_White,Start_X_Pos,Start_Y_Pos)

class Rook(Chess_Piece):
	def __init__(self,Is_White,Start_X_Pos,Start_Y_Pos):
		Chess_Piece.__init__(self,Is_White,Start_X_Pos,Start_Y_Pos)

class Bishop(Chess_Piece):
	def __init__(self,Is_White,Start_X_Pos,Start_Y_Pos):
		Chess_Piece.__init__(self,Is_White,Start_X_Pos,Start_Y_Pos)

class Queen(Chess_Piece):
	def __init__(self,Is_White,Start_X_Pos,Start_Y_Pos):
		Chess_Piece.__init__(self,Is_White,Start_X_Pos,Start_Y_Pos)

class King(Chess_Piece):
	def __init__(self,Is_White,Start_X_Pos,Start_Y_Pos):
		Chess_Piece.__init__(self,Is_White,Start_X_Pos,Start_Y_Pos)
