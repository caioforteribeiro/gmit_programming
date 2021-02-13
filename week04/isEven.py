#Program that reads a number and tells if it's even or odd
#Author: Caio Forte Ribeiro

#input should be an integer, 
#as floats cannot be evaluated as evens or odds
number = int(input("Enter a number:\n"))

while number != -1:
    #tests if number is divisible by 2
    if (number%2 == 0):
        print("The number {} is even".format(number))

    #if not, then:
    else:
        print("The number {} is odd".format(number))
        
    number = int(input("Dude, you should really try entering -1!\n"))

if number == -1:
    print("Yey, now we're talking")