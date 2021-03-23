import random

def random_line(f):
    line = next(f)
    for num, aline in enumerate(f, 2):
      if random.randrange(num): continue
      line = aline
    return line

def listToString(s):      
    # initialize an empty string 
    str1 = ""      
    # traverse in the string   
    for ele in s:  
        str1 = str1 + ' ' + ele      
    # return string   
    return str1  

def play_again():
    while True:
        keep_playing = input("\nDo you want to play another round?(y/n): ")
        if keep_playing == 'y' or keep_playing == 'Y':
            gameOn = True
            break
        elif keep_playing == 'n' or keep_playing == 'N':
            gameOn = False
            break
        else:
            print("Incorrect Answer. Please answer yes or no(y/n)")

    return gameOn


# -------------------MAIN------------------------------- #
print("######## Welcome to Hangman! ########\n")


gameOn = True
while gameOn == True:
    f = open('sowpods.txt')
    word = random_line(f)
    delim = "_"
    print(word)    
    wordl = len(word)

    toComp = []
    for i in range(wordl-1):
        toComp.append('_')

    wrong = "_ _ _ _ _ _"

    while True:
        print("\n",listToString(toComp),"\tIncorect Letters: ", wrong, "\n \n")
        

        letter = (input("\nGuess a letter: ")).upper()
        if word.find(letter) != -1 :
            for i in range(len(word)):
                if(word[i] == letter ):
                    toComp[i] = letter
        else:
            print("\nYou guessed wrong :(")
            #========== TO DO ============
            if wrong.find(delim) != -1:
                wrong = wrong.replace(delim, letter, 1)
            else:
                print("\n======== You run out of lifes ========\n")  
                break

        if listToString(toComp).find('_') == -1:
            print("\nBravoo! You ve won! :)\n")
            break
    gameOn = play_again()
    

print("\n### See you soon. Bye! ###")