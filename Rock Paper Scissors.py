#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
#compare them, print out a message of congratulations to the winner,
#and ask if the players want to start a new game)

print("Welcome to our Rock-Paper-Scissors game")

win_matrix = [
    [0,2,1],
    [1,0,2],
    [2,1,0]
]

def int_to_move(num):
    if num == 1:
        return "Rock"
    elif num == 2:
        return "Paper"
    elif num == 3:
        return "Scissors"
    else:
        return "N/A"

def move_select(player_num):
    print("Player",player_num,"Select your move: \n"
          "1. Rock \n"
          "2. Paper \n"
          "3. Scissors")

    move = int(input("Enter your move: "))

    repeat = True
    while repeat:
        if move in (1,2,3):
            repeat = False
        else:
            move = int(input("Please enter a valid move: "))
            repeat = True
    return move

repeat = True
while repeat:

    player1 = move_select(1)
    player2 = move_select(2)

    winner = win_matrix[player1-1][player2-1]
    if winner == 0:
        print("Match is a draw")
    elif winner == 1:
        print("Player 1 wins because", int_to_move(player1),"beats",int_to_move(player2))
    elif winner == 2:
        print("Player 2 wins because", int_to_move(player2),"beats",int_to_move(player1))
    else:
        print("Something is broken")

    again = input("Would you like to play again \n"
                  "-to continue write yes-\n"
                  "")
    if again == "Yes" or again == "yes":
        repeat = True
    else:
        repeat = False