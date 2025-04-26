def find_average(a: float, b: float) -> float:
    
    return (a + b) / 2

def main():
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    average = find_average(num1, num2)
    print(f"The average of {num1} and {num2} is {average}")

if __name__ == '__main__':
    main()
