#Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
#File 1 contains prime numbers up to 1000
#Fİle 2 contains happy numbers up to 1000

primes = []
with open('Writings/primenumbers.txt', 'r') as primeFile:
    for line in primeFile:
        primes.append(int(line))

happies = []
with open('Writings/happynumbers.txt', 'r') as happyFile:
    for line in happyFile:
        happies.append(int(line))



overlaps = set(primes).intersection(set(happies))
print('These are the primes: ', primes)
print('These are the happies: ', happies)
print('These are the overlapping numbers: ', overlaps)
