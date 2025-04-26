def phonebook_program():
    # Initialize an empty dictionary for our phonebook
    phonebook = {}
    
    print("Welcome to the Phonebook Program!")
    print("Commands: add, lookup, delete, list, quit")
    
    while True:
        command = input("\nEnter a command: ").lower()
        
        # Add a new contact
        if command == "add":
            name = input("Enter contact name: ")
            number = input("Enter phone number: ")
            phonebook[name] = number
            print(f"Added {name} to the phonebook.")
        
        # Look up a contact
        elif command == "lookup":
            name = input("Enter name to look up: ")
            if name in phonebook:
                print(f"{name}'s number: {phonebook[name]}")
            else:
                print(f"{name} not found in phonebook.")
        
        # Delete a contact
        elif command == "delete":
            name = input("Enter name to delete: ")
            if name in phonebook:
                del phonebook[name]
                print(f"Deleted {name} from phonebook.")
            else:
                print(f"{name} not found in phonebook.")
        
        # List all contacts
        elif command == "list":
            if not phonebook:
                print("Phonebook is empty.")
            else:
                print("\nPhonebook Contacts:")
                for name, number in sorted(phonebook.items()):
                    print(f"{name}: {number}")
        
        # Quit the program
        elif command == "quit":
            print("Goodbye!")
            break
        
        # Handle invalid commands
        else:
            print("Invalid command. Please try again.")

# Run the program
phonebook_program()