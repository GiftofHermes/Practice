#Read the Training_01.txt file. Count how many of each “category” of each image there are

category = dict()
with open('Writings/Training_01.txt', 'r') as file:
    for line in file:
        img = file.readline()
        img = img.split('/')
        if img[2] in category:
            category[img[2]] += 1
        else:
            category[img[2]] = 1


print(category)

