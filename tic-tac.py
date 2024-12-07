# tic tac toe 
def display(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("----------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("----------")
    print(f"{board[6]} | {board[7]} | {board[8]}")



def check_winner(board,player):
    winning_conditions = [(0,1,2),(3,4,5),(6,7,8),
                          (0,4,8),(2,4,6),(0,3,6),
                          (1,4,7),(2,5,8)]
    return any(board[a] == board[b] == board[c] == player for a,b,c in winning_conditions)

def is_board_full(board):
    return all( spot in["X","O"] for spot in board)

def game():
    board =[str(i) for i in range(0,9)]
    current_player = "X"

    while True:

        display(board) 
        print(f"player {current_player} turn")        
        
        move = int(input("enter the position (0-8):"))   
        try:
            if board[move] in ["X","O"]:
                print("that spot is already taken")
                continue
        except(ValueError,IndexError):
            print("please provide values from 0-8")    
            continue
        board[move] = current_player
        if check_winner(board,current_player):
            winning_player = current_player
            display(board)
            print(f"player {current_player} won")
            break

        if is_board_full(board):
            display(board)
            print("its a tie")
            break

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"     
game()