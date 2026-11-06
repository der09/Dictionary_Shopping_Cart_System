# Diane Hsieh 
# AM 
# Shopping Cart System with Dictionary
# import 
from datetime import date
# dictionary of products 
# products = {
#     "Chips": 2.99, 
#     "Soda": 2.50, 
#     "Candy": 1.50, 
#     "Cookies": 3.00, 
#     "Water": 1.00, 
#     "Sandwich": 5.00
#     }

products = {
    "Carrot": 0.30,
    "Yogurt": 3.49,
    "Garlic": 0.75,
    "Cereal": 4.99, 
    "Cheese": 3.99
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
    while (chosen < 1 or chosen > 6):
        print("Invalid product!")
        print("Please choose a number between 1 and 6. ")
        chosen = int(input("Enter product number: "))

    quantity = int(input("How many would you like to add?: "))
    while quantity < 0: 
        print("Not valid")
        quantity = int(input("How many would you like to add?: "))


    shopping_cart[list(products)[chosen - 1]] = quantity
    print([list(products)[chosen - 1]], "was added to your cart!")
    print(chosen, "quantity is now", quantity)

def remove_product(shopping_cart):
# customer chooses option 3: remove product from cart 
    
    print(" ======== YOUR SHOPPING CART ======== ")

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
        print("Removed 1", shopping_cart[remove - 1], "from your cart!")
        new_quantity = shopping_cart[list(products)[remove - 1]] - 1 
        print([list(products)[remove - 1]], "quantity is now", new_quantity)
        shopping_cart[list(products)[remove - 1]] = new_quantity

        # when quantity is zero 
        if new_quantity == 0: 
            shopping_cart.pop([list(products)[remove - 1]])

def view_cart(products, shopping_cart):
    # customer chooses option 4: view shopping cart
        print(" ======== YOUR SHOPPING CART ======== ")
        if len(shopping_cart) == 0:
            print("Your shopping cart is empty!")
        else:
            # displaying the current shopping cart
            print("Product      Unit Price   Quantity   Line Total")
            for index, (item, quantity) in enumerate(shopping_cart.items()): 
                print(f"{index + 1}. {item}  ${products[item]}   {quantity}   ${(quantity * products[item]):.2f}")
            print() 
            new_quantity = 0 
            for quantity in shopping_cart.values(): 
                new_quantity += quantity
            print("Total Items:", new_quantity)
            subtotal = 0 
            for line_total in shopping_cart.values(): 
                subtotal += line_total
                print(f"Subtotal: ${subtotal}")

def current_total(products, shopping_cart): 
    price = 0 
    for item, quantity in shopping_cart:
        price += products[item] * quantity
    print(f"Total ${price}")
    return price 

def checkout_and_discounts(products, shopping_cart): 
    discount = 0 

    if current_total(products, shopping_cart) < 10: 
        discount = 0
    elif current_total(products, shopping_cart) < 20: 
        discount = 0.05 
    elif current_total(products, shopping_cart) < 40: 
        discount = 0.10 
    else: 
        discount = 0.15 
    return discount 

print() 
amount_saved = current_total(products, shopping_cart) * checkout_and_discounts(products, shopping_cart)
final_total = current_total(products, shopping_cart) - amount_saved 


print() 
choice = main_menu(products, shopping_cart)


# while loop 
while choice != 6: 
    if choice == 1 : 
        available_products(products)
        choice = main_menu(products, shopping_cart)
        print()
    elif choice == 2: 
        add_product(products, shopping_cart)
        choice = main_menu(products, shopping_cart)
        print()
    elif choice == 3: 
        remove_product(shopping_cart) 
        choice = main_menu(products, shopping_cart)
        print()
    elif choice == 4: 
        view_cart(products, shopping_cart) 
        choice = main_menu(products, shopping_cart)
        print()
    elif choice == 5: 
        current_total(products, shopping_cart) 
        choice = main_menu(products, shopping_cart)
        print()
    elif choice == 6: 
        print("cannot checkout")
        print()
    main_menu(products, shopping_cart)

checkout_and_discounts(products, shopping_cart)
print()
print(f"Amount saved.  ${amount_saved}")
print()
print(f"Final Total  ${final_total}")
print()
print()
    

        







