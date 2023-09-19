from Admin import Admin
from Shopper import Shopper
from Product import Product
from datetime import datetime
global productsFlag
global usersFlag
flag = None
usersFlag= None
productsFlag = None

def add_product(users_list):
    print("Add product function")
    user_id = input("Enter your User ID: ")

    # Check if the entered user ID is in the users list
    user = next((user for user in users_list if user.user_id == user_id), None)

    if user is None:
        print("Access Denied: User ID not found.")
        return
    print(user.role)
    if user.role == 'admin':
        # The user is an admin, allow them to add a product
        # Get input for the new product from the admin
        product_id = input("Enter Product ID: ")
        # Check if the entered user ID is unique
        existing_product_ids = [product.product_id for product in products]
        if len(product_id) != 6:
            print("ID Length must be 6")
            return
        if product_id in existing_product_ids:
            print("Product ID must be unique. Product not added.")
            return
        product_name = input("Enter Product Name: ")
        product_category = input("Enter Product Category: ")
        inventory = input("Enter Product Inventory: ")
        price = float(input("Enter Price: "))
        supplier = input("Enter Supplier: ")
        has_an_offer = input("Does it have an offer? (1 for Yes, 0 for No): ")
        offer_price = 0.0
        valid_until = ""

        if has_an_offer == '1':
            offer_price = float(input("Enter Offer Price: "))
            while True:
                valid_until = input("Enter Valid Until (DD/MM/YYYY): ")
                try:
                    datetime.strptime(valid_until, "%d/%m/%Y")
                    break  # Break the loop if the date is valid
                except ValueError:
                    print("Invalid date format. Please use DD/MM/YYYY format.")
            # Create a new Product instance
            new_product = Product(
                    product_id,
                    product_name,
                    product_category,
                    price,
                    inventory,
                    supplier,
                    has_an_offer,
                    offer_price,
                    valid_until,
            )
        else:
            offer_price = None
            valid_until = None
            # Create a new Product instance
            new_product = Product(
                product_id,
                product_name,
                product_category,
                price,
                inventory,
                supplier,
                has_an_offer,
                offer_price,
                valid_until,
            )


        # Append the new product to the products list
        products.append(new_product)
        print("Product added successfully.")
    else:
        # The user is not an admin, print "Access Denied"
        print("Access Denied: You are not authorized to add products.(only admins)")

def place_item_on_sale(users_list):
    print("Place item on sale function")
    user_id = input("Enter your User ID: ")

    # Check if the entered user ID is in the users list
    user = next((user for user in users_list if user.user_id == user_id), None)

    if user is None:
        print("Access Denied: User ID not found.")
        return
    print(user.role)
    if user.role == 'admin':
        product_id = input("Enter Product ID: ")
        # Check if the entered user ID is unique
        existing_product_ids = [product.product_id for product in products]
        if product_id not in existing_product_ids:
            print("No product here")
            return
        for product in products:
            if product_id == product.product_id:
                if product.has_an_offer == 1:
                    print("Product already has an offer")
                    return
                else:
                    product.has_an_offer = 1
                    offer_price = input("Enter Offer price: ")
                    product.offer_price = offer_price
                    date1 = input("Enter the date you want: ")
                    product.valid_until = date1
    else:
        # The user is not an admin, print "Access Denied"
        print("Access Denied: You are not authorized to add products.(only admins)")
