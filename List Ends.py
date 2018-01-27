#Write a program that takes a list of numbers and makes a new list of only the first
#and last elements of the given list. For practice, write this code inside a function.

a = [5, 10, 15, 20, 25]

def first_and_last(a):
    b = a.pop()
    a = a[0:1]
    a.append(b)
    print(a)

first_and_last(a)