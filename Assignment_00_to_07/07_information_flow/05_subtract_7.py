def subtract_seven():
    num = int(input("Enter a number: "))
    return num - 7
def main():

    print("Welcome to the subtract 7 program!")
    result = subtract_seven()
    print(f"The result is: {result}")
if __name__ == "__main__":
    main()