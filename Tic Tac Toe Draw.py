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

def print_board(game_state):
    print('-Game State-')
    for line in game_state:
        print(line)

print_board(game_state)