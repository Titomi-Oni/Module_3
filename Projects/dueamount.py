bill_amount = float(input("Enter total bill amount: "))
amount_paid = float(input("Enter amount paid: "))

change_amount = amount_paid - bill_amount

print("Cashier should give back:", change_amount)