import random

round_limit = 5  # Number of rounds to play

def main():
    print("Welcome to the High-Low game!")
    print(f"You will play {round_limit} rounds. Try to guess correctly to earn points!\n")
    
    score = 0  # Initialize the player's score

    for round_number in range(1, round_limit + 1):
        print(f"Round {round_number} of {round_limit}")
        
        user_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        print(f"Your number is {user_number}")
        
        # Ask the user for their guess
        user_guess = input("Enter 'h' if your number is higher, 'l' if it is lower  than computer: ").lower()
        
        # Validate input
        while user_guess not in ['h', 'l']:
            user_guess = input("Invalid input. Please enter 'h' for higher or 'l' for lower: ").lower()
        
        # Determine if the user's guess is correct
        if (user_guess == 'h' and user_number > computer_number) or (user_guess == 'l' and user_number < computer_number):
            print("Correct! You earned a point.")
            score += 1
        else:
            print("Wrong guess!")
        
        print(f"The computer's number was {computer_number}.\n")
    
    # Game over, display the final score
    print(f"Game over! Your final score is {score} out of {round_limit}.")

if __name__ == "__main__":
    main()