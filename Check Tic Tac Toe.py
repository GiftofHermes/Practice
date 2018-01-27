#given a 3 by 3 list of lists that represents a Tic Tac Toe game board,
# tell me whether anyone has won, and tell me which player won, if any
winner_is_2 = [[2, 2, 0],
	            [2, 1, 0],
	            [2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	            [2, 1, 0],
	            [2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	                [2, 1, 0],
	                [2, 1, 1]]

no_winner = [[1, 2, 0],
	        [2, 1, 0],
	        [2, 1, 2]]

also_no_winner = [[1, 2, 0],
	            [2, 1, 0],
	            [2, 1, 0]]

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

print('winner is ', check_win(winner_is_2))
print('winner is ', check_win(winner_is_1))
print('winner is ', check_win(winner_is_also_1))
print('winner is ', check_win(no_winner))
