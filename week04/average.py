#Program that reads numbers until user enters 0
#then prints average of entered numbers
#Author: Caio Forte Ribeiro

numbers = []

number = int(input("Enter a number (enter 0 to quit):\n"))

while number != 0:
    numbers.append(number)
    
    number = int(input("Enter another number (0 to quit):\n"))

for x in numbers: #for loops do not require preset variables
    print(x)

average = float(sum(numbers) / len((numbers)))
print("The average of all your numbers is: {}".format(average))