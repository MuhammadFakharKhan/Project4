def print_multiple(message:str, num:int):
    for i in range(num):
        print(message)
def main():
    print("This program prints a message multiple times")
    message = input("Enter a message: ")
    num = int(input("Enter the number of times to print the message: "))
    print_multiple(message, num)


if __name__ == "__main__":
    main()