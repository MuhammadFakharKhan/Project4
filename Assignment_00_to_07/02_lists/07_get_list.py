def main():
    # Initialize an empty list
    values = []

    while True:
        # Prompt the user to enter a value
        user_input = input("Enter a value: ")
        
        # Check if the user pressed enter without typing anything
        if user_input == "":
            break
        
        # Add the entered value to the list
        values.append(user_input)

    # Print the final list
    print("Here's the list:", values)

if __name__ == "__main__":
    main()