import Players
import Board
import operator

class ReinforcePlayer(Players.RandomPlayer): #access random move. 
	def __init__(self,number,strat):
		#strat is mutable, so just keep extending the strats.
		super().__init__(number)
		self.strat = strat
		self.movehist = []
	
	def eval_board(self, board):
		###############################################################
		##### list is not hashable, so will need to strat with int.####
		###############################################################
		#be sure to remember the moves made also. 
		#if board in self.strat.keys():
		#	return self.strat[board]
		#else:
			return 0 #default is zero.
		#elif  self.rotate90(board) in self.strat.keys:
		#	return self.strat[self.rotate90(board)]
		#elif  self.rotate180(board) in self.strat.keys:
		#	return self.strat[self.rotate180(board)]
		#elif  self.rotate270(board) in self.strat.keys:
		#	return self.strat[self.rotate270(board)]
		#elif  self.reflecthrz(board) in self.strat.keys:
		#	return self.strat[self.reflecthrz(board)]
		#elif  self.reflectvrt(board) in self.strat.keys:
		#	return self.strat[self.reflectvrt(board)]
		
	
	def eval_moves(self,board):
		avail_moves = []
		evaluations = {}
		for x in range(3):
			for y in range(3):
				if not board.is1(x,y) and not board.is2(x,y):
					avail_moves.append((x,y))
		for move in avail_moves:
			newboard = Board.GameBoard(board.gameboard)
			newboard.makemove(self.number,move[0], move[1])
			#keep an eye out if newboard going out of scope whacks the key.
			#there's got to be a more elegant way to do this?
			###############################################################
			##### list is not hashable, so will need to strat with int.####
			###############################################################
			evaluations[newboard.gameboard]=(move,self.eval_board(newboard.gameboard))
			
		sorted_evals = sorted(evaluations.items(), key=operator.itemgetter(0))
		best_eval = sorted_evals[len(sorted_evals) - 1][1] #sorted eval is a list of tuples
		movehist.append(best_eval[1]) #save board position
		return best_eval[0] #make the move.
		
	
	def get_move(self, board):
		return self.eval_moves(board) #super().get_move(board)
	def report_win(self):
		#update strat for win
		pass
	def report_loss(self):
		#update strat for loss
		pass
	def report_draw(self):
		#update strat for draw
		pass

class ReinforceInterface(object):
	#remembers the strategies, generates reinforceplayers for play
	# and writes to disk.
	def read_strat_from_disk(self,strat):
		pass
	def write_strat_to_disk(self,strat):
		pass
	def __init__(self):
		self.strat={}
		self.read_strat_from_disk(self.strat)
		pass
	def generate_reinforceplayer(self,number):
		reinforceplayer = ReinforcePlayer(number,self.strat)
		return reinforceplayer
	def __del__(self):
		self.write_strat_to_disk(self.strat)
		