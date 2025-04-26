def count_numbers():
    # Initialize an empty dictionary to store number counts
    counts = {}
    
    # Ask the user how many numbers they want to enter
    num_inputs = int(input("How many numbers do you want to enter? "))
    
    # Loop to get all the numbers from the user
    for i in range(num_inputs):
        num = int(input(f"Enter a number ({i+1}/{num_inputs}): "))
        
        # If the number is already in the dictionary, increment its count
        if num in counts:
            counts[num] += 1
        # Otherwise, add it to the dictionary with count 1
        else:
            counts[num] = 1
    
    # Print the results
    print("\nNumber counts:")
    for num, count in sorted(counts.items()):
        print(f"{num} appears {count} {'time' if count == 1 else 'times'}.")

# Run the function
count_numbers()