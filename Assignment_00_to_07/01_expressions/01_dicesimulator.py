import random

# Global variables
dice1_global = 0
dice2_global = 0

def roll_dice():
    # Local variables - only exist within this function
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2

def roll_and_display():
    # Declare we're using global variables first
    global dice1_global, dice2_global
    
    # Function-scoped variables (different from global ones)
    local_dice1 = "Function dice"
    local_dice2 = "Function dice"
    
    # Roll dice three times
    for roll in range(1, 4):
        # Get new local variables each time we call roll_dice()
        die1, die2 = roll_dice()
        
        print(f"\nRoll {roll}:")
        print(f"Local dice: {die1}, {die2}")
        print(f"Function-scoped variables: {local_dice1}, {local_dice2}")
        
        # Update the global variables
        dice1_global, dice2_global = die1, die2
        print(f"Global dice after update: {dice1_global}, {dice2_global}")

# Main program
print("=== Dice Rolling Simulation ===")
print(f"Initial global dice: {dice1_global}, {dice2_global}\n")

roll_and_display()

print("\nFinal global dice values:", dice1_global, dice2_global)