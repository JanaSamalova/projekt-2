"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jana Šámalová
email: samalova.jana@gmail.com
"""
import random

def generate_secret_number() -> str:
    """
    Generates a random 4-digit secret number with unique digits.
    The first digit cannot be zero.
    
    Returns:
        str: The generated 4-digit secret number.
    """
    digits = list("0123456789")
    random.shuffle(digits)
    if digits[0] == '0':
        digits[0], digits[1] = digits[1], digits[0]
    return "".join(digits[:4])

def is_valid_guess(guess: str) -> bool:
    """
    Validates the user's guess.
    The guess must be a 4-digit number with unique digits and cannot start with zero.
    
    Args:
        guess (str): The user's input guess.
    
    Returns:
        bool: True if the guess is valid, False otherwise.
    """
    if not guess.isdigit():
        print("Invalid input! Please enter a 4 digit number.")
        return False
    if len(guess) != 4:
        print("Invalid length! The number must be exactly 4 digits.")
        return False
    if guess[0] == '0':
        print("The number cannot start with zero.")
        return False
    if len(set(guess)) != 4:
        print("The digits must be unique.")
        return False
    return True

def evaluate_guess(secret: str, guess: str) -> tuple[int, int]:
    """
    Evaluates the user's guess against the secret number.
    
    Args:
        secret (str): The secret 4-digit number.
        guess (str): The user's guess.
    
    Returns:
        tuple[int, int]: Number of bulls (correct digits in correct place) 
                         and cows (correct digits in wrong place).
    """
    bulls = sum(1 for s, g in zip(secret, guess) if s == g)
    cows = sum(1 for g in guess if g in secret) - bulls
    return bulls, cows

def print_text(text: str) -> None:
    """
    Prints the given text.
    
    Args:
        text (str): The text to be printed.
    """
    print(text)

def main() -> None:
    """
    Main function to run the Bulls and Cows game.
    """
    greeting = """Hi there!
-----------------------------------------------
I've generated a random 4-digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------"""
    
    print_text(greeting)
    secret_number = generate_secret_number()
    attempts = 0
    
    while True:
        guess = input(">>> ")
        if not is_valid_guess(guess):
            continue
        
        attempts += 1
        bulls, cows = evaluate_guess(secret_number, guess)
        if bulls != 4:
            print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'}")
        
        if bulls == 4:
            print("Correct, you've guessed the right number")
            print(f"in {attempts} guesses!")
            print("-----------------------------------------------")
            print("That's amazing!")
            break

if __name__ == "__main__":
    main()