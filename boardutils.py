def get_pow(x,y):
	#---------------------------------
	#x=0| 0=0+0*3 | 1=1+0*3 | 2=2+0*3|
	#x=1| 3=0+1*3 | 4=1+1*3 | 5=2+1*3|
	#x=2| 6=0+2*3 | 7=1+2*3 | 8=2+2*3|
	#---------------------------------
	#      y=0     y=1     y=2
	#power = y + x^3
	approp_pow = ((x*3+y))
	return approp_pow
	
def get_multiplier(x,y):
	return 10**get_pow(x,y)

def encode_board(board):
	#encodes a board (list) into an 9-digit integer, which is hashable.
	
	encboard = 0;
	for x in range(3): #row
		for y in range(3): #col
			encboard = encboard + board[x][y]*get_multiplier(x,y)
	return encboard

def decode_board(encboard, decboard):
	#decodes a y-digit board integer into a board-list.
	if not isinstance(decboard,list):
		return
	while len(decboard) > 0:
		decboard.pop() #clean the board
		
	strboard = str(encboard) #use list comprehension to get the digit.
	while len(strboard) < 9:
		strboard = '0' + strboard
	for x in range(3):
		row = []
		for y in range(3):
			the_pow = get_pow(x,y)
			loc = 8 - the_pow #1st digit would be in position 8
			row.append(int(strboard[loc]))
		decboard.append(row)
	
	
