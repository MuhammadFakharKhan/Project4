def add_three_copies(lst, data):
    # Add three copies of the data to the list
    lst.append(data)
    lst.append(data)
    lst.append(data)
    # No return statement needed because lists are mutable

# Example usage
user_list = []
print("List before:", user_list)

user_input = input("Enter a message to copy: ")
add_three_copies(user_list, user_input)

print("List after:", user_list)