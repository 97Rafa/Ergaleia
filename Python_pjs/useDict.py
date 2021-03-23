def makeDictionary():
    f=open('inputTeams')
    myList=list(f.read().splitlines()) 
    myDict={}
    for i in myList:
        line=i
        lab=line[:6]
        xy=line[7:]
        myDict[lab]=xy
    return myDict


def connectTeams(myDict):
    tmp=0
    for i in range (len(myDict)):
        lstK=list(myDict.keys())
        lstV=list(myDict.values())
    tmp2=0 
    ps=int(len(lstV))
    el=lstV[ps-1]
    for i in lstV:
        tmp2+=1
        if len(i)==11:
            tmp=tmp+1
            if (tmp%2)!=0:
                pos=i
            if tmp%2==0:
                for j in range (0,ps):
                    if pos in lstV[j]:
                        lstK.append(lstK[j])
                        lstV.append(i+' '+pos)
                        break
                if tmp2==ps:
                    break
    i=0
    while i!=ps:
        if len(lstV[i])==11:
            del(lstV[i])
            del(lstK[i])
            i=0
        else:
            i+=1
        ps=int(len(lstV))
        if el==lstV[i]:
            break
    
    res = {} 
    for key in lstK: 
        for value in lstV: 
            res[key] = value 
            lstV.remove(value) 
            break  
    return res
    


myDict=makeDictionary()
choice=0
while choice!=5:
    print("\n1.Team Connection")
    print("2.Print Teams")
    print("3.Search Spesific Team")
    print("4.Search Spesific Student")
    print("5.Exit")
    choice = int(input("What do you want to do? ")) 
    if choice==1:
        myDictCon=connectTeams(myDict)
        print("Teams after connection is:")
        # for keys in myDictCon:
        #     print(keys, ":", myDictCon[keys])
        myDict=myDictCon
    elif choice == 2:
        f = open("outputTeams", "w")
        for key in myDict:            
            print(key, ":", myDict[key])
            f.write(key + ":" + str(myDict[key]) + "\n")
        f.close()
    elif choice == 3:
        teamToPrint = input("\nWhich group are you looking for? : ")
        if teamToPrint in myDict:
            print("\nThe students of this group are the following: ", myDict[teamToPrint])
        else:
            print("\nThis group does not exist.")
    elif choice == 4:
        temp = "The student does not exist in the lab."
        studToFind = str(input("\n Who are you looking for? : "))
        for key in myDict:
            st1 = " "
            st2 = " "
            if len(myDict[key]) == 11:
                st1 = myDict[key]
            else:
                st1, st2 = myDict[key].split()
            
            if studToFind == str(st1) or studToFind == str(st2):
                temp = key

        print(temp)
    elif choice==5:
        print("Exit..")
        break
    else:
        print("Choice out of bound, try again..")