days = 1
month = []
total = 0
while days <= 30:
    income = int(input("Παρακαλώ παραχωρήστε το εισόδημα για τη μέρα " + str(days) + " : "))

    month.append(income)
    days = days + 1
    total = total + income

average = total / 30
print("\nΟ μέσος όρος των μισθών είναι: ", average)

low_inc_days = 0
for data in month:
    if data < average:
        low_inc_days = low_inc_days + 1

print(low_inc_days, " μέρες του μήνα ο μισθός ήταν χαμηλότερος απ' τον μέσο όρο.")        
