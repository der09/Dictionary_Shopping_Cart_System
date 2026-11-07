# Diane Hsieh 
# AM 
# Shopping Cart System with Dictionary
# import 

from datetime import date
date = date.today()
# dictionary of products 
products = {
     "Chips": 2.99, 
     "Apple": 2.50, 
     "Candy": 1.50, 
     "Cookie": 3.00, 
     "Water": 1.00, 
     "Coffee": 5.00
     }


# empty dictionary to add in based off user 
shopping_cart = {}


def main_menu(products, shopping_cart):
    
    print() 
    print() 
    
    print(" ========== SMART SHOPPING CART ========== ")
    print("1. View Available Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Shopping Cart")
    print("5. View Current Total")
    print("6. Checkout")
    print() 

    choice = int(input("Enter your choice: "))
    while choice > 6 or choice < 1: 
        print("Invalid")
        choice = int(input("Enter your choice: "))
    return choice

# gets user's first choice 
choice = main_menu(products, shopping_cart)

def available_products(products): 
# customer chooses option 1 : view available products 
    print(" ======== AVAILABLE PRODUCTS ======== ")
    for index, (item, price) in enumerate(products.items()): 
        print(f"{index + 1}. {item}  ${price:.2f}")

def add_product(products, shopping_cart):
    # customer chooses option 2: add product to cart 
    print("Which product would you like to add?")
    for index, (item, price) in enumerate(products.items()): 
            print(f"{index + 1}. {item}  ${price:.2f}")
    chosen = int(input("Enter product number: "))

    # to validate that product number exists 
    while (chosen < 1 or chosen > len(products)):
        print("Invalid product!")
        chosen = int(input("Enter product number: "))

    quantity = int(input("How many would you like to add?: "))
    while quantity < 0: 
        print("Not valid")
        quantity = int(input("How many would you like to add?: "))

    # adds product to shopping cart
    product = list(products)[chosen - 1]
    shopping_cart[product] = shopping_cart.get(product, 0) + quantity
    print(f"{list(products)[chosen - 1]} was added to your cart!")
    print(f"{list(products)[chosen - 1]} quantity is now {quantity}")


def remove_product(shopping_cart):
# customer chooses option 3: remove product from cart 
    
    print(" ======== YOUR SHOPPING CART ======== ")

    #if shopping cart has nothing in it 
    if len(shopping_cart) == 0:
        print("Your shopping cart is empty!")
        print("There is nothing to remove.")
    else:
        # displaying the current shopping cart
        for index, (item, quantity) in enumerate(shopping_cart.items()): 
                print(f"{index + 1}. {item}  ${quantity}")
        print("Which item would you like to remove?")
        remove = int(input("Enter the item number: "))
    
        # validate that the item number exists in the cart
        while (remove < 1 or remove > len(shopping_cart)):
            print("Invalid item number!")
            print("Please choose a number between 1 and", len(shopping_cart))
            remove = int(input("Enter the item number: "))

        # removes item from cart 
        print(f"Removed 1 {list(shopping_cart)[remove - 1]} from your cart!")
        new_quantity = shopping_cart[list(shopping_cart)[remove - 1]] - 1 
        print([list(shopping_cart)[remove - 1]], "quantity is now", new_quantity)

        # when quantity is zero 
        if new_quantity == 0: 
            del shopping_cart[list(shopping_cart)[remove - 1]]


# sees what's in the shopping cart 
def view_cart(products, shopping_cart):
    # customer chooses option 4: view shopping cart

    total_items = 0 
    subtotal = 0 
    print(" ======== YOUR SHOPPING CART ======== ")
    if len(shopping_cart) == 0:
        print("Your shopping cart is empty!")
    else:
        # displaying the current shopping cart
        print("Product     Unit Price     Quantity     Line Total")
        for index, (item, quantity) in enumerate(shopping_cart.items()): 
            print(f"{index+1}. {item}      ${(products[item]):.2f}          {quantity}          ${(products[item] * quantity):.2f}")

            total_items += quantity
            subtotal += (products[item] * quantity)
        print() 

        print(f"Total Items:   {total_items}")
        print(f"Subtotal   :  ${subtotal:.2f}")


# find the subtotal
def current_total(products, shopping_cart): 
    price = 0 
    for item, quantity in shopping_cart.items():
        price += (products[item] * quantity)
    print()
    print(f"Total ${price:.2f}")
    return price 

# while loop 
# what runs the code 
while choice != 6 or len(shopping_cart) == 0: 
    if choice == 1 : 
        available_products(products)
        print()
    elif choice == 2: 
        add_product(products, shopping_cart)
        print()
    elif choice == 3: 
        remove_product(shopping_cart) 
        print()
    elif choice == 4: 
        view_cart(products, shopping_cart) 
        print()
    elif choice == 5: 
        current_total(products, shopping_cart) 
        print()
    elif choice == 6: 
        print("cannot checkout")
        print()
        break
    choice = main_menu(products, shopping_cart)


# makes a variable for the funciton of current total
total = current_total(products, shopping_cart) 

#checks if eligible for any discounts
def checkout_and_discounts(total): 
    discount = 0 

    if total > 40: 
        discount = 0.15 
    elif total >= 20: 
        discount = 0.10 
    elif total >= 10: 
        discount = 0.05

    return discount 

print() 
amount_saved = total * checkout_and_discounts(total)
final_total = total - amount_saved 


print()

# the end 
# the receipt 
print() 
print(" ========== RECEIPT ========== ")
print(date)
print() 
if total > 0: 
    print("Product     Unit Price     Quantity     Line Total")
    for index, (item, quantity) in enumerate(shopping_cart.items()): 
        print(f"{index+1}. {item}      ${(products[item]):.2f}          {quantity}          ${(products[item] * quantity):.2f}")
print() 
print(f"Discount: {checkout_and_discounts(total) * 100}%")
print()
print(f"Amount saved.  ${amount_saved:.2f}")
print()
print(f"Final Total  ${final_total:.2f}")
print()
print("Thank you!")
print() 
print()
