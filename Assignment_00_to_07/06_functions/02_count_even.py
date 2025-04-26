def count_even():
    # Initialize an empty list to store numbers
    numbers = []
    
    # Keep asking for input until user presses Enter
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        
        # Stop if user pressed Enter without entering anything
        if user_input == "":
            break
            
        # Try to convert input to integer
        try:
            num = int(user_input)
            numbers.append(num)
        except ValueError:
            print("Please enter a valid integer or press enter to stop.")
    
    # Count even numbers
    even_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
    
    # Print the result
    print(f"Number of even numbers: {even_count}")

# Example usage
if __name__ == "__main__":
    count_even()