def update_product(users_list):
    print("Update product function")
    user_id = input("Enter your User ID: ")

    # Check if the entered user ID is in the users list
    user = next((user for user in users_list if user.user_id == user_id), None)

    if user is None:
        print("Access Denied: User ID not found.")
        return
    print(user.role)
    if user.role == 'admin':
        product_id = input("Enter Product ID: ")
        # Check if the entered user ID is unique
        existing_product_ids = [product.product_id for product in products]
        if product_id not in existing_product_ids:
            print("No product here")
            return
        field_update = input("Enter the field you want to update:(product_id, product_name, product_category, price, inventory,supplier, has_an_offer)")
        for product in products:
            if product_id == product.product_id:
                if field_update == "product_id":
                    print("You can't change the code")
                elif field_update == "product_name":
                    updated_field = input("Enter the new name: ")
                    product.product_name = updated_field
                elif field_update == "product_category":
                    updated_field = input("Enter the new category: ")
                    product.product_category = updated_field
                elif field_update == "price":
                    updated_field = input("Enter the new price: ")
                    product.price = updated_field
                elif field_update == "inventory":
                    updated_field = input("Enter the new inventory: ")
                    product.inventory = updated_field
                elif field_update == "supplier":
                    updated_field = input("Enter the new supplier: ")
                    product.product_name = updated_field
                elif field_update == "has_an_offer":
                    if product.has_an_offer == 1:
                        product.has_an_offer = 0
                        print("Has an offer set to 0")
                        return
                    else:
                        product.has_an_offer = 1
                        print("Has an offer set to 1")
                        offer_price = input("Enter Offer price: ")
                        product.offer_price = offer_price
                        date1 = input("Enter the date you want: ")
                        product.valid_until = date1
    else:
        # The user is not an admin, print "Access Denied"
        print("Access Denied: You are not authorized to add products.(only admins)")

def add_new_user(users_list):
    print("Add new user function")
    user_id = input("Enter your User ID: ")

    # Check if the entered user ID is in the users list
    user = next((user for user in users_list if user.user_id == user_id), None)

    if user is None:
        print("Access Denied: User ID not found.")
        return
    print(user.role)
    if user.role == 'admin':
        # Get user information from the user
        user_id = input("Enter User ID (6-digit unique code): ")
        # Check if the entered user ID is unique
        existing_user_ids = [user.user_id for user in users_list]
        if len(user_id) != 6:
            print("ID Length must be 6")
            return
        if user_id in existing_user_ids:
            print("User ID must be unique. User not added.")
            return
        user_name = input("Enter User Name: ")
        user_date_of_birth = input("Enter User Date of Birth (DD/MM/YYYY): ")
        role = input("Enter Role (admin or shopper): ").lower()
        # Check if the role is valid
        if role not in ["admin", "shopper"]:
            print("Invalid role. User not added.")
            return
        active = input("Is the user active? (1 for Yes, 0 for No): ")
        # Create a new user instance
        if role == "shopper":
            new_user = Shopper(user_id, user_name, user_date_of_birth, role, active, "", 0)
            shoppers.append(new_user)
        else:
            new_user = Admin(user_id, user_name, user_date_of_birth, role, active)
            admins.append(new_user)

        if role == "shopper":
            while True:
                product_id = input("Enter Product ID to add to basket (or 'done' to finish): ")
                product = next((product for product in products if product.product_id == product_id), None)
                while True:
                    if product is None and product_id.lower() != "done":
                        print("No products with this id available")
                        product_id = input("Enter Product ID to add to basket (or 'done' to finish): ")
                    elif product_id.lower() == "done":
                        break
                    else: break
                if product_id.lower() == "done":
                    break
                quantity = int(input("Enter quantity for this product: "))
                new_user.basket[product_id] = quantity
        # Append the new user to the users list
        print("User added successfully.")
    else:
        # The user is not an admin, print "Access Denied"
        print("Access Denied: You are not authorized to add products.(only admins)")

