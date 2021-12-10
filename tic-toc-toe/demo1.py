from IPython.display import clear_output

'''
display board
take a input
choose a position
check winner looser

'''
board=[[" - "," - "," - "],[" - "," - "," - "],[" - "," - "," - "]]

def test_board():
	for row in board:
		for slot in row:
			print(f"{slot}", end="")
		print()
		


def quit(user_input):
	if user_input == "q":
		print("thanks for playing")
		return True
	else:
		return False


def check_input(user_input):
	# checks its number
	#check its 1-9
	pass	

def isnum(user_input):
	if not user_input.isnumeric():
		return False 
	else: return True

def bounds(user_input):
	user_input=int(user_input)
	if user_input>9 or user_input<1:		
		return False
	else: return True

def coordinates(user_input):
	row=int(user_input/3)
	col=user_input
	
	if col > 2: col=int(col%3)
	return (row,col)

def istaken(coords,board):
	row=coords[0]
	col=coords[1]
	if board[row][col] != '-':
		print("this possition already taken")
		return True
	else:return False


while True:
	print(test_board())
	user_input=input("please enter a digit (1 to 9) and enter \"Q\" to quit: ")
	if quit(user_input): break
	if not isnum(user_input):
		print("this is not valid number. ")
		continue
	if not bounds(user_input):
		print("this number is out of bound")

	user_input=int(user_input)-1
	coords=coordinates(user_input)
	board[0][0]="X"
	if istaken(coords, board):
		print("plese try again")
		continue
	print(quit(user_input))



