def GetNamesFromFile(filename):
    file = open(filename, 'r')
    nameList = [name.replace(',\n', '') for name in file.readlines()]
    file.close() # Don't forget to close the file once done
    return nameList

def main():
    import random

    # Open and read 'first.txt' and 'last.txt'
    firstnamesFilename = './data/first.txt'
    lastnamesFilename = './data/last.txt'
    firstList = GetNamesFromFile(firstnamesFilename)
    lastList = GetNamesFromFile(lastnamesFilename)

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