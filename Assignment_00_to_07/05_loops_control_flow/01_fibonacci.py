def fibonacci_sequence(max_value):
    """Prints Fibonacci sequence terms up to the specified max value."""
    a, b = 0, 1
    
    
    print(a, end=' ')
    
    
    while b <= max_value:
        print(b, end=' ')
        
        a, b = b, a + b


MAX_VALUE = 10000


print("Fibonacci sequence up to", MAX_VALUE, ":")
fibonacci_sequence(MAX_VALUE)