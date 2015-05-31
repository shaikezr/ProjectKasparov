#Players.py

class HumanPlayer(object):
	def __init__(self, number):
		self.number = number
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