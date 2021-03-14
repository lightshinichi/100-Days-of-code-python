bill_amt = float(input('Enter the bill amount $ '))
people_no = int(input('Enter the number of people '))
tip = int(input('Enter the tip amount % '))
amount_to_pay = (bill_amt + ((tip / 100) * bill_amt))/ people_no
print('Each should pay', round(amount_to_pay,2))
