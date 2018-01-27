#Write a password generator in Python. Be creative with how you generate passwords -
#strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
#The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.

#Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
import random

def get_level():
    level = str(input("How hard would you like your password to be: \n"
              "1-Easy \n"
              "2-Normal \n"
              "3-Hard \n"
              "4-Very Hard\n"))
    while level not in ("1","2","3","4"):
        level = str(input("Please enter 1,2,3 or 4. What you entered was not valid\n"))
    return level


with open("google-10000-english-master/google-10000-english-usa-no-swears-medium.txt", "r") as words:
    medium_words = words.read()
    medium_words = medium_words.split("\n")
    word_count = 5461

def easy_password():
    password = ""
    for i in range(2):
        password += medium_words[random.randint(1,word_count)]
    return password

#print(easy_password())

def normal_password():
    password = ""
    password += medium_words[random.randint(1,word_count)]

    password = password.title()
    password = password[0:-1] + password[-1].capitalize()
    nums = str(random.randint(10,99))
    password = password + nums
    return password

#print(normal_password())

def hard_password():
    password = ""
    num1 = str(random.randint(10,99))
    num2 = str(random.randint(10,99))
    word1 = medium_words[random.randint(1,word_count)]
    word2 = medium_words[random.randint(1,word_count)]
    while word1 == word2:
        word2 = medium_words[random.randint(1,word_count)]
    word1 = word1.replace("e","3")
    word1 = word1.replace("l","1")
    word2 = word2.title()
    word2 = word2[0:-1] + word2[-1].capitalize()
    word1 += num1
    word2 += num2
    password = word1 + word2
    return password

#print(hard_password())

def very_hard_password():
    password = ""
    num1 = str(random.randint(10,99))
    num2 = str(random.randint(10,99))
    word1 = medium_words[random.randint(1,word_count)]
    word2 = medium_words[random.randint(1, word_count)]
    while word2 == word1:
        word2 = medium_words[random.randint(1, word_count)]
    word3 = medium_words[random.randint(1, word_count)]
    while word3 == word1 or word3 == word1:
        word3 = medium_words[random.randint(1,word_count)]

    specials = ("&","%","+","?")
    #word transformations
    word1 = word1[0:1] + word1[1:].capitalize()
    word2 = word2[0:-1].title() + word2[-1].capitalize()
    word3 = word3[0:2] + word3[2:].capitalize()
    password = word1 + num1 + word2 + specials[random.randint(0,3)] + word3
    return password

#print(very_hard_password())

password_levels = (easy_password, normal_password, hard_password, very_hard_password)

level = int(get_level())

print(password_levels[level-1]())