student_objects_list = []
cse_students = []
eee_students = []
civil_students = []
mech_students = []
ece_students = []

cse_subjects = set()
eee_subjects = set()
civil_subjects = set()
mech_subjects = set()
ece_subjects = set()


class Student:

    def __init__(self, id_no, name, department, subjects):
        self.id_no = id_no
        self.name = name
        self.department = department
        self.subjects = subjects
        student_objects_list.append(self)

    def display_student_details(self):
        print("Id_no - {0}\nName - {1}\nDepartment - {2}\nSubjects- {3}\n".format(self.id_no, self.name, self.department, self.subjects))

    def append_in_department(self):
        if self.department == "CSE":
            cse_students.append(self)
            cse_subjects.update(self.subjects)
        elif self.department == "EEE":
            eee_students.append(self)
            eee_subjects.update(self.subjects)
        elif self.department == "Civil":
            civil_students.append(self)
            civil_subjects.update(self.subjects)
        elif self.department == "Mech":
            mech_students.append(self)
            mech_subjects.update(self.subjects)
        elif self.department == "ECE":
            ece_students.append(self)
            ece_subjects.update(self.subjects)


stud_obj1 = Student("36110986", "A.Preetha", "CSE", ["maths", "c_lang", "problem solving", "english"])
stud_obj2 = Student("36110389", "S.Gayathri", "CSE", ["maths", "c_lang", "english"])
stud_obj3 = Student("34025455", "S.Ajaytha", "EEE", ["maths", "electrical", "english"])
stud_obj4 = Student("35579520", "D.Mohan", "Civil", ["maths", "geology", "english"])
stud_obj5 = Student("36100679", "A.Yogesh", "Mech", ["maths", "machines", "english"])
stud_obj6 = Student("36120985", "K.Pachai", "ECE", ["maths", "c_lang", "english"])

Student.append_in_department(stud_obj1)
Student.append_in_department(stud_obj2)
Student.append_in_department(stud_obj3)
Student.append_in_department(stud_obj4)
Student.append_in_department(stud_obj5)
Student.append_in_department(stud_obj6)


def departments(department_students):
    print("No of students: {}".format(len(department_students)))
    for student in department_students:
        print(student.name)


print("Departments (cse, eee, ece, mech, civil)")
dept_name = input("Enter any of the above department which details you want to display:\n")
if dept_name == "cse":
    print("CSE department student details\n")
    departments(cse_students)
    print("CSE department subjects - ", cse_subjects)
elif dept_name == "eee":
    print("EEE department student details\n")
    departments(eee_students)
    print("EEE department subjects - ", eee_subjects)
elif dept_name == "ece":
    print("ECE department student details\n")
    departments(ece_students)
    print("ECE department subjects - ", ece_subjects)
elif dept_name == "civil":
    print("Civil department student details\n")
    departments(civil_students)
    print("Civil department subjects - ", civil_subjects)
elif dept_name == "mech":
    print("Mechanical department student details\n")
    departments(mech_students)
    print("Mechanical department subjects - ", mech_subjects)
else:
    print("Entered wrong input")

print("\nName of the departments where students take more than 3 courses")
depts_3_courses_above = set()
for student in student_objects_list:
    if len(student.subjects) > 3:
        depts_3_courses_above.add(student.department)
print(depts_3_courses_above)

# Just give two lists of department subjects to find common subjects like the below line
print("\nCommon subjects between cse & eee departments - ", cse_subjects.intersection(eee_subjects))

'''
Output:
Departments (cse, eee, ece, mech, civil)
Enter any of the above department which details you want to display:
cse
CSE department student details

No of students: 2
A.Preetha
S.Gayathri
CSE department subjects -  {'maths', 'english', 'c_lang', 'problem solving'}

Name of the departments where students take more than 3 courses
{'CSE'}

Common subjects between cse & eee departments -  {'english', 'maths'}
'''






