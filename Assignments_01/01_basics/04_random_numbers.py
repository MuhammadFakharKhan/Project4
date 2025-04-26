import random

def random_numbers():
    print("Random Numbers")
    print("Here are 10 random numbers between 1 and 100:")
    for random_number in range(10):
        print(random.randint(1, 100), end=" ")

random_numbers()
