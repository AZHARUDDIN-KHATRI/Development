import random
import string

# Define character pools
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = letters + digits + symbols

# Set the desired password length
password_length = 12

# Generate the password
password = "".join(random.choice(all_characters) for i in range(password_length))

print("Generated Password:", password)