def main():
    print("=== Division and Remainder Calculator ===")
    dividend = int(input("Please enter an integer to be divided: "))
    divisor = int(input("Please enter an integer to divide by: "))
    
    quotient = dividend // divisor
    remainder = dividend % divisor
    
    print(f"The result of this division is {quotient} with a remainder of {remainder}.")
    print("Division and remainder calculation complete.")

if __name__ == '__main__':
    main()