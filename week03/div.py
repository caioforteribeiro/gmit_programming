#Reads 2 numbers, divides the first by the second and return the remainder as an int
#Author: Caio Forte Ribeiro

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

div = x // y #floor division
remainder = x % y

print("{} divided by {} is {} with {} as remainder.". format(x, y, div, remainder))