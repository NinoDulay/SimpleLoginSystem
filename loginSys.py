from database_handler import register, update_first_name, update_last_name, update_username, update_password, login, get_account_info
from datetime import datetime

def loginRights(username, password):
    while True:
        print("What do you want to do?")
        print("1. Change First Name")
        print("2. Change Last Name")
        print("3. Change Username")
        print("4. Change Password")
        print("5. Show Data")
        print("6. Logout")
        user_input = input(">>> ")

        if user_input == "1":
            new_first = input("Enter new first name: ")
            update_first_name(username, password, new_first)
            print(f"First name changed to {new_first}!")
        elif user_input == "2":
            new_last = input("Enter new last name: ")
            update_last_name(username, password, new_last)
            print(f"Last name changed to {new_last}!")
        elif user_input == "3":
            new_user = input("Enter new username: ")
            update_username(username, password, new_user)
            username = new_user
            print(f"Username changed to {new_user}!")
        elif user_input == "4":
            new_pw = input("Enter new password: ")
            update_password(username, password, new_pw)
            password = new_pw
            print(f"Password changed to {new_pw}!")
        elif user_input == "5":
            accInfo = get_account_info(username, password)
            print()
            print("-"*20)
            print(f"{'Your Data':^20}")
            print("-"*20)
            print(f"First Name: {accInfo[0]}")
            print(f"Last Name: {accInfo[1]}")
            print(f"Username: {accInfo[2]}")
            print(f"Password: {accInfo[3]}")
            print(f"Date Registered: {accInfo[4]}")
            print("-"*20)
            print()
        elif user_input == "6":
            print()
            print("Logging Out.")
            print()
            break

def main():
    while True:
        print("Welcome to Login System!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        user_input = input(">>> ")

        if user_input == "1":
            while True:
                first = input("First Name: ")
                last = input("Last Name: ")
                un = input("Username: ")
                pw = input("Password: ")
                date = datetime.strftime(datetime.now(), '%m/%d/%Y %I:%M:%p')
                print()
                sure = input("Are you sure (Y/N)?")
                if sure.lower() == 'y':
                    register(first, last, un, pw, date)
                    print(f"{un} registered!")
                    print()
                    break
                elif sure.lower() == 'n':
                    continue
        elif user_input == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            print()
            if login(username, password):
                print("You are now logged in!")
                print()
                loginRights(username, password)
            else:
                print("There is no account in the database with those credentials")
                print()
                continue
        elif user_input == "3":
            print("Exiting...")
            break


main()