def update_user(users_list):
    global flag
    print("Update user function")
    user_id = input("Enter your User ID: ")

    # Check if the entered user ID is in the users list
    user = next((user for user in users_list if user.user_id == user_id), None)

    if user is None:
        print("Access Denied: User ID not found.")
        return

    if user.role == 'admin':
        user_update_id = input("Enter user id you want to update: ")

        # Check if the user to update exists
        for user2 in users_list:
            if user_update_id == user2.user_id:
                if user2.role == "shopper":
                    flag = "shopper"
                    break

        user_update_field = input("Enter the field you want to update:(User_id;User_name;User_DoB;Role;Active) ")

        if flag == "shopper":
            for shopper in shoppers:
                if shopper.user_id == user_update_id:
                    if user_update_field == "User_id":
                        print("You can't update the User ID.")
                        return
                    elif user_update_field == "User_name":
                        new_user_field = input("Enter new User Name: ")
                        shopper.user_name = new_user_field
                    elif user_update_field == "User_DoB":
                        new_user_field = input("Enter new User Date of Birth (DD/MM/YYYY): ")
                        shopper.user_date_of_birth = new_user_field
                    elif user_update_field == "Role":
                        if user.role == "admin":
                            user.role = "shopper"
                            admins.remove(user)
                            shoppers.append(user)
                        else:
                            user.role = "admin"
                            shoppers.remove(user)
                            admins.append(user)
                            return
                    elif user_update_field == "Active":
                        new_user_field = input("Enter new Active mode: ")
                        shopper.active = new_user_field
        else:
            for admin in admins:
                if admin.user_id == user_update_id:
                    if user_update_field == "User_id":
                        print("You can't update the User ID.")
                        return
                    elif user_update_field == "User_name":
                        new_user_field = input("Enter new User Name: ")
                        admin.user_name = new_user_field
                    elif user_update_field == "User_DoB":
                        new_user_field = input("Enter new User Date of Birth (DD/MM/YYYY): ")
                        admin.user_date_of_birth = new_user_field
                    elif user_update_field == "Role":
                        if user.role == "admin":
                            user.role = "shopper"
                            admins.remove(user)
                            shoppers.append(user)
                        else:
                            user.role = "admin"
                            shoppers.remove(user)
                            admins.append(user)
                            return
                    elif user_update_field == "Active":
                        new_user_field = input("Enter new Active mode: ")
                        admin.active = new_user_field
    else:
        # The user is not an admin, print "Access Denied"
        print("Access Denied: You are not authorized to update users (only admins)")
    flag = None


def display_all_users(users_list):
    print("Display all users function")
    user_id = input("Enter your User ID: ")

    # Check if the entered user ID is in the users list
    user = next((user for user in users_list if user.user_id == user_id), None)

    if user is None:
        print("Access Denied: User ID not found.")
        return

    if user.role == 'admin':
        print("Users Information:")

        # Print user information
        for user in users:
            print(f"User ID: {user.user_id}")
            print(f"User Name: {user.user_name}")
            print(f"Date of Birth: {user.user_date_of_birth}")
            print(f"Role: {user.role}")
            print(f"Active: {'Yes' if user.active else 'No'}")

            if isinstance(user, Shopper):
                print(f"Basket: {user.basket}")
                print(f"Order: {user.order}")
            print()
    else:
        # The user is not an admin, print "Access Denied"
        print("Access Denied: You are not authorized to display users (only admins)")
def print_proudcts():
    for product in products:
        print(f"Product ID: {product.product_id}")
        print(f"Product Name: {product.product_name}")
        print(f"Product Category: {product.product_category}")
        print(f"Inventory: {product.inventory}")
        print(f"Price: {product.price}")
        print(f"Supplier: {product.supplier}")
        print(f"Has an Offer: {'Yes' if product.has_an_offer else 'No'}")
        if product.has_an_offer:
            print(f"Offer Price: {product.offer_price}")
            print(f"Valid Until: {product.valid_until}")
        print()

