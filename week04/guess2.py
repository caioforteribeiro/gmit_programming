#Program that asks the user to guess a random number
#and says if the guess was too high, or too low
#Author: caio Forte Ribeiro

import random

number = random.randint(1,100)

guess = int(input("Try to guess my number:\n"))

while guess != number:
    if guess > number:
        guess = int(input("Nope... too high. Try again:\n"))
    else:
        guess = int(input("Too low. Try again:\n"))

print("You've nailed it: my number is {} indeed!".format(guess))