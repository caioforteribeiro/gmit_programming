#Program removes one number at a time from a list
#and prints the resulting lists each time
#Author: Caio Forte Ribeiro

import random

#define variables
queue = []
queueLenght = 10
queueRange = 100

#sets the size of the resulting list
for number in range(0, queueLenght):
    #adds random numbers, from 1 to 100, to the list
    queue.append(random.randint(1, queueRange))

print("This is your queue:\n", queue)

while len(queue) > 0:
    removedNumber = queue.pop(0)
    print("The number ", removedNumber, " was removed. Your new queue is now:\n", queue)

print("Your queue is now empty.")