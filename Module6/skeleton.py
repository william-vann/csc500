# Module 6 Portfolio Milestone
# CSC500 William Vann

####################
# ITEM TO PURCHASE #
####################

class ItemToPurchase:
   
    def __init__(self, item_name='none', item_price=0.0, item_quantity=0, item_description='none'):
        self.item_name = str(item_name)
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)
        self.item_description = str(item_description)

    def print_item_cost(self):
        total_item_cost = round((self.item_price * self.item_quantity))
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_item_cost}')

#################
# SHOPPING CART #
#################

class ShoppingCart:

    def __init__(self, customer_name='none', current_date='January 1, 2020'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
            
        print(f'Item not found in cart. Nothing removed.')

    def modify_item(self, item):
        for item in self.cart_items:
            # if item.item_name == item_name:
                
            #     new_quantity = int(input(f'Enter new quantity:\n'))
            #     self.cart_items.append()
            #     return
            
        print(f'Item not found in cart. Nothing modified.')
    
    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity
    
    def get_cost_of_cart(self):
        total_cost = 0.0
        for item in self.cart_items:
            total_cost += (item.quantity * item.price)
        return round(total_cost)
    
    def print_total(self):
        if self.cart_items:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f'Number of items: {self.get_num_items_in_cart()}')
            for item in self.cart_items:
                print(f'{item.name} {item.quantity} @ ${item.price} = ${item.quantity * item.price}')
            print(f'Total: ${self.get_cost_of_cart()}')
        else:
            print(f'SHOPPING CART IS EMPTY')

    def print_descriptions(self):
        if self.cart_items:
            print(f"OUTPUT ITEMS' DESCRIPTIONS")
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f'Item Descriptions')
            for item in self.cart_items:
                print(f'{item.item_name}: {item.item_description}')            
        else:
            print(f'SHOPPING CART IS EMPTY')

    def output_shopping_cart(self):
        if self.cart_items:
            print(f'OUTPUT SHOPPING CART')
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f'Number of Items: {self.get_num_items_in_cart()}')
            for item in self.cart_items:
                item.print_item_cost()     
            print()       
        else:
            print(f'SHOPPING CART IS EMPTY')


#########################

def print_menu(ShoppingCart):
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
            item_description = str(input('Enter the item description: \n'))
            item_price = float(input('Enter the item price: \n'))
            item_quantity = int(input('Enter the item quantity: \n'))
            print()
            item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            ShoppingCart.add_item(item)

        elif choice == 'r':
            item = input(f'Enter item name:\n')
            ShoppingCart.remove_item(item)

        elif choice == 'c':
            print()
            item_name = input(f'Enter item name:\n')
            print()
            ShoppingCart.modify_item(item_name)

        elif choice == 'i':
            print()
            ShoppingCart.print_descriptions()

        elif choice == 'o':
            print()
            ShoppingCart.output_shopping_cart()
        
        else:
            print()
            print(f'Please enter a valid choice.')
            choice = ''

############################   
   
if __name__ == "__main__":

    # Create new shopping cart
    customer_name = input(f'Customer name:\n')
    current_date = input(f'Enter current date:\n')
    newCustomerCart = ShoppingCart(customer_name, current_date)
    print_menu(newCustomerCart)