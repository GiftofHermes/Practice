#Generate a random number between 1 and 9 (including 1 and 9).
#Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

#Keep the game going until the user types “exit”

#Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

number = random.randint(1,10)

counter = 0
guess = False
while guess != True:
    counter += 1
    num1 = input("Guess a number between 1 and 10: ")
    if num1 == "exit":
        print("Exiting the game")
        print("Done")
        break
    num1 = int(num1)
    if num1 < number:
        print("Number you entered is too low")
    elif num1 > number:
        print("Number you entered is too high")
    elif num1 == number:
        print("Bingo, the number was", number)
        guess = True
        print("You have found the number after",counter,"tries")