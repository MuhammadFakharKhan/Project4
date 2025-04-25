def sum_numbers(numbers):
    total = 0  
    
    for num in numbers:
        total += num  
    
    return total  # Return the final sum

numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_numbers(numbers_list)
print(f"The sum is: {result}")  