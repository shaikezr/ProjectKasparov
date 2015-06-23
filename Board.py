import copy
import boardutils

class GameBoard(object):
	def __init__(self, board = None):
		self.gameboard = [[0,0,0],[0,0,0],[0,0,0]]
		if not board == None:
			self.gameboard=copy.deepcopy(board)
		
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
		
	def printboard_debug(self):
		saveboard = self.gameboard
		
		print("original")
		self.printboard()
		
		print("rotate 90")
		self.gameboard = boardutils.rotate90(saveboard)
		self.printboard()
		
		print("rotate 180")
		self.gameboard = boardutils.rotate180(saveboard)
		self.printboard()
		
		print("rotate 270")
		self.gameboard = boardutils.rotate270(saveboard)
		self.printboard()
		
		print("reflect hrz")
		self.gameboard = boardutils.reflecthrz(saveboard)
		self.printboard()
		
		print("reflect vrt")
		self.gameboard = boardutils.reflectvrt(saveboard)
		self.printboard()
		
		self.gameboard = saveboard
		print("back to original")
		self.printboard()
	
	def makemove(self,turn,row,col):
		self.gameboard[row][col] = turn