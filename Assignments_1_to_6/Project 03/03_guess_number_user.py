import random

def get_user_guess(low, high):
    
    while True:
        try:
            guess = int(input(f"Enter your guess ({low} to {high}): "))
            if low <= guess <= high:
                return guess
            print(f"Please enter a number between {low} and {high}.")
        except ValueError:
            print("Please enter a valid integer.")

def play_game(low, high):
    
    
    secret_number = random.randint(low, high)
    attempts = 0
    
    print(f"I'm thinking of a number between {low} and {high}. Try to guess it!")
    
    while True:
        
        guess = get_user_guess(low, high)
        attempts += 1
        
        
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

def main():
    
    print("Welcome to the Guess the Number Game!")
    try:
        low = int(input("Enter the lower bound of the range: "))
        high = int(input("Enter the upper bound of the range: "))
        if low >= high:
            print("Lower bound must be less than upper bound.")
            return
        play_game(low, high)
    except ValueError:
        print("Please enter valid integers for the range.")

if __name__ == "__main__":
    main()
    
    
    while True:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == 'y':
            main()
        elif play_again == 'n':
            print("Thanks for playing!")
            break
        else:
            print("Please enter 'y' or 'n'.")