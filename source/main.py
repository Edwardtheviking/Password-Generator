import random;import string;import os; import sys;version = "1.0.0";lowercase = string.ascii_lowercase;uppercase = string.ascii_uppercase;digits = string.digits;special_characters = r".,-?:_;*'\"+!%/=()\\$[]<>#&@{}";
def generate_password(length, special=0):
    characters = lowercase + uppercase + digits
    if special:characters += special_characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def set_window_title(title):
    if os.name == 'nt':
        os.system(f'title {title}')
def main():
    set_window_title("Password Generator")
    print(f"Welcome to Password Generator v{version}!")
    while True:
        user_input = input("").strip().split()
        if not user_input:continue
        command = user_input[0]
        if command == '--help':print("--------------------------------------");print("help - prints out existing commands");print("generate <length> <special> - generates a password with <length> length, and with the input of 0 or 1 for <special> characters");print("--------------------------------------")
        elif command == '--generate':
            if len(user_input) < 2:print("Missing arguments.");continue
            try:
                length = int(user_input[1])
                special = int(user_input[2]) if len(user_input) > 2 else 0
                if special not in [0, 1]:raise ValueError
                password = generate_password(length, special);print(password)
            except ValueError:print("Invalid arguments.")
        else:print("Invalid input.")
if __name__ == "__main__":main()