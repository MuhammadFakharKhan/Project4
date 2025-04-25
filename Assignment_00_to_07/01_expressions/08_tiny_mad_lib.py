def main():
    SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"
    
    print("Please type an adjective and press enter.")
    adjective = input().strip()
    
    print("Please type a noun and press enter.")
    noun = input().strip()
    
    print("Please type a verb and press enter.")
    verb = input().strip()
    
    print(f"{SENTENCE_START} {adjective} {noun} {verb}!")

if __name__ == '__main__':
    main()