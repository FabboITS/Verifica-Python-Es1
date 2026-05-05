import random
import string

ALPHANUMERIC_CHARS = string.ascii_letters + string.digits
COMPLEX_ASCII_CHARS = ''.join(chr(i) for i in range(33, 127))


def generate_simple_password(length=8):
    print(f"DEBUG: Generating simple password with length={length}")
    password = ''.join(random.choice(ALPHANUMERIC_CHARS) for _ in range(length))
    print(f"DEBUG: Simple password generated={password}")
    return password


def generate_complex_password(length=20):
    print(f"DEBUG: Generating complex password with length={length}")
    password = ''.join(random.choice(COMPLEX_ASCII_CHARS) for _ in range(length))
    print(f"DEBUG: Complex password generated={password}")
    return password


def prompt_user_choice():
    print("Come desidera la password?")
    print("1. semplice (8 caratteri alfanumerici)")
    print("2. complessa (20 caratteri ASCII)")
    while True:
        choice = input("Inserisci 1 o 2: ").strip()
        print(f"DEBUG: User input choice={choice}")
        if choice in {"1", "2"}:
            return int(choice)
        print("Input non valido. Per favore inserisci 1 o 2.")

if __name__ == "__main__":
    user_choice = prompt_user_choice()
    if user_choice == 1:
        password = generate_simple_password()
        print("Password semplice generata:", password)
    else:
        password = generate_complex_password()
        print("Password complessa generata:", password)