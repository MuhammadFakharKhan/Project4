import random
import string

def generate_password(length):
    
    
    characters = (
        string.ascii_uppercase +  
        string.ascii_lowercase + 
        string.digits +          
        string.punctuation       
    )
    
    
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    
    return password

def generate_passwords(num_passwords, length):
    
    passwords = []
    for _ in range(num_passwords):
        password = generate_password(length)
        passwords.append(password)
    return passwords

def main():
    
    print("Welcome to the Password Generator!")
    
    
    while True:
        try:
            num_passwords = int(input("How many passwords do you want to generate? "))
            if num_passwords <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")
    
    
    while True:
        try:
            length = int(input("Enter the length of each password: "))
            if length <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")
    
    
    passwords = generate_passwords(num_passwords, length)
    print("\nGenerated Passwords:")
    for i, password in enumerate(passwords, 1):
        print(f"Password {i}: {password}")
    
    
    while True:
        replay = input("\nDo you want to generate more passwords? (y/n): ").lower()
        if replay == 'y':
            main()
        elif replay == 'n':
            print("Thank you for using the Password Generator!")
            break
        else:
            print("Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()