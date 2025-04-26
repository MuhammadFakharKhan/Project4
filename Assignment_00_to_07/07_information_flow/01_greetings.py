def greet(name: str):
    return f"Greetings {name}!"

def main():
    name = input("What's your name? ")
    print(greet(name))  # Call greet and print the returned greeting

if __name__ == "__main__":
    main()
