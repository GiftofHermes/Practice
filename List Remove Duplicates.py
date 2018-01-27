#Write a program (function!) that takes a list and returns a new list
#that contains all the elements of the first list minus all the duplicates.

#Write two different functions to do this - one using a loop and constructing a list, and another using sets.

import random

rand_list = []
for i in range(20):
    rand_list.append(random.randint(1,100))

def unique_with_sets(numbers):
    numbers = list(set(numbers))
    numbers.sort()
    return numbers

print(unique_with_sets(rand_list))

def unique_with_loops(numbers):
    unique = []
    for number in numbers:
        if number not in unique:
            unique.append(number)
    unique.sort()
    return unique

print(unique_with_loops(rand_list))