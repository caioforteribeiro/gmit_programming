#Program that asks the user to guess a number
#Author: caio Forte Ribeiro

number = 19

guess = int(input("Try to guess my number:\n"))

while guess != number:
    guess = int(input("Nope, but I'll let you try one more time:\n"))

print("You've nailed it: my number is {} indeed!".format(guess))