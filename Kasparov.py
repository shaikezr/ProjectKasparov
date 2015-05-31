#Game board will be represented by a 3x4 integer array.
#[0,0,0]
#[0,0,0]
#[0,0,0]
# First mover will be 1
# Second mover will be 2

import Players

class GameBoard(object):
	def __init__(self):
		self.gameboard = [[0,0,0],[0,0,0],[0,0,0]]
	
	def is1(self,row,col): #check if p1 has won
		if self.gameboard[row][col] == 1:
			return True
		else:
			return False
		
	def is2(self, row, col): #check if p2 has won
		if self.gameboard[row][col] == 2:
			return True
		else:
			return False
	
	
	
	def printrow(self, row):
		c1 = ' '
		c2 = ' '
		c3 = ' '
		if self.is1(row,0):
			c1 = 'o'
		elif self.is2(row,0):
			c1 = 'x'
			
		if self.is1(row,1):
			c2 = 'o'
		elif self.is2(row,1):
			c2 = 'x'
			
		if self.is1(row,2):
			c3 = 'o'
		elif self.is2(row,2):
			c3 = 'x'
		row = "+ {0} | {1} | {2} +".format(c1,c2,c3);
		print(row)
	
	def printboard(self):
		print("+++++++++++++")
		self.printrow(0)
		print("+-----------+")
		self.printrow(1)
		print("+-----------+")
		self.printrow(2)
		print("+++++++++++++")
	
	def makemove(self,turn,row,col):
		self.gameboard[row][col] = turn
		

class Game(object):
	def __init__(self, Player1, Player2):
		self.player1 = Player1
		self.player2 = Player2
		self.board = GameBoard()
		self.turn = 1
		
	def checkwin(self): #check if someone has won
		if(
			#horizontals
			(self.board.is1(0,0) and self.board.is1(0,1) and self.board.is1(0,2)) or
			(self.board.is1(1,0) and self.board.is1(1,1) and self.board.is1(1,2)) or
			(self.board.is1(2,0) and self.board.is1(2,1) and self.board.is1(2,2)) or
			#verticals
			(self.board.is1(0,0) and self.board.is1(1,0) and self.board.is1(2,0)) or
			(self.board.is1(0,1) and self.board.is1(1,1) and self.board.is1(2,1)) or
			(self.board.is1(0,2) and self.board.is1(1,2) and self.board.is1(2,2)) or
			#diagonals
			(self.board.is1(0,0) and self.board.is1(1,1) and self.board.is1(2,2)) or
			(self.board.is1(0,2) and self.board.is1(1,1) and self.board.is1(2,0))
		  ):
			return 1 #1 wins
		elif (
			#horizontals
			(self.board.is2(0,0) and self.board.is2(0,1) and self.board.is2(0,2)) or
			(self.board.is2(1,0) and self.board.is2(1,1) and self.board.is2(1,2)) or
			(self.board.is2(2,0) and self.board.is2(2,1) and self.board.is2(2,2)) or
			#verticals
			(self.board.is2(0,0) and self.board.is2(1,0) and self.board.is2(2,0)) or
			(self.board.is2(0,1) and self.board.is2(1,1) and self.board.is2(2,1)) or
			(self.board.is2(0,2) and self.board.is2(1,2) and self.board.is2(2,2)) or
			#diagonals
			(self.board.is2(0,0) and self.board.is2(1,1) and self.board.is2(2,2)) or
			(self.board.is2(0,2) and self.board.is2(1,1) and self.board.is2(2,0))
		  ):
			return 2 # 2 wins
		else:
			has_valid_move = False
			for i in range(3):
				for j in range(3):
					if not self.board.is1(i,j) and not self.board.is2(i,j):
						has_valid_move = True
						break;
				if has_valid_move:
					break;
			
			if has_valid_move:
				return 0 # keep going
			else:
				return -1 # draw.
		
	def prompt_for_move(self):
		move = [-1,-1]
		if self.turn == 1:
			move = self.player1.get_move(self.board)
		elif self.turn == 2:
			move = self.player2.get_move(self.board)	
			
		self.board.makemove(self.turn,move[0],move[1])
		if self.turn == 1:
			self.turn = 2
		else:
			self.turn = 1
		
	def play(self):
		while self.checkwin() == 0:
			self.board.printboard()
			self.prompt_for_move()
			
		self.board.printboard();
		if self.checkwin() == 1:
			print("Player 1 wins")
		elif self.checkwin() == 2:
			print("Player 2 wins")
		elif self.checkwin() == -1:
			print("Draw")
		else:
			print("Something went wrong")
		
Player1 = Players.HumanPlayer(1)
Player2 = Players.HumanPlayer(2)
KaspGame = Game(Player1, Player2);
KaspGame.play();