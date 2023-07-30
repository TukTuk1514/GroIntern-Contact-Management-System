contacts = {}

def add_contact(name, phone_number, email):
    contacts[name] = {'phone': phone_number, 'email': email}
    print(f"Contact '{name}' added successfully.")

def display_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def update_contact(name):
    if name in contacts:
        phone_number = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        contacts[name] = {'phone': phone_number, 'email': email}
        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

def search_contact(name):
    if name in contacts:
        info = contacts[name]
        print(f"Contact Details for '{name}':")
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print(f"Contact '{name}' not found.")

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == '1':
        name = input("Enter contact name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email address: ")
        add_contact(name, phone_number, email)

    elif choice == '2':
        display_contacts()

    elif choice == '3':
        name = input("Enter contact name to update: ")
        update_contact(name)

    elif choice == '4':
        name = input("Enter contact name to delete: ")
        delete_contact(name)

    elif choice == '5':
        name = input("Enter contact name to search: ")
        search_contact(name)

    elif choice == '6':
        print("Exiting the Contact Management System.")
        break

    else:
        print("Invalid choice. Please try again.")
