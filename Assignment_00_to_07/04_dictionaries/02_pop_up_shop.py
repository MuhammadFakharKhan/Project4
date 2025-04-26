def fruit_shop_calculator():
    
    fruit_prices = {
        'apple': 2.5,
        'durian': 15.0,
        'jackfruit': 10.0,
        'kiwi': 1.75,
        'rambutan': 5.0,
        'mango': 3.5
    }
    
    total_cost = 0.0
    
    print("Welcome to the Fruit Shop Calculator!")
    print("Available fruits:", ", ".join(fruit_prices.keys()))
    print()
    
    
    for fruit, price in fruit_prices.items():
        while True:
            try:
                quantity = int(input(f"How many ({fruit}) do you want?: "))
                if quantity >= 0:
                    total_cost += quantity * price
                    break
                else:
                    print("Please enter a positive number or zero.")
            except ValueError:
                print("Please enter a whole number.")
    
    
    print(f"\nYour total is ${total_cost:.2f}")


fruit_shop_calculator()