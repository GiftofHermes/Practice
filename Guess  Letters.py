#For this exercise, write the logic that asks a player to guess a letter
# and displays letters in the clue word that were guessed correctly.
# For now, let the player guess an infinite number of times until
# they get the entire word.

# As a bonus, keep track of the letters the player guessed
# and display a different message if the player tries to guess
# that letter again.

# Remember to stop the game when all the letters have been guessed correctly!

word = 'EVAPORATE'

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

guess_state(word,guess_set)
print(guess)

guess_count = 0
while not win:
    guess_count += 1
    old_set_len = len(guess_set)
    new_letter = input('Enter your guess: ')
    guess_set.add(new_letter)
    new_set_len = len(guess_set)
    if old_set_len == new_set_len:
        print('You already guessed', new_letter)
    guess_state(word, guess_set)
    print(guess)
    check_win()

print('You win after', guess_count,'tries')
