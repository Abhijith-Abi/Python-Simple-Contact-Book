import os
import json


# Add Json file
contact_file = 'contacts.json'


# Load contacts from file
def load_contacts():
    if os.path.exists(contact_file):
        with open(contact_file, "r") as file:
            return json.load(file)
    else:
        return []


# Save contacts to file
def save_contacts(contacts):
    with open(contact_file, "w") as file:
        json.dump(contacts, file, indent=4)


# Add Contacts
def add_contacts():
    contacts = load_contacts()

    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    new_contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(new_contact)
    save_contacts(contacts)
    print(f"\n✅ Contact '{name}' added successfully!")


# View contacts file
def view_contacts():
    contacts = load_contacts()

    if contacts:
        print("\n📒 Contact List:")
        for contact in contacts:
            name = contact.get('name', '')
            phone = contact.get('phone', '')
            email = contact.get('email', '')
            print(f"Name : {name} , Phone : {phone} , Email : {email}")
    else:
        print("No contacts found.")

# Delete Contact


def delete_contact():
    contacts = load_contacts()

    if not contacts:
        print("No contacts to delete.")
        return

    view_contacts()
    index = int(input("\nEnter contact number: ")) - 1

    if 0 <= index < len(contacts):
        contacts.pop(index)
        save_contacts(contacts)
        print("✅ Contact deleted!")
    else:
        print("Invalid number.")


# Console Run
def run_console():
    while True:
        print("\n=== Contact Manager ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_contacts()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    run_console()
