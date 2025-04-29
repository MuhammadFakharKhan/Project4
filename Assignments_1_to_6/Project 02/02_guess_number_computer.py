import random

def get_user_feedback(guess, low, high):
    """Get feedback from the user about the computer's guess."""
    while True:
        print(f"Is {guess} your number? (Enter 'h' if too high, 'l' if too low, 'c' if correct): ")
        feedback = input().lower()
        if feedback in ['h', 'l', 'c']:
            return feedback
        print(f"Please enter 'h', 'l', or 'c'. The range is {low} to {high}.")

def computer_guess(low, high):
    """Function where the computer guesses the user's number."""
    print(f"Think of a number between {low} and {high}, and I'll try to guess it!")
    attempts = 0
    
    while True:
        if low > high:
            print("Invalid range detected. Please check your feedback.")
            break
        
        # Computer makes a guess (using binary search strategy for efficiency)
        guess = (low + high) // 2
        attempts += 1
        
        # Get user feedback
        feedback = get_user_feedback(guess, low, high)
        
        if feedback == 'c':
            print(f"I guessed your number {guess} in {attempts} attempts!")
            break
        elif feedback == 'h':
            high = guess - 1  # Number is lower than the guess
        elif feedback == 'l':
            low = guess + 1   # Number is higher than the guess

def main():
    """Main function to set up and start the game."""
    print("Welcome to the Guess the Number Game!")
    try:
        low = int(input("Enter the lower bound of the range: "))
        high = int(input("Enter the upper bound of the range: "))
        if low >= high:
            print("Lower bound must be less than upper bound.")
            return
        computer_guess(low, high)
    except ValueError:
        print("Please enter valid integers for the range.")

if __name__ == "__main__":
    main()

    # Ask if the user wants to play again
    while True:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == 'y':
            main()
        elif play_again == 'n':
            print("Thanks for playing!")
            break
        else:
            print("Please enter 'y' or 'n'.")