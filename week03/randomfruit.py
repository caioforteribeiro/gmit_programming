#Program that returns a random fruit from a list
#Author: Caio Forte Ribeiro

import random

fruits = ["Apple", "Banana", "Peach", "Pear", "Strawberry"] #creates list of fruits

index = random.randint(0, len(fruits)-1) #pulls a random index from the list / indexes start on 0

randomFruit = fruits[index] #stores the random index of the list in randomFruit

print("Here's your random fruit: {}".format(randomFruit)) #prints the random indexed item from the list