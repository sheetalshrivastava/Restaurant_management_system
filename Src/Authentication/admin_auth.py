import uuid
import getpass
import json
import os

DATABASE_PATH = os.path.join("database", "admin_data.json")

def is_alpha_only(text):
    return text.isalpha()

def is_valid_email(email):
    return ("@" in email and ".com" in email and not email.isdigit())

def is_valid_password(password):
    has_letter = False
    has_digit = False
    has_special = False
    for char in password:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True
    return has_letter and has_digit and has_special

def is_valid_contact(contact):
    return (contact.isdigit() and len(contact) == 10 and not all(c == contact[0] for c in contact))

def is_valid_address(address):
    for char in address:
        if not (char.isalnum() or char.isspace() or char == ','):
            return False
    return True

def load_data():
    if os.path.exists(DATABASE_PATH):
        with open(DATABASE_PATH, "r") as file:
            return json.load(file)
    return []

def save_data(data):
    with open(DATABASE_PATH, "w") as file:
        json.dump(data, file, indent=4)

def admin_signup():
    admin = {}
    admin['id'] = str(uuid.uuid4())[:6]

    name = input("Enter Admin Name: ")
    while not is_alpha_only(name):
        print(" Name must contain only letters.")
        name = input("Enter Admin Name: ")
    admin['name'] = name

    email = input("Enter Email ID: ")
    while not is_valid_email(email):
        print(" Invalid email format.")
        email = input("Enter Email ID: ")
    admin['email'] = email

    password = getpass.getpass("Create Password: ")
    while not is_valid_password(password):
        print(" Password must have letters, numbers, and special characters.")
        password = getpass.getpass("Create Password: ")
    admin['password'] = password

    contact = input("Enter Contact Number: ")
    while not is_valid_contact(contact):
        print(" Invalid contact number.")
        contact = input("Enter Contact Number: ")
    admin['contact'] = contact

    address = input("Enter Address: ")
    while not is_valid_address(address):
        print(" Invalid address. No special characters allowed except comma.")
        address = input("Enter Address: ")
    admin['address'] = address

    data = load_data()
    data.append(admin)
    save_data(data)
    print(" Admin registered successfully!\n")

def admin_login():
    email = input("Enter Email ID: ")
    password = getpass.getpass("Enter Password: ")

    data = load_data()
    for admin in data:
        if admin['email'] == email and admin['password'] == password:
            print(f"\n Welcome {admin['name']} to Admin Dashboard!\n")
            return True
    print(" Invalid credentials.")
    return False

def admin_menu():
    while True:
        print("\n--- Admin Panel ---")
        print("1. Admin Sign Up")
        print("2. Admin Login")
        print("0. Back to Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            admin_signup()
        elif choice == "2":
            admin_login()
        elif choice == "0":
            break
        else:
            print(" Invalid option.")
