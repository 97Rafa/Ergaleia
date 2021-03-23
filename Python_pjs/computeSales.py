import os
from collections import Counter
from pathlib import Path

def allCharactersSame(s):
    n = len(s)
    for i in range(1, n):
        if s[i] != s[0]:
            return False

    return True

def newInput(i):
    f = open(i, "r", encoding='utf - 8')

    start = 0
    counter = 0
    op = ''

    for x in f.read().split("\n"):
        if allCharactersSame(x) == True:
            if start == 1:
                temp = open(str(counter) + ".txt", "w", encoding='utf - 8')
                temp.write(op)
                temp.close()
                op = ''
                counter += 1
        elif x == '':
            start = 0
        else:
            start = 1
            if op == '':
                op = x
            else:
                op = op + '\n' + x

    for i in range(counter):

        t = open(str(i) + ".txt", "r", encoding='utf - 8')
        for line in t.readlines():
            words = line.split()
            if words[0] == "ΑΦΜ:":
                afm = words[1]
            elif words[0] == "ΣΥΝΟΛΟ:":
                totalCost = words[1]
            else:
                if words[2] != " ":
                    quantity = words[1]
                    #price = words[2]
                    #totalPrice = words[3]
                    food = words[0].replace(":", "")
                    stats = open("statistics.txt", "a", encoding='utf - 8')
                    stats.write(afm + "\t" + food.upper() + "\t" + quantity + "\t" + "\n")
                    stats.close()
        t.close()

        os.remove(str(i) + ".txt")
    f.close()


def productDetails():
    stats = open("statistics.txt", "r", encoding='utf - 8')

    exists = False

    toBeSorted = list()
    for line in stats.readlines():
        words = line.split()
        toBeSorted.append(words[0] + "\t" + words[1] + "\t" + words[2])
    toBeSorted.sort()

    askedFood = input("Which food do you want to learn about?\n").upper()
    for line in toBeSorted:
        words = line.split()
        if len(words) == 0:
            continue
        elif words[1] == askedFood:
            print(words[0] + "\t" + words[2])
            exists = True


    if exists == False:
        print("The product was not found.\n")

    stats.close()

def afmDetails():
    stats = open("statistics.txt", "r", encoding='utf - 8')

    exists1 = False

    toBeSorted = list()
    for line in stats.readlines():
        words1 = line.split()
        toBeSorted.append(words1[1] + "\t" + words1[2] + "\t" + words1[0] + "\n")
    toBeSorted.sort()

    askedAfm = input("Which Customer do you want to learn about?\n")
    for line in toBeSorted:
        words = line.split()
        if len(words) == 0:
            continue
        elif words[2] == askedAfm:
            print(words[0] + "\t" + words[1])
            exists1 = True

    if exists1 == False:
         print("The customer was not found.\n")
    stats.close()


ans = True
while ans:

    print("""
    1.Read new input file
    2.Print statistics for a specific product
    3.Print statistics for a specific AFM
    4.Exit the program
    """)
    ans = input("\nGive your preference...\n")
    if ans == "1":
        y = input("\n Insert path of input.\n")
        x = input("\n Insert input name.\n")

        data_folder = Path(y)
        file_to_open = data_folder / x
        if os.path.exists(file_to_open) != True:
            print("This file does not exist...try again!\n")
            continue
        newInput(file_to_open)

        print("\n Receipt Added")
    elif ans == "2":
        productDetails()
    elif ans == "3":
        afmDetails()
    elif ans == "4":
        print("\n Goodbye!")
        break
    elif ans != "":
        print("\n Not Valid Choice Try again")


if os.path.exists("statistics.txt"):
    os.remove("statistics.txt")


