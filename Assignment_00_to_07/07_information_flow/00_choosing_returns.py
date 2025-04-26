def is_adult(age:int):
    return age >=18

def main():
    print("Welcome to the adult checker!")
    age = int(input("Enter your age: "))
    if is_adult(age):
        print("You are an adult.")
    else:
        print("You are not an adult.")


if __name__ == "__main__":
    main()