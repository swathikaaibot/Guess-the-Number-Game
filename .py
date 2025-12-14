# Guess the Number Game

import random

print("Welcome to the Guess the Number Game!")
print("I have selected a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try a higher number.")
    elif guess > secret_number:
        print("Too high! Try a lower number.")
    else:
        print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        break
