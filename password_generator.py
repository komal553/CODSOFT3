import random
import string

def generate_password(length=8):
    if length < 4:
        return "Password too short! Must be at least 4 characters."

    # Characters to choose from
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure password has at least one of each type
    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random characters
    all_chars = upper + lower + digits + symbols
    password += random.choices(all_chars, k=length - 4)

    # Shuffle to avoid predictable patterns
    random.shuffle(password)
    return ''.join(password)

# Ask user for length
try:
    length = int(input("Enter password length: "))
    print("Generated Password:", generate_password(length))
except ValueError:
    print("Please enter a valid number.")
