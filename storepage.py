# Naming the store item names:



with open('products_list.txt', "r") as f:
    products = eval(f.read())



def display_products(current_user):  # Defining a products list
    while True:
        print("=" * 50)
        print("\t\t\tProducts Available")  # design
        print("=" * 50)
        print("ID\t\tName\t\t\t\tPrice\t\tStock ")
        print("-" * 50)

        for product in products:
            id_str = str(product["id"]).ljust(5)  # The ljust() method will left align the string, using a specified character (space is default) as the fill character.
            name_str = product["name"].ljust(23)
            price_str = str(product["price"]).ljust(13)
            stock_str = str(product["stock"])
            print(id_str + name_str + price_str + stock_str)

        print("=" * 50)

        item = int(input("Enter id of product you want [press 0 for menu] :  "))
        if item == 0:
            break

        quantity = int(input("How many do you want?: "))
        if products[item - 1]["stock"] >= quantity:  # quantity should be less than stock quantity
            products[item - 1]["stock"] -= quantity  # Minus the item from stock after selecting a item

            from datetime import date               #date needed, imported here for simplicity
            today = date.today()

            with open(f"./userdata/{current_user}_cart.txt", "a+") as f:
                f.seek(0)
                user_cart = eval(f.read())
                user_cart.extend([item, quantity, str(today)])


            with open("products_list.txt", 'w') as f:
                f.write(str(products))                      #write updated product list (with reduced stock) back to file, overwriting previous list

            with open(f"./userdata/{current_user}_cart.txt", "w") as f:
                f.write(str(user_cart))                                 # opens current users file, overwrites previous data, saves current cart




        else:
            print("out of stock")





def display_cart(current_user):
    global bill

    while True:
        print("=" * 50)
        print("\t\t\tYour cart:")  # decorative text
        print("=" * 50)
        print("No.\t  Name\t\t\t\t\tPrice\t\tQuantity")
        print("-" * 50)

        with open(f"./userdata/{current_user}_cart.txt", 'r') as f:
            user_cart = eval(f.read())

        order_counter = 1           #to keep track of how many orders are in cart, and to let user select an order
        bill = 0

        for i in range(0, len(user_cart), 3): #steps of 3 since each order is 3 elements in the list 'user_cart',to get to next order,u must do +3
            sr_num = str(order_counter).ljust(5)
            item = str(products[user_cart[i]-1]["name"]).ljust(22)      # complicated, key 'name' used to get name of item from dictionary within the list 'products'

            quantity = user_cart[i + 1]
            price = products[user_cart[i]-1]["price"]
            bill += quantity*price

            price = str(price).ljust(15)
            quantity = str(quantity)

            print(sr_num, item, price, quantity)
            order_counter += 1

        print('-' * 50)
        print(f"\t\t\t\t\t\t\tTotal bill:- Rs{bill}/-")
        print('-' * 50)

        print("\nEnter: (1) Remove items (2) Checkout and Exit (3) Go back to menu")
        choice = int(input())
        if choice == 1:         # remove products from cart:
            remove_order = int(input("Enter the Order No. you wish to remove: "))
            if 1 <= remove_order < order_counter:  # makes sure the order number exists according to current items in cart
                user_cart.pop((remove_order * 3) - 1)  # formula to get to needed index in list according to order number
                user_cart.pop((remove_order * 3) - 2)  # each order has 3 elements, so we pop 3 items in a row
                user_cart.pop((remove_order * 3) - 3)

                with open(f"./userdata/{current_user}_cart.txt", "w") as f:
                    f.write(str(user_cart))                 # immediately writes the changed cart back to disk
                    f.flush()
            else:
                print("That order number doesnt exist, try again.\n")

        elif choice == 2:

            if len(user_cart) != 0:     # if cart isnt empty
                checkout(current_user)
                break

            else:
                input("Your cart appears to be empty!\nEnter any key to go back: ")  # input is wasted, to let user read prompt and go back
                break

        elif choice == 3:
            break

        else:
            print("Invalid choice, try again!")


def checkout(current_user):
    with open(f"./userdata/{current_user}_history.txt", "r") as f:
        user_history = eval(f.read())               # read users existing history to memory


    with open(f"./userdata/{current_user}_cart.txt", 'r') as f:
        user_cart = eval(f.read())                  # read cart to memory

    user_history.extend(user_cart)                #saves current cart as history
    user_cart = []                                #empties cart

    with open(f"./userdata/{current_user}_history.txt", "w") as f:
        f.write(str(user_history))                  #writes current history to disk, overwriting previous

    with open(f"./userdata/{current_user}_cart.txt", 'w') as f:
        f.write(str(user_cart))


    print('-'*30)
    print(f'Your bill is Rs.{bill}/-\nReady to checkout!')
    print('-'*30)

    # example user input, not actually used. payment process omitted.
    address = input("Enter your delivery address here: ")
    phone = input("Enter phone number: ")

    print("\nThank You for shopping with us!\nYour order will arrive in 30-45 mins.\nGoodbye!")
    exit()

def view_history(current_user):
    with open(f"./userdata/{current_user}_history.txt", 'r') as f:
        user_history = eval(f.read())



    if len(user_history) != 0:
        while True:
            print("=" * 60)
            print("\t\t\tYour past orders:")  # decorative text
            print("=" * 60)
            print("No.\t  Name\t\t\t\t Quantity\t\tDate Ordered")
            print("-" * 60)



            order_counter = 1           #to keep track of how many orders are in history
            total_bill = 0

            for i in range(0, len(user_history), 3): #steps of 3 since each order is 3 elements in the list 'user_history',to get to next order,u must do +3
                sr_num = str(order_counter).ljust(5)
                item = str(products[user_history[i]-1]["name"]).ljust(22)      # complicated, key 'name' used to get name of item from dictionary within the list 'products'
                date = str(user_history[i+2])

                price = products[user_history[i] - 1]["price"]
                quantity = user_history[i+1]
                total_bill += price*quantity

                quantity = str(quantity).ljust(10)

                print(sr_num, item, quantity, date)
                order_counter += 1
            print("-" * 60)
            print(f"\t\tTotal spent in our store: Rs.{total_bill}\-")
            print("-" * 60)

            input("\nEnter any key to go back: ")         #dummy input, to let user read then go back
            break
    else:
        print("-" * 40)
        print("You dont have any previous orders!")
        print("-" * 40)

def display_menu(current_user):
    # opens current users file, reads currents user cart to memory
    with open(f"./userdata/{current_user}_cart.txt", "r") as f:
        f.seek(0)
        user_cart = eval(f.read())

    while True:
        print('\n')
        print("*" * 35)  # decorative text for menu
        print("Welcome to the Trio Taste Bakery!")
        print("*" * 35)
        print("1. View Products")
        print("2. View Cart and Checkout")
        print("3. View Order History")
        print("4. Exit")
        print("*" * 35)

        choice = input("Enter your choice (1-3 , press 4 to exit): ")

        if choice == '1':
            print("\n")
            display_products(current_user)


        elif choice == '2':
            print('\n')
            display_cart(current_user)

        elif choice == '3':
            print('\n')
            view_history(current_user)


        elif choice == '4':
            print("Exiting! Thank you for shopping with us!")
            exit("Closing program")

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

