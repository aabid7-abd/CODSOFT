import json


class ContactBook:
    def __init__(self, file_path="contacts.txt"):
        self.contacts = []
        self.file_path = file_path
        self.load_contacts()

    def add_contact(self, name, phone, email="", address=""):
        contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
        self.contacts.append(contact)
        self.save_contacts()
        print("Contact added successfully!")

    def view_contacts(self):
        if self.contacts:
            for contact in self.contacts:
                print(f"Name:{contact['Name']}  \nContact:{contact['Phone']} \nAddress:{contact['Address']}")
                print()
        else:
            print("No contacts available.")

    def search_contact(self, Search_Term):
        found_contacts = [contact for contact in self.contacts
                          if Search_Term.lower() in contact['Name'].lower() or
                          Search_Term in contact['Phone']]
        if found_contacts:
            for contact in found_contacts:
                print(f"{contact['Name']} - {contact['Phone']}")
        else:
            print("No matching contacts found.")

    def update_contact(self, search_term, updated_name, updated_phone, updated_email="", updated_address=""):
        for contact in self.contacts:
            if search_term.lower() in contact['Name'].lower() or search_term in contact['Phone']:
                contact.update(
                    {'Name': updated_name, 'Phone': updated_phone, 'Email': updated_email, 'Address': updated_address})
                self.save_contacts()
                print("Contact updated successfully!")
                return
        print("No matching contact found.")

    def delete_contact(self):
        if self.contacts:
            for contact in self.contacts:
                print(f"Name:{contact['Name']}  \nContact:{contact['Phone']} \nAddress:{contact['Address']}")
                print()
        else:
            print("No contacts available.")
            return

        Search_Term = input("Enter name or phone number to delete: ")
        for contact in self.contacts:
            if Search_Term.lower() in contact['Name'].lower() or Search_Term in contact['Phone']:
                self.contacts.remove(contact)
                self.save_contacts()
                print("Contact deleted successfully!")
                return
        print("No matching contact found.")

    def load_contacts(self):
        try:
            with open(self.file_path, 'r') as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            pass  # The file doesn't exist, so we start with an empty list

    def save_contacts(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.contacts, file, indent=2)


# Example usage:

contact_book = ContactBook()

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email (optional): ")
        address = input("Enter address (optional): ")
        contact_book.add_contact(name, phone, email, address)

    elif choice == '2':
        print("\nContact List:")
        contact_book.view_contacts()

    elif choice == '3':
        search_term = input("Enter name or phone number to search: ")
        print("\nSearch Results:")
        contact_book.search_contact(search_term)

    elif choice == '4':
        search_term = input("Enter name or phone number to update: ")
        updated_name = input("Enter new name: ")
        updated_phone = input("Enter new phone number: ")
        updated_email = input("Enter new email (optional): ")
        updated_address = input("Enter new address (optional): ")
        contact_book.update_contact(search_term, updated_name, updated_phone, updated_email, updated_address)

    elif choice == '5':
        contact_book.delete_contact()

    elif choice == '6':
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
