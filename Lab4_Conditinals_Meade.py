#Date: 9/25/2025 Name: Ji'Yahna Meade
import random

compNumber = random.randint(1,100)
guess = int(input("Guess a number between 1 and 100: "))

if guess < compNumber:
    print("Too low")
elif guess > compNumber:
    print("Too high")
else:
    print("Correct! You guessed the number!")

