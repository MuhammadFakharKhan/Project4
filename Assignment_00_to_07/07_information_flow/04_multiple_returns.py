def get_user_data():
    user_first_name = input("Enter your first name: ")
    user_last_name = input("Enter your last name: ")
    user_email = input("Enter your email: ")
    return user_first_name, user_last_name, user_email
def main():
    print("Welcome to the user data collector!")
    first_name, last_name, email = get_user_data()
    print(f"{first_name} {last_name} {email} ")
    

if __name__ == "__main__":
    main()