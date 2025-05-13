import uuid
import getpass
import json
import os

DATABASE_PATH = os.path.join("database", "staff_data.json")

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

def staff_signup():
    staff = {}
    staff['id'] = str(uuid.uuid4())[:6]

    name = input("Enter Staff Name: ")
    while not is_alpha_only(name):
        print("❌ Name must contain only letters.")
        name = input("Enter Staff Name: ")
    staff['name'] = name

    email = input("Enter Email ID: ")
    while not is_valid_email(email):
        print("❌ Invalid email format.")
        email = input("Enter Email ID: ")
    staff['email'] = email

    password = getpass.getpass("Create Password: ")
    while not is_valid_password(password):
        print("❌ Password must have letters, numbers, and special characters.")
        password = getpass.getpass("Create Password: ")
    staff['password'] = password

    contact = input("Enter Contact Number: ")
    while not is_valid_contact(contact):
        print("❌ Invalid contact number.")
        contact = input("Enter Contact Number: ")
    staff['contact'] = contact

    address = input("Enter Address: ")
    while not is_valid_address(address):
        print("❌ Invalid address. No special characters allowed except comma.")
        address = input("Enter Address: ")
    staff['address'] = address

    data = load_data()
    data.append(staff)
    save_data(data)
    print("✅ Staff registered successfully!\n")

def staff_login():
    email = input("Enter Email ID: ")
    password = getpass.getpass("Enter Password: ")

    data = load_data()
    for staff in data:
        if staff['email'] == email and staff['password'] == password:
            print(f"\n✅ Welcome {staff['name']} to Staff Dashboard!\n")
            return True
    print("❌ Invalid credentials.")
    return False

def staff_menu():
    while True:
        print("\n--- Staff Panel ---")
        print("1. Staff Sign Up")
        print("2. Staff Login")
        print("0. Back to Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            staff_signup()
        elif choice == "2":
            staff_login()
        elif choice == "0":
            break
        else:
            print("❌ Invalid option.")
