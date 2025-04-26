def print_divisors(num:int):
    print(f"The divisors of {num} are:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)
def main():
    print("This program prints the divisors of a number")
    num = int(input("Enter a number: "))
    print_divisors(num)

if __name__ == "__main__":
    main()