import hashlib

def hash_password(password):
    """Hashes a password using SHA-256 algorithm"""
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):
    """
    Checks if the provided password matches the stored hash for the given email
    
    Args:
        email: User's email address
        password_to_check: Password to verify
        stored_logins: Dictionary of {email: hashed_password}
    
    Returns:
        bool: True if password matches, False otherwise
    """
    # Check if email exists in stored_logins
    if email not in stored_logins:
        return False
    
    # Hash the provided password
    hashed_password = hash_password(password_to_check)
    
    # Compare with stored hash
    return stored_logins[email] == hashed_password

# Example usage
if __name__ == "__main__":
    # Sample database of stored logins (email: hashed_password)
    stored_logins = {
        "5593@gmail.com": hash_password("hello123"),
        "idgni@gmail.com": hash_password("securePass!")
    }
    

    print("Welcome to the login system!")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    if login(email, password, stored_logins):
        print("Login successful!")
    else:
        print("Invalid email or password.")
   

