cse_students = []
eee_students = []
civil_students = []
mech_students = []
ece_students = []

cse_subjects = []
eee_subjects = []
civil_subjects = []
mech_subjects = []
ece_subjects = []


class Student:

    def __init__(self, id_no, name, department, subjects):
        self.id_no = id_no
        self.name = name
        self.department = department
        self.subjects = subjects

    def display_student_details(self):
        print("Id_no - {0}\nName - {1}\nDepartment - {2}\nSubjects- {3}\n".format(self.id_no, self.name, self.department, list(self.subjects)))

    def department_details(self):
        if self.department == "CSE":
            cse_students.append(self)
            for subject in self.subjects:
                if subject not in cse_subjects:
                    cse_subjects.append(subject)

        elif self.department == "EEE":
            eee_students.append(self)
            for subject in self.subjects:
                if subject not in eee_subjects:
                    eee_subjects.append(subject)

        elif self.department == "Civil":
            civil_students.append(self)
            for subject in self.subjects:
                if subject not in civil_subjects:
                    civil_subjects.append(subject)

        elif self.department == "Mech":
            mech_students.append(self)
            for subject in self.subjects:
                if subject not in mech_subjects:
                    mech_subjects.append(subject)

        elif self.department == "ECE":
            ece_students.append(self)
            for subject in self.subjects:
                if subject not in ece_subjects:
                    ece_subjects.append(subject)


stud_obj1 = Student("36110986", "A.Preetha", "CSE", ["maths", "c_lang", "problem solving", "english"])
stud_obj2 = Student("36110389", "S.Gayathri", "CSE", ["maths", "c_lang", "english"])
stud_obj3 = Student("34025455", "S.Ajaytha", "EEE", ["maths", "electrical", "english"])
stud_obj4 = Student("35579520", "D.Mohan", "Civil", ["maths", "geology", "english"])
stud_obj5 = Student("36100679", "A.Yogesh", "Mech", ["maths", "machines", "english"])
stud_obj6 = Student("36120985", "K.Pachai", "ECE", ["maths", "c_lang", "english"])

Student.department_details(stud_obj1)
Student.department_details(stud_obj2)
Student.department_details(stud_obj3)
Student.department_details(stud_obj4)
Student.department_details(stud_obj5)
Student.department_details(stud_obj6)


def departments(department_students):
    print("No of students: {}\n".format(len(department_students)))
    for student in department_students:
        Student.display_student_details(student)


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
student_list = [stud_obj1, stud_obj2, stud_obj3, stud_obj4, stud_obj5, stud_obj6]
for student in student_list:
    if len(student.subjects) > 3:
        print(student.department)


# Just give two lists of department subjects to find common subjects like the below line
print("\nCommon subjects between cse & eee departments - ", set(cse_subjects).intersection(eee_subjects))

'''
Output:
CSE department student details

No of students: 2

Id_no - 36110986
Name - A.Preetha
Department - CSE
Subjects- ['maths', 'c_lang', 'problem solving', 'english']

Id_no - 36110389
Name - S.Gayathri
Department - CSE
Subjects- ['maths', 'c_lang', 'english']

CSE department subjects -  ['maths', 'c_lang', 'problem solving', 'english']

Name of the departments where students take more than 3 courses
CSE

Common subjects between cse & eee departments -  {'english', 'maths'}
'''






