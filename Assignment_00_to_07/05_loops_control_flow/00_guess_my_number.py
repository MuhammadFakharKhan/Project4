import random
def main ():

    secret_number = random.randint(1, 100)

    attempts = 10

    print("Guess My Number Game")
    print("I have selected a number between 1 and 100.")
    print("You have 10 attempts to guess it.")
    guess =int(input("Enter a number: "))

    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
            attempts -= 1
            if attempts == 0:
                print("You have run out of attempts. The number was", secret_number)
                break
            else:
                print("You have", attempts, "attempts left.")
        guess = int(input("Enter a number: "))
    if guess == secret_number:
        print("Congratulations! You guessed the number", secret_number, "correctly.")



if __name__ == "__main__":
    main()