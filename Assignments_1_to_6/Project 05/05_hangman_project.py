import random
import string

def get_word():
    
    words = ["python", "programming", "computer", "algorithm", "database", "network", "software", "developer"]
    return random.choice(words).upper()

def display_hangman(lives):
    
    stages = [
        """
           ------
           |    |
           O    |
          /|\\   |
          / \\   |
                |
        =========
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
          /     |
                |
        =========
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
                |
                |
        =========
        """,
        """
           ------
           |    |
           O    |
          /|    |
                |
                |
        =========
        """,
        """
           ------
           |    |
           O    |
           |    |
                |
                |
        =========
        """,
        """
           ------
           |    |
           O    |
                |
                |
                |
        =========
        """,
        """
           ------
           |    |
                |
                |
                |
                |
        =========
        """
    ]
    return stages[lives]

def get_valid_guess(guessed_letters):
    
    while True:
        guess = input("Guess a letter: ").upper()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess not in string.ascii_uppercase:
            print("Please enter a valid letter (A-Z).")
        elif guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
        else:
            return guess

def play_hangman():
    
    word = get_word()
    word_letters = set(word)  # Letters in the word to be guessed
    guessed_letters = set()   # Letters guessed by the user
    lives = 6                 # Number of lives (incorrect guesses allowed)
    
    print("\nWelcome to Hangman!")
    print("Try to guess the word, one letter at a time.")
    
    while lives > 0 and word_letters:
        
        print(display_hangman(lives))
        print("Word: ", " ".join(letter if letter in guessed_letters else "_" for letter in word))
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
        print(f"Lives remaining: {lives}")
        
        
        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)
        
        
        if guess in word_letters:
            word_letters.remove(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
    
    
    print(display_hangman(lives))
    if word_letters:
        print(f"Game Over! The word was: {word}")
    else:
        print(f"Congratulations! You guessed the word: {word}")

def main():
    
    while True:
        play_hangman()
        
        
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again == 'n':
            print("Thanks for playing!")
            break
        elif play_again != 'y':
            print("Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()