def list_products():
    print("List products function")
    print("All products:")

    # Print all products
    print_proudcts()

    print("Products with discount: ")

    # Print products with discounts
    for product in products:
        if (product.has_an_offer == True):
            print(f"Product ID: {product.product_id}")
            print(f"Product Name: {product.product_name}")
            print(f"Product Category: {product.product_category}")
            print(f"Inventory: {product.inventory}")
            print(f"Price: {product.price}")
            print(f"Supplier: {product.supplier}")
            print(f"Has an Offer: {'Yes' if product.has_an_offer else 'No'}")
            if product.has_an_offer:
                print(f"Offer Price: {product.offer_price}")
                print(f"Valid Until: {product.valid_until}")
            print()

    category_in = input("Enter category you want: ")
    print("Products with category ")

    # Print products with a specific category
    for product in products:
        if (product.product_category == category_in):
            print(f"Product ID: {product.product_id}")
            print(f"Product Name: {product.product_name}")
            print(f"Product Category: {product.product_category}")
            print(f"Inventory: {product.inventory}")
            print(f"Price: {product.price}")
            print(f"Supplier: {product.supplier}")
            print(f"Has an Offer: {'Yes' if product.has_an_offer else 'No'}")
            if product.has_an_offer:
                print(f"Offer Price: {product.offer_price}")
                print(f"Valid Until: {product.valid_until}")
            print()

    name_in = input("Enter name you want: ")
    print("Products with name ")

    # Print products with a specific name
    for product in products:
        if (product.product_name == name_in):
            print(f"Product ID: {product.product_id}")
            print(f"Product Name: {product.product_name}")
            print(f"Product Category: {product.product_category}")
            print(f"Inventory: {product.inventory}")
            print(f"Price: {product.price}")
            print(f"Supplier: {product.supplier}")
            print(f"Has an Offer: {'Yes' if product.has_an_offer else 'No'}")
            if product.has_an_offer:
                print(f"Offer Price: {product.offer_price}")
                print(f"Valid Until: {product.valid_until}")
            print()
def list_shoppers(users_list):
    print("List shoppers function")
    user_id = input("Enter your User ID: ")

    # Check if the entered user ID is in the users list
    user = next((user for user in users_list if user.user_id == user_id), None)

    if user is None:
        print("Access Denied: User ID not found.")
        return
    print(user.role)

    # Check if the user is an admin
    if user.role == 'admin':
        # Print loaded shopper data
        print("All Shoppers Data:")
        for shopper in shoppers:
            print(f"User ID: {shopper.user_id}")
            print(f"User Name: {shopper.user_name}")
            print(f"Date of Birth: {shopper.user_date_of_birth}")
            print(f"Role: {shopper.role}")
            print(f"Active: {'Yes' if shopper.active else 'No'}")
            print(f"Basket: {shopper.basket}")
            print(f"Order: {shopper.order}")
            print()

        # Print shoppers with items in their baskets
        print("Shoppers with items in their basket:")
        for shopper in shoppers:
            if len(shopper.basket) != 0:
                print(f"User ID: {shopper.user_id}")
                print(f"User Name: {shopper.user_name}")
                print(f"Date of Birth: {shopper.user_date_of_birth}")
                print(f"Role: {shopper.role}")
                print(f"Active: {'Yes' if shopper.active else 'No'}")
                print(f"Basket: {shopper.basket}")
                print(f"Order: {shopper.order}")
                print()

        # Print shoppers with unprocessed orders
        print("Shoppers with unprocessed orders:")
        for shopper in shoppers:
            if shopper.order == 0:
                print(f"User ID: {shopper.user_id}")
                print(f"User Name: {shopper.user_name}")
                print(f"Date of Birth: {shopper.user_date_of_birth}")
                print(f"Role: {shopper.role}")
                print(f"Active: {'Yes' if shopper.active else 'No'}")
                print(f"Basket: {shopper.basket}")
                print(f"Order: {shopper.order}")
                print()

        # Print shoppers who have requested an order
        print("Shoppers who have requested an order:")
        for shopper in shoppers:
            if shopper.order == 1:
                print(f"User ID: {shopper.user_id}")
                print(f"User Name: {shopper.user_name}")
                print(f"Date of Birth: {shopper.user_date_of_birth}")
                print(f"Role: {shopper.role}")
                print(f"Active: {'Yes' if shopper.active else 'No'}")
                print(f"Basket: {shopper.basket}")
                print(f"Order: {shopper.order}")
                print()
    else:
        # The user is not an admin, print "Access Denied"
        print("Access Denied: You are not authorized to list shoppers (only admins)")

