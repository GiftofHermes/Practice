#Ask the user for a string and print out whether this string is a palindrome or not.
#(A palindrome is a string that reads the same forwards and backwards.)

word = input("Please enter a word: ")
rev_word = word[::-1]

if word == rev_word:
    print(word, "is a palindrome")
else:
    print(word,"is not a palindrome")