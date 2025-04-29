name = input("Please enter your name: ")
while True:
    try:
        fav_number_str = input("Please enter your favorite whole number: ")
        fav_number = int(fav_number_str)
        break # Exit the loop if input is valid
    except ValueError:
        print("Invalid input. Please enter a whole number.")

print(f"Hello, {name}! Your favorite number is {fav_number}.")
print(f"That's the square root of {fav_number**2}.")
