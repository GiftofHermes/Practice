#load the birthday dictionary from a JSON file on disk,
# rather than having the dictionary defined in the program.

#Ask the user for another scientist’s name and birthday
#  to add to the dictionary, and update the JSON file
# you have on disk with the scientist’s name.

import json

with open('Writings/info.json', 'r') as f:
    info = json.load(f)

print('We have birthdate data of')
for key in info:
    print('-{}'.format(key))

person = input("Who's birthday you want to look up?\n")
if person in info:
    print('Birthday of {person} is {bday}'.format(bday= info[person], person= person))
else:
    print('person you entered is not valid')

add = input('Do you want to add another birthdate to our database?\n')
if(add == 'Yes'):
    new_person, new_birthday = input('Enter: as Xxxxx Xxxx,DD/MM/YYYY\n').split(',')
    info[new_person] == new_birthday
    with open('Writings/info.json', 'w') as f:
        json.dump(info,f)

