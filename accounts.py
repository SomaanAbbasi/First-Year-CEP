# logged_in = False       #why is this here??
current_user = ""
from pathlib import Path        # needed to make directory 'userdata' to store user accs/carts/history

# Create a directory for storing user information
Path("userdata").mkdir(exist_ok=True)


def createaccount():
    # global logged_in
    # global current_user
    digits = '0123456789'
    special_chr = '!@#$%^&*()-_'


    # Name input:

    while True:

        first_name = input("Enter your first name: ")

        if first_name.isalpha():  # check the alphabets
            break

        else:
            print("Name can only contain alphabets, try again")

    while True:

        last_name = input("Enter your last name: ")

        if last_name.isalpha():
            break

        else:
            print("Name can only contain alphabets, try again")

    # Email input:
    while True:
        email = input("Enter your email address: ")

        if ('@gmail.com' in email) or ('@yahoo.com' in email):
            break

        else:
            print("Invalid email, enter a valid Gmail or Yahoo email address.")

    # Username input
    while True:
        username = input("Enter a username: ")
        digit_check = False
        unique_check = True

        for i in username:  # checks if each character in username is a digit
            if i in digits:
                digit_check = True
                break

        if digit_check == False:
            print("username must contain a number")
            continue

        with open('./userdata/userdata.txt', 'a+') as f:
            f.seek(0)
            users = f.read().split('\n')
            for i in range(0, len(users)):
                if username == users[i]:  # checks if username already exists in file
                    unique_check = False
                    break

        if unique_check == True:
            break

        else:
            print("Username already exists")    # username is not unique



    # Password input and validation
    while True:
        length_check = False
        digit_check = False
        special_check = False

        password = input("Enter a password: ")

        if 8 <= (len(password)) <= 16:
            length_check = True

        for i in password:
            if i in digits:
                digit_check = True
                break

        for j in password:
            if j in special_chr:
                special_check = True
                break

        if ((length_check and digit_check) and special_check):
            print("password accepted")

            # save created account to file:
            with open('./userdata/userdata.txt', "a+") as f:
                f.write(username + '\n')
                f.write(password + '\n')
                f.write('\n')
                f.flush()

                # logged_in = True
                current_user =  username


                # creates an empty cart and empty history for new user, only done once when creating acc:
                with open(f"./userdata/{current_user}_cart.txt", "w") as f:
                    f.write(str([]))                #writes empty list as user cart

                with open(f"./userdata/{current_user}_history.txt", "w") as f:
                    f.write(str([]))                    #writes empty list as user history

                return current_user


            break

        else:
            print("Password must be between 8 to 16 characters;\nand contain atleast 1 digit and 1 special character")



def login():

    with open('./userdata/userdata.txt', 'a+') as f:
        f.seek(0)
        users = f.read().split('\n')

        while True:
            print("Sign in to your account: ")
            username_input = input("Enter your username: ")
            password_input = input("Enter your password: ")

            for i in range(len(users)):
                if users[i] == username_input and users[i + 1] == password_input:
                    print("Logged in succesfully")
                    current_user = username_input
                    return current_user


            else:
                print('invalid username or password\n')




