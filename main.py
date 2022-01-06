def main():
    import random

    # Open and read 'first.txt' and 'last.txt'
    fFirst = open('./data/first.txt', 'r') # reads file 'first.txt'
    firstList = [name.replace(',\n', '') for name in fFirst.readlines()] # cleans the data from ',\n' after the names

    fLast = open('./data/last.txt', 'r') # reads file 'first.txt'
    lastList = [name.replace(',\n', '') for name in fLast.readlines()]

    # Close files
    fFirst.close()
    fLast.close()

    # Randomly select a first and lastname
    while True:
        first = random.choice(firstList)
        last = random.choice(lastList)

        # Present the randomly generated name
        print("A name is chosen: {} {}".format(first, last))

        choice = input("Do you want another name? (Press 'Enter' else n or q to quit)\n")
        if choice.lower() == 'n' or choice.lower() == 'q':
            print('Exiting...')
            break
    # Option: Add 'user input' as to ask if they want to get a new name -> Repeat

# safe way of running python apps (good to have as a habit)
if __name__ == '__main__':
    main()