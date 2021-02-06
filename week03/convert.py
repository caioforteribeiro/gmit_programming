#Converts float dollars into absolute cents
#Author: Caio Forte Ribeiro

dollar = float(input("Enter your amount in dollars:\n"))

#limited decimals considered for converting to 2
#in case the user enters a value with multiple decimals, like 2.5678
cents = round(dollar, 2) * 100

#absolute value in cents will return as float
#so we convert to int, as the expected output
absoluteCents = int(abs(cents))

print("Your absolute amount in cents is {}".format(absoluteCents))