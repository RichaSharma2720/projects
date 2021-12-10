from IPython.display import clear_output

board=['-','-','-','-','-','-','-','-','-']

#if game stll going


#who won or tie?
winner=None  #for now
#whos turn is it

currunt_player="X"

def display_board():   
    
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | "+board[7]+" | "+board[8])

#handle a single trun of an arbitrary player
def handle_turn(player):
    print(player + "'s turn")
    position=input("Enter a Position (1-9) : ")
    valid=False
    while not valid:
            
        while position not in ["1","2","3","4","5","6","7","8","9"]:
                position=input("invalid position !!! Enter a Position (1-9) : ")

        position=int(position)-1
        if board[position] == "-":
            valid=True
        else:
            print("you can't go there. Go Again...")

    board[position]=player
    display_board()
    check_if_tie()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner(): 
    #setup global variable
    global winner
    #check row
    row_winner=check_rows()
    column_winner= check_coloum()
    diagonal_winner=check_diagonals()

    #Get the winner
    if row_winner:
        winner=row_winner
    elif column_winner:        
        winner=column_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner=None
    return  


def check_rows():
    #setup variable
    global game_still_going
    #check if any of the  rows have allthe same value (and is not empty  )
    row_1=board[0] == board[1] == board[2] != "-"
    row_2=board[3] == board[4] == board[5] != "-"
    row_3=board[6] == board[7] == board[8] != "-"
    #if any rows does havea match,flag that there is win
    if row_1 or row_2 or row_3 :
        game_still_going=True
        #return the winner X or O

        if row_1:
            return board[0]

        elif row_2:
            return board[3]

        elif row_3:
            return board[6]
        return


def check_coloum():
    
    #setup variable
    global game_still_going
    #check if any of the  rows have allthe same value and is not empty  
    coloum_1=board[0] == board[3] == board[6] != "-"
    coloum_2=board[1] == board[4] == board[7] != "-"
    coloum_3=board[2] == board[5] == board[8] != "-"
    #if any rows does havea match,flag that there is win
    if coloum_1 or     coloum_2 or coloum_3 :
        game_still_going=True

        #return the winner X or O

        if coloum_1:
            return board[0]

        elif coloum_2:
            return board[3]

        elif coloum_3:
            return board[6]
        return
def check_diagonals():
    
    #setup variable
    global game_still_going
    #check if any of the  rows have allthe same value and is not empty  
    diagonals_1=board[0] == board[4] == board[8] != "-"
    diagonals_2=board[6] == board[4] == board[2] != "-"
    #if any rows does havea match,flag that there is win
    if diagonals_1 or     diagonals_2  :
        game_still_going= True
        #return the winner X or O

        if diagonals_1:
            return board[0]

        elif diagonals_2:
            return board[6]

        return
def check_if_tie():
    global game_still_going
    if "-" not in board:
        
        game_still_going= False
        
    
    return

def flip_player():
    global currunt_player
    if currunt_player == "X":
        currunt_player="O"

    elif currunt_player == "O":
        currunt_player ="X"
    return
#play game of tic tac toe
def tictactoe():
    display_board()
    
    while True:
        #the game has ended
        if winner=="X" or winner == "O":
            print(winner + ": won.")
            break
        
    
        #handle a single turn of an arbitary player
        handle_turn(currunt_player)
        #check if the game has ended
        check_if_game_over()
        #flip to the other player
        flip_player()

            
            



tictactoe()