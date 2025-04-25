def main():
    print("Type a number to see its square:")
    user_input = float(input())  # Convert input to float for decimal support
    squared = user_input ** 2  # Calculate the square
    print(f"The square of {user_input} is {squared}")


if __name__ == '__main__':
    main()
