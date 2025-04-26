Sorry = "Sorry I only tell jokes"

Joke = "Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'."
def main():

    print("Welcome to the Joke Bot!")
    prompt = input("What do you want: ")
    if prompt == "Joke" or prompt == "joke" or prompt == "JOKES" or prompt == "jokes" or prompt == "Jokes":
        print(Joke)
    else:
        print(Sorry)

if __name__ == "__main__":
    main()
