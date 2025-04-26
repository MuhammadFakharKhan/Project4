import random
def main():
    secret_number = random.randint(0, 99)
    guess_limit = 7
    print("Guess My Number")
    print("I am thinking of a number between 0 and 99...")
    print(f"You have {guess_limit} attempts to guess the number.")
    
    while guess_limit > 0:
        try:
            guess = int(input("Enter a guess: "))
            guess_limit -= 1
            if guess < secret_number:
                print("Your guess is too low")
            elif guess > secret_number:
                print("Your guess is too high")
            else:
                print(f"Congrats! The number was: {secret_number}")
                break
            if guess_limit > 0:
                print(f"You have {guess_limit} attempts remaining.")
            else:
                print(f"Sorry, you've run out of attempts. The number was: {secret_number}")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()

