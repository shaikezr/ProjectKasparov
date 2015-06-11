import Kasparov



class GeneticPlayer(Player):
	def __init__(self,number,gene):
		super().__init__(self,number)
		self.gene = gene
		self.fitness = 0
	def get_move(self,board):
		#search the genes for the board position. 
		pass
		
	def report_win(self):
		self.fitness = 1
	def report_loss(self):
		self.fitness = 0
	def report_draw(self):
		self.fitness = 0.5
	
class GeneticIndividual(Object):
	def __init__(self):
		self.fitness = 0
		self.gene = {} #either use random or 
		pass
	def makerandomgene(self):
		#make random gene. Generate every board position, 
		#random move.
		