while True:
    try:
        income = int(input("Please enter your taxable income in india: "))
    except ValueError:
        print("Sorry, We didn't understand that please enter taxable income as a number")
        continue
    else:
        break
if income <= 500000:
    tax = 0
elif income <= 750000: 
    tax = (income - 500000) * 0.10
elif income <= 100000: 
    tax = (income - 750000) * 0.20 + 25000 

else:
    tax = (income - 2500000) * 0.30 + 75000
print("you owe", tax, "Rupees in tax!")
