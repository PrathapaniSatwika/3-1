income=int(input())
tax_payable = 0
if income <= 500000:
    tax_payable = 0
elif (income > 500000 and income <= 750000): 
    tax_payable = (income - 500000) * 0.10
elif (income > 750000 and income <= 100000): 
    tax_payable = tax_payable + (income - 750000) * 0.20 

else:
    tax_payable = tax_payable + (income - 2500000) * 0.20
    tax_payable += tax_payable + (income - 1000000)*0.30
print(tax_payable)
