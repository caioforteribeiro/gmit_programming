#function that counts how many times a program was run
#Author: Caio Forte Ribeiro

import os.path
filename = "count.txt"

def readNumber():
    try:
        with open(filename) as f:
            number = int(f.read())
            return number
    except IOError:
        return 0
def writeNumber(number):
    with open(filename, "wt") as f:
        f.write(str(number))

if not os.path.isfile(filename):
    print("File does not exist")
    writeNumber(0)
    
num = readNumber()
num += 1
print("You have run this program {} times".format(num))
writeNumber(num)
