class ContactManagementSystem:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email):
        self.contacts[name] = {'phone': phone_number, 'email': email}
        print(f"Contact '{name}' added successfully.")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contacts:")
            for name, info in self.contacts.items():
                print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

    def update_contact(self, name):
        if name in self.contacts:
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            self.contacts[name] = {'phone': phone_number, 'email': email}
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def search_contact(self, name):
        if name in self.contacts:
            info = self.contacts[name]
            print(f"Contact Details for '{name}':")
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
        else:
            print(f"Contact '{name}' not found.")


def main():
    contact_manager = ContactManagementSystem()

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
            contact_manager.add_contact(name, phone_number, email)

        elif choice == '2':
            contact_manager.display_contacts()

        elif choice == '3':
            name = input("Enter contact name to update: ")
            contact_manager.update_contact(name)

        elif choice == '4':
            name = input("Enter contact name to delete: ")
            contact_manager.delete_contact(name)

        elif choice == '5':
            name = input("Enter contact name to search: ")
            contact_manager.search_contact(name)

        elif choice == '6':
            print("Exiting the Contact Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
