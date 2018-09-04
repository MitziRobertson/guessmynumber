# Guessing game based on an idea from Teach Your Kids to Code by Bryson Payne

import random

# ask the user to enter the lowest number
lowest = int(input("plesas enter the lowest number: "))

# ask the user to enter the biggest number
biggest = int(input("plesas enter the biggest number: "))

the_number = random.randint(lowest, biggest)

print("Guess a number between ", lowest, " and ", biggest)

guess = int(input(": "))

while guess != the_number:
    if guess > the_number:
        print(guess, "was too high. try again.")
    if guess < the_number:
        print(guess, "was too low. try again:")
    guess = int(input("Guess again: "))

print(guess, "was the number! you win!")

