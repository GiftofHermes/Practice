#Time for some fake graphics! Let’s say we want to draw game boards that look like this:
#
# --- --- ---
#|   |   |   |
# --- --- ---
#|   |   |   |
# --- --- ---
#|   |   |   |
# --- --- ---

#This one is 3x3
#Ask the user what size game board they want to draw, and draw it for them

print('How long and wide do you want the game board to be? \n')
n = input('for nxn n is : ')

while (not isinstance(n, int)):
    try:
        n = int(n)
    except:
        n = input('value you entered is not a valid number. Please enter again. n : ')

for i in range(n):
    print(' ---' * (n))
    if i+1 != n:
        print('|   ' * (n-1) + '|   |')
