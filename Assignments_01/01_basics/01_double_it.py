def main():
    user = int(input("Enter a number: "))
    curr_value = user

    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value, end=" ")

if __name__ == "__main__":
    main()