def tictactoe():
    print("Game is starting")
    while True:
        board=['','','','','','','','','']
        player=1
        if player>2:
            player=1
        print("player", player,"select your marker")
        marker=input("Enter your marker : ")
        player_1,player_2 = set_marker(marker)

        while True:
            print("player", player, ": enter your position")
            pos=int(input("Enter your pos: "))
            if check_pos(pos,board):
                continue
            if player ==1 :
                set_board(board,pos,player_1)

            else:
                set_board(board,player_2,pos)

            display(board)
            if player ==1:
                if check_win(board, player_1):
                    print("player",player , "has won")

                    break
                else:
                    if check_win(board,player_2):
                        print("player", player," has won")
                        break

                if check_space(board):
                    print("draw!!!")
                    break
                player+=1

                if replay():
                    True


def set_marker(marker):
    if marker=="X":
        return ("X", "O")
    else:
        return ("O","X")

def check_pos(pos,board):
    if board[pos]==" ":
        return False
    else:
        return True

def set_board(board,marker,pos):
    board[pos] =marker

def display(board):
    print(f"{board[7]} | {board[8]} |{board[9]} ")
    print("----------------")
    print(f"{board[4]} | {board[5]} |{board[6]} ")
    print("----------------")
    print(f"{board[1]} | {board[2]} |{board[3]} ")
    print("----------------")

def check_win(board,marker):
    return board[1]==marker and board[2]==marker and board[3]==marker or board[4]==marker and board[5]==marker and board[6]==marker or board[7]==marker and board[8]==marker and board[9]==marker

def check_space(board):
    if " " in board:
        return False
    else:
        return True

def replay():
    print("Do you want to play again Y/N")
    ans=input()
    if ans=="Y" or ans == "y" :
        return True
    else:
        return False


print(tictactoe())