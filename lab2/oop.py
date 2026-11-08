class StudentNotFoundError(Exception):
    pass
class CourseNotAvailableError(Exception):
    pass
class InvalidGradeError(Exception):
    pass
class AlreadyEnrolledError(Exception):
    pass
class Discipline:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
class Department:
    def __init__(self, name):
        self.name = name
        self.curriculum = {}  
    def add_course(self, specialty, semester, discipline):
        if specialty not in self.curriculum:
            self.curriculum[specialty] = {}
        if semester not in self.curriculum[specialty]:
            self.curriculum[specialty][semester] = []
        self.curriculum[specialty][semester].append(discipline)
    def teaches_course(self, specialty, semester, discipline):
        if specialty in self.curriculum:
            if semester in self.curriculum[specialty]:
                return discipline in self.curriculum[specialty][semester]
        return False
class Student:
    def __init__(self, student_id, name, specialty):
        self.student_id = student_id
        self.name = name
        self.specialty = specialty
        self.semester = 1
        self.grades = {}
        self.enrolled_courses = set()
    def add_grade(self, discipline, grade):
        if discipline not in self.enrolled_courses:
            raise InvalidGradeError(f"студент не записан на дисциплину '{discipline.name}'")
        if grade < 2 or grade > 5:
            raise InvalidGradeError(f"оценка должна быть от 4 до 10, получено {grade}")
        self.grades[discipline] = grade
    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)
    def save_report(self, filename, faculty):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"ведомость успеваемости\n\n")
            f.write(f"студент: {self.name}\n")
            f.write(f"ID: {self.student_id}\n")
            f.write(f"специальность: {self.specialty}\n")
            f.write(f"семестр: {self.semester}\n")
            f.write(f"средний балл: {self.get_average():.2f}\n\n")
            f.write("дисциплины:\n")
            for discipline, grade in self.grades.items():
                department_name = faculty.find_department_for_course(
                    self.specialty, self.semester, discipline
                )
                f.write(f"  {discipline.name}: {grade} (кафедра: {department_name})\n")
            if not self.grades:
                f.write("  оценок пока нет\n")
class Faculty:
    def __init__(self, name):
        self.name = name
        self.departments = []
        self.students = {}
    def add_department(self, department):
        self.departments.append(department)
    def enroll_student(self, student_id, name, specialty):
        if student_id in self.students:
            raise ValueError(f"студент с ID {student_id} уже существует")
        student = Student(student_id, name, specialty)
        self.students[student_id] = student
        return student
    def expel_student(self, student_id):
        if student_id not in self.students:
            raise StudentNotFoundError(f"студент с ID {student_id} не найден")
        del self.students[student_id]
    def add_student_to_course(self, student_id, discipline):
        if student_id not in self.students:
            raise StudentNotFoundError(f"студент с ID {student_id} не найден")
        student = self.students[student_id]
        if discipline in student.enrolled_courses:
            raise AlreadyEnrolledError(f"студент уже записан на '{discipline.name}'")