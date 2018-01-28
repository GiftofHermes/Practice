#Create a dictionary (in your file) of names and birthdays.
# When you run your program it should ask the user to
# enter a name, and return the birthday of that person back to them.

data = {
    'Albert Einstein': '14/03/1879',
    'Benjamin Franklin': '17,01,1706',
    'Ada Lovelace': '10,12,1815'
}

print('We have birthdate data of')
for key in data:
    print('-{}'.format(key))

person = input("Who's birthday you want to look up?\n")
if person in data:
    print('Birthday of {person} is {bday}'.format(bday= data[person], person= person))
else:
    print('person you entered is not valid')