# Module 6 Portfolio Milestone
# CSC500 William Vann

####################
# ITEM TO PURCHASE #
####################

# Define ItemToPurchase class
# this represents the items added to shopping cart

class ItemToPurchase:
   
    def __init__(self, name='none', price=0.0, quantity=0, description='none'):
        self.name = str(name)
        self.price = float(price)
        self.quantity = int(quantity)
        self.description = str(description)

    def print_item_cost(self):
        total_item_cost = round((self.price * self.quantity))
        print(f'{self.name} {self.quantity} @ ${self.price} = ${total_item_cost}')

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
        # print(f'Adding item object to cart list')
        self.cart.append(item_object)

    def remove_item(self, item_name):
        # print(f'Removing item name object from cart list')
        for item in self.cart:
            if item.name == item_name:
                self.cart.remove(item)
                return
        print(f'Item not found in cart. Nothing removed.')

    def modify_item(self, item_name):
        # print(f'Modifying item name object in cart list')
        for item in self.cart:
            if item.name == item_name:
                new_name = item_name
                new_price = float(input(f'Enter new price:\n'))
                new_quantity = int(input(f'Enter new quantity:\n'))
                new_description = str(input(f'Enter new description:\n')) 

                self.cart.remove(item)                              
                new_item_object = ItemToPurchase(new_name, new_price, new_quantity, new_description)
                
                self.cart.append(new_item_object)
                return
        print(f'Item not found in cart. Nothing modified.')

    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart:
            total_quantity += item.quantity
        return total_quantity
    
    def get_cost_of_cart(self):
        total_cost = 0.0
        for item in self.cart:
            total_cost += (item.quantity * item.price)
        return round(total_cost)
    
    def print_total(self):
        if self.cart:
            print(f"{self.name}'s Shopping Cart - {self.date}")
            print(f'Number of items: {self.get_num_items_in_cart()}')
            for item in self.cart:
                print(f'{item.name} {item.quantity} @ ${item.price} = ${item.quantity * item.price}')
            print(f'Total: ${self.get_cost_of_cart()}')
        else:
            print(f'SHOPPING CART IS EMPTY')

    def print_descriptions(self):
        if self.cart:
            print(f"OUTPUT ITEMS' DESCRIPTIONS")
            print(f"{self.name}'s Shopping Cart - {self.date}")
            print(f'Item Descriptions')
            for item in self.cart:
                print(f'{item.name}: {item.description}')            
        else:
            print(f'SHOPPING CART IS EMPTY')

    def output_shopping_cart(self):
        if self.cart:
            print(f'OUTPUT SHOPPING CART')
            print(f"{self.name}'s Shopping Cart - {self.date}")
            print(f'Number of Items: {self.get_num_items_in_cart()}')
            for item in self.cart:
                item.print_item_cost()     
            print(f'Total: ${self.get_cost_of_cart()}')       
        else:
            print(f'SHOPPING CART IS EMPTY')


#########################

# main user interaction menu

def print_menu(NewCart):
    choice = ''
    while True:
        print()
        print(f'====================================')
        print(f'                MENU                ')
        print(f'====================================')
        print(f'    a - Add item to cart            ')
        print(f'    r - Remove item from cart       ')
        print(f'    c - Change item quantity        ')
        print(f"    i - Output items' descriptions. ")
        print(f'    o - Output shopping cart.       ')  
        print(f'    q - Quit                        ')
        print(f'====================================')
        print()
        choice = input(f'Choose an option:\n')
        
        if choice == 'q':
            break

        elif choice == 'a':
            print()
            item_name = str(input('Enter the item name: \n'))
            item_price = float(input('Enter the item price: \n'))
            item_quantity = int(input('Enter the item quantity: \n'))
            item_description = str(input('Enter the item description: \n'))
            print()

            # create ItemToPurchase object
            item_object = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            
            # add to ShoppingCart
            NewCart.add_item(item_object)

        elif choice == 'r':
            item_name = input(f'Enter item name:\n')
            NewCart.remove_item(item_name)

        elif choice == 'c':
            print()
            item_name = input(f'Enter item name:\n')
            print()
            NewCart.modify_item(item_name)

        elif choice == 'i':
            print()
            NewCart.print_descriptions()

        elif choice == 'o':
            print()
            NewCart.output_shopping_cart()
        
        else:
            print()
            print(f'Please enter a valid choice.')
            choice = ''

############################   
   
if __name__ == "__main__":

    # Create new shopping cart and call menu function

    customer_name = input(f'Customer name:\n')
    current_date = input(f'Enter current date:\n')

    newCustomerCart = ShoppingCart(customer_name, current_date)

    print_menu(newCustomerCart)