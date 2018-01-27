#Ask the user for a number and determine whether the number is prime or not.

num = int(input("Please enter a number: "))

divisor = num - 1


while divisor > 1:
    if (num / divisor) % 1  == 0.0:
        prime = False
        break

    divisor -= 1
    prime = True

if prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")