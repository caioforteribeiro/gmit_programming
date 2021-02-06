#Reads 2 numbers and subtracts the second from the first
#Author: Caio Forte Ribeiro

#Create variables and store convert them into int
firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))

#store results in a variable "subtraction"
subtraction = firstNumber - secondNumber

#print a mix of str and int using format function
print("{} minus {} is equal to {}". format(firstNumber, secondNumber, subtraction))
