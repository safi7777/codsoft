import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    if not (use_uppercase or use_lowercase or use_digits or use_special):
        raise ValueError("At least one character type must be selected.")
   
    # Define the character sets
    all_characters = ""
    if use_uppercase:
        all_characters += string.ascii_uppercase
    if use_lowercase:
        all_characters += string.ascii_lowercase
    if use_digits:
        all_characters += string.digits
    if use_special:
        all_characters += string.punctuation
   
    # Ensure the password contains at least one character from each selected type
    password_chars = []
    if use_uppercase:
        password_chars.append(random.choice(string.ascii_uppercase))
    if use_lowercase:
        password_chars.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password_chars.append(random.choice(string.digits))
    if use_special:
        password_chars.append(random.choice(string.punctuation))
   
    # Fill the rest of the password length with random characters
    if len(password_chars) > length:
        raise ValueError("Password length is too short to accommodate all character types.")
   
    remaining_length = length - len(password_chars)
    password_chars += [random.choice(all_characters) for _ in range(remaining_length)]
   
    # Shuffle the list to ensure randomness
    random.shuffle(password_chars)
   
    # Join list into a string
    return ''.join(password_chars)

def main():
    print("Welcome to Password Generator Application!")

    # Prompt the user to specify the length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Length must be a positive integer. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
   
    # Prompt the user for character types
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
   
    try:
        # Generate the password
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        # Display the password
        print("Generated password:", password)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
