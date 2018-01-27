#Create a program that will play the “cows and bulls” game with the user. The game works like this:

#Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
#For every digit that the user guessed correctly in the correct place,
#they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull".
#Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
#Once the user guesses the correct number, the game is over.
#Keep track of the number of guesses the user makes throughout the game and tell the user at the end.

import random

def generate_goal():
    '''generates a 4 digit number and returns it'''
    goal = random.randint(1000,9999)
    return goal

def divide_num(num):
    '''takes a 4 digit number and returns its tigits as a tuple'''
    num = str(num)
    thousands = int(num[0])
    hundreds = int(num[1])
    tens = int(num[2])
    ones = int(num[3])

    return (thousands, hundreds, tens, ones)


def check_cows_and_bulls(guess, goal):
    '''
    takes a goal and a number
    checks whether the number guesses correct or not
    returns a tuple of (cows,bulls)
    '''
    cows  = 0
    bulls = 0

    for i in range(4):
        if guess[i] == goal[i]:
            cows += 1
        else:
            bulls += 1

    return (cows,bulls)

if __name__=="__main__":
    guess_count = 0
    goal = generate_goal()
    divided_goal = divide_num(goal)
    print("welcome to Cows and Bulls game\n")

    gameover = False
    while not gameover:
        guess = int(input("Enter your guess: "))
        while guess >9999 or guess <1000:
            guess = int(input("Please enter a 4 digit number: "))

        guess_count += 1

        divided_guess = divide_num(guess)
        check = check_cows_and_bulls(divided_guess,divided_goal)

        print(check[0],"cows and",check[1],"bulls")

        if check[0] == 4:
            print("Congratulations, you Win after", guess_count,"number of guesses")
            guess_count = 0
            goal = generate_goal()
            divided_goal = divide_num(goal)
            repeat = int(input("would you like to play again \n"
                           "1- Yes\n"
                           "2- No\n"))
            print("\n")
            if repeat != 1:
                gameover = True