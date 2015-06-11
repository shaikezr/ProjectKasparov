import Players

class ReinforcePlayer(RandomPlayer): #access random move. 
	def __init__(self,number,strat):
		#figure out how to pass the strat by reference here. 
		#don't need to use global, I wouldn't think.
		super().__init__()
		self.strat = strat
		self.movehist = []
	def rotate90(self,board):
		pass
	def rotate180(self,board):
		pass
	def rotate270(self,board):
		pass
	def reflecthrz(self,board):
		pass
	def reflectvrt(self,board):
		pass
	def get_move(self, board):
		#be sure to remember the moves made also. 
		if board in self.strat.keys:
			return self.strat[board]
		elif  self.rotate90(board) in self.strat.keys:
			return self.strat[self.rotate90(board)]
		elif  self.rotate180(board) in self.strat.keys:
			return self.strat[self.rotate180(board)]
		elif  self.rotate270(board) in self.strat.keys:
			return self.strat[self.rotate270(board)]
		elif  self.reflecthrz(board) in self.strat.keys:
			return self.strat[self.reflecthrz(board)]
		elif  self.reflectvrt(board) in self.strat.keys:
			return self.strat[self.reflectvrt(board)]
		else
			return super().get_move()
	def report_win(self):
		#update strat for win
		pass
	def report_loss(self):
		#update strat for loss
		pass
	def report_draw(self):
		#update strat for draw
		pass

class ReinforceInterface(Object):
	#remembers the strategies, generates reinforceplayers for play
	# and writes to disk.
	def read_strat_from_disk(self,strat):
		pass
	def write_strat_to_disk(self,strat):
		pass
	def __init__(self):
		self.strat={}
		read_strat_from_disk(self.strat)
		pass
	def generate_reinforceplayer(self,number):
		pass
	def __del__(self):
		write_strat_to_disk(self.strat)
		