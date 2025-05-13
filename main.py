from Src.Authentication.admin_auth import admin_menu
from Src.Authentication.staff_auth import staff_signup, staff_login
from Src.Authentication.customer_auth import customer_signup, customer_login

def main_menu():
    while True:
        print("\n=== Main Menu ===")
        print("1. Admin Dashboard")
        print("2. Staff Dashboard")
        print("3. Customer Dashboard")
        print("0. Exit")

        choice = input("Enter choice: ")
        if choice == '1':
            admin_menu()
        elif choice == '2':
            print("\n--- Staff ---")
            print("1. Sign Up")
            print("2. Login")
            print("0. Back")
            sub = input("Enter option: ")
            if sub == '1':
                staff_signup()
            elif sub == '2':
                staff_login()   
            elif sub == '0':
                print("Returning to Main Menu....")
                break
            else:
                print("Invalid option.")

        elif choice == '3':
            print("\n--- Customer ---")
            print("1. Sign Up")
            print("2. Login")
            print("0. Back")
            sub = input("Enter option: ")
            if sub == '1':
                customer_signup()
            elif sub == '2':
                customer_login()
            elif sub == '0':
                print("Invalid option.")
        elif choice == '0':
            print("Exiting... Goodbye.")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main_menu()
