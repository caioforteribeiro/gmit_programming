#Program that stores and prints out data from a student
#(name, list of courses, grades)
#Author: Caio Forte Ribeiro

student = {
    "name": "Caio",
    "courses": [
        {
            "courseName": "Programming and Scripting",
            "grade": 75
        },
        {
            "courseName": "Computer Architecture & Technology Convergence",
            "grade": 70
        }      
    ]
}

print("Student: {}".format(student["name"]))

for course in student["courses"]:
    print("\t {}: {}".format(course["courseName"],course["grade"]))