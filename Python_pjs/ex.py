def superSales(dict):    


files = list()

files = input("Please provide the files' names: ").split()



for f in files:
    myDict = {}
    op=open(f,"r")
    result=[]
    lines = op.readlines()
    listSm = list()
    listPrice = list()

    for line in lines:
        cust,sm,price = line.split()
        
        myDict[sm] = (sm, price)
        
    op.close()
    # print(listSm)
    for key in myDict:
        print(key, ":", myDict[key])
    
            
            
   


