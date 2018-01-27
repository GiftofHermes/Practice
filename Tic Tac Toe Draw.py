#As a reminder, our tic tac toe game is really a list of lists.
#The game starts out with an empty game board like this:

#game = [[0, 0, 0],
#	     [0, 0, 0],
#	     [0, 0, 0]]

#The computer asks Player 1 (X) what their move is (in the format row,col), and say they type 1,3. Then the game would print out
#
#game = [[0, 0, X],
#	    [0, 0, 0],
#	    [0, 0, 0]]


game_state = [[0,0,0],
              [0,0,0],
              [0,0,0]]

#is the board completely filled with moves
is_full= False

def print_board(game_state):
    print('-Game State-')
    for line in game_state:
        print(line)

def check_win(board):
    '''takes a board state and returns a win state. 1-2 win or draw'''
    if (board[0][0] == board[0][1] == board[0][2]) and board[0][0] != 0:
        return board[0][0]
    elif (board[1][0] == board[1][1] == board[1][2]) and board[1][0] != 0:
        return board[1][0]
    elif (board[2][0] == board[2][1] == board[2][2]) and board[2][0] != 0:
        return board[2][0]
    elif (board[0][0] == board[1][0] == board[2][0]) and board[0][0] != 0:
        return board[0][0]
    elif (board[0][1] == board[1][1] == board[2][1]) and board[0][1] != 0:
        return board[0][1]
    elif (board[0][2] == board[1][2] == board[2][2]) and board[0][2] != 0:
        return board[1][3]
    elif (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != 0:
        return board[0][0]
    elif (board[0][2] == board[1][1] == board[2][0]) and board[0][2] != 0:
        return board[0][2]
    else:
        return 0

def check_is_full(game_state):
    global is_full
    zero_count = 0
    for row in game_state:
        for col in row:
            if col == 0:
                zero_count += 1
    if zero_count == 0:
        is_full = True
    else:
        is_full = False
def play_move(move):
    # because normal people count by starting from 1
    if game_state[move[0] -1][move[1] -1] == 0:
        game_state[move[0] -1][move[1] -1] = move[2]
    else:
        print('that move is not vaild')



while check_win(game_state) == 0 and is_full != True:
    print_board(game_state)
    move = list(input('Enter row and column you want to play ').split(','))
    move[0] = int(move[0])
    move[1] = int(move[1])
    play_move(move)
    check_win(game_state)
    check_is_full(game_state)
    print(is_full)

print_board(game_state)
if check_win(game_state) != 0:
    print('player',check_win(game_state),'wins')
else:
    print('game is a draw')

