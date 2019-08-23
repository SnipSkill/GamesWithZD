import pygame

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
	pass
		
class Knight(Chess_Piece):
	pass

class Rook(Chess_Piece):
	pass

class Bishop(Chess_Piece):
	pass

class Queen(Chess_Piece):
	pass

class King(Chess_Piece):
	pass

Game_Board=[[] for i in range(8)] for i in range(8)

for i in range(0,2):
	for  j in range(0,2):
		Game_Board[i][j]=Tile(i,j,False,False)