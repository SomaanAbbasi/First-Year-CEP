from accounts import *          # accounts.py handles creating new accounts, and logging in existing accs
from storepage import *         # storepage.py handles basically everything else (products, carts, history, etc)





while True:
    print('='*40)
    print("\tWELCOME to Trio Taste Bakery!!")
    print('~'*40)
    print("1:Sign up")
    print("2:Sign in")
    print("3:Close")

    choice = int(input("\nEnter a choice: "))

    if choice == 1:
        current_user = createaccount()
        display_menu(current_user)

    if choice == 2:
        current_user = login()
        display_menu(current_user)


    if choice == 3:
        break


    elif choice>3 or choice<1:
        print("Invalid choice try again")