def add_product_to_basket(users_list):
    print("Add product to the basket function")
    user_id = input("Enter your User ID: ")

    # Check if the entered user ID is in the users list
    user = next((user for user in users_list if user.user_id == user_id), None)

    if user is None:
        print("Access Denied: User ID not found.")
        return
    print(user.role)

    # Check if the user is a shopper
    if user.role == 'shopper':
        for shopper in shoppers:
            if shopper.user_id == user_id:
                while True:
                    product_id = input("Enter Product ID to add to the basket (or 'done' to finish): ")
                    product = next((product for product in products if product.product_id == product_id), None)
                    for shopper in shoppers:
                        if shopper.user_id == user_id:
                            for productc in products:
                                for item in shopper.basket:
                                    if item == product_id:
                                        print("The prdouct is already in the basket")
                                        return
                    while True:
                        if product is None and product_id.lower() != "done":
                            print("No products with this id available")
                            product_id = input("Enter Product ID to add to basket (or 'done' to finish): ")
                        elif product_id.lower() == "done":
                            break
                        else:
                            break
                    if product_id.lower() == "done":
                        break
                    quantity = int(input("Enter quantity for this product: "))
                    shopper.basket[product_id] = quantity
    else:
        # The user is not a shopper, print "Access Denied"
        print("Access Denied: You are not authorized to add products to the basket (only shoppers)")

def display_basket(users_list):
    sum_price = 0
    print("Display basket function")
    user_id = input("Enter your User ID: ")

    # Check if the entered user ID is in the users list
    user = next((user for user in users_list if user.user_id == user_id), None)

    if user is None:
        print("Access Denied: User ID not found.")
        return
    print(user.role)

    # Check if the user is a shopper
    if user.role == 'shopper':
        for shopper in shoppers:
            if shopper.user_id == user_id:
                for product in products:
                    for item in shopper.basket:
                        if item == product.product_id:
                            print(f"Product ID: {product.product_id}")
                            print(f"Product Name: {product.product_name}")
                            print(f"Product Category: {product.product_category}")
                            print(f"Inventory: {product.inventory}")
                            print(f"Price: {product.price}")
                            print(f"Supplier: {product.supplier}")
                            print(f"Has an Offer: {'Yes' if product.has_an_offer else 'No'}")
                            if product.has_an_offer:
                                print(f"Offer Price: {product.offer_price}")
                                print(f"Valid Until: {product.valid_until}")
                                # Convert the user input string to a datetime object
                                user_date = datetime.strptime(product.valid_until, "%d/%m/%Y")
                                 # Get the current date
                                current_date = datetime.now()
                                # Format the dates as strings in the desired format
                                user_date_str = user_date.strftime("%d/%m/%Y")
                                current_date_str = current_date.strftime("%d/%m/%Y")
                                # Compare the dates
                                if user_date < current_date:
                                    print(f"The offer is in this date ({user_date_str}) is in the past you cant benefit of it.")
                                    price = int(shopper.basket[item]) * int(product.price)
                                else:
                                    price = int(shopper.basket[item]) * int(product.offer_price)
                            else:
                                price = int(shopper.basket[item]) * int(product.price)
                            print("Quantity: ", shopper.basket[item])
                            print()
                            sum_price += price
        print("----------------------------------------")
        print("Basket Cost: ", sum_price)
        print()
    else:
        # The user is not a shopper, print "Access Denied"
        print("Access Denied: You are not authorized to display the basket (only shoppers)")

