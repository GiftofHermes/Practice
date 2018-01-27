#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
#Take this opportunity to think about how you can use functions.
#Make sure to ask the user to enter the number of numbers in the sequence to generate.

def fibonacci(n):
    series = []
    x = 0
    y = 1
    for i in range(n):
        series.append(y)
        x,y = y, x+y

    print(series)

n = int(input("How many numbers of fibonacci series do you want to see: "))

fibonacci(n)

