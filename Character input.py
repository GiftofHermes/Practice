#Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they will turn 100 years old.

#Êxtras Add on to the previous program by asking the user for another number and printing out that many copies of the previous message

name = input("Please enter your name: ")

age = input("Please enter your age: ")
age = int(age)

repeat = input("How many times should the message be repeated: ")
repeat = int(repeat)

over100 = 0
if age > 100:
    over100 = 1

if over100:

    print((name ,"you are already over 100 years old") * repeat)
else:
    remaining = 100 - age
    print((name, "there are", remaining, "years until you turn 100 years old") * repeat)