def update_basket(users_list):
    print("Update basket function")
    user_id = input("Enter your User ID: ")

    # Check if the entered user ID is in the users list
    user = next((user for user in users_list if user.user_id == user_id), None)

    if user is None:
        print("Access Denied: User ID not found.")
        return

    print(user.role)

    # Check if the user is a shopper
    if user.role == 'shopper':
        update_product_choice = input("Choose what you want to update (clear/remove/update): ")

        for shopper in shoppers:
            if shopper.user_id == user_id:
                if update_product_choice == "clear":
                    shopper.basket.clear()
                    return
                elif update_product_choice == "remove":
                    product_id_update = input("Enter product id to remove: ")
                    items_to_remove = []  # Create a list to store keys to remove

                    for item in shopper.basket:
                        if item == product_id_update:
                            items_to_remove.append(item)

                    # Remove the items from the dictionary
                    for item in items_to_remove:
                        del shopper.basket[item]
                elif update_product_choice == "update":
                    product_id_update = input("Enter product id to update quantity: ")

                    for item in shopper.basket:
                        if item == product_id_update:
                            update_quantity = input("Enter the new quantity for the product: ")
                            shopper.basket[item] = update_quantity
                else:
                    print("Option not found. Please try again later.")
    else:
        print("You are an admin. Only shoppers can access this function.")
    print()

def place_order(users_list):
    print("Place order function")
    user_id = input("Enter your User ID: ")

    # Check if the entered user ID is in the users list
    user = next((user for user in users_list if user.user_id == user_id), None)

    if user is None:
        print("Access Denied: User ID not found.")
        return

    print(user.role)

    # Check if the user is a shopper
    if user.role == 'shopper':
        for shopper in shoppers:
            if shopper.user_id == user_id:
                if shopper.order == 0:
                    shopper.order = 1
                    print("Your order status updated to 1. You can purchase.")
                else:
                    shopper.order = 0
                    print("Your order status updated to 0. You can't purchase.")
    else:
        print("You are an admin. Only shoppers can access this function.")
    print()

def execute_order(users_list):
    print("Execute order function")
    user_id = input("Enter your User ID: ")

    # Check if the entered user ID is in the users list
    user = next((user for user in users_list if user.user_id == user_id), None)

    if user is None:
        print("Access Denied: User ID not found.")
        return

    if user.role == 'admin':
        execute_choice = input("Enter what you want to execute (deduct/clear): ")

        if execute_choice == "deduct":
            for shopper in shoppers:
                if len(shopper.basket) != 0:
                    for item in shopper.basket:
                        for product in products:
                            if item == product.product_id:
                                product.inventory = int(product.inventory) - int(shopper.basket[item])
        elif execute_choice == "clear":
            shopper_id = input("Enter the shopper id you want to clear basket for: ")
            for shopper in shoppers:
                if shopper.user_id == shopper_id:
                    if len(shopper.basket) != 0:
                        shopper.basket.clear()
        else:
            print("Your choice is not recognized. Please try again later.")
    else:
        print("You are a shopper. Only admins can access this function.")
    print()
def save_products_to_file(users_list):
    print("Save products to a file function")
    user_id = input("Enter your User ID: ")

    # Check if the entered user ID is in the users list
    user = next((user for user in users_list if user.user_id == user_id), None)

    if user is None:
        print("Access Denied: User ID not found.")
        return

    # Check if the user is an admin
    if user.role == 'admin':
        save_product_file = input("Enter the name of the file you want to save products in: ")
        try:
            with open(save_product_file, "w") as file:
                # Write the product information to the file
                for product in products:
                    file.write(f"Product ID: {product.product_id}\n")
                    file.write(f"Product Name: {product.product_name}\n")
                    file.write(f"Product Category: {product.product_category}\n")
                    file.write(f"Inventory: {product.inventory}\n")
                    file.write(f"Price: {product.price}\n")
                    file.write(f"Supplier: {product.supplier}\n")
                    file.write(f"Has an Offer: {'Yes' if product.has_an_offer else 'No'}\n")
                    if product.has_an_offer:
                        file.write(f"Offer Price: {product.offer_price}\n")
                        file.write(f"Valid Until: {product.valid_until}\n")
                    file.write("\n")

            print(f"Products saved to '{save_product_file}' successfully.")
        except Exception as e:
            print(f"An error occurred while saving products: {str(e)}")
    else:
        print("You are a shopper. Only admins can access this function.")
    print()

