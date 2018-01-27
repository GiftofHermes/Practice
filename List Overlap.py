#write a program that returns a list that contains only the elements that are common between the lists
#Make sure your program works on two lists of different sizes.

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#Randomly generate two lists to test this

def difference(a,b):
    a = set(a)
    b = set(b)
    c = a.intersection(b)
    return c

print(difference(a,b))

d = list()
e = list()
for i in range(12):
    d.append(random.randint(1,20))
    e.append(random.randint(1,20))

print("this is list 1:",d)
print("this is list 2:",e)
print("this is their intersection",difference(d,e))