#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

number = input("Please enter a number: ")
number = int(number)
divisor = number -1

divisors = []

while divisor > 0:
    if divisor % 10000 == 0:
        print(divisor)
    if number % divisor == 0:
        divisors.append(divisor)
    divisor -= 1

print("number", number, "'s divisors are:", divisors)