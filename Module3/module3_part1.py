# Module 3 - Part 1
# This program calculates the total amount for a restaurant bill, including tip, and sales tax

# Percentage constants
tip_percent = 0.18
sales_tax_percent = 0.07

# Get user input for food charge
food_charge = float(input('\nEnter food cost: $ '))

# Calculate tip, sales tax, and total amount
tip_charge = food_charge * tip_percent
sales_tax_charge = food_charge * sales_tax_percent
total_amount = food_charge + tip_charge + sales_tax_charge

# Output results
print('Food charge: $', '{:.2f}'.format(food_charge))
print('Tip charge: $', '{:.2f}'.format(tip_charge))
print('Sales tax charge: $', '{:.2f}'.format(sales_tax_charge))
print('==========================')
print('Total amount: $', '{:.2f}'.format(total_amount), '\n')