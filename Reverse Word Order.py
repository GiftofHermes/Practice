#Write a program (using functions!) that asks the user for a long string containing multiple words.
#Print back to the user the same string, except with the words in backwards order.

string = "Python has a lot of interesting things you can do with strings. I will show a few here, but you can see many more methods that may or may not be useful at the official Python documentation about the string format. Remember that strings are lists."

def reverse_word_order(string):
    words = string.split()
    words = words[::-1]
    string = " ".join(words)
    return string

print(reverse_word_order(string))