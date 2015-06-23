#Game board will be represented by a 3x4 integer array.
#[0,0,0]
#[0,0,0]
#[0,0,0]
# First mover will be 1
# Second mover will be 2

import Players
from Board import GameBoard
import Reinforce
		
class Game(object):
	def __init__(self, Player1, Player2):
		self.player1 = Player1
		self.player2 = Player2
		self.board = GameBoard()
		self.turn = 1
		
	@staticmethod	
	def checkwin(board): #check if someone has won
		curboard  = 0 
		if isinstance(board,GameBoard): #typechecking is not working consistently. 
			curboard = board
		elif isinstance(board, list):
			curboard = GameBoard(board)
		else:
			return 1 #SOMETHING WENT WRONG.
			
		if(
			#horizontals
			(curboard.is1(0,0) and curboard.is1(0,1) and curboard.is1(0,2)) or
			(curboard.is1(1,0) and board.is1(1,1) and curboard.is1(1,2)) or
			(curboard.is1(2,0) and curboard.is1(2,1) and curboard.is1(2,2)) or
			#verticals
			(curboard.is1(0,0) and curboard.is1(1,0) and curboard.is1(2,0)) or
			(curboard.is1(0,1) and curboard.is1(1,1) and curboard.is1(2,1)) or
			(curboard.is1(0,2) and curboard.is1(1,2) and curboard.is1(2,2)) or
			#diagonals
			(curboard.is1(0,0) and curboard.is1(1,1) and curboard.is1(2,2)) or
			(curboard.is1(0,2) and curboard.is1(1,1) and curboard.is1(2,0))
		  ):
			return 1 #1 wins
		elif (
			#horizontals
			(curboard.is2(0,0) and curboard.is2(0,1) and curboard.is2(0,2)) or
			(curboard.is2(1,0) and curboard.is2(1,1) and curboard.is2(1,2)) or
			(curboard.is2(2,0) and curboard.is2(2,1) and curboard.is2(2,2)) or
			#verticals
			(curboard.is2(0,0) and curboard.is2(1,0) and curboard.is2(2,0)) or
			(curboard.is2(0,1) and curboard.is2(1,1) and curboard.is2(2,1)) or
			(curboard.is2(0,2) and curboard.is2(1,2) and curboard.is2(2,2)) or
			#diagonals
			(curboard.is2(0,0) and curboard.is2(1,1) and curboard.is2(2,2)) or
			(curboard.is2(0,2) and curboard.is2(1,1) and curboard.is2(2,0))
		  ):
			return 2 # 2 wins
		else:
			has_valid_move = False
			for i in range(3):
				for j in range(3):
					if not curboard.is1(i,j) and not curboard.is2(i,j):
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
		while self.checkwin(self.board) == 0:
			self.board.printboard_debug()
			self.prompt_for_move()
			
		self.board.printboard();
		if self.checkwin(self.board) == 1:
			self.player1.report_win()
			self.player2.report_loss()
		elif self.checkwin(self.board) == 2:
			self.player2.report_win()
			self.player1.report_loss()
		elif self.checkwin(self.board) == -1:
			self.player1.report_draw()
			self.player2.report_draw()
		else:
			print("Something went wrong, checkwin is {0}".format(self.checkwin(self.board)))

			
ReinforceInt = Reinforce.ReinforceInterface()
Player1 = Players.RandomPlayer(1)#ReinforceInt.generate_reinforceplayer(1)
Player2 = Players.RandomPlayer(2)
KaspGame = Game(Player1, Player2)
KaspGame.play();