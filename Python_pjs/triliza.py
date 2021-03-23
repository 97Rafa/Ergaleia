import numpy as np

def win(A):
    resultC = False
    resultR = False
    flag = True
    for x in range(0,3):
        
        #rows check
        r = A[[x],:]
        resultR = np.all(r == r[0,0])
        resultR = resultR and (1 in r  or 2 in r)

        #columns check
        c = A[:,[x]]
        resultC = np.all(c == c[0])
        resultC = resultC and (1 in c  or 2 in c)

        if resultC == True or resultR == True:
            flag = False
            print("\n\n_________ WIN _________\n")
        return flag
        

exit = False

while exit == False:
    A = np.zeros((3,3))
    player = input("Ποιος παίκτης παίζει πρώτος;(Είσοδος: 1 ή 2): ")

    gameOn = True
    while gameOn == True:
        while True:
            x,y = input("Παίκτη " + player + " σειρά σου:").split()  
            x = int(x)
            y = int(y)
            if x<=2 and x>=0 and y<=2 and y>=0:
                if A[x][y] == 0: 
                    break
                else:
                    print("Η θέση αυτή είναι πιασμένη. Δοκιμάστε ξανά")
            else:
                print("Η θέση αυτή δεν είναι έγκυρη.(Out of bounds)")

        if player == '1':
            A[x][y] = 1
            player = '2'
        elif player == '2':
            A[x][y] = 2
            player = '1'

        
        print(A)
        gameOn = win(A)

        if A.all() != 0:
            print("\n \n")
            print("###Game Over###")
            print("\n \n")
            gameOn = False


    while True:
        ans = input("Έξοδος: Y/y ή N/n: ")
        if ans == 'Y' or ans == 'y':
            exit = True
            print("### Καλή συνέχεια! ###")
            break
        elif ans == 'N' or ans == 'n':
            exit = False
            break
        else:
            print("Λάθος απάντηση. Παρακαλώ επιλέξτε ανάμεσα σε Y/y ή N/n: ")


