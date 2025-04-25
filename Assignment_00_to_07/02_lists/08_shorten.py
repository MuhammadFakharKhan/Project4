def shorten(lst):
    
    MAX_LENGTH = 3  # Ensure MAX_LENGTH is defined within the function
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  # Remove the last item
        print(f"Removed: {removed_item}")  # Print the removed item
    return lst

def main():
    lst = [1, 2, 3, 4, 5]  # Example list for testing
    shortened_list = shorten(lst)
    print(f"Shortened list: {shortened_list}")  # Output the shortened list

if __name__ == "__main__":
    main()
