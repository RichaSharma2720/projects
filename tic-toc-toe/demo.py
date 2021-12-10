from IPython.display import clear_output
import random
def display_board(board):
    print(' | |')
    print(board[7]+"|"+board[8]+"|"+board[9])
    print(' | |')
    print('-------')
    print(' | |')
    print(board[4]+"|"+board[5]+"|"+board[6])
    print(' | |')
    print('------')
    print(' | |')

    print(board[1]+"|"+board[2]+"|"+board[3])
    print(' | |')
    
test_board=['#','X','O','X','O','X','O','X','O','X']
print(display_board(test_board))

def player_input():
    '''
    output=(player1 marker, player2 marker)
    '''

    marker=''
    while not (marker =='X' or marker == 'O'):
        marker=input("Player1, select any one from X or O : ").upper()
       
    if marker == 'X':
         return ('X', 'O')
    else:
        return ('O','X')
print(player_input())

def place_marker(board, marker, position):
    board[position]=marker
print( place_marker(test_board,'#',8))
print(display_board(test_board))

def win_check (board, mark):
    #win tic tac toe
    return((board[7]== mark and board[8]==mark and board[9]==mark) or #across the up
    (board[4]== mark and board[5]==mark and board[6]==mark) or #across the middle
    (board[1]== mark and board[2]==mark and board[3]==mark) or #across the bottom 
    (board[7]== mark and board[4]==mark and board[1]==mark) or #down the middle
    (board[8]== mark and board[5]==mark and board[2]==mark) or #down the middle
    (board[9]== mark and board[6]==mark and board[3]==mark) or #down the right
    (board[7]== mark and board[5]==mark and board[3]==mark) or #across the up
    (board[9]== mark and board[5]==mark and board[1]==mark)) 

print(win_check(test_board,'X'))

def choose_first():

    flip=random.randint(0,1)
    if flip == 0:
        return 'player 1'
    else:
        return 'player 2'

def space_check(board, position):
    return board[position] == ' '

#print(space_check(test_board, 5))

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
            #board is full is we return true
    return True

def player_choice(board):
    position=0
    while  position not in [1,2,3,4,5,6,7,8,9] or not space_check( board,position):
        position=int(input('choose a position(1-9)'))

    return position

def replay():
    choice=input('play again ? Enter yes or No')

    return choice== 'yes'



print('Welcome to tic toc toe')

while True:
    #play the game
    # set everything up(board, whod first. choose marker X, O)
    the_board=[''] *10
    player1_marker, player2_marker=player_input()
    turn=choose_first()
    print(turn+"will go first")
    play_game=input("REadt to play? Y or N")
    if play_game == 'Y ':
        game_on=True
    else:
        game_on=False
    ## game play
    while game_on:
        if turn=='player 1':
            #show the board
            display_board(the_board)
            #choose a position
            position=player_choice(the_board)
            #place the markeron the position
            place_marker(the_board,player1_marker,position)
            #CHECK IF THEY WON
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 has won!!')
                game_on=False

            else:

                if full_board_check(the_board):
                    display_board(the_board)
                    print('tie game')
                    game_on= False
                else:
                    turn='player 2'

    else:

        display_board(the_board)
        #choose the position
        position=player_choice(the_board)
        #place the marker on position

        place_marker(the_board,player2_marker,position)
        #check they won
        if win_check(the_board,player2_marker):
            display_board(the_board)

    ### play one turn
    ### pkay two turn

    if not replay():
        break

print(replay())