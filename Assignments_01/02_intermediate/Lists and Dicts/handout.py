def initialize_list():
    return ["apple", "banana", "orange", "grape", "pineapple"]

def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."

def slice_list(lst, start, end):
    return lst[start:end]

def main():
    fruit_list = initialize_list()
    print("Welcome to the fruit list program!")
    print("Current list:", fruit_list)

    while True:
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            index = int(input("Enter the index to access: "))
            print("Element at index", index, ":", access_element(fruit_list, index))
        elif choice == "2":
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            result = modify_element(fruit_list, index, new_value)
            if isinstance(result, str): 
                print(result)
            else:
                print("Updated list:", result)
        elif choice == "3":
            start = int(input("Enter the start index: "))
            end = int(input("Enter the end index: "))
            print("Sliced list:", slice_list(fruit_list, start, end))
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()