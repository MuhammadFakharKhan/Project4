def main():
    print("This program adds two numbers.")
    num1 = input("Please Enter first number: ")
    num1 = int(num1)
    num2  = input("Please Enter second number: ")
    num2 = int(num2)
    total = num1 + num2
    print("The sum of the two numbers you provided is : " + str(total) + ".")


if __name__ == '__main__':
    main()