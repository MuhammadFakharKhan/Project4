def get_first_element(lst):
    # Print the first element of the list
    print(lst[0])

def main():

    # The following code is provided to get user input
    user_list = []
    print("Enter list elements one at a time (enter 'done' to finish):")
    while True:
        element = input("> ")
        if element.lower() == 'done':
            break
        user_list.append(element)

    get_first_element(user_list)
    get_first_element(user_list)






if __name__ == "__main__":
    main()