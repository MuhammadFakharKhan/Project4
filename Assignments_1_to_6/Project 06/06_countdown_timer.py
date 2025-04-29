import time

def countdown(seconds):
    
    while seconds > 0:
        
        minutes = seconds // 60
        secs = seconds % 60
        
        timer = f"{minutes:02d}:{secs:02d}"
        print(f"Time remaining: {timer}", end="\r") 
        time.sleep(1) 
        seconds -= 1
    
    print("Time's up!          ")  

def main():
    
    print("Welcome to the Countdown Timer!")
    while True:
        try:
            seconds = int(input("Enter the countdown duration in seconds: "))
            if seconds <= 0:
                print("Please enter a positive number of seconds.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")
    
    countdown(seconds)
    
    
    while True:
        replay = input("Do you want to start another countdown? (y/n): ").lower()
        if replay == 'y':
            main()
        elif replay == 'n':
            print("Thank you for using the Countdown Timer!")
            break
        else:
            print("Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()