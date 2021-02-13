#Program that asks for a mark
#and returns the corresponding grade

#Author: Caio Forte Ribeiro

mark = round(float(input("Enter your mark:\n")))

if mark < 0 or mark > 100: #marks should be between 0 and 100
    print("Enter a number between 0 and 100")

elif mark < 40: #not including 40
    print("Fail")
elif mark < 50: #not including 50
    print("Pass")
elif mark < 60: #not including 60
    print("Merit1")
elif mark < 70: #not including 70
    print("Merit2")
else: #from 70 (included) to 100 (also included)
    print("Distinction")
