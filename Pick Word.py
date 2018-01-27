#In this exercise, the task is to write a function
# that picks a random word from a list of words
# from the SOWPODS dictionary.

import random
with open('.\\Writings\\sowpods.txt','r') as sowpods:
    sowpods_words = sowpods.read().split()
    line_num = random.randint(0, len(sowpods_words))
    print(sowpods_words[line_num])