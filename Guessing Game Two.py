#You, the user, will have in your head a number between 0 and 100.
#The program will guess a number, and you, the user,
#will say whether it is too high, too low, or your number.

#At the end of this exchange, your program should print out
#how many guesses it took to get your number.

import random

print('Guess a number between 0 and 100')
print('Think about it for a moment. There is no need to rush')

num = random.randint(1,99)
guess_count = 1

print('I guess your number is ', num)
print('Is it high, low or just right')

guess_res = input()

minimum_guess = 0
maximum_guess = 100
while guess_res != 'just right':


    if guess_res == 'high':
        maximum_guess = num -1
        num = random.randint(minimum_guess,maximum_guess)
        guess_count +=1
        print('I guess your number is ', num)
        print('Is it high, low or just right')
        guess_res = input()
    if guess_res == 'low':
        minimum_guess = num +1
        guess_count +=1
        num = random.randint(minimum_guess,maximum_guess)
        print('I guess your number is ', num)
        print('Is it high, low or just right')
        guess_res = input()

print('haha i knew your number was', num)
print('I only guessed for', guess_count, 'just to mess with you')