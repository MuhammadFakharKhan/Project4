def main():
    print("This program converts Fahrenheit to Celsius.")

    fahrenheit = float(input("Enter temperature in Fahrenheit (°F): "))
    
    # Convert Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    
    # Output the result
    print(f"The temperature of {fahrenheit}°F in Celsius is: {celsius:.2f}°C")


if __name__ == '__main__':
    main()