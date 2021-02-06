# Program that prints names, types and values of 5 pre-defined variables
#Author: Caio Forte Ribeiro

i = 3
fl = 3.5
isa = True #the name of the variable is slightly changed, as "is" is a built-in python operator
memo = "how now Brown Cow"
lots = []

#variable names are printed as str, types as types and values depending on type
print("variable {} is of type: {} and value: {}". format ("i", type(i), i))
print("variable {} is of type: {} and value: {}". format ("fl", type(fl), fl))
print("variable {} is of type: {} and value: {}". format ("is", type(isa), isa))
print("variable {} is of type: {} and value: {}". format ("memo", type(memo), memo))
print("variable {} is of type: {} and value: {}". format ("lots", type(lots), lots))