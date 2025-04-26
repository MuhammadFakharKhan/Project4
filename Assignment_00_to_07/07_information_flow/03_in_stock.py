def num_in_stock(fruit: str):
    if fruit == "apple":
        return 25
    if fruit == "banana":
        return 30
    if fruit == "orange":
        return 15
    if fruit == "grape":
        return 40
    else:
        return 0
def main():
    print("Welcome to the fruit stock checker!")
    fruit = input("Enter the fruit name: ")
    stock = num_in_stock(fruit)
    if stock == 0:
        print(f"Sorry, {fruit} is out of stock!")
    else:
        print(f"{fruit} is in {stock}!")
    

if __name__ == "__main__":
    main()