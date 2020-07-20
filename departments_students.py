student_objects = []
cse_student_objects = []
eee_student_objects = []
civil_student_objects = []
mech_student_objects = []
ece_student_objects = []

cse_subjects = ["Maths", "English", "C-programming", "PST"]
eee_subjects = ["Maths", "English", "BEE", "Electronics"]
civil_subjects = ["Maths", "Machines", "Geology"]
mech_subjects = ["Maths", "Machines", "C-programming"]
ece_subjects = ["Maths", "Electronics", "C-programming"]


class Student:

    def __init__(self, id_no, name, department, subjects):
        self.id_no = id_no
        self.name = name
        self.department = department
        self.subjects = subjects
        student_objects.append(self)

    def display_student_details(self):
        print("Id_no - {0}\nName - {1}\nDepartment - {2}\nSubjects- {3}\n".format(self.id_no, self.name, self.department, self.subjects))

    def append_in_department(self):
        if self.department == "CSE":
            cse_student_objects.append(self)
        elif self.department == "EEE":
            eee_student_objects.append(self)
        elif self.department == "Civil":
            civil_student_objects.append(self)
        elif self.department == "Mech":
            mech_student_objects.append(self)
        elif self.department == "ECE":
            ece_student_objects.append(self)


stud_obj1 = Student("36110986", "A.Preetha", "CSE", cse_subjects)
stud_obj2 = Student("36110389", "S.Gayathri", "CSE", cse_subjects)
stud_obj3 = Student("34025455", "S.Ajaytha", "EEE", eee_subjects)
stud_obj4 = Student("35579520", "D.Mohan", "Civil", civil_subjects)
stud_obj5 = Student("36100679", "A.Yogesh", "Mech", mech_subjects)
stud_obj6 = Student("36120985", "K.Pachai", "ECE", ece_subjects)
Student.append_in_department(stud_obj1)
Student.append_in_department(stud_obj2)
Student.append_in_department(stud_obj3)
Student.append_in_department(stud_obj4)
Student.append_in_department(stud_obj5)
Student.append_in_department(stud_obj6)


class Department:

    def __init__(self, name, students, subjects):
        self.name = name
        self.students = students
        self.subjects = subjects

    def cse_details(self):
        print("CSE students:\n")
        for student in cse_student_objects:
            Student.display_student_details(student)

    def eee_details(self):
        print("EEE students:\n")
        for student in eee_student_objects:
            Student.display_student_details(student)

    def civil_details(self):
        print("Civil students:\n")
        for student in civil_student_objects:
            Student.display_student_details(student)

    def mech_details(self):
        print("Mechanical students:\n")
        for student in mech_student_objects:
            Student.display_student_details(student)

    def ece_details(self):
        print("ECE students:\n")
        for student in ece_student_objects:
            Student.display_student_details(student)


dept_obj1 = Department("CSE", cse_student_objects, cse_subjects)
dept_obj2 = Department("EEE", eee_student_objects, eee_subjects)
dept_obj3 = Department("Civil", civil_student_objects, civil_subjects)
dept_obj4 = Department("Mech", mech_student_objects, mech_subjects)
dept_obj5 = Department("ECE", ece_student_objects, eee_subjects)
Department.cse_details(dept_obj1)
Department.eee_details(dept_obj2)
Department.civil_details(dept_obj3)
Department.mech_details(dept_obj4)
Department.ece_details(dept_obj5)

'''
Output:
CSE students:

Id_no - 36110986
Name - A.Preetha
Department - CSE
Subjects- ['Maths', 'English', 'C-programming', 'PST']

Id_no - 36110389
Name - S.Gayathri
Department - CSE
Subjects- ['Maths', 'English', 'C-programming', 'PST']

EEE students:

Id_no - 34025455
Name - S.Ajaytha
Department - EEE
Subjects- ['Maths', 'English', 'BEE', 'Electronics']

Civil students:

Id_no - 35579520
Name - D.Mohan
Department - Civil
Subjects- ['Maths', 'Machines', 'Geology']

Mechanical students:

Id_no - 36100679
Name - A.Yogesh
Department - Mech
Subjects- ['Maths', 'Machines', 'C-programming']

ECE students:

Id_no - 36120985
Name - K.Pachai
Department - ECE
Subjects- ['Maths', 'Electronics', 'C-programming']
'''