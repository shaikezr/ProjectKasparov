#Game board will be represented by a 3x4 integer array.
#[0,0,0]
#[0,0,0]
#[0,0,0]
# First mover will be 1
# Second mover will be 2

class GameBoard(object):
	def __init__(self):
		self.gameboard = [[0,0,0],[0,0,0],[0,0,0]]
		self.turn = 1;
	
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
	
	def checkwin(self): #check if someone has won
		if(
			#horizontals
			(self.is1(0,0) and self.is1(0,1) and self.is1(0,2)) or
			(self.is1(1,0) and self.is1(1,1) and self.is1(1,2)) or
			(self.is1(2,0) and self.is1(2,1) and self.is1(2,2)) or
			#verticals
			(self.is1(0,0) and self.is1(1,0) and self.is1(2,0)) or
			(self.is1(0,1) and self.is1(1,1) and self.is1(2,1)) or
			(self.is1(0,2) and self.is1(1,2) and self.is1(2,2)) or
			#diagonals
			(self.is1(0,0) and self.is1(1,1) and self.is1(2,2)) or
			(self.is1(0,2) and self.is1(1,1) and self.is1(2,0))
		  ):
			return 1 #1 wins
		elif (
			#horizontals
			(self.is2(0,0) and self.is2(0,1) and self.is2(0,2)) or
			(self.is2(1,0) and self.is2(1,1) and self.is2(1,2)) or
			(self.is2(2,0) and self.is2(2,1) and self.is2(2,2)) or
			#verticals
			(self.is2(0,0) and self.is2(1,0) and self.is2(2,0)) or
			(self.is2(0,1) and self.is2(1,1) and self.is2(2,1)) or
			(self.is2(0,2) and self.is2(1,2) and self.is2(2,2)) or
			#diagonals
			(self.is2(0,0) and self.is2(1,1) and self.is2(2,2)) or
			(self.is2(0,2) and self.is2(1,1) and self.is2(2,0))
		  ):
			return 2 # 2 wins
		else:
			has_valid_move = False
			for i in range(3):
				for j in range(3):
					if not self.is1(i,j) and not self.is2(i,j):
						has_valid_move = True
						break;
				if has_valid_move:
					break;
			
			if has_valid_move:
				return 0 # keep going
			else:
				return -1 # draw.
	
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
		
	def prompt_for_move(self):
		got_move = False
		move = [-1,-1]
		if self.turn == 1:
			print("Player 1 (o): \n")
		elif self.turn == 2:
			print("Player 2 (x): \n")
			
		while not got_move:
			row = input("What is your move (row)?")
			if row.isdigit() and int(row) >= 0 and int(row) <= 2:
				col = input("What is your move (col)?")
				if col.isdigit() and int(col) >= 0 and int(col) <= 2:
					if self.is1(int(row),int(col)) or self.is2(int(row),int(col)):
						print("Square is already taken. \n")
					else:
						move[0] = int(row);
						move[1] = int(col);
						got_move = True;
				else:
					print("Column is not valid. Please input a number from 0 to 2 \n")
					continue
			else:
				print("Row is not valid. Please input a number from 0 to 2\n")
				continue
		
		self.gameboard[move[0]][move[1]] = self.turn
		
		if self.turn == 1:
			self.turn = 2
		else:
			self.turn = 1
			
	def play(self):
		while self.checkwin() == 0:
			self.printboard();
			self.prompt_for_move()
			
		self.printboard();
		if self.checkwin() == 1:
			print("Player 1 wins")
		elif self.checkwin() == 2:
			print("Player 2 wins")
		elif self.checkwin() == -1:
			print("Draw")
		else:
			print("Something went wrong")
		
Game = GameBoard();
Game.play();