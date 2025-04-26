def get_name(name:str):
    return name
def main():
    name = input("Enter your name : ")
    print(f"Hello {get_name(name)}")


if __name__ == "__main__":
    main()
