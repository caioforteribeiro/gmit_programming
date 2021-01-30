#Reads user's name and age, and prints them in a sentence
#Author: Caio Forte Ribeiro

#Asks user's name and age and stores in variables "name" and "age"
name = input("What's your name?\n")
age = input("How old are you?\n")

#Prints out greeting
print("Hello, {}!\tYour age is {}.".format(name,age))