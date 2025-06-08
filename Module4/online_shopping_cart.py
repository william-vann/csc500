# Module 4 Portfolio Milestone
# CSC500 William Vann

# Define class for item purchase
class ItemToPurchase():
    # Default class constructor
    def __init__(self, item_name='none', item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    # Print item cost method
    def print_item_cost(self):
        self.transaction_cost = self.item_price * self.item_quantity
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.transaction_cost:.2f}')

# Function to gather user inputs
def get_user_input():
    item_name = str(input('Enter the item name: \n'))
    item_price = float(input('Enter the item price: \n'))
    item_quantity = int(input('Enter the item quantity: \n'))
    return item_name, item_price, item_quantity

# Create 2 objects from ItemToPurchase class, unpack user inputs
item1 = ItemToPurchase(*get_user_input())
item2 = ItemToPurchase(*get_user_input())

# Output results
print(f'TOTAL COST')
item1.print_item_cost()
item2.print_item_cost()
print(f'Total: ${(item1.transaction_cost + item2.transaction_cost):.2f}')