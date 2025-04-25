def main():
    print("=== Dice Roller ===")
    import random
    # Simulate rolling two dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    # Calculate the sum of the two dice
    total = dice1 + dice2
    # Display the results
    print(f"Dice 1: {dice1}")
    print(f"Dice 2: {dice2}")
    print(f"Total: {total}")
    print("Roll complete.")


    # Ask the user if they want to roll again
    while True:
        roll_again = input("Do you want to roll again? (yes/no): ").strip().lower()
        if roll_again == 'yes':
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            total = dice1 + dice2
            print(f"Dice 1: {dice1}")
            print(f"Dice 2: {dice2}")
            print(f"Total: {total}")
        elif roll_again == 'no':
            print("Thank you for playing!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    print("Goodbye!")

if __name__ == '__main__':
    main()