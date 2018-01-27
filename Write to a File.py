#Get a file name from the user. Write something to a file named as such.

file_name = input("Please enter a file name : ")

with open('Writings/'+file_name+".txt",'w') as file:
    file.write("Some text to write to a file")