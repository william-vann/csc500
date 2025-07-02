# full_shopping_app.py
# CSC500 Portfolio Project
# William Vann

# Function to gather user inputs
def get_user_input():
    print('=' * 50)
    while True:
        
        try:
            item_name = str(input('Enter the item name: \n'))
            item_price = float(input('Enter the item price: \n'))
            item_quantity = int(input('Enter the item quantity: \n'))
            item_description = str(input('Enter the item description: \n'))
            return item_name, item_price, item_quantity, item_description
        
        except (ValueError, TypeError):
            print('Could not parse item information. Try again!')
            
# # Output results
def print_total_cost(item1, item2):
    print(f'\nTOTAL COST')
    print('=' * 50)

    item1.print_item_cost()
    item2.print_item_cost()
    print(f'TOTAL: ${(item1.total_item_cost + item2.total_item_cost):.2f}')

####################
# ITEM TO PURCHASE #
####################

# Define ItemToPurchase class
# this represents the items added to shopping cart

class ItemToPurchase:
   
    def __init__(self, name='none', price=0.00, quantity=0, description=''):
        self.name = str(name)
        self.price = float(price)
        self.quantity = int(quantity)
        self.description = str(description)

    def print_item_cost(self):
        self.total_item_cost = (self.price * self.quantity)
        print(f'{self.name} {self.quantity} @ ${self.price:.2f} = ${self.total_item_cost:.2f}')

#################
# SHOPPING CART #
#################

# Define ShoppingCart class
# this represents the record of customer shopping on a particular date

class ShoppingCart:

    def __init__(self, name='none', date='January 1, 2020'):
        self.name = str(name)
        self.date = str(date)
        self.cart = []

    def add_item(self, item_object):       
        self.cart.append(item_object)
        print(f'{item_object.name} ADDED SUCCESSFULLY.')

    def remove_item(self, item_name):
        for item in self.cart:
            if item.name == item_name:
                self.cart.remove(item)
                print(f'{item.name} REMOVED SUCCESSFULLY.')
                return
        print(f'ITEM NOT FOUND IN CART. NOTHING REMOVED.')

    def modify_item(self, item_name):
        for item in self.cart:
            if item.name == item_name:
                new_name = item_name
                new_price = item.price
                new_quantity = int(input(f'Enter new quantity:\n'))
                if new_quantity == 0:
                    self.cart.remove(item)
                    print(f'{item.name} REMOVED SUCCESSFULLY.')
                    return
                else:
                    new_description = item.description 

                self.cart.remove(item)                              
                new_item_object = ItemToPurchase(new_name, new_price, new_quantity, new_description)
                
                self.cart.append(new_item_object)
                print(f'QUANTITY CHANGED TO {new_quantity}.')
                return
        print(f'ITEM NOT FOUND IN CART. NOTHING MODIFIED.')

    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart:
            total_quantity += item.quantity
        return total_quantity
    
    def get_cost_of_cart(self):
        total_cost = 0.0
        for item in self.cart:
            total_cost += (item.quantity * item.price)
        return f'{total_cost:.2f}'
    
    def print_total(self):
        if self.cart:
            print('=' * 50)
            print(f"{self.name}'s SHOPPING CART - {self.date}")
            print('=' * 50)
            print(f'NUMBER OF ITEMS: {self.get_num_items_in_cart()}')
            for item in self.cart:
                print(f'{item.name} {item.quantity} @ ${item.price} = ${(item.quantity * item.price):.2f}')
            print('=' * 50)
            print(f'TOTAL: ${self.get_cost_of_cart()}')
        else:
            print(f'SHOPPING CART IS EMPTY\n')

    def print_descriptions(self):
        if self.cart:
            print('=' * 50)
            print(f"OUTPUT ITEMS' DESCRIPTIONS")
            print('=' * 50)
            print(f"{self.name}'s SHOPPING CART - {self.date}")
            print(f'ITEM DESCRIPTIONS')
            print('-' * len('ITEM DESCRIPTIONS'))
            for item in self.cart:
                print(f'{item.name}: {item.description}')            
        else:
            print(f'SHOPPING CART IS EMPTY\n')

    def output_shopping_cart(self):
        if self.cart:
            # print('=' * 50)
            # print(f'OUTPUT SHOPPING CART')
            print('=' * 50)
            print(f"{self.name}'s SHOPPING CART - {self.date}")
            print('=' * 50)

            print(f'NUMBER OF ITEMS: {self.get_num_items_in_cart()}')
            print('-' * 50)
            for item in self.cart:
                item.print_item_cost()     
            print('-' * 50)
            print(f'TOTAL: ${self.get_cost_of_cart()}')       
        else:
            print(f'SHOPPING CART IS EMPTY\n')


#########################

# main user interaction menu

def print_menu(NewCart):
    choice = ''
    while True:
        print()
        print('=' * 30)
        print(' ' * 12, 'MENU')
        print('=' * 30)
        print('a - Add item to cart')
        print('r - Remove item from cart')
        print('c - Change item quantity')
        print("i - Output items' descriptions")
        print('o - Output shopping cart')  
        print('q - Quit')
        print('=' * 30)
        print()
        choice = input(f'Choose an option:\n')
        
        if choice == 'q':
            break

        elif choice == 'a':
            print('=' * 50)
            
            # create ItemToPurchase object
            item_object = ItemToPurchase(*get_user_input())

            # add to ShoppingCart
            NewCart.add_item(item_object)

        elif choice == 'r':
            print('=' * 50)
            item_name = input(f'Enter item name:\n')
            NewCart.remove_item(item_name)

        elif choice == 'c':
            print('=' * 50)
            item_name = input(f'Enter item name:\n')
            NewCart.modify_item(item_name)
            
        elif choice == 'i':
            print()
            NewCart.print_descriptions()

        elif choice == 'o':
            print()
            NewCart.output_shopping_cart()
        
        else:
            print()
            print(f'PLEASE ENTER A VALID CHOICE!\n')
            choice = ''

############################   
   
if __name__ == "__main__":

    # Create 2 items from ItemToPurchase class, unpack user inputs
    item1 = ItemToPurchase(*get_user_input())
    item2 = ItemToPurchase(*get_user_input())

    # Add the costs of the two items and output the total cost
    print_total_cost(item1, item2)

    # Create new shopping cart and call menu function
    print('=' * 50)
    customer_name = input(f'Customer name:\n')
    current_date = input(f'Enter current date:\n')

    newCustomerCart = ShoppingCart(customer_name, current_date)
    newCustomerCart.add_item(item1)
    newCustomerCart.add_item(item2)

    print('=' * 50)
    print(f'WELCOME {customer_name}, 2 ITEMS ADDED TO YOUR CART!\n')
    
    print_menu(newCustomerCart)