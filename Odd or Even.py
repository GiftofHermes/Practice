#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
#Hint: how does an even / odd number react differently when divided by 2?

#If the number is a multiple of 4, print out a different message.

#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
#If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

first_number = input("Give me a number: ")
first_number = int(first_number)

second_number = input("Give me a second number: ")
second_number = int(second_number)

mod_check = first_number % second_number
mod4 = first_number % 4

first_word = ""

if mod_check == 0:
    print(first_number, "is divisible by", second_number)
    first_word = "Also"
elif mod_check != 0:
    print(first_number, "is not divisible by", second_number)
    first_word = "But"
if mod4 == 0:
    print(first_word, first_number, "is divisible by 4")