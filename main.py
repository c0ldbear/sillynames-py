
# Open and read 'first.txt' and 'last.txt'
fFirst = open('./data/first.txt', 'r') # reads file 'first.txt'
first = [name.replace(',\n', '') for name in fFirst.readlines()] # cleans the data from ',\n' after the names

fLast = open('./data/last.txt', 'r') # reads file 'first.txt'
last = [name.replace(',\n', '') for name in fLast.readlines()]

# Randomly select a first and lastname

# Present the randomly generated name

# Option: Add 'user input' as to ask if they want to get a new name -> Repeat