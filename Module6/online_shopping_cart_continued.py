# Module 6 Portfolio Milestone
# CSC500 William Vann

#############################################
# STEP 1
#############################################
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

#############################################
# STEP 2
#############################################
# Function to gather user inputs
def get_user_input():
    item_name = str(input('Enter the item name: \n'))
    item_price = float(input('Enter the item price: \n'))
    item_quantity = int(input('Enter the item quantity: \n'))
    return item_name, item_price, item_quantity

# Create 2 objects from ItemToPurchase class, unpack user inputs
item1 = ItemToPurchase(*get_user_input())
item2 = ItemToPurchase(*get_user_input())


#############################################
# STEP 3
#############################################
# Output results
print(f'TOTAL COST')
item1.print_item_cost()
item2.print_item_cost()
print(f'Total: ${(item1.transaction_cost + item2.transaction_cost):.2f}')

#############################################
# STEP 4
#############################################
# Define class for shopping cart

class OnlineShoppingCart():
    # Default class constructor
    def __init__(self, customer_name='none', current_date='January 1, 2020'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # Add item method
    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    # Remove item method
    def remove_item(self, ItemToPurchase.item_name):
        if ItemToPurchase.item_name not in self.cart_items:
            print(f'Item not found in cart. Nothing removed.')
        else:
            self.cart_items.remove(ItemToPurchase.item_name)

    # Modify item method
    def modify_item(self, ItemToPurchase):
        if ItemToPurchase.item_name not in ItemToPurchase.cart_items:
            print(f'Item not found in cart. Nothing modified.')
        else:
            pass # check if parameter has default values for description, price, and quantity. If not, modify item in cart.


    # Get num items in cart method
    def get_num_items_in_cart(self):
        return len(self.cart_items)


    # Get cost of cart method
    def get_cost_of_cart(self):
        cost_of_cart = [(item.price*item.quantity) for item in self.cart_items]
        return '{:.2f}'.format(sum(cost_of_cart))

    # Print total method
    def print_total(self):
        pass

    # Print descriptions method
    def print_descriptions(self):
        pass


#############################################
# STEP 5
#############################################

# Implement print_menu() function

def print_menu(ShoppingCart):
    pass



#############################################
# STEP 6
#############################################

# Implement output_shopping_cart__menu() function

def output_shopping_cart_menu(ShoppingCart):
    pass

#############################################
# MAIN
#############################################

def main()
    pass

