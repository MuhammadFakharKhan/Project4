def get_last_element(lst):
    # Print the last element of the list
    print(lst[-1])

def main():
    # The following code is provided to get user input
    user_list = []
    print("Enter list elements one at a time (enter 'done' to finish):")
    while True:
        element = input("> ")
        if element.lower() == 'done':
            break
        user_list.append(element)

    # Call the function with the user's list
    get_last_element(user_list)


if __name__ == "__main__":
    main()