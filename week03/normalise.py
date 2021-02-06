#Program that reads a string, 
#removes leading and trailing spaces, 
#converts the string to lowercase, 
#and gives the input and output lenghts of the string

#Author: Caio Forte Ribeiro

originalString = input("Please enter a string:\n") #Asks for user's input
noTrail = originalString.strip() #removes trailing and leading spaces
lowercase = noTrail.lower() #converts the whole string to lowercase
inputLenght = len(originalString) 
outputLenght = len(lowercase)

print ("Your normalised string is: "+ lowercase) #prints resulting string

#prints input and output lenghts
print("Your original string had {} characters, and was trimmed down to {} characters.".format(inputLenght, outputLenght))

