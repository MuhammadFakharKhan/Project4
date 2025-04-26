def tall_enough_extension():
    print("This program checks if you are tall enough to ride the roller coaster.")
    
    while True:
        height_input = input("What is your height in ft? (Press Enter to quit): ")
        
        if not height_input:  
            print("Good riddance!")
            break
        
        try:
            height = int(height_input)
            if height >= 5:
                print("You are tall enough to ride the roller coaster!")
            else:
                print("You are not tall enough to ride the roller coaster.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    tall_enough_extension()