#Program that generates a list of 10 random numbers (0-100)
#and print the top three numbers
#Author: Caio Forte Ribeiro

import random

rangeFrom = 0
rangeTo = 100
listSize = 10
top3 = 3

numbers = []

for x in range(0,10):
    numbers.append(random.randint(rangeFrom,rangeTo))

print ("Here are your {} random numbers:\n {}".format(listSize,numbers))

topNumbers = numbers.copy()
topNumbers.sort(reverse = True)

print ("And here are your top {} numbers:\n {}".format(top3,topNumbers[0:top3]))
