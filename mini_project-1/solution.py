import ast
class MusicSchool:
    students = {"Gino":   [15, "653-235-345", ["Piano", "Guitar"]],
    "Talina": [28, "555-765-452", ["Cello"]],
    "Eric":   [12, "583-356-223", ["Singing"]]}

    def __init__(self, working_hours, revenue):
        self.working_hours = working_hours
        self.revenue = revenue
    
    def print_students_data(self):
        for student in MusicSchool.students:
            self.print_student(student)

    def print_student(self, student):
        info = MusicSchool.students[student]
        print(f"Student: {student} who is {info[0]} years old and is taking {info[2]}")

    def add_student(self, student, info):
        MusicSchool.students[student] = info

musicSchool1 = MusicSchool(8,15000)
musicSchool1.print_students_data()
musicSchool1.print_student("Eric")
musicSchool1.add_student("binu", [38, "5545-765-4552", ["Cello, mirdangam"]])
print("\n after adding \n ")
musicSchool1.print_students_data()

#challenge
file1 = open("students.txt","w+") 

file1.write(str(MusicSchool.students))

file1.close()
contents = open("students.txt","r").read() 
dictionary = ast.literal_eval(contents)
print(dictionary)
