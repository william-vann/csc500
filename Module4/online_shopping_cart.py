# CSC500 William Vann
# Module 4 Portfolio Milestone
# Online Shopping Cart




class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        transaction_cost = self.item_price * self.item_quantity
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${transaction_cost}')

# Step 2: Prompt user for 2 items and create 2 class objects
'''

Example:

Item 1
Enter the item name:
Chocolate Chips
Enter the item price:
3
Enter the item quantity:
1

Item 2
Enter the item name:
Bottled Water
Enter the item price:
1
Enter the item quantity:
10

'''

# Set number of user prompts (2 for this example)
num_user_prompts = 2

for i in range(1, num_user_prompts+1):
    print(f'Item {i}')
    item_name = str(input('Enter the item name:\n')))
    item_price = float(input('Enter the item price:\n'))
    item_quantity = int(input('Enter the item quantity:\n'))
    
    # Create an instance of ItemToPurchase
    item = ItemToPurchase(item_name, item_price, item_quantity)
    
# Step 3: Add costs of the 2 items and print the total cost
''' 

Example:

TOTAL COST

Chocolate Chips 1 @ $3 = $3

Bottled Water 10 @ $1 = $10

Total: $13 

'''
print(f'TOTAL COST\n')

total_cost = 0.0

for i in range(1, num_user_prompts+1):
    print(f'{item}')
print(f'\nTotal: ${total_cost}')


