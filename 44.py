class Student:
    student_count = 0

    def __init__(self, first_name, last_name, year, median):
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.median = median
        Student.student_count += 1

    def displayStudent(self):
        print(f"""Imię: {self.first_name} {self.last_name}
Rok studiów: {self.year}
Średnia ocen: {self.median}\n""")

    @classmethod
    def displayCount(cls):
        print(f"Aktualna liczba studentów: {cls.student_count}")

def create_students():
    students = []

    student1 = Student("Szymon", "Wiezowski", 4, 4.5)
    student2 = Student("Kuba", "Kubek", 1, 2)
    student3 = Student("Jan", "Brzechwa", 3, 4.2)

    students.extend([student1, student2, student3])

    return students

def displayStudentCLS(student):
    student.displayStudent()

def existCheck(student_list, first_name, last_name):
    for student in student_list:
        if student.first_name == first_name and student.last_name == last_name:
            return True
    print(f"\nStudent {first_name} {last_name} nie istnieje.")
    return False

if __name__ == "__main__":
    students_list = create_students()
    Student.displayCount()

    for student in students_list:
        displayStudentCLS(student)

    fName = "Szymon"
    lName = "Wiezowski"
    if existCheck(students_list, fName, lName):
        print(f"\nDane studenta {fName} {lName}:")
        for student in students_list:
            if student.first_name == fName and student.last_name == lName:
                student.displayStudent()
