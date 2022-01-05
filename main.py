import random

# Open and read 'first.txt' and 'last.txt'
fFirst = open('./data/first.txt', 'r') # reads file 'first.txt'
firstList = [name.replace(',\n', '') for name in fFirst.readlines()] # cleans the data from ',\n' after the names

fLast = open('./data/last.txt', 'r') # reads file 'first.txt'
lastList = [name.replace(',\n', '') for name in fLast.readlines()]

# Randomly select a first and lastname

first = random.choice(firstList)
last = random.choice(lastList)

# Present the randomly generated name
print("A new name is chosen: {} {}".format(first, last))

# Option: Add 'user input' as to ask if they want to get a new name -> Repeat