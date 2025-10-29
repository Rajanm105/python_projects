import secrets
import string

def generate_strong_password(length=16):

    if length < 12:
        raise ValueError("Password length should be at least 12")
    
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars

    while True:
        password = ''.join(secrets.choice(alphabet) for _ in range(length))

        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in special_chars for c in password)):
            return password
        
if __name__ == "__main__":
    try:
        pw_length = int(input("Enter desired password length (12 or more): "))
        new_password = generate_strong_password(pw_length)
        print("Generated Password: ", new_password)
    except ValueError as e:
        print(e)