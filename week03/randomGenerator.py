#Programs that prints out a random number within an interval
#Author: Caio Forte Ribeiro

#imports random module
import random

x = int(input("Enter first number: ")) #asks for values and stores them in int variables
y = int(input("Enter second number: "))

#sets random number within the interval randint between x and y
number = random.randint(x,y)

print("Your random number between {} and {} is {}".format(x, y, number))