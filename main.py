"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jana Šámalová
email: samalova.jana@gmail.com
"""
import random

def generate_secret_number():
    digits = list("123456789")
    random.shuffle(digits)
    digits.append(random.choice("0123456789"))
    return "".join(digits[:4])

def is_valid_guess(guess):
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

def evaluate_guess(secret, guess):
    bulls = sum(1 for s, g in zip(secret, guess) if s == g)
    cows = sum(1 for g in guess if g in secret) - bulls
    return bulls, cows

print("""Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------""")

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