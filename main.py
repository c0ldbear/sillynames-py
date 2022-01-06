import random

def main():
    # Open and read 'first.txt' and 'last.txt'
    firstnamesFilename = './data/first.txt'
    lastnamesFilename = './data/last.txt'
    firstList = GetListOfNamesFromFile(firstnamesFilename)
    lastList = GetListOfNamesFromFile(lastnamesFilename)

    # Randomly select a first and lastname
    while True:
        first = GetRandomNameFromList(firstList)
        last = GetRandomNameFromList(lastList)

        # Present the randomly generated name
        DisplayFullName(first, last)

        # Option: Add 'user input' as to ask if they want to get a new name -> Repeat
        if ContinueOrExitApp():
            break

def GetListOfNamesFromFile(filename):
    file = open(filename, 'r')
    nameList = [name.replace(',\n', '') for name in file.readlines()]
    file.close() # Don't forget to close the file once done
    return nameList

def GetRandomNameFromList(listOfNames):
    return random.choice(listOfNames)

def DisplayFullName(first, last):
        print("A name is chosen: {} {}".format(first, last))

def ContinueOrExitApp():
    choice = input("Do you want another name? (Press 'Enter' else n or q to quit)\n")
    if choice.lower() == 'n' or choice.lower() == 'q':
        print('Exiting...')
        return True 
    return False

# safer way of running python apps (good to have as a habit)
if __name__ == '__main__':
    main()