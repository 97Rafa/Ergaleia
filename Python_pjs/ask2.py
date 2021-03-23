total = 0
counter = 0
average = 0

cust_dict = {}
while True:
    counter = counter + 1

    customer = input("Δώστε το όνομα του πελάτη: ")

    if customer == "end" :
        break

    mon_spent = int(input("Δώστε πόσα χρήματα ξόδεψε ο πελάτης: "))
    cust_dict[customer] = mon_spent

    total = total + mon_spent 

average = total / counter

for keys in cust_dict:
    
    if cust_dict[keys] > average:
        print(keys)




