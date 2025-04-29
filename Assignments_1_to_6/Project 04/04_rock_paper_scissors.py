import random

def get_user_choice():
    
    valid_choices = ["rock", "paper", "scissors"]
    while True:
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if choice in valid_choices:
            return choice
        print("Invalid choice! Please enter rock, paper, or scissors.")

def get_computer_choice():
    
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    
    if user_choice == computer_choice:
        return "It's a tie!"
    
    winning_combinations = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    
    if winning_combinations[user_choice] == computer_choice:
        return "You win!"
    return "Computer wins!"

def play_game():
    
    print("\nLet's play Rock, Paper, Scissors!")
    
    
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

def main():
    
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        play_game()
        
        
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again == 'n':
            print("Thanks for playing!")
            break
        elif play_again != 'y':
            print("Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()