def save_users_to_text_file(users_list):
    user_id = input("Enter your User ID: ")

    # Check if the entered user ID is in the users list
    user = next((user for user in users_list if user.user_id == user_id), None)

    if user is None:
        print("Access Denied: User ID not found.")
        return

    # Check if the user is an admin
    if user.role == 'admin':
        save_user_file = input("Enter the name of the file you want to save users in: ")
        try:
            with open(save_user_file, "w") as file:
                # Write the user information to the file
                for user in users:
                    file.write(f"User ID: {user.user_id}\n")
                    file.write(f"User Name: {user.user_name}\n")
                    file.write(f"Date of Birth: {user.user_date_of_birth}\n")
                    file.write(f"Role: {user.role}\n")
                    file.write(f"Active: {'Yes' if user.active else 'No'}\n")

                    if isinstance(user, Shopper):
                        file.write(f"Basket: {user.basket}\n")
                        file.write(f"Order: {user.order}\n")
                    file.write("\n")

            print(f"Users saved to '{save_user_file}' successfully.")
        except Exception as e:
            print(f"An error occurred while saving users: {str(e)}")
    else:
        print("You are a shopper. Only admins can access this function.")
    print()
users = []  # List to store user objects
admins = []  # List to store admin objects
shoppers = []  # List to store shopper objects

# Read user data from 'users.txt' and create admin and shopper objects
with open('users.txt', 'r') as file:
    for line in file:
        data = line.strip().split(';')
        if data[3] == 'admin' and data[0] != 'User_id' and len(data) >= 4:
            admins.append(Admin(*data))
        elif data[3] == 'shopper' and data[0] != 'User_id' and len(data) >= 6:
            shoppers.append(Shopper(*data))

products = []  # List to store product objects

# Read product data from 'products.txt' and create product objects
with open('products.txt', 'r') as file:
    for line in file:
        data = line.strip().split(';')
        if len(data) >= 9 and data[0] != 'Product_id':
            products.append(Product(*data))

while True:
    # Add admin and shopper objects to the users list
    for admin in admins:
        users.append(admin)
    for shopper in shoppers:
        users.append(shopper)

    # Display the menu options
    print("\nMenu:")
    print("1. Add product (admin-only)")
    print("2. Place an item on sale (admin-only)")
    print("3. Update product (admin-only)")
    print("4. Add a new user (admin-only)")
    print("5. Update user (admin-only)")
    print("6. Display all users (admin-only)")
    print("7. List products (admin and shopper)")
    print("8. List shoppers (admin-only)")
    print("9. Add product to the basket (shopper-only)")
    print("10. Display basket (shopper-only)")
    print("11. Update basket (shopper-only)")
    print("12. Place order (shopper-only)")
    print("13. Execute order (admin-only)")
    print("14. Save products to a file (admin-only)")
    print("15. Save users to a text file (admin-only)")
    print("16. Exit")

    choice = input("Enter your choice (1-16): ")

    # Handle user choices based on input
    if choice == '1':
        add_product(users)
    elif choice == '2':
        place_item_on_sale(users)
    elif choice == '3':
        update_product(users)
    elif choice == '4':
        add_new_user(users)
    elif choice == '5':
        update_user(users)
    elif choice == '6':
        display_all_users(users)
    elif choice == '7':
        list_products()
    elif choice == '8':
        list_shoppers(users)
    elif choice == '9':
        add_product_to_basket(users)
    elif choice == '10':
        display_basket(users)
    elif choice == '11':
        update_basket(users)
    elif choice == '12':
        place_order(users)
    elif choice == '13':
        execute_order(users)
    elif choice == '14':
        save_products_to_file(users)
        productsFlag = 1
    elif choice == '15':
        save_users_to_text_file(users)
        usersFlag = 1
    elif choice == '16':
        if productsFlag == 1:
            if usersFlag == 1:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Users haven't saved to a file yet you can't exit")
        else:
            if usersFlag == 1:
                print("Products haven't saved to a file yet you can't exit")
            else:
                print("Products and users haven't saved to a file yet you can't exit")

    else:
        print("Invalid choice. Please enter a valid option (1-16).")

    users.clear()  # Clear the users list after each menu option