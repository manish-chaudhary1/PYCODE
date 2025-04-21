usable_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_+=<>?/|\\{}[]~`")
usable_symbols = set("!@#$%^&*()-_+=<>?/|\\{}[]~`")
print("Welcome to the password validator!")
print("Please enter a password to validate.")
print("Password must contain at least one uppercase letter, one lowercase letter, one digit, and one symbol.")
password = input("Enter password: ")
length = len(password)
if length < 8:
    print("Password must be at least 8 characters long.")
    
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
# Maintain a history of previously entered passwords

# Check for digits in the password
has_digit = any(char.isdigit() for char in password)
has_symbol = any(char in usable_symbols for char in password)
if not has_upper:
    print("Password must contain at least one uppercase letter.")
if not has_lower:
    print("Password must contain at least one lowercase letter.")
if not has_digit:
    print("Password must contain at least one digit.")
if not has_symbol:
    print("Password must contain at least one symbol.")

if not has_digit or not has_symbol or not has_upper or not has_lower:
    print("Password is invalid.")
if has_upper and has_lower and has_digit and has_symbol:
    print("Password is valid.")

import os

# Load password history from a file
password_history_file = "password_history.txt"
if os.path.exists(password_history_file):
    with open(password_history_file, "r") as file:
        password_history = file.read().splitlines()
else:
    password_history = []

# Check if the password is already used
if password in password_history:
    print("Password has already been used. Please choose a new password.")
else:
    password_history.append(password)
    with open(password_history_file, "a") as file:
        file.write(password + "\n")