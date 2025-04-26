def make_sentence(word: str, part_of_speech: int):
    if part_of_speech == 0:
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("Invalid part of speech.")
    
def main():
    print("This program generates a sentence based on the word you provide.")
    word = input("Enter a word: ")
    print("Choose a part of speech:")
    print("0 - Noun")
    print("1 - Verb")
    print("2 - Adjective")
    part_of_speech = int(input("Enter the number corresponding to your choice: "))
    
    make_sentence(word, part_of_speech)

if __name__ == "__main__":
    main()