#In Part 1, we loaded a random word list and picked a word from it.
# In Part 2, we wrote the logic for guessing the letter and displaying
# that information to the user. In this exercise,
# we have to put it all together and add logic for handling guesses.

#Only let the user guess 6 times, and tell the user how many guesses they have left.
# Keep track of the letters the user guessed.
# If the user guesses a letter they already guessed,
# don’t penalize them - let them guess again.

#When the player wins or loses, let them start a new game.

import random
word = ''
def random_word():
    with open('.\\Writings\\sowpods.txt','r') as sowpods:
        sowpods_words = sowpods.read().split()
        line_num = random.randint(0, len(sowpods_words))
        return sowpods_words[line_num]

guess_set = set()

guess = ''

win = False

def check_win():
    global guess
    global win

    if '_' in guess:
        win = False
    else:
        win = True

def guess_state(word,guess_set):
    global guess
    guess = ''
    for letter in word:
        if letter in guess_set:
            guess += letter + ' '
        else:
            guess += '_ '

game_continue = 'Yes'
while game_continue != 'No':
    win = False
    word = random_word()
    guess_state(word,guess_set)
    print(guess)

    guess_count = 0
    while (not win) and (guess_count < 7):
        guess_count += 1
        old_set_len = len(guess_set)
        old_guess = guess
        new_letter = input('Enter your guess: ')
        guess_set.add(new_letter)
        new_set_len = len(guess_set)
        if old_set_len == new_set_len:
            print('You already guessed', new_letter)
            guess_count -= 1
        guess_state(word, guess_set)
        new_guess = guess
        if old_guess != new_guess:
            guess_count -=1
        print(guess)
        check_win()

    if win:
        print('You win after', guess_count,'tries')
    else:
        print('haha, you lost. Word was', word)
    guess_set = set()
    game_continue = input('Do you want to continue? \n')