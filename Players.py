#Players.py

class Player(object):
	def __init__(self, number):
		self.number = number
	def report_win(self):
		print("Player {0} wins".format(self.number))
	def report_loss(self):
		pass
	def report_draw(self):
		print("Draw")

class HumanPlayer(Player):
	def get_move(self,board):
		if self.number == 1:
			print("Player 1 (o): \n")
		elif self.number == 2:
			print("Player 2 (x): \n")
			
		got_move = False
		move = [-1,-1]
		while not got_move:
			row = input("What is your move (row)?")
			if row.isdigit() and int(row) >= 0 and int(row) <= 2:
				col = input("What is your move (col)?")
				if col.isdigit() and int(col) >= 0 and int(col) <= 2:
					if board.is1(int(row),int(col)) or board.is2(int(row),int(col)):
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
		
		return move

import random	
class RandomPlayer(Player): #just make random moves.
	def get_move(self,board):
		print("Making random move.")
		while True: 
			row = random.randint(0,2)
			col = random.randint(0,2)
			if not board.is1(row,col) and not board.is2(row,col):
				break #if square is empty, make the move.
		move = [row,col]
		return move
		