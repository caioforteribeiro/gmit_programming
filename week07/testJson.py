#using json module to store dict
#Author: Caio Forte Ribeiro

import json
students = []
filename = "students.json"

def writeDict(obj):
    with open(filename, "wt") as f:
        json.dump(obj, f)

def displayMenu():
    print("Select an action from the following:")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(s) Save students")
    print("\t(q) Quit")
    choice = input ("Type one letter (a/v/s/q):\n")

    return choice

def doAdd():
    currentStudent = {}
    currentStudent["name"] = input("Enter name: ")
    currentStudent["modules"] = readModules()
    students.append(currentStudent)

def readModules():
    modules = []
    moduleName = input("\tEnter the name of the first module (blank to quit): ").strip()

    while moduleName != "":
        module = {}
        module["name"] = moduleName
        module["grade"] = int(input("\t\tEnter grade: "))
        modules.append(module)
        moduleName = input("\tEnter next module name (blank to quit): ").strip()
    
    return modules

def displayModules(modules):
    print("\tName:      \tGrade:")
    for module in modules:
        print("\t{}     \t{}".format(module["name"], module["grade"]))

def doView():
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])

def doSave():
    writeDict(students)
    print("Students saved")

    
students = []
choice = displayMenu()
while choice != "q":
    if choice == "a":
        doAdd()
    elif choice == "v":
        doView()
    elif choice == "s":
        doSave()
    elif choice != "q":
        print("\n\nPlease select a, v, s, or q\n\n")
    choice = displayMenu()