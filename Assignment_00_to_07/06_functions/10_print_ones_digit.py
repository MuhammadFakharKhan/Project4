def print_ones_digit(num:int):
    print(f"The ones digit of {num} is {num % 10}")

def main():
    print("This program prints the ones digit of a number")
    num = int(input("Enter a number: "))
    print_ones_digit(num)


if __name__ == "__main__":
    main()