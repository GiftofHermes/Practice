# Implement a function that takes as input three variables,
# and returns the largest of the three.
# Do this without using the Python max() function!

largest_num = 0
numbers = input('Enter three numbers with , as seperator \n').split(',')
num1 ,num2, num3 = [int(num) for num in numbers]

largest_num = num1
if num2 > largest_num:
    largest_num = num2
if num3 > largest_num:
    largest_num = num3

print('largest number is', largest_num)
