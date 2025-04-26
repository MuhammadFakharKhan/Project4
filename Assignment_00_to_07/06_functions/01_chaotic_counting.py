import random

DONE_LIKELIHOOD = 0.2  

def done():
    """Returns True with probability DONE_LIKELIHOOD"""
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
   
    for i in range(1, 11):  
        print(i, end=' ')
        if done():
            return  

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.", end=' ')
    chaotic_counting()
    print("\nI'm done.")

if __name__ == "__main__":
    main()