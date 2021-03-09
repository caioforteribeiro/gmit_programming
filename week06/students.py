#Program that allows the user to view students on a dataset
#It also alloes the user to add new students to the dataset
#Author: Caio Forte Ribeiro

def displayMenu():
    print("Select an action from the following:")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input ("Type one letter (a/v/q):\n")

    return choice

def doAdd(students):
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

def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])
    
students = []
choice = displayMenu()
while choice != "q":
    if choice == "a":
        doAdd(students)
    elif choice == "v":
        doView(students)
    elif choice != "q":
        print("\n\nPlease select a, v, or q\n\n")
    choice = displayMenu()

print("You chose {}".format(choice))