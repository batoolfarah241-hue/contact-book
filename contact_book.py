"""
Contact Book Manager
A simple command-line contact manager that saves contacts to a JSON file
so they are still there the next time you run the program.

Concepts covered:
- Functions
- Dictionaries and lists
- File handling (JSON read/write)
- Exception handling
- A menu-driven while loop
"""

import json
import os

DATA_FILE = "contacts.json"


def load_contacts():
    """Load contacts from the JSON file. Returns an empty list if none exist yet."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_contacts(contacts):
    """Save the contacts list back to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(contacts, f, indent=4)


def add_contact(contacts):
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"Contact '{name}' added.\n")


def view_contacts(contacts):
    if not contacts:
        print("No contacts saved yet.\n")
        return

    print("\n--- Contact List ---")
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c['name']} | {c['phone']} | {c['email']}")
    print()


def search_contact(contacts):
    keyword = input("Enter name to search: ").strip().lower()
    results = [c for c in contacts if keyword in c["name"].lower()]

    if not results:
        print("No matching contacts found.\n")
        return

    print("\n--- Search Results ---")
    for c in results:
        print(f"{c['name']} | {c['phone']} | {c['email']}")
    print()


def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        choice = int(input("Enter the number of the contact to delete: "))
        removed = contacts.pop(choice - 1)
        save_contacts(contacts)
        print(f"Deleted '{removed['name']}'.\n")
    except (ValueError, IndexError):
        print("Invalid selection.\n")


def main():
    contacts = load_contacts()

    menu = """
==== Contact Book ====
1. Add contact
2. View all contacts
3. Search contact
4. Delete contact
5. Exit
"""

    while True:
        print(menu)
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please enter a number between 1 and 5.\n")


if __name__ == "__main__":
    main()
