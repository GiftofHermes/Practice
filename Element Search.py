#Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number.
#The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

#Use binary search.

import numpy

ordered = numpy.random.randint(0,200,100)
ordered = sorted(ordered)
print(ordered)


def search(list, num):
    while list.__len__() > 1:
        print(list)
        print("This is number: ", num)
        if list[list.__len__()// 2] > num:
            print(list.__len__()// 2)
            list = list[:list.__len__() // 2]
        else:
            list = list[list.__len__() // 2:]

    if list[0] == num:
        return True
    else:
        return False


answer = search(ordered,28)
print("this is the answer of search function", answer)
