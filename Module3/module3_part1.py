# Module 3 - Part 1
# This program calculates the total amount for a restaurant bill, including tip, and sales tax.

# percentage constants
tip_percent = 0.18
sales_tax_percent = 0.07

# get user input for food charge
food_charge = float(input('Enter food cost: $ '))

# calculate tip, sales tax, and total amount
tip_charge = food_charge * tip_percent
sales_tax_charge = food_charge * sales_tax_percent
total_amount = food_charge + tip_charge + sales_tax_charge

# output results
print('Food charge: $', '{:.2f}'.format(food_charge))
print('Tip charge: $', '{:.2f}'.format(tip_charge))
print('Sales tax charge: $', '{:.2f}'.format(sales_tax_charge))
print('Total amount: $', '{:.2f}'.format(total_amount))