def in_range(n, low, high):
    """Returns True if n is between low and high, inclusive."""
    return low <= n <= high
def main():
    print("Welcome to the range checker!")
    n = int(input("Enter a number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))
    
    if in_range(n, low, high):
        print(f"{n} is in the range [{low}, {high}]")
    else:
        print(f"{n} is not in the range [{low}, {high}]")

if __name__ == "__main__":
